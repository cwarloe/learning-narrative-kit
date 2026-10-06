#!/usr/bin/env python3
"""Render a track manifest to a table-of-contents page for GitHub Pages.

Usage:
  python tools/render_track.py tracks/<track>.yaml

Writes docs/<track_id>/index.html. Never hand-edit the output; edit the manifest
(order, part headings, blurbs) and re-run. After changing a track's order, also
re-render its units so their Previous / Next links follow.
"""
from __future__ import annotations

import argparse
import html
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit(
        "PyYAML is required. Try:\n"
        "  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt"
    )

from _track import flat_units, load_track  # noqa: E402  (needs yaml)

KIT_ROOT = Path(__file__).resolve().parent.parent

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <style>
    :root {{
      --bg: #0f172a; --surface: #1e293b; --surface-border: #334155;
      --text-main: #e2e8f0; --text-muted: #94a3b8; --primary: #38bdf8;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background: var(--bg); color: var(--text-main); line-height: 1.6;
      min-height: 100vh; padding: 2rem 1.25rem;
    }}
    .wrap {{ max-width: 760px; margin: 0 auto; }}
    .crumb {{ font-size: 0.82rem; margin-bottom: 1.25rem; }}
    .crumb a, .start {{ color: var(--primary); text-decoration: none; }}
    .crumb a:hover {{ text-decoration: underline; }}
    h1 {{ font-size: 1.8rem; color: #fff; letter-spacing: -0.02em; margin-bottom: 0.5rem; line-height: 1.25; }}
    .sub {{ color: var(--primary); font-size: 1rem; font-weight: 600; margin: -0.2rem 0 0.75rem; }}
    .lede {{ color: var(--text-muted); font-size: 0.97rem; margin-bottom: 1rem; }}
    .stats {{ color: var(--text-muted); font-size: 0.85rem; margin-bottom: 1.25rem; }}
    .start {{
      display: inline-block; border: 1px solid var(--primary); border-radius: 8px;
      padding: 0.55rem 1rem; font-weight: 600; margin-bottom: 2rem;
    }}
    .start:hover {{ background: rgba(56, 189, 248, 0.12); }}
    section {{ margin-bottom: 2.25rem; }}
    h2 {{
      font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.08em;
      color: var(--primary); font-weight: 700; margin-bottom: 0.3rem;
    }}
    .part-lede {{ color: var(--text-muted); font-size: 0.88rem; margin-bottom: 0.9rem; }}
    ol {{ list-style: none; display: flex; flex-direction: column; gap: 0.7rem; }}
    a.ch {{
      display: grid; grid-template-columns: 2.4rem 1fr; gap: 0 0.9rem;
      background: var(--surface); border: 1px solid var(--surface-border); border-radius: 10px;
      padding: 0.95rem 1.1rem; text-decoration: none; color: var(--text-main);
      transition: border-color 0.15s, background 0.15s;
    }}
    a.ch:hover {{ border-color: var(--primary); background: #243044; }}
    .num {{
      grid-row: span 4; font-size: 1.35rem; font-weight: 700; color: var(--primary);
      font-variant-numeric: tabular-nums; line-height: 1.3;
    }}
    .mod {{ font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-muted); }}
    .t {{ font-weight: 600; color: #fff; font-size: 1.05rem; }}
    .blurb {{ font-size: 0.9rem; margin-top: 0.15rem; }}
    .meta {{ font-size: 0.78rem; color: var(--text-muted); margin-top: 0.3rem; }}
    footer {{ font-size: 0.78rem; color: var(--text-muted); border-top: 1px solid var(--surface-border); padding-top: 1rem; }}
    @media (max-width: 480px) {{
      body {{ padding: 1.25rem 1rem; }}
      h1 {{ font-size: 1.45rem; }}
      a.ch {{ grid-template-columns: 1.9rem 1fr; padding: 0.85rem 0.9rem; }}
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="crumb"><a href="../">&larr; All tracks</a></div>
    <h1>{title}</h1>
{subtitle}    <p class="lede">{description}</p>
    <p class="stats">{n_units} chapters · {n_terms} terms · about {hours} hours of reading</p>
    <a class="start" href="../{first}/">Start with chapter 1 &rarr;</a>{glossary_link}
{sections}
    <footer>Each chapter page has Previous / Next links and a link back here. Hover a highlighted term in any story for its course definition.</footer>
  </div>
</body>
</html>
"""


def render_track(manifest: Path, kit_root: Path = KIT_ROOT) -> Path:
    track = load_track(manifest)
    units = flat_units(track)
    number = {u["id"]: i + 1 for i, u in enumerate(units)}
    total_terms = total_minutes = 0
    sections = []
    for part in track["parts"]:
        items = []
        for u in part.get("units") or []:
            unit_dir = kit_root / "examples" / u["id"]
            if not (unit_dir / "unit.yaml").is_file():
                raise SystemExit(f"{manifest}: no unit at {unit_dir}")
            meta = yaml.safe_load((unit_dir / "unit.yaml").read_text(encoding="utf-8"))
            gloss = yaml.safe_load((unit_dir / "glossary.yaml").read_text(encoding="utf-8"))
            n_terms = len(gloss.get("terms") or [])
            minutes = int(meta.get("estimated_minutes") or 0)
            total_terms += n_terms
            total_minutes += minutes
            title = (meta.get("title") or u["id"]).split(" — ", 1)[-1]
            items.append(
                f'        <li><a class="ch" href="../{u["id"]}/">'
                f'<span class="num">{number[u["id"]]}</span>'
                f'<span class="mod">{html.escape(u.get("module", ""))}</span>'
                f'<span class="t">{html.escape(title)}</span>'
                f'<span class="blurb">{html.escape(u.get("blurb", ""))}</span>'
                f'<span class="meta">{n_terms} terms · ~{minutes} min</span>'
                "</a></li>"
            )
        lede = part.get("lede")
        sections.append(
            "    <section>\n"
            f"      <h2>{html.escape(part.get('title', ''))}</h2>\n"
            + (f'      <p class="part-lede">{html.escape(lede)}</p>\n' if lede else "")
            + "      <ol>\n" + "\n".join(items) + "\n      </ol>\n    </section>"
        )
    page = PAGE.format(
        title=html.escape(track.get("title") or track["track_id"]),
        subtitle=(f'    <p class="sub">{html.escape(track["subtitle"])}</p>\n' if track.get("subtitle") else ""),
        description=html.escape(track.get("description") or ""),
        n_units=len(units),
        n_terms=total_terms,
        hours=round(total_minutes / 60, 1),
        first=units[0]["id"],
        glossary_link=(' <a class="start" href="glossary/">Glossary: every term, A&ndash;Z</a>' if track.get("glossary") else ""),
        sections="\n".join(sections),
    )
    out_dir = kit_root / "docs" / track["track_id"]
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "index.html"
    out.write_text(page, encoding="utf-8")
    print("Wrote", out, f"({len(units)} units)")
    return out


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Render tracks/<track>.yaml to docs/<track_id>/index.html")
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args(argv)
    render_track(args.manifest)


if __name__ == "__main__":
    main()
