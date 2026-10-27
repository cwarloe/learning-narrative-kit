#!/usr/bin/env python3
"""Build the ITM 310 Exam 2 study-card unit from cards.yaml.

Writes narrative.md, glossary.yaml and review.yaml beside this script. Those three files
are generated: edit cards.yaml (or the source glossaries it names), then rerun:

    python3 examples/itm310-exam2-cards/build_cards.py

Checks, and exits 1 on any failure:
  - every term in every listed glossary has a home band (red list or a concept card)
  - every id in cards.yaml exists in a glossary
  - no red card's front still names its own term (the answer would show)
  - no card text would break the lnk-deck fence (a line of ---, a backtick fence)
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
KIT = HERE.parents[1]

BAND_NAMES = {"red": "Red", "green": "Green", "yellow": "Yellow", "blue": "Blue"}


def load_terms(cfg: dict) -> dict:
    """id -> term dict (with 'module'), first glossary wins; modules follow cfg order."""
    terms: dict = {}
    for mod, info in cfg["modules"].items():
        g = yaml.safe_load((KIT / info["glossary"]).read_text(encoding="utf-8"))
        for t in g["terms"]:
            if t["id"] not in terms:
                terms[t["id"]] = dict(t, module=mod, source_bank=g.get("bank_id", info["glossary"]))
    return terms


def term_names(title: str) -> list[str]:
    """Ways a definition may name its own term: full title, title without (ABBR), the ABBR, singular."""
    names = {title}
    m = re.match(r"^(.*?)\s*\(([^)]+)\)\s*$", title)
    if m:
        names.update({m.group(1), m.group(2)})
    for n in list(names):
        if n.lower().endswith("ies"):
            names.add(n[:-3] + "y")
        elif n.lower().endswith("s") and len(n) > 3:
            names.add(n[:-1])
    if title.lower().startswith("extraction, transformation"):
        names.add("ETL")
    return sorted(names, key=len, reverse=True)


def blank(definition: str, title: str) -> str:
    out = definition
    for n in term_names(title):
        out = re.sub(r"(?<![\w-])" + re.escape(n) + r"(?![\w-])", "_____", out, flags=re.I)
    out = re.sub(r"(_____[\s,]*)+_____", "_____", out)
    out = out.replace("_____ (_____)", "_____")
    out = re.sub(r"^(An?|The)\s+_____", "_____", out)
    return out


def leaks(front: str, title: str) -> list[str]:
    """Names of the term still on the front. (Single shared words such as 'database' in
    'graph database' are fine: the textbook's definition uses them, and so will the exam.)"""
    return [n for n in term_names(title)
            if re.search(r"(?<![\w-])" + re.escape(n) + r"(?![\w-])", front, re.I)]


def fence(title: str, meta: str, size: str, band: str, cards: list[dict]) -> str:
    lines = ["```lnk-deck", f"title: {title}", f"meta: {meta}", f"size: {size}", f"band: {band}"]
    for c in cards:
        lines.append("---")
        for k in ("tag", "q", "a", "why", "back_tag", "band", "hint"):
            if c.get(k):
                lines.append(f"{k if k not in ('q', 'a') else k.upper()}: {c[k]}")
    lines.append("```")
    return "\n".join(lines)


def main() -> int:
    cfg = yaml.safe_load((HERE / "cards.yaml").read_text(encoding="utf-8"))
    terms = load_terms(cfg)
    mods = cfg["modules"]
    problems: list[str] = []
    home: dict = {}          # id -> (band, where)

    # Red decks
    red_decks = []
    for mod, ids in cfg["red"].items():
        cards = []
        for tid in ids:
            t = terms.get(tid)
            if not t:
                problems.append(f"red list {mod}: unknown term id '{tid}'")
                continue
            if t["module"] != mod:
                problems.append(f"red list {mod}: '{tid}' comes from {t['module']}")
            front = cfg.get("red_fronts", {}).get(tid) or blank(t["definition"], t["title"])
            bad = leaks(front, t["title"])
            if bad and tid not in cfg.get("red_fronts", {}):
                problems.append(f"red card '{tid}': front still names the term ({', '.join(bad)}). "
                                f"Add a red_fronts entry. Front: {front}")
            back = cfg.get("red_backs", {}).get(tid) or t["title"]
            back = back[0].upper() + back[1:]
            cards.append({"tag": mods[mod]["short"], "q": front, "a": back, "hint": "Name the term"})
            home.setdefault(tid, ("red", f"{mods[mod]['short'].title()} red deck"))
        red_decks.append((mod, cards))

    # Concept decks
    concept = {"green": [], "screen": [], "yellow": [], "blue": []}
    for i, c in enumerate(cfg["concept_cards"], 1):
        mod = c["module"]
        why = c.get("why", "")
        if c.get("check"):
            why = (why + " " if why else "") + "This list is from the Bidgoli chapter, not the course glossary: check it against your book."
        card = {"tag": mods[mod]["short"], "q": c["q"], "a": c["a"], "why": why, "band": c["band"]}
        concept[c.get("deck") or c["band"]].append(card)
        for tid in c.get("terms") or []:
            if tid not in terms:
                problems.append(f"concept card {i} ('{c['q'][:40]}'): unknown term id '{tid}'")
                continue
            short = c["q"] if len(c["q"]) <= 70 else c["q"][:67].rsplit(" ", 1)[0] + "…"
            home.setdefault(tid, (c["band"], short))

    for tid, t in terms.items():
        if tid not in home:
            problems.append(f"term '{tid}' ({t['module']}) has no card: add it to `red` or to a concept card")

    every_card = [c for _, cs in red_decks for c in cs] + [c for cs in concept.values() for c in cs]
    for c in every_card:
        for k, v in c.items():
            if re.search(r"(^|\n)\s*(---|```)", str(v)) or "\n" in str(v):
                problems.append(f"card text would break the fence: {k}: {v[:60]}")

    if problems:
        for p in problems:
            print("FAIL", p)
        return 1

    # ---- narrative.md
    n_red = sum(len(cs) for _, cs in red_decks)
    n_con = sum(len(cs) for cs in concept.values())
    out = [
        "# ITM 310 Exam 2: Study Cards",
        "",
        f"Every key term the Exam 2 study guide and review deck point to, sorted into the four "
        f"rubber bands and turned into cards: {len(terms)} terms, {n_red + n_con} cards. The cards come "
        "from Bidgoli Modules 3, 9, 4, 5 and 6, Knaflic Chapter 1, and the CRISP-DM and Power BI "
        "lectures. Definitions follow the course glossary and the class slides; nothing here is a "
        "rival definition.",
        "",
        "Each band asks for a different kind of study, so each gets its own deck.",
        "",
        "| Band | What goes in it | Card | How to study it |",
        "|---|---|---|---|",
        "| Red | Terms you only need to recognize | 3x5 | Fast. Read the definition, say the term, flip. If you hesitate, the card goes back in. Short bursts, twice a day, in the last two days. |",
        "| Green | The parts of a system and what each part does | 4x6 | Say every part out loud before you flip. Missing one part counts as a miss. |",
        "| Yellow | Look-alikes you have to tell apart | 4x6 | Say the difference in one sentence. The exam's wrong answers are usually the other look-alike. |",
        "| Blue | Order, and getting from a situation to the answer | 4x6 | Put the steps in order, or reason from the clue to the answer, then check. |",
        "",
        "Every card works the same way: click the card or press Space to flip it, and use the arrow "
        "keys or the buttons to move. Shuffle mixes the deck. The sort sheet at the bottom lists "
        "every term with its band, which is a good start on your one-page note sheet.",
        "",
        "## Red cards: recognize the term",
        "",
    ]
    for mod, cards in red_decks:
        out += [fence(f"Red · {mods[mod]['label']}", f"{len(cards)} cards · definition on the front, term on the back",
                      "3x5", "red", cards), ""]
    out += ["## Green cards: name the parts", "",
            fence("Green · parts of a system", f"{len(concept['green'])} cards · say every part before you flip",
                  "4x6", "green", concept["green"]), "",
            "The Power BI screen labels from the study guide (A to Q) have their own deck. Picture the "
            "Power BI Desktop window as you go: left-hand navigation, ribbon, canvas, then the panes on the right.",
            "",
            fence("Green · the Power BI screen, A to Q", f"{len(concept['screen'])} cards · labels from the study guide",
                  "3x5", "green", concept["screen"]), "",
            "## Yellow cards: tell them apart", "",
            fence("Yellow · look-alikes", f"{len(concept['yellow'])} cards · say the difference in one sentence",
                  "4x6", "yellow", concept["yellow"]), "",
            "## Blue cards: order and reasoning", "",
            fence("Blue · order and reasoning", f"{len(concept['blue'])} cards · reason it out, then flip",
                  "4x6", "blue", concept["blue"]), "",
            "## Sort sheet: every term and its band", "",
            "Each term appears once, in its home band. Highlighted terms show the course definition "
            "when you hover over them, and the glossary on the side lists them all.", ""]
    for mod, info in mods.items():
        rows = [(tid, t) for tid, t in terms.items() if t["module"] == mod]
        if not rows:
            continue
        out += [f"**{info['label']}** ({len(rows)} terms)", "", "| Term | Band | Card |", "|---|---|---|"]
        order = {"red": 0, "green": 1, "yellow": 2, "blue": 3}
        rows.sort(key=lambda r: (order[home[r[0]][0]], r[1]["title"].lower()))
        for tid, t in rows:
            band, where = home[tid]
            out.append(f"| [[{tid}|{t['title']}]] | {BAND_NAMES[band]} | {where} |")
        out.append("")
    checks = [c for c in cfg["concept_cards"] if c.get("check")]
    out += ["## Before you trust a card", "",
            f"{len(checks)} cards carry lists the course glossary doesn't spell out, such as the five "
            "parts of a DBMS or the four Rs of case-based reasoning. They come from the Bidgoli chapters "
            "and say so on the back. Check them against your book.",
            "",
            "The review deck and the study guide disagree on the name of the third view icon (label C). "
            "The study guide's key says Data View; slide 47 says Model View, and slide 46 says "
            "Relationships View. The C card gives Model view and says why. Ask your instructor which "
            "answer the exam will accept.",
            "",
            "The Knaflic definitions are working summaries of Chapter 1, because the study guide names "
            "the ideas without defining them. Read them against the chapter.",
            "",
            "Review deck slide 20 dates the Children's Online Privacy Protection Act to 1988. The act "
            "is from 1998. No card asks for the year.",
            "",
            "Some study-guide objectives have no card yet, because the course materials we have don't "
            "list them. They include the three recent trends in database design, the categories of "
            "natural-language processing, the five benefits of adding AI to decision support systems, "
            "AI's effect on automation, and the ethical issues of AI. Fill these in from the Bidgoli "
            "chapters.",
            ""]
    (HERE / "narrative.md").write_text("\n".join(out), encoding="utf-8")

    # ---- glossary.yaml (only fields the kit's glossary format uses)
    keep = ("id", "title", "definition", "context", "status", "tags", "tier", "refs")
    gl_terms = []
    for tid, t in terms.items():
        g = {k: t[k] for k in keep if t.get(k)}
        g["tags"] = list(dict.fromkeys((t.get("tags") or []) + [f"band-{home[tid][0]}"]))
        g.setdefault("tier", "exam")
        g["refs"] = list(dict.fromkeys((t.get("refs") or []) + [f"Glossary: examples/{t['source_bank']}"]))
        gl_terms.append(g)
    gloss = {"bank_id": cfg["unit_id"], "title": "ITM 310 Exam 2 study cards — glossary",
             "source": "Merged from the course glossaries listed in cards.yaml (MindTap MIS export, "
                       "ITM 310 Week 7 slides, Exam 2 study guide and review deck). Generated by build_cards.py.",
             "terms": gl_terms}
    header = "# GENERATED by build_cards.py from cards.yaml. Do not edit by hand.\n"
    (HERE / "glossary.yaml").write_text(header + yaml.safe_dump(gloss, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")

    # ---- review.yaml (one card per term, same shape as other units)
    review = {"deck_id": cfg["unit_id"], "cards": [
        {"id": g["id"], "prompt": g["title"], "answer": g["definition"], "tags": g["tags"], "tier": g["tier"]}
        for g in gl_terms]}
    (HERE / "review.yaml").write_text(header + yaml.safe_dump(review, sort_keys=False, allow_unicode=True, width=1000), encoding="utf-8")

    counts = {b: sum(1 for v in home.values() if v[0] == b) for b in BAND_NAMES}
    print(f"OK: {len(terms)} terms ({', '.join(f'{k} {v}' for k, v in counts.items())}); "
          f"{n_red} red cards, {n_con} concept cards")
    return 0


if __name__ == "__main__":
    sys.exit(main())
