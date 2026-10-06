#!/usr/bin/env python3
"""Render one A-Z glossary page for a whole track.

Usage:
  python tools/render_glossary.py tracks/<track>.yaml

Writes docs/<track_id>/glossary/index.html from every unit's glossary.yaml, in
track order. Terms with the same name in several chapters become one entry with a
link to each chapter; if their definitions differ, each is shown with its
chapter. Each link opens the chapter at the term (chapter/#term=<id>), which
docs/unit.js scrolls to and highlights. Never hand-edit the output; re-run this
after any glossary or track change.
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from collections import OrderedDict
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required. Try: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt")

from _track import flat_units, load_track  # noqa: E402  (needs yaml)

KIT_ROOT = Path(__file__).resolve().parent.parent


def _norm(t: str) -> str:
    return re.sub(r"[^a-z0-9%]+", " ", t.lower()).strip()


def entry_keys(title: str) -> list[str]:
    """Every name a term goes by: 'Extraction, transformation, and loading (ETL)' is
    known as both the spelled-out form and 'etl'. Entries sharing any name merge."""
    t = title.strip()
    m = re.match(r"^(.*?)\s*\(([^)]*)\)\s*$", t)
    keys = [_norm(m.group(1)), _norm(m.group(2))] if m else [_norm(t)]
    return [k for k in keys if k]


def entry_key(title: str) -> str:
    return entry_keys(title)[0]


def cap(s: str) -> str:
    return s[:1].upper() + s[1:]


def sort_key(title: str) -> tuple:
    t = title.strip().lower()
    return (0 if t[:1].isalpha() else 1, re.sub(r"[^a-z0-9 ]", "", t))


def short_labels(units: list[dict]) -> dict[str, str]:
    """'MIS 3 · Data and…' -> 'MIS 3'; fall back to two parts when the first repeats."""
    first = {u["id"]: u.get("module", u["id"]).split(" · ")[0] for u in units}
    counts: dict[str, int] = {}
    for v in first.values():
        counts[v] = counts.get(v, 0) + 1
    out = {}
    for u in units:
        parts = u.get("module", u["id"]).split(" · ")
        out[u["id"]] = first[u["id"]] if counts[first[u["id"]]] == 1 else " · ".join(parts[:2])
    return out


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Glossary</title>
  <style>
    :root {{
      --bg: #0f172a; --surface: #1e293b; --surface-border: #334155;
      --text-main: #e2e8f0; --text-muted: #94a3b8; --primary: #38bdf8;
      --exam: #38bdf8; --support: #a78bfa;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg); color: var(--text-main); line-height: 1.55; padding: 2rem 1.25rem 4rem;
    }}
    .wrap {{ max-width: 820px; margin: 0 auto; }}
    a {{ color: var(--primary); }}
    .crumb {{ font-size: 0.82rem; margin-bottom: 1.1rem; }}
    .crumb a {{ text-decoration: none; }}
    h1 {{ font-size: 1.75rem; color: #fff; letter-spacing: -0.02em; line-height: 1.25; }}
    .sub {{ color: var(--primary); font-weight: 600; margin: 0.2rem 0 0.6rem; }}
    .lede {{ color: var(--text-muted); font-size: 0.93rem; margin-bottom: 1.25rem; }}
    .tools {{
      position: sticky; top: 0; z-index: 5; background: var(--bg);
      padding: 0.75rem 0 0.6rem; border-bottom: 1px solid var(--surface-border); margin-bottom: 1.25rem;
    }}
    .row {{ display: flex; gap: 0.5rem; flex-wrap: wrap; align-items: center; }}
    #q {{
      flex: 1 1 240px; padding: 0.6rem 0.75rem; border-radius: 8px; border: 1px solid var(--surface-border);
      background: #0b1220; color: #fff; font-size: 0.95rem;
    }}
    #q:focus {{ outline: 2px solid var(--primary); outline-offset: 1px; }}
    .tier {{ display: flex; gap: 0.35rem; }}
    .tier button {{
      padding: 0.5rem 0.7rem; border-radius: 8px; border: 1px solid var(--surface-border);
      background: #0b1220; color: var(--text-muted); font-size: 0.82rem; font-weight: 600; cursor: pointer;
    }}
    .tier button[aria-pressed="true"] {{ border-color: var(--primary); color: #fff; background: rgba(56,189,248,0.15); }}
    .letters {{ display: flex; flex-wrap: wrap; gap: 0.15rem; margin-top: 0.6rem; }}
    .letters a {{
      display: inline-block; min-width: 1.7rem; text-align: center; padding: 0.15rem 0.2rem; border-radius: 5px;
      text-decoration: none; font-size: 0.82rem; font-weight: 600;
    }}
    .letters a:hover {{ background: var(--surface); }}
    .letters span {{ display: inline-block; min-width: 1.7rem; text-align: center; font-size: 0.82rem; color: #475569; }}
    .count {{ font-size: 0.8rem; color: var(--text-muted); margin-top: 0.45rem; }}
    section {{ margin-bottom: 1.6rem; scroll-margin-top: 9.5rem; }}
    section > h2 {{
      font-size: 1.05rem; color: var(--primary); border-bottom: 1px solid var(--surface-border);
      padding-bottom: 0.25rem; margin-bottom: 0.4rem;
    }}
    dl {{ display: block; }}
    .entry {{ padding: 0.7rem 0; border-bottom: 1px solid rgba(51,65,85,0.5); }}
    .entry:last-child {{ border-bottom: none; }}
    dt {{ font-weight: 650; color: #fff; font-size: 1rem; }}
    .badge {{
      display: inline-block; margin-left: 0.4rem; font-size: 0.64rem; font-weight: 700; letter-spacing: 0.05em;
      text-transform: uppercase; padding: 1px 6px; border-radius: 4px; vertical-align: 2px;
    }}
    .badge.exam {{ color: var(--exam); background: rgba(56,189,248,0.12); }}
    .badge.support {{ color: var(--support); background: rgba(167,139,250,0.12); }}
    dd {{ margin: 0.25rem 0 0; font-size: 0.92rem; }}
    dd .ctx {{ color: var(--text-muted); font-size: 0.85rem; margin-top: 0.15rem; }}
    dd + dd {{ margin-top: 0.5rem; }}
    .def-from {{ font-size: 0.72rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); }}
    .in {{ margin-top: 0.4rem; display: flex; flex-wrap: wrap; gap: 0.35rem; align-items: center; font-size: 0.78rem; color: var(--text-muted); }}
    .in a {{
      text-decoration: none; padding: 0.15rem 0.5rem; border-radius: 999px; border: 1px solid var(--surface-border);
      background: var(--surface); color: var(--text-main); font-size: 0.78rem;
    }}
    .in a:hover {{ border-color: var(--primary); }}
    .hidden {{ display: none !important; }}
    #none {{ color: var(--text-muted); padding: 1rem 0; }}
    @media (max-width: 480px) {{ body {{ padding: 1.25rem 1rem 3rem; }} h1 {{ font-size: 1.45rem; }} }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="crumb"><a href="../">&larr; Contents</a> · <a href="../../">All tracks</a></div>
    <h1>{title}</h1>
    <p class="sub">Glossary of every term</p>
    <p class="lede">{n_entries} terms from {n_units} chapters, A to Z. Each chapter link opens the
      story at the spot where the term is used.</p>
    <div class="tools" role="search">
      <div class="row">
        <input id="q" type="search" placeholder="Search terms and definitions…" autocomplete="off" aria-label="Search the glossary">
        <div class="tier" role="group" aria-label="Which terms">
          <button type="button" data-tier="all" aria-pressed="true">All</button>
          <button type="button" data-tier="exam" aria-pressed="false">Exam only</button>
        </div>
      </div>
      <nav class="letters" aria-label="Jump to letter">{letters}</nav>
      <div class="count" id="count" aria-live="polite"></div>
    </div>
    <p id="none" class="hidden">No terms match.</p>
{sections}
  </div>
<script>
(function () {{
  var q = document.getElementById('q'), count = document.getElementById('count');
  var none = document.getElementById('none');
  var entries = Array.prototype.slice.call(document.querySelectorAll('.entry'));
  var sections = Array.prototype.slice.call(document.querySelectorAll('section'));
  var tier = 'all';
  entries.forEach(function (e) {{ e._text = e.textContent.toLowerCase(); }});
  function apply() {{
    var words = q.value.toLowerCase().split(/\\s+/).filter(Boolean), shown = 0;
    entries.forEach(function (e) {{
      var ok = words.every(function (w) {{ return e._text.indexOf(w) !== -1; }});
      if (tier === 'exam' && e.getAttribute('data-exam') !== '1') ok = false;
      e.classList.toggle('hidden', !ok);
      if (ok) shown++;
    }});
    sections.forEach(function (s) {{
      s.classList.toggle('hidden', !s.querySelector('.entry:not(.hidden)'));
    }});
    none.classList.toggle('hidden', shown !== 0);
    count.textContent = shown === entries.length ? entries.length + ' terms' : shown + ' of ' + entries.length + ' terms';
  }}
  q.addEventListener('input', apply);
  document.querySelectorAll('.tier button').forEach(function (b) {{
    b.addEventListener('click', function () {{
      tier = b.getAttribute('data-tier');
      document.querySelectorAll('.tier button').forEach(function (x) {{
        x.setAttribute('aria-pressed', x === b ? 'true' : 'false');
      }});
      apply();
    }});
  }});
  apply();
}})();
</script>
</body>
</html>
"""


