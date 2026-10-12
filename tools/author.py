#!/usr/bin/env python3
"""Authoring workflow helpers: brief → plan → (draft) → review → status.

The author makes the creative and editorial decisions; an agent (Codex, Claude, or a
person) does the writing. This tool does the bookkeeping that is easy to get wrong by
hand: checking a brief, mapping every term to a chapter, finding gaps and forward
references, gathering automated checks into one review report, and keeping a
resumable record of where a job stands. It never writes narrative.

Usage (from the repo root):
  python tools/author.py brief-check briefs/<id>.brief.yaml
  python tools/author.py plan        briefs/<id>.brief.yaml [--refresh]
  python tools/author.py plan-check  briefs/<id>.brief.yaml [--chapter chNN]
  python tools/author.py review      <unit_dir> [--brief briefs/<id>.brief.yaml --chapter chNN] [--out FILE]
  python tools/author.py status      briefs/<id>.brief.yaml [--init]

See schema/BRIEF.md for the brief format and AGENTS.md → Authoring workflow.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import re
import subprocess
import sys
from collections import OrderedDict
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required. Try: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt")

KIT = Path(__file__).resolve().parent.parent
MODES = ("term-set", "course-glossary", "source-material", "track-extension")
MARK_RE = re.compile(r"\[\[([^|\]]+)\|([^\]]*)\]\]")
TODO = "TODO"

DEFAULTS = {
    "scope": {"chapters": "auto", "words_per_chapter": 1800, "terms_per_chapter_max": 30},
    "creative": {
        "tone": "plain, grounded workplace realism; dry humor allowed",
        "pov": "third person, close to one character per chapter",
        "tense": "past",
        "setting": None,
        "endings": "cost",
        "headings": "scene",
        "notes": "",
    },
}

STAGES = {
    "course-glossary": ["brief", "definitions", "plan", "plan-approved", "draft", "review",
                        "revise", "validate", "preview", "author-accepts", "publish"],
    "default": ["brief", "definitions", "draft", "review", "revise", "validate", "preview",
                "author-accepts", "publish"],
}


# ---------------------------------------------------------------- helpers

def rel(p: Path) -> str:
    try:
        return str(p.resolve().relative_to(KIT))
    except ValueError:
        return str(p)


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8")) or {}


def dump_yaml(obj, path: Path, header: str = "") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = yaml.safe_dump(obj, sort_keys=False, allow_unicode=True, width=100)
    path.write_text(header + text, encoding="utf-8")


def norm(title: str) -> str:
    return re.sub(r"[^a-z0-9%]+", " ", title.lower()).strip()


def base_title(title: str) -> str:
    return re.sub(r"\s*\([^)]*\)\s*$", "", title).strip()


def acronym(title: str) -> str | None:
    m = re.search(r"\(([A-Z][A-Za-z0-9&/]{1,7})\)\s*$", title)
    return m.group(1) if m else None


def cover_strip(text: str) -> str:
    return MARK_RE.sub(lambda m: m.group(2), text)


def words(text: str) -> int:
    return len(re.findall(r"\b[\w']+\b", text))


def slug(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower()).strip("_")[:40]


# ---------------------------------------------------------------- brief

class Brief:
    def __init__(self, path: Path):
        self.path = path
        self.raw = load_yaml(path)
        self.errors: list[str] = []
        self.applied_defaults: list[str] = []
        b = self.raw
        for key in ("brief_id", "mode", "reader", "purpose"):
            if not b.get(key):
                self.errors.append(f"missing required field: {key}")
        if b.get("mode") and b["mode"] not in MODES:
            self.errors.append(f"mode must be one of {', '.join(MODES)}")
        if isinstance(b.get("reader"), dict) and not b["reader"].get("who"):
            self.errors.append("reader.who is required")
        inputs = b.get("inputs") or {}
        if not any(inputs.get(k) for k in ("glossaries", "glossary_csv", "terms", "sources")):
            self.errors.append("inputs needs at least one of: glossaries, glossary_csv, terms, sources")
        if b.get("mode") == "source-material" and not inputs.get("sources"):
            self.errors.append("mode source-material needs inputs.sources")
        if b.get("mode") == "track-extension" and not (b.get("track") or {}).get("manifest"):
            self.errors.append("mode track-extension needs track.manifest (and usually track.canon)")
        for section, defaults in DEFAULTS.items():
            got = b.setdefault(section, {}) or {}
            b[section] = got
            for k, v in defaults.items():
                if k not in got:
                    got[k] = v
                    self.applied_defaults.append(f"{section}.{k} = {v!r}")
        self.id = b.get("brief_id", path.stem.replace(".brief", ""))
        self.mode = b.get("mode")
        self.workdir = KIT / ((b.get("output") or {}).get("workdir") or f"workshop/{self.id}")
        track = b.get("track") or {}
        self.manifest = KIT / track["manifest"] if track.get("manifest") else None
        self.canon = KIT / track["canon"] if track.get("canon") else None
        for p in [self.manifest, self.canon]:
            if p and not p.is_file():
                self.errors.append(f"track file not found: {rel(p)}")
        for s in inputs.get("sources") or []:
            if isinstance(s, dict) and s.get("path") and not (KIT / s["path"]).exists():
                self.errors.append(f"source not found: {s['path']} (give a repo path, or describe it with note:)")

    # Terms, in course order, each with a group (future chapter) and a definition status.
    def terms(self) -> list[dict]:
        inputs = self.raw.get("inputs") or {}
        out: list[dict] = []
        for g in inputs.get("glossaries") or []:
            gp = KIT / g
            if not gp.is_file():
                self.errors.append(f"glossary not found: {g}")
                continue
            data = load_yaml(gp)
            group = gp.parent.name if gp.name == "glossary.yaml" else gp.stem
            for t in data.get("terms") or []:
                out.append({
                    "id": t["id"], "title": t.get("title", t["id"]), "group": group,
                    "definition": (t.get("definition") or "").strip(), "sense": t.get("sense", ""),
                    "status": "source" if t.get("definition") else "missing",
                    "source": data.get("source", rel(gp)), "tier": t.get("tier", "exam"),
                })
        csvspec = inputs.get("glossary_csv")
        if csvspec:
            cp = KIT / csvspec["path"]
            if not cp.is_file():
                self.errors.append(f"glossary_csv not found: {csvspec['path']}")
            else:
                with cp.open(encoding="utf-8-sig", newline="") as fh:
                    for row in csv.DictReader(fh):
                        term = (row.get(csvspec.get("term_column", "Term")) or "").strip()
                        if not term:
                            continue
                        d = (row.get(csvspec.get("definition_column", "Definition")) or "").strip()
                        out.append({
                            "id": slug(term), "title": term,
                            "group": (row.get(csvspec.get("group_column", "")) or "all").strip(),
                            "definition": d, "sense": "", "status": "source" if d else "missing",
                            "source": rel(cp), "tier": "exam",
                        })
        for t in inputs.get("terms") or []:
            if isinstance(t, str):
                t = {"term": t}
            d = (t.get("definition") or "").strip()
            out.append({
                "id": t.get("id") or slug(t["term"]), "title": t["term"], "group": t.get("group", "brief"),
                "definition": d, "sense": t.get("sense", ""),
                "status": t.get("status") or ("source" if d else "missing"),
                "source": t.get("source", "brief"), "tier": t.get("tier", "exam"),
            })
        # Qualify ids that collide across groups so every term has one key.
        seen: dict[str, int] = {}
        for t in out:
            seen[t["id"]] = seen.get(t["id"], 0) + 1
        for t in out:
            t["key"] = f'{t["group"]}:{t["id"]}' if seen[t["id"]] > 1 else t["id"]
        return out

    def groups(self, terms: list[dict]) -> list[str]:
        order = list(OrderedDict.fromkeys(t["group"] for t in terms))
        seq = (self.raw.get("inputs") or {}).get("sequence", "inputs")
        if isinstance(seq, list):
            missing = [g for g in order if g not in seq]
            return [g for g in seq if g in order] + missing
        return order


def definition_report(terms: list[dict]) -> dict:
    by_title: dict[str, list[dict]] = {}
    for t in terms:
        by_title.setdefault(norm(base_title(t["title"])), []).append(t)
    conflicts = []
    for k, ts in by_title.items():
        defs = {t["definition"] for t in ts if t["definition"]}
        if len(ts) > 1 and len(defs) > 1:
            conflicts.append({"term": ts[0]["title"], "in": [t["key"] for t in ts]})
    by_def: dict[str, list[dict]] = {}
    for t in terms:
        if t["definition"]:
            by_def.setdefault(t["definition"], []).append(t)
    same_def = [{"terms": [t["key"] for t in ts]} for ts in by_def.values()
                if len({norm(base_title(t["title"])) for t in ts}) > 1]
    return {
        "needs_definition": [t["key"] for t in terms if t["status"] == "missing"],
        "proposed": [t["key"] for t in terms if t["status"] == "proposed"],
        "conflicts": conflicts,
        "same_definition_different_terms": same_def,
    }


def cmd_brief_check(args) -> int:
    b = Brief(Path(args.brief))
    terms = b.terms()
    print(f"Brief: {rel(b.path)}  (mode: {b.mode})")
    r = b.raw.get("reader") or {}
    print(f"Reader: {r.get('who') if isinstance(r, dict) else r}")
    print(f"Purpose: {' '.join(str(b.raw.get('purpose', '')).split())[:160]}")
    if b.manifest:
        print(f"Track: {rel(b.manifest)}  canon: {rel(b.canon) if b.canon else '(none)'}")
    srcs = (b.raw.get("inputs") or {}).get("sources") or []
    if srcs:
        print(f"Sources: {len(srcs)}")
        for s in srcs:
            print(f"  - {s.get('path') or s.get('note', '')[:70] if isinstance(s, dict) else s}")
    if terms:
        groups = b.groups(terms)
        print(f"Terms: {len(terms)} in {len(groups)} group(s)")
        for g in groups:
            n = sum(1 for t in terms if t["group"] == g)
            flag = "  <- over terms_per_chapter_max" if n > b.raw["scope"]["terms_per_chapter_max"] else ""
            print(f"  {g}: {n}{flag}")
        rep = definition_report(terms)
        counts = {s: sum(1 for t in terms if t["status"] == s) for s in ("source", "confirmed", "proposed", "missing")}
        print("Definitions: " + ", ".join(f"{k} {v}" for k, v in counts.items()))
        if rep["needs_definition"]:
            print(f"NEEDS A DEFINITION before drafting ({len(rep['needs_definition'])}): " + ", ".join(rep["needs_definition"]))
        if rep["proposed"]:
            print(f"PROPOSED, awaiting author approval ({len(rep['proposed'])}): " + ", ".join(rep["proposed"]))
        for c in rep["conflicts"]:
            print(f"CONFLICT: '{c['term']}' is defined differently in {', '.join(c['in'])}")
        for s in rep["same_definition_different_terms"]:
            print(f"NOTE: same definition, different terms: {', '.join(s['terms'])}")
    if b.applied_defaults:
        print("Defaults applied: " + "; ".join(b.applied_defaults))
    for e in b.errors:
        print(f"ERROR: {e}")
    blocked = len(definition_report(terms)["needs_definition"]) + len(definition_report(terms)["proposed"]) if terms else 0
    if b.errors:
        print("RESULT: FAIL")
    elif blocked:
        print(f"RESULT: OK (brief is complete; {blocked} term(s) block drafting until defined or confirmed)")
    else:
        print("RESULT: OK")
    return 1 if b.errors else 0


# ---------------------------------------------------------------- plan

def term_patterns(t: dict) -> list[re.Pattern]:
    pats = []
    bt = base_title(t["title"])
    if len(bt) >= 4:
        pats.append(re.compile(r"\b" + re.escape(bt) + r"\b", re.I))
    ac = acronym(t["title"])
    if ac and len(ac) >= 2:
        pats.append(re.compile(r"\b" + re.escape(ac) + r"\b"))
    return pats


def accepted_units(brief: Brief) -> dict[str, Path]:
    """Units already in the track (or named like the groups) that exist in examples/."""
    out = {}
    if brief.manifest and brief.manifest.is_file():
        for part in load_yaml(brief.manifest).get("parts", []):
            for u in part.get("units") or []:
                d = KIT / "examples" / u["id"]
                if (d / "narrative.md").is_file():
                    out[u["id"]] = d
    return out


def build_plan(b: Brief, terms: list[dict], previous: dict | None) -> dict:
    groups = b.groups(terms)
    chap_of = {}
    chapters = []
    accepted = accepted_units(b)
    prev_ch = {c["group"]: c for c in (previous or {}).get("chapters", [])}
    for i, g in enumerate(groups, 1):
        cid = f"ch{i:02d}"
        ts = [t for t in terms if t["group"] == g]
        for t in ts:
            chap_of[t["key"]] = cid
        old = prev_ch.get(g, {})
        unit = g if g in accepted else old.get("unit_id")
        title = old.get("title")
        if not title and unit:
            title = (load_yaml(KIT / "examples" / unit / "unit.yaml").get("title") or "").split(" — ", 1)[-1]
        chapters.append({
            "id": cid, "group": g, "unit_id": unit,
            "status": old.get("status") or ("accepted" if unit else "planned"),
            "title": title or TODO,
            "terms_introduced": [t["key"] for t in ts],
            "builds_on": [],
            "situation": old.get("situation") or {
                "pov": TODO, "goal": TODO, "complication": TODO, "decision": TODO,
                "cost": TODO, "carries_forward": TODO,
            },
            "notes": old.get("notes", ""),
            "risks": [],
        })
        generated = ("id", "group", "terms_introduced", "builds_on", "risks")
        for k, v in old.items():  # keep any other field the author added (candidate, owner, …)
            if k not in chapters[-1] and k not in generated:
                chapters[-1][k] = v
    by_key = {t["key"]: t for t in terms}
    idx = {c["id"]: n for n, c in enumerate(chapters)}
    pats = {t["key"]: term_patterns(t) for t in terms}
    term_map: dict[str, dict] = {}
    for t in terms:
        deps = []
        for k, ps in pats.items():
            if k == t["key"] or norm(base_title(by_key[k]["title"])) == norm(base_title(t["title"])):
                continue
            if any(p.search(t["definition"]) for p in ps):
                deps.append(k)
        term_map[t["key"]] = {"title": t["title"], "introduced_in": chap_of[t["key"]],
                              "status": t["status"], "depends_on": deps, "revisited_in": []}
    # Revisits already present in accepted chapter text (mentions of earlier chapters' terms).
    texts = {}
    for c in chapters:
        if c["unit_id"] and (KIT / "examples" / c["unit_id"] / "narrative.md").is_file():
            texts[c["id"]] = cover_strip((KIT / "examples" / c["unit_id"] / "narrative.md").read_text(encoding="utf-8"))
    for k, info in term_map.items():
        home = idx[info["introduced_in"]]
        for cid, text in texts.items():
            if idx[cid] > home:
                bt = base_title(by_key[k]["title"])
                strong = [p for p in pats[k] if len(bt) >= 6 or " " in bt or p.flags & re.I == 0]
                if any(p.search(text) for p in strong):
                    info["revisited_in"].append(cid)
    forward = []
    for k, info in term_map.items():
        here = idx[info["introduced_in"]]
        for d in info["depends_on"]:
            there = idx[term_map[d]["introduced_in"]]
            if there > here:
                forward.append({"term": k, "chapter": info["introduced_in"], "needs": d,
                                "introduced_later_in": term_map[d]["introduced_in"]})
            elif there < here:
                ch = chapters[here]
                if d not in ch["builds_on"]:
                    ch["builds_on"].append(d)
    dependents = {k: 0 for k in term_map}
    for info in term_map.values():
        for d in info["depends_on"]:
            dependents[d] += 1
    for c in chapters:
        n = len(c["terms_introduced"])
        if n > b.raw["scope"]["terms_per_chapter_max"]:
            c["risks"].append(f"catalog-chapter risk: {n} terms (max {b.raw['scope']['terms_per_chapter_max']}); "
                              "plan two scenes with different stakes, or split")
        fw = [f for f in forward if f["chapter"] == c["id"]]
        if fw:
            c["risks"].append(f"{len(fw)} term(s) here depend on terms introduced later (see gaps.forward_references)")
    rep = definition_report(terms)
    gaps = {
        "needs_definition": rep["needs_definition"],
        "proposed_definitions": rep["proposed"],
        "conflicting_definitions": rep["conflicts"],
        "same_definition_different_terms": rep["same_definition_different_terms"],
        "forward_references": forward,
        "never_revisited": [k for k, v in term_map.items() if not v["revisited_in"] and not dependents[k]]
        if texts else "not computed (no chapter text yet)",
    }
    foundational = sorted(dependents.items(), key=lambda kv: -kv[1])[:12]
    plan = dict([
        ("plan_id", b.id),
        ("brief", rel(b.path)),
        ("approved", (previous or {}).get("approved", False)),
        ("generated", dt.date.today().isoformat()),
        ("story", (previous or {}).get("story") or {
            "premise": TODO, "setting": b.raw["creative"].get("setting") or (rel(b.canon) if b.canon else TODO),
            "cast": "from canon" if b.canon else TODO,
            "through_line": TODO,
        }),
        ("summary", {
            "chapters": len(chapters), "terms": len(terms),
            "definitions": {s: sum(1 for t in terms if t["status"] == s) for s in ("source", "confirmed", "proposed", "missing")},
            "suggested_dependencies": sum(len(v["depends_on"]) for v in term_map.values()),
            "most_depended_on": [f"{by_key[k]['title']} ({n})" for k, n in foundational if n],
        }),
        ("chapters", chapters),
        ("gaps", gaps),
        ("terms", term_map),
    ])
    for k, v in (previous or {}).items():  # keep top-level fields the author added (approval_note, …)
        if k not in plan:
            plan[k] = v
    return plan


def plan_markdown(plan: dict) -> str:
    L = [f"# Plan: {plan['plan_id']}", "",
         f"Brief: `{plan['brief']}` · generated {plan['generated']} · "
         f"**{'approved' if plan['approved'] else 'NOT YET APPROVED'}** by the author", ""]
    s = plan["summary"]
    L += [f"{s['chapters']} chapters · {s['terms']} terms · definitions: "
          + ", ".join(f"{k} {v}" for k, v in s["definitions"].items())
          + f" · {s['suggested_dependencies']} suggested dependencies", ""]
    if s["most_depended_on"]:
        L += ["Most depended-on concepts (introduce them early and well): " + ", ".join(s["most_depended_on"]), ""]
    st = plan["story"]
    L += ["## Story", ""] + [f"- **{k.replace('_', ' ').capitalize()}:** {v}" for k, v in st.items()] + [""]
    L += ["## Chapters", "", "| # | Group | Status | Title | Terms | Builds on | Risks |", "|---|---|---|---|---|---|---|"]
    for c in plan["chapters"]:
        L.append(f"| {c['id']} | {c['group']} | {c['status']} | {c['title']} | {len(c['terms_introduced'])} | "
                 f"{len(c['builds_on'])} | {'; '.join(c['risks']) or ''} |")
    L += [""]
    for c in plan["chapters"]:
        sit = c["situation"]
        L += [f"### {c['id']} · {c['title']}", ""]
        L += [f"- **{k.replace('_', ' ').capitalize()}:** {v}" for k, v in sit.items()]
        if c.get("notes"):
            L += [f"- **Notes:** {' '.join(str(c['notes']).split())}"]
        L += [""]
    g = plan["gaps"]
    L += ["## Gaps and decisions for the author", ""]
    L.append(f"- **Needs a definition:** {', '.join(g['needs_definition']) or 'none'}")
    L.append(f"- **Proposed definitions awaiting approval:** {', '.join(g['proposed_definitions']) or 'none'}")
    L.append(f"- **Conflicting definitions:** " + ("; ".join(f"{c['term']} ({', '.join(c['in'])})" for c in g["conflicting_definitions"]) or "none"))
    L.append(f"- **Same definition, different terms:** " + ("; ".join(", ".join(x["terms"]) for x in g["same_definition_different_terms"]) or "none"))
    fw = g["forward_references"]
    L.append(f"- **Forward references** (a term's definition relies on a term introduced later): {len(fw)}")
    for f in fw[:40]:
        L.append(f"  - {f['term']} ({f['chapter']}) needs {f['needs']} (introduced in {f['introduced_later_in']})")
    nr = g["never_revisited"]
    if isinstance(nr, list):
        L.append(f"- **Introduced once, never revisited or built on:** {len(nr)} of {s['terms']} terms (not a defect by itself; a list to draw on when planning callbacks)")
    L += ["", "## Term map", "", "| Term | Introduced | Depends on | Revisited in |", "|---|---|---|---|"]
    for k, v in plan["terms"].items():
        L.append(f"| {v['title']} | {v['introduced_in']} | {', '.join(v['depends_on']) or ''} | {', '.join(v['revisited_in']) or ''} |")
    return "\n".join(L) + "\n"


def cmd_plan(args) -> int:
    b = Brief(Path(args.brief))
    terms = b.terms()
    if b.errors:
        for e in b.errors:
            print(f"ERROR: {e}")
        return 1
    if not terms:
        print("ERROR: no terms in the inputs; a plan maps terms to chapters")
        return 1
    plan_path = b.workdir / "plan.yaml"
    previous = None
    if plan_path.exists():
        if not args.refresh:
            print(f"{rel(plan_path)} exists. Use --refresh to update the generated parts "
                  "(terms, gaps, chapter term lists) and keep the author's story, situations, titles, and approval.")
            return 1
        previous = load_yaml(plan_path)
    plan = build_plan(b, terms, previous)
    dump_yaml(dict(plan), plan_path,
              "# Course-companion plan. Generated parts: summary, chapters[*].terms_introduced/builds_on/risks,\n"
              "# gaps, terms. Author parts (kept on --refresh): approved, story, chapters[*].title/status/situation/notes.\n")
    (b.workdir / "plan.md").write_text(plan_markdown(plan), encoding="utf-8")
    s = plan["summary"]
    print(f"Wrote {rel(plan_path)} and plan.md: {s['chapters']} chapters, {s['terms']} terms, "
          f"{s['suggested_dependencies']} suggested dependencies, "
          f"{len(plan['gaps']['forward_references'])} forward references")
    return 0


def cmd_plan_check(args) -> int:
    b = Brief(Path(args.brief))
    terms = b.terms()
    plan_path = b.workdir / "plan.yaml"
    if not plan_path.is_file():
        print(f"ERROR: no plan at {rel(plan_path)}; run: python tools/author.py plan {args.brief}")
        return 1
    plan = load_yaml(plan_path)
    keys = [t["key"] for t in terms]
    by_key = {t["key"]: t for t in terms}
    placed: dict[str, list[str]] = {}
    for c in plan.get("chapters", []):
        for k in c.get("terms_introduced") or []:
            placed.setdefault(k, []).append(c["id"])
    problems, notes = [], []
    unplaced = [k for k in keys if k not in placed]
    twice = {k: v for k, v in placed.items() if len(v) > 1}
    unknown = [k for k in placed if k not in by_key]
    if unplaced:
        problems.append(f"{len(unplaced)} term(s) not introduced in any chapter: {', '.join(unplaced)}")
    if twice:
        problems.append("introduced in more than one chapter: " + ", ".join(f"{k} {v}" for k, v in twice.items()))
    if unknown:
        problems.append(f"chapter lists terms not in the inputs: {', '.join(unknown)}")
    story_todo = [k for k, v in (plan.get("story") or {}).items() if v == TODO]
    if story_todo:
        notes.append(f"story fields still TODO: {', '.join(story_todo)}")
    print(f"Plan: {rel(plan_path)}  approved: {plan.get('approved')}")
    print(f"Coverage: {len(keys) - len(unplaced)}/{len(keys)} terms introduced exactly once"
          if not twice else f"Coverage: {len(keys) - len(unplaced)}/{len(keys)} placed; duplicates present")
    for c in plan.get("chapters", []):
        todo = [k for k, v in (c.get("situation") or {}).items() if v == TODO]
        st = c.get("status")
        line = f"  {c['id']} {c.get('title', '')[:40]:40} {st:9} terms {len(c.get('terms_introduced') or []):3}"
        if todo and st != "accepted":
            line += f"  situation TODO: {', '.join(todo)}"
        print(line)
    if args.chapter:
        ch = next((c for c in plan.get("chapters", []) if c["id"] == args.chapter), None)
        if not ch:
            problems.append(f"no chapter {args.chapter} in the plan")
        else:
            gate = []
            if not plan.get("approved"):
                gate.append("the plan is not approved (set approved: true in plan.yaml after the author signs off)")
            todo = [k for k, v in (ch.get("situation") or {}).items() if v == TODO]
            if todo:
                gate.append(f"situation fields TODO: {', '.join(todo)}")
            bad = [k for k in ch.get("terms_introduced") or [] if by_key.get(k, {}).get("status") in ("missing", "proposed")]
            if bad:
                gate.append(f"terms without a dependable definition: {', '.join(bad)}")
            print(f"Chapter {args.chapter}: " + ("READY TO DRAFT" if not gate else "NOT READY"))
            for g in gate:
                print(f"  - {g}")
            if gate:
                problems.append(f"{args.chapter} not ready to draft")
    for n in notes:
        print(f"NOTE: {n}")
    for p in problems:
        print(f"PROBLEM: {p}")
    print("RESULT: " + ("FAIL" if problems else "OK"))
    return 1 if problems else 0


# ---------------------------------------------------------------- review

DECISION_CUES = re.compile(
    r"\b(decid\w*|chose|choose|approv\w*|refus\w*|defer\w*|cost\w*|wouldn't|won't|instead|"
    r"agreed|signed|cut|bought|declin\w*|asked whether|said no|picked|switched|stopped|kept)\b", re.I)
MONTHS = ("January|February|March|April|May|June|July|August|September|October|November|December")
STOP_CAPS = set("""I A An The This That These Those It Its He She They We You His Her Their Our
Then When While After Before Once If But And Or So Yes No Not Nobody Somebody Everyone Everything
Monday Tuesday Wednesday Thursday Friday Saturday Sunday""".split()) | set(MONTHS.split("|"))


def run(cmd: list[str]) -> tuple[int, str]:
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=KIT)
    return p.returncode, (p.stdout + p.stderr).strip()


def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?\"”])\s+(?=[A-Z\"“\[])", text) if s.strip()]


def known_names(canon: Path | None, exclude_unit: str | None, manifest: Path | None) -> dict[str, str]:
    """Names already established: the canon's cast table, plus capitalized words that
    recur in accepted chapters (with the first chapter they appear in)."""
    names: dict[str, str] = {}
    if canon and canon.is_file():
        for line in canon.read_text(encoding="utf-8").splitlines():
            m = re.match(r"^\|\s*([A-Z][\w.'-]+(?:\s+[A-Z][\w.'-]+)*)\s*\|", line)
            if m and m.group(1) not in ("Person",):
                for part in m.group(1).split():
                    names.setdefault(part, "canon")
    if manifest and manifest.is_file():
        for part in load_yaml(manifest).get("parts", []):
            for u in part.get("units") or []:
                if u["id"] == exclude_unit:
                    continue
                p = KIT / "examples" / u["id"] / "narrative.md"
                if p.is_file():
                    for w in re.findall(r"(?<![.!?]\s)(?<!^)\b[A-Z][a-z]{2,}\b", cover_strip(p.read_text(encoding="utf-8"))):
                        names.setdefault(w, u["id"])
    return names


def cmd_review(args) -> int:
    unit = Path(args.unit_dir)
    narr_path = unit / "narrative.md"
    if not narr_path.is_file():
        print(f"ERROR: no narrative.md in {unit}")
        return 1
    md = narr_path.read_text(encoding="utf-8")
    meta = load_yaml(unit / "unit.yaml") if (unit / "unit.yaml").is_file() else {}
    gloss = {t["id"]: t for t in (load_yaml(unit / "glossary.yaml").get("terms") or [])}
    body = re.sub(r"```.*?```", "", md, flags=re.S)  # exhibits aside
    prose_paras = [p for p in body.split("\n\n") if p.strip() and not p.lstrip().startswith(("#", "*Tamarack", "* * *", "|"))]
    brief = Brief(Path(args.brief)) if args.brief else None
    canon = brief.canon if brief else (Path(args.canon) if args.canon else None)
    manifest = brief.manifest if brief else (Path(args.track) if args.track else None)

    out = [f"# Review: {meta.get('title', unit.name)}", "",
           f"Candidate: `{rel(unit)}` · {dt.date.today().isoformat()}", "",
           "This report separates three things. **Automated checks** are mechanical and either pass or fail. "
           "**Heuristic flags** are patterns that often mean a problem; each one needs a person to look, and a passage "
           "that reads well and is accurate stays as it is (schema/README.md rule 9). "
           "**Editorial review** is judgment, and **learning effectiveness** is not measured here at all.", ""]

    # 1. Automated
    out += ["## 1. Automated checks", ""]
    code, v = run([sys.executable, "tools/validate_unit.py", str(unit)])
    vl = [l for l in v.splitlines() if l.startswith(("Words", "Marks", "Mark density", "Tiers", "Headings", "WARN", "FAIL", "RESULT"))]
    out += ["```", *vl, "```", ""]
    code2, vc = run([sys.executable, "tools/voice_check.py", str(narr_path)])
    stats = next((l.strip() for l in vc.splitlines() if l.strip().startswith("sentences=")), "")
    stats2 = next((l.strip() for l in vc.splitlines() if l.strip().startswith("fragments=")), "")
    out += [f"Voice metrics (reading aid; ITM control: mean 19.7w, sd 14.0, 11% short): `{stats}` `{stats2}`", ""]
    automated_ok = code == 0

    # Plan conformance
    if brief and args.chapter:
        plan_path = brief.workdir / "plan.yaml"
        if plan_path.is_file():
            plan = load_yaml(plan_path)
            ch = next((c for c in plan.get("chapters", []) if c["id"] == args.chapter), None)
            if ch:
                planned = [k.split(":")[-1] for k in ch.get("terms_introduced") or []]
                marked = set(m.group(1) for m in MARK_RE.finditer(md))
                missing = [k for k in planned if k not in marked]
                text = cover_strip(md).lower()
                bo = ch.get("builds_on") or []
                titles = {k: (plan["terms"].get(k) or {}).get("title", k) for k in bo}
                present = [k for k in bo if base_title(titles[k]).lower() in text]
                out += [f"Plan {args.chapter}: {len(planned) - len(missing)}/{len(planned)} planned terms marked"
                        + (f"; missing: {', '.join(missing)}" if missing else ""),
                        f"Builds on {len(bo)} earlier term(s); {len(present)} mentioned in the text"
                        + (f" ({', '.join(titles[k] for k in present[:12])})" if present else ""), ""]
                automated_ok = automated_ok and not missing

    # 2. Heuristics
    out += ["## 2. Heuristic flags (need a person to look)", ""]
    echo, cluster, decision_marks, total_marks = [], [], 0, 0
    for para in prose_paras:
        marks = list(MARK_RE.finditer(para))
        total_marks += len(marks)
        if len(marks) >= 4:
            cluster.append(cover_strip(para)[:110])
        if marks and DECISION_CUES.search(cover_strip(para)) or (marks and '"' in para):
            decision_marks += len(marks)
        for s in sentences(para):
            for m in MARK_RE.finditer(s):
                d = gloss.get(m.group(1), {}).get("definition", "")
                dw = {w for w in re.findall(r"[a-z]{4,}", d.lower())}
                sw = {w for w in re.findall(r"[a-z]{4,}", cover_strip(s).lower())}
                if len(dw) >= 5 and len(dw & sw) / len(dw) >= 0.6:
                    echo.append(f"{m.group(1)}: \"{cover_strip(s)[:120]}\"")
    pct = round(100 * decision_marks / total_marks) if total_marks else 0
    # Inline gloss: the mark is followed straight away by its explanation ("X meant…", "X, a…", "X: …").
    gloss_re = re.compile(r"\]\](?:\s+(?:meant|means|was|is|were|are)\b|,\s+(?:a|an|the|which|where)\b|:\s)")
    glossed = sum(len(gloss_re.findall(p)) for p in prose_paras)
    gpct = round(100 * glossed / total_marks) if total_marks else 0
    # Exposition run: consecutive paragraphs that each introduce a new term with no dialogue.
    streak = best = 0
    seen_ids: set[str] = set()
    for para in prose_paras:
        ids = {m.group(1) for m in MARK_RE.finditer(para)}
        if ids - seen_ids and '"' not in para and "“" not in para:
            streak += 1
            best = max(best, streak)
        else:
            streak = 0
        seen_ids |= ids
    out += [f"- **Definition echo:** {len(echo)} mark(s) sit in a sentence that restates most of the glossary definition. "
            "Fine when a character explains because the scene needs it (schema/README.md rule 8); many in a row is the vocabulary-parade pattern."]
    out += [f"  - {e}" for e in echo[:15]]
    out += [f"- **Inline glosses:** {glossed} of {total_marks} marks ({gpct}%) are followed at once by their explanation "
            "(\"X meant…\", \"X, a…\", \"X: …\"). Context only: this did not separate strong from weak chapters in calibration."]
    out += [f"- **Longest exposition run:** {best} consecutive paragraphs each introduce a new term with no dialogue. "
            "Five or more is the tour-guide pattern (a booth, a term, the next booth)."]
    out += [f"- **Mark clusters:** {len(cluster)} paragraph(s) with 4+ marked terms (a list wearing prose)."]
    out += [f"  - {c}…" for c in cluster[:8]]
    out += [f"- **Marks near decisions or dialogue:** {pct}% of marks are in paragraphs with dialogue or a decision word. "
            "Low numbers suggest terms in exposition rather than at the complication or pivot (schema/README.md → Beat structure)."]
    last = [p for p in prose_paras][-1:] if prose_paras else []
    if last:
        out += [f"- **Ending** (does it charge a cost? schema/VOICE.md → The structural tell): \"{cover_strip(last[0])[-280:]}\""]
    out += [""]

    # 3. Continuity
    out += ["## 3. Continuity (for the author to confirm)", ""]
    if canon or manifest:
        # A revision of an accepted chapter may reuse that chapter's names; only exclude the unit's own
        # text when reviewing the accepted version itself.
        own = KIT / "examples" / str(meta.get("unit_id", "")) / "narrative.md"
        reviewing_accepted = own.is_file() and own.resolve() == narr_path.resolve()
        known = known_names(canon, meta.get("unit_id") if reviewing_accepted else None, manifest)
        text = cover_strip("\n\n".join(prose_paras))
        unmarked = MARK_RE.sub("term", "\n\n".join(prose_paras))  # term names aren't characters
        found = OrderedDict()
        for s in sentences(unmarked):
            for w in re.findall(r"\b[A-Z][a-z]{2,}\b", s)[1:]:
                if w not in STOP_CAPS and w not in ("Internet", "Web"):
                    found.setdefault(w, 0)
                    found[w] += 1
        new = [w for w in found if w not in known]
        out += [f"- **Names and proper nouns not in the canon or any accepted chapter:** {', '.join(new) or 'none'}. "
                "New characters or places are allowed; confirm each is intended, and add recurring ones to the canon."]
        dated = [cover_strip(s)[:140] for s in sentences(text) if re.search(rf"\b({MONTHS})\b|\b20\d\d\b", s)]
        out += [f"- **Dated statements to check against the track timeline:** {len(dated)}"]
        out += [f"  - {d}" for d in dated[:12]]
        nums = sorted(set(re.findall(r"\$[\d,]+(?:\.\d+)?|\b\d{1,3}(?:,\d{3})+\b|\b\d+(?:\.\d+)?\s?(?:percent|%|tons|hours|days)\b"
                                  r"|\b(?:two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|fifteen|twenty|thirty|forty|fifty|sixty|"
                                  r"ninety|hundred)[\w-]*\s(?:percent|dollars|hours|days|weeks|months|degrees|stores|customers|minutes)\b", text, re.I)))
        out += [f"- **Figures stated** (each should come from a calculation, schema/README.md → Prove the story): {', '.join(nums[:30]) or 'none'}"]
    else:
        out += ["- No canon or track given; continuity not checked."]
    accepted = KIT / "examples" / str(meta.get("unit_id", "")) / "narrative.md"
    if accepted.is_file() and accepted.resolve() != narr_path.resolve():
        a = cover_strip(accepted.read_text(encoding="utf-8"))
        out += [f"- **Compared with the accepted version** (`{rel(accepted)}`): {words(a)} → {words(cover_strip(md))} words; "
                f"{len(re.findall(r'^## ', a, flags=re.M))} → {len(re.findall(r'^## ', md, flags=re.M))} headings."]
    out += [""]

    # 4. Editorial
    out += ["## 4. Editorial review (judgment; fill in)", "",
            "- [ ] **Cover test:** read the marks-stripped text (`*.cover.txt` next to this report). Do the concepts' relationships still come through?",
            "- [ ] **Concepts matter:** each major term changes a goal, complication, decision, or consequence; none is decoration.",
            "- [ ] **Instructional accuracy:** every claim about a concept matches its glossary definition or a cited source; nothing unverified is stated as fact.",
            "- [ ] **Continuity:** names, dates, numbers, and standing facts agree with the canon and accepted chapters.",
            "- [ ] **Explanations are earned:** any technical explanation has a reason in the scene and reads as an exchange, not a lecture (schema/README.md rule 8).",
            "- [ ] **The pivot costs something,** and the ending doesn't explain the chapter.",
            "- [ ] **Voice:** reads like a person, not a generator (schema/VOICE.md).",
            "",
            "## 5. Not measured",
            "",
            "Whether readers learn more with this chapter alongside their course materials than without it. The chapter supports "
            "the course; it doesn't replace it. Finding out needs readers: "
            "for example a short pre/post question set on the chapter's relationships, given to a few students.",
            ""]
    report = Path(args.out) if args.out else unit / "REVIEW.md"
    report.parent.mkdir(parents=True, exist_ok=True)
    report.write_text("\n".join(out), encoding="utf-8")
    cover = report.with_suffix(".cover.txt")
    cover.write_text(cover_strip(md), encoding="utf-8")
    print(f"Wrote {rel(report)} and {rel(cover)}")
    print(f"Automated: {'PASS' if automated_ok else 'FAIL'} · definition echo {len(echo)} · mark clusters {len(cluster)} · "
          f"marks near decisions/dialogue {pct}% · inline glosses {gpct}% · exposition run {best}")
    return 0 if automated_ok else 1


# ---------------------------------------------------------------- status

def cmd_status(args) -> int:
    b = Brief(Path(args.brief))
    path = b.workdir / "status.yaml"
    if args.init:
        if path.exists():
            print(f"{rel(path)} exists; not overwriting")
            return 1
        stages = STAGES["course-glossary" if b.mode == "course-glossary" else "default"]
        dump_yaml({
            "job": b.id, "brief": rel(b.path), "updated": dt.date.today().isoformat(),
            "max_revisions": 2, "revisions": 0,
            "stages": [{"stage": s, "state": "todo", "note": ""} for s in stages],
            "open_issues": [], "next_action": "Run: python tools/author.py brief-check " + rel(b.path),
        }, path, "# Resumable record for this job. Update after each stage.\n")
        print(f"Wrote {rel(path)}")
        return 0
    if not path.is_file():
        print(f"No status yet. Start one: python tools/author.py status {args.brief} --init")
        return 1
    st = load_yaml(path)
    print(f"Job {st['job']} · updated {st.get('updated')} · revisions {st.get('revisions', 0)}/{st.get('max_revisions', 2)}")
    for s in st.get("stages", []):
        mark = {"done": "x", "todo": " ", "blocked": "!", "skipped": "-", "in-progress": "~"}.get(s.get("state"), "?")
        print(f"  [{mark}] {s['stage']:15} {s.get('note', '')}")
    issues = st.get("open_issues") or []
    if issues:
        print("Open issues:")
        for i in issues:
            print(f"  - {i}")
    if st.get("revisions", 0) > st.get("max_revisions", 2):
        print("WARNING: revision limit exceeded; return the chapter to the author instead of revising again")
    print(f"Next: {st.get('next_action')}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("brief-check", help="validate a brief, fill defaults, report definition gaps")
    p.add_argument("brief")
    p.set_defaults(fn=cmd_brief_check)
    p = sub.add_parser("plan", help="write workshop/<id>/plan.yaml and plan.md from a brief")
    p.add_argument("brief")
    p.add_argument("--refresh", action="store_true", help="update generated parts, keep the author's")
    p.set_defaults(fn=cmd_plan)
    p = sub.add_parser("plan-check", help="coverage and the drafting gate")
    p.add_argument("brief")
    p.add_argument("--chapter", help="check whether this chapter is ready to draft")
    p.set_defaults(fn=cmd_plan_check)
    p = sub.add_parser("review", help="one review report: automated checks, heuristic flags, continuity, editorial checklist")
    p.add_argument("unit_dir")
    p.add_argument("--brief")
    p.add_argument("--chapter")
    p.add_argument("--canon", help="canon markdown, when no brief is given")
    p.add_argument("--track", help="track manifest, when no brief is given")
    p.add_argument("--out", help="report path (default: <unit_dir>/REVIEW.md)")
    p.set_defaults(fn=cmd_review)
    p = sub.add_parser("status", help="show or start the resumable job record")
    p.add_argument("brief")
    p.add_argument("--init", action="store_true")
    p.set_defaults(fn=cmd_status)
    args = ap.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
