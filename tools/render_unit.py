#!/usr/bin/env python3
"""Render a learning-narrative unit dir to docs/<unit_id>/index.html.

Source of truth remains markdown + YAML. Generated HTML is a Pages artifact.

Usage:
  python tools/render_unit.py examples/secplus-ports-helpdesk
  python tools/render_unit.py examples/secplus-auth-helpdesk

Requires PyYAML (see Setup in AGENTS.md: python3 -m venv .venv).
"""
from __future__ import annotations

import argparse
import html
import json
import re
import sys
from pathlib import Path

from _unit_page_template import render_html

try:
    import yaml
except ImportError:
    sys.exit(
        "PyYAML is required. Try:\n"
        "  python3 -m venv .venv && .venv/bin/pip install -r requirements.txt\n"
        "then: .venv/bin/python tools/render_unit.py <unit_dir>"
    )

KIT_ROOT = Path(__file__).resolve().parent.parent
MARK_RE = re.compile(r"\[\[([a-z0-9_]+)\|([^\]]+)\]\]")


def load_glossary(path: Path):
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    terms = {}
    for t in data["terms"]:
        terms[t["id"]] = {
            "id": t["id"],
            "title": t["title"],
            "definition": t.get("definition", ""),
            "context": t.get("context"),
            "tier": t.get("tier", "exam"),
            "tags": t.get("tags") or [],
            "refs": t.get("refs") or [],
        }
    return data, terms


def escape_text(s: str) -> str:
    return html.escape(s, quote=False)


def escape_inline(s: str) -> str:
    """Escape HTML then apply light inline md: *em* and `code`."""
    s = escape_text(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)
    return s


def inline_md(text: str, terms: dict, used_ids: list) -> str:
    """Convert inline markdown + [[id|text]] marks; escape plain text."""
    parts = []
    pos = 0
    for m in MARK_RE.finditer(text):
        if m.start() > pos:
            parts.append(escape_inline(text[pos : m.start()]))
        tid = m.group(1)
        surface = m.group(2)
        used_ids.append(tid)
        if tid not in terms:
            raise SystemExit(f"Unknown glossary id in narrative: {tid!r}")
        tier = terms[tid]["tier"]
        parts.append(
            f'<span class="term {tier}" data-term="{html.escape(tid)}" '
            f'data-tier="{html.escape(tier)}">{escape_text(surface)}</span>'
        )
        pos = m.end()
    if pos < len(text):
        parts.append(escape_inline(text[pos:]))
    return "".join(parts)


def md_to_html(md: str, terms: dict):
    lines = md.splitlines()
    used_ids: list[str] = []
    title = None
    byline = None
    body_start = 0
    if lines and lines[0].startswith("# "):
        title = lines[0][2:].strip()
        body_start = 1
        while body_start < len(lines) and not lines[body_start].strip():
            body_start += 1
        if (
            body_start < len(lines)
            and lines[body_start].startswith("*")
            and lines[body_start].endswith("*")
        ):
            byline = lines[body_start].strip("*").strip()
            body_start += 1

    paras: list[str] = []
    buf: list[str] = []

    def flush_para():
        nonlocal buf
        if not buf:
            return
        text = " ".join(buf)
        paras.append(f"<p>{inline_md(text, terms, used_ids)}</p>")
        buf = []

    for line in lines[body_start:]:
        if not line.strip():
            flush_para()
            continue
        if line.startswith("## "):
            flush_para()
            heading = line[3:].strip()
            paras.append(f"<h2>{inline_md(heading, terms, used_ids)}</h2>")
            continue
        if line.startswith("# "):
            flush_para()
            heading = line[2:].strip()
            paras.append(f"<h1>{inline_md(heading, terms, used_ids)}</h1>")
            continue
        buf.append(line.strip())
    flush_para()

    return title, byline, "\n".join(paras), used_ids