def render_glossary(manifest: Path, kit_root: Path = KIT_ROOT) -> Path:
    track = load_track(manifest)
    units = flat_units(track)
    labels = short_labels(units)
    entries: "OrderedDict[int, dict]" = OrderedDict()
    alias: dict[str, int] = {}
    for u in units:
        unit_dir = kit_root / "examples" / u["id"]
        meta = yaml.safe_load((unit_dir / "unit.yaml").read_text(encoding="utf-8"))
        chapter = (meta.get("title") or u["id"]).split(" — ", 1)[-1]
        gloss = yaml.safe_load((unit_dir / "glossary.yaml").read_text(encoding="utf-8"))
        for t in gloss["terms"]:
            keys = entry_keys(t["title"])
            hits = sorted({alias[k] for k in keys if k in alias})
            if hits:
                eid = hits[0]
                for other in hits[1:]:          # this title joins two entries: fold them
                    e2 = entries.pop(other)
                    entries[eid]["titles"] += e2["titles"]
                    entries[eid]["uses"] += e2["uses"]
                    for k, v in list(alias.items()):
                        if v == other:
                            alias[k] = eid
            else:
                eid = len(alias) + len(entries) + 1
                entries[eid] = {"titles": [], "uses": []}
            for k in keys:
                alias[k] = eid
            e = entries[eid]
            e["titles"].append(t["title"])
            e["uses"].append({
                "unit": u["id"], "label": labels[u["id"]], "chapter": chapter, "id": t["id"], "title": t["title"],
                "definition": (t.get("definition") or "").strip(), "context": (t.get("context") or "").strip(),
                "tier": t.get("tier", "exam"),
            })

    def display_title(e):  # prefer the fullest form, e.g. "Key performance indicator (KPI)"
        return cap(max(e["titles"], key=lambda s: (("(" in s), len(s))))

    ordered = sorted(entries.values(), key=lambda e: sort_key(display_title(e)))
    groups: "OrderedDict[str, list]" = OrderedDict()
    for e in ordered:
        first = display_title(e).strip()[:1].upper()
        groups.setdefault(first if first.isalpha() else "#", []).append(e)

    sections, present = [], set(groups)
    for letter, items in groups.items():
        anchor = "num" if letter == "#" else letter
        rows = []
        for e in items:
            title = display_title(e)
            tiers = {x["tier"] for x in e["uses"]}
            exam = "exam" in tiers
            badge = "exam" if exam else "support"
            defs, seen = [], OrderedDict()
            for x in e["uses"]:
                seen.setdefault(x["definition"], []).append(x)
            for definition, xs in seen.items():
                ctx = next((x["context"] for x in xs if x["context"]), "")
                from_ = ""
                if len(seen) > 1:
                    names = []
                    for x in xs:
                        same_unit = sum(1 for y in e["uses"] if y["unit"] == x["unit"]) > 1
                        names.append(f'{cap(x["title"])} · {x["label"]}' if same_unit else x["label"])
                    from_ = f'<div class="def-from">{html.escape(", ".join(names))}</div>'
                defs.append(
                    f"<dd>{from_}{html.escape(definition)}"
                    + (f'<div class="ctx">{html.escape(ctx)}</div>' if ctx else "")
                    + "</dd>"
                )
            links, linked = [], set()
            for x in e["uses"]:
                if x["unit"] in linked:          # one chip per chapter; it opens the first variant
                    continue
                linked.add(x["unit"])
                links.append(
                    f'<a href="../../{x["unit"]}/#term={html.escape(x["id"])}" '
                    f'title="{html.escape(x["chapter"])}">{html.escape(x["label"])} · {html.escape(x["chapter"])}</a>'
                )
            links = "".join(links)
            rows.append(
                f'      <div class="entry" data-exam="{1 if exam else 0}">'
                f'<dt>{html.escape(title)}<span class="badge {badge}">{badge}</span></dt>'
                f'{"".join(defs)}<div class="in">In: {links}</div></div>'
            )
        sections.append(
            f'    <section id="{anchor}" aria-labelledby="h-{anchor}">\n'
            f'      <h2 id="h-{anchor}">{html.escape(letter)}</h2>\n      <dl>\n'
            + "\n".join(rows) + "\n      </dl>\n    </section>"
        )
    letters = "".join(
        f'<a href="#{"num" if L == "#" else L}">{L}</a>' if L in present else f"<span>{L}</span>"
        for L in [chr(c) for c in range(ord("A"), ord("Z") + 1)] + ["#"]
    )
    page = PAGE.format(
        title=html.escape(track.get("title") or track["track_id"]),
        n_entries=len(ordered), n_units=len(units), letters=letters, sections="\n".join(sections),
    )
    out_dir = kit_root / "docs" / track["track_id"] / "glossary"
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "index.html"
    out.write_text(page, encoding="utf-8")
    n_uses = sum(len(e["uses"]) for e in ordered)
    print(f"Wrote {out} ({len(ordered)} terms, {n_uses} chapter uses, {len(units)} chapters)")
    return out


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Render a track's A-Z glossary page")
    parser.add_argument("manifest", type=Path)
    render_glossary(parser.parse_args(argv).manifest)


if __name__ == "__main__":
    main()
