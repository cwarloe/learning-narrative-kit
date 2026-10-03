"""Track manifests (tracks/*.yaml): reading order for a set of units.

Used by render_track.py (table-of-contents page) and render_unit.py (per-unit
Contents / Previous / Next links). A unit that is in no track renders as before.
"""
from __future__ import annotations

import html
from pathlib import Path

import yaml


def load_track(path: Path) -> dict:
    track = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(track, dict) or not track.get("track_id") or not track.get("parts"):
        raise SystemExit(f"{path}: track manifest needs track_id and parts")
    return track


def flat_units(track: dict) -> list[dict]:
    """All units in reading order, each annotated with its part title."""
    out = []
    for part in track["parts"]:
        for u in part.get("units") or []:
            out.append({**u, "part": part.get("title", "")})
    return out


def find_track_for(unit_id: str, kit_root: Path) -> dict | None:
    for path in sorted((kit_root / "tracks").glob("*.yaml")):
        track = load_track(path)
        if any(u["id"] == unit_id for u in flat_units(track)):
            return track
    return None


def unit_title(kit_root: Path, unit_id: str) -> str:
    unit = yaml.safe_load((kit_root / "examples" / unit_id / "unit.yaml").read_text(encoding="utf-8"))
    return unit.get("title") or unit_id


NAV_CSS = """
.track-nav { display: flex; flex-wrap: wrap; align-items: center; gap: 0.4rem 1rem;
  font-size: 0.82rem; color: var(--text-muted); margin-bottom: 1.25rem; }
.track-nav a { color: var(--primary); text-decoration: none; }
.track-nav a:hover { text-decoration: underline; }
.track-nav .pos { margin-left: auto; }
.track-pager { display: grid; grid-template-columns: 1fr 1fr; gap: 0.85rem;
  margin-top: 2.5rem; padding-top: 1.5rem; border-top: 1px solid var(--surface-border); }
.track-pager a { display: block; padding: 0.85rem 1rem; border: 1px solid var(--surface-border);
  border-radius: 10px; text-decoration: none; color: var(--text-main); background: var(--bg); }
.track-pager a:hover { border-color: var(--primary); }
.track-pager .dir { display: block; font-size: 0.72rem; text-transform: uppercase;
  letter-spacing: 0.06em; color: var(--text-muted); margin-bottom: 0.2rem; }
.track-pager .next { text-align: right; grid-column: 2; }
.track-pager .t { font-weight: 600; color: #fff; font-size: 0.95rem; }
@media (max-width: 600px) { .track-pager { grid-template-columns: 1fr; }
  .track-pager .next { grid-column: 1; } .track-nav .pos { margin-left: 0; } }
"""


def nav_html(track: dict, unit_id: str, kit_root: Path) -> tuple[str, str]:
    """Return (top bar, bottom pager) HTML for a unit page inside a track."""
    units = flat_units(track)
    idx = next(i for i, u in enumerate(units) if u["id"] == unit_id)
    me = units[idx]
    toc = f"../{track['track_id']}/"
    top = (
        '<nav class="track-nav" aria-label="Track">'
        f'<a href="{toc}">&larr; Contents</a>'
        f"<span>{html.escape(me.get('module', ''))}</span>"
        f'<span class="pos">Chapter {idx + 1} of {len(units)}</span>'
        "</nav>"
    )
    cells = []
    if idx > 0:
        p = units[idx - 1]
        cells.append(
            f'<a class="prev" href="../{p["id"]}/"><span class="dir">&larr; Previous</span>'
            f'<span class="t">{html.escape(unit_title(kit_root, p["id"]))}</span></a>'
        )
    if idx + 1 < len(units):
        n = units[idx + 1]
        cells.append(
            f'<a class="next" href="../{n["id"]}/"><span class="dir">Next &rarr;</span>'
            f'<span class="t">{html.escape(unit_title(kit_root, n["id"]))}</span></a>'
        )
    else:
        cells.append(
            f'<a class="next" href="{toc}"><span class="dir">Finished &rarr;</span>'
            '<span class="t">Back to contents</span></a>'
        )
    bottom = '<nav class="track-pager" aria-label="Chapter">' + "".join(cells) + "</nav>"
    return top, bottom