def render_unit(unit_dir: Path, kit_root: Path | None = None, also_local: Path | None = None) -> Path:
    """Render unit_dir → docs/<unit_id>/index.html. Returns output path."""
    kit_root = kit_root or KIT_ROOT
    unit_dir = unit_dir.resolve()
    unit_path = unit_dir / "unit.yaml"
    narrative_path = unit_dir / "narrative.md"
    glossary_path = unit_dir / "glossary.yaml"

    for p in (unit_path, narrative_path, glossary_path):
        if not p.is_file():
            raise SystemExit(f"Missing required file: {p}")

    unit = yaml.safe_load(unit_path.read_text(encoding="utf-8"))
    unit_id = unit.get("unit_id")
    if not unit_id:
        raise SystemExit(f"unit.yaml missing unit_id: {unit_path}")

    _, terms = load_glossary(glossary_path)
    md = narrative_path.read_text(encoding="utf-8")
    title, byline, body_html, used_ids = md_to_html(md, terms)

    page_title = unit.get("title") or title or unit_id
    if byline:
        subtitle = byline
    else:
        subtitle = unit.get("audience") or "A learning narrative"

    missing = [u for u in used_ids if u not in terms]
    if missing:
        raise SystemExit(f"Missing glossary ids: {missing}")

    exam_marks = sum(1 for u in used_ids if terms[u]["tier"] == "exam")
    support_marks = sum(1 for u in used_ids if terms[u]["tier"] == "support")
    unique_used = sorted(set(used_ids))

    gloss_list = [
        terms[tid] for tid in sorted(terms.keys(), key=lambda k: terms[k]["title"].lower())
    ]
    gloss_json = json.dumps({t["id"]: t for t in gloss_list}, ensure_ascii=False, separators=(',', ':'))

    html_out = render_html(page_title, subtitle, body_html, gloss_json)

    out_dir = kit_root / "docs" / unit_id
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "index.html"
    out_path.write_text(html_out, encoding="utf-8")
    body = body_html.strip() + "\n"
    # Split large narratives so Pages artifacts stay MCP-push-friendly
    parts = []
    max_size = 15000
    if len(body) <= max_size:
        parts = [body]
    else:
        import re as _re
        chunks = _re.split(r"(?<=</p>)|(?<=</h2>)|(?<=</h1>)", body)
        buf = ""
        for c in chunks:
            if not c:
                continue
            if buf and len(buf) + len(c) > max_size:
                parts.append(buf)
                buf = c
            else:
                buf += c
        if buf:
            parts.append(buf)
        final = []
        for p in parts:
            while len(p) > max_size:
                final.append(p[:max_size])
                p = p[max_size:]
            if p:
                final.append(p)
        parts = final
    # Remove prior narrative parts
    for oldp in out_dir.glob("narrative*.html"):
        oldp.unlink()
    part_names = []
    for i, part in enumerate(parts):
        name = f"narrative.{i}.html" if len(parts) > 1 else "narrative.0.html"
        (out_dir / name).write_text(part, encoding="utf-8")
        part_names.append(name)
        print("Wrote", out_dir / name, len(part))
    import json as _json
    manifest = {"parts": part_names}
    (out_dir / "narrative.manifest.json").write_text(
        _json.dumps(manifest) + "\n", encoding="utf-8"
    )
    print("Wrote", out_dir / "narrative.manifest.json")
    gloss_js = "window.__GLOSSARY__ = " + gloss_json + ";\n"
    (out_dir / "glossary.js").write_text(gloss_js, encoding="utf-8")
    print("Wrote", out_dir / "glossary.js")

    if also_local is not None:
        also_local.write_text(html_out, encoding="utf-8")

    unused = sorted(set(terms.keys()) - set(used_ids))
    print("Wrote", out_path)
    if also_local is not None:
        print("Wrote", also_local)
    print(f"Marks total: {len(used_ids)} (exam={exam_marks}, support={support_marks})")
    print(f"Unique glossary ids used: {len(unique_used)} / {len(terms)}")
    if unused:
        print("Unused glossary ids:", ", ".join(unused))
    else:
        print("All glossary ids appear in narrative.")
    return out_path


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Render a unit directory to docs/<unit_id>/index.html"
    )
    parser.add_argument(
        "unit_dir",
        type=Path,
        help="Path to unit directory (must contain narrative.md + glossary.yaml + unit.yaml)",
    )
    parser.add_argument(
        "--kit-root",
        type=Path,
        default=None,
        help="Kit root (default: parent of tools/)",
    )
    args = parser.parse_args(argv)
    render_unit(args.unit_dir, kit_root=args.kit_root)


if __name__ == "__main__":
    main()
