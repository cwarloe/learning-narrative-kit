#!/usr/bin/env python3
"""Theme check: every color, font and corner on the site comes from a tokens file.

Usage:
  python3 tools/check_theme.py          list findings, exit 1 if any

The rule and how to change the look: docs/THEMING.md.

Looks for, outside the tokens files:
  - hex colors (#abc, #aabbcc), rgb()/rgba()/hsl()/hsla(), and colors inside data-URI images (%23abc)
  - font families written out instead of var(--font-...)
  - border-radius in px instead of var(--radius-...)

Where it looks:
  - every .css, .html and .js file under docs/ and template/ (generated pages included, so a renderer
    that slips in a raw value is caught after it runs)
  - the renderers that write those pages (RENDERERS below), so a raw value is caught before it ships
  - Portland Desk markdown, but only inside style="..." attributes, where a raw value would land on the page

A line that really needs a literal says why with a comment containing "theme-ok: <reason>".
@font-face lines are skipped (they name a font file, they don't style anything).
EXEMPT pages are listed with their counts, not failed. Each has a reason.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# The files allowed to hold raw values. docs/tokens.css serves the published site;
# template/assets/tokens.css is the copy a new Docsify course starts from.
TOKENS = {"docs/tokens.css", "template/assets/tokens.css"}

# Source files that write HTML or CSS into docs/.
RENDERERS = [
    "tools/build_hub_index.py",
    "tools/render_unit.py",
    "tools/_unit_page_template.py",
    "tools/render_track.py",
    "tools/render_glossary.py",
    "tools/_track.py",
    "tools/_deck.py",
    "tools/_workbench.py",
]

# Reviewed exceptions: listed with a count, not failed.
EXEMPT = {
    # Design mockups: options that haven't been picked, each with its own proposed look.
    # When one is chosen, move its values into tokens.css and drop it from this list.
    "docs/comic_card_mockup.html": "design mockup, not picked yet",
    "docs/handcrafted_cards_mockup.html": "design mockup, not picked yet",
    # A 1280x720 storyboard that a separate playbook records to .mp4. It mimics Wireshark's screen,
    # keeps its colors in its own :root block, and a token change could not reach the recorded video.
    "docs/portland-desk/assets/video/wireshark-find-the-conversation.html": "video storyboard, recorded to mp4",
}

# Markdown folders whose style="..." attributes reach the page.
MARKDOWN = ["docs/portland-desk"]

HEX = re.compile(r"(?<=[:\s,('\"=])#(?:[0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})(?=[;}\s,)!'\"]|$)")
FUNC = re.compile(r"\b(?:rgba?|hsla?)\(\s*[\d.]")
URI = re.compile(r"%23[0-9a-fA-F]{3,8}\b")
FONT = re.compile(r"\bfont(?:-family)?\s*:\s*([^;}{]*)")
FAMILY = re.compile(
    r"\"[^\"]+\"|'[^']+'|\b(?:serif|sans-serif|monospace|cursive|system-ui|ui-monospace|Arial|Helvetica|"
    r"Impact|Georgia|Verdana|Times|Consolas|Menlo|Monaco)\b"
)
RADIUS = re.compile(r"\bborder(?:-[a-z]+)?-radius\s*:\s*([^;}\"]*)")
STYLE_ATTR = re.compile(r"style=\"([^\"]*)\"|style='([^']*)'")


def line_hits(line: str) -> list[str]:
    hits = HEX.findall(line) + [m.rstrip("0123456789. ") + "(…)" for m in FUNC.findall(line)] + URI.findall(line)
    for m in FONT.finditer(line):
        value = m.group(1)
        if "var(--" not in value and FAMILY.search(value):
            hits.append("font: " + value.strip()[:40])
    for m in RADIUS.finditer(line):
        if re.search(r"(?<![\w-])\d*\.?\d+px", m.group(1)):
            hits.append("radius: " + m.group(1).strip()[:30])
    return hits


def scan_text(rel: str, text: str, markdown: bool = False) -> list[tuple[int, list[str]]]:
    out = []
    for i, raw in enumerate(text.split("\n"), 1):
        if "theme-ok:" in raw or "@font-face" in raw:
            continue
        if markdown:
            raw = " ".join(a or b for a, b in STYLE_ATTR.findall(raw))
            if not raw:
                continue
            raw = ";" + raw  # so a value at the start of the attribute still has a delimiter before it
        hits = line_hits(raw)
        if hits:
            out.append((i, hits))
    return out


def targets():
    for base in ("docs", "template"):
        for p in sorted((ROOT / base).rglob("*")):
            if p.suffix in (".css", ".html", ".js") and p.is_file():
                yield p, False
    for rel in RENDERERS:
        p = ROOT / rel
        if p.exists():
            yield p, False
    for base in MARKDOWN:
        for p in sorted((ROOT / base).rglob("*.md")):
            yield p, True


def scan():
    findings, exempt = [], {}
    for path, markdown in targets():
        rel = path.relative_to(ROOT).as_posix()
        if rel in TOKENS:
            continue
        results = scan_text(rel, path.read_text(encoding="utf-8"), markdown)
        if not results:
            continue
        if rel in EXEMPT:
            exempt[rel] = sum(len(h) for _, h in results)
            continue
        for ln, hits in results:
            findings.append(f"{rel}:{ln}  {', '.join(dict.fromkeys(hits))}")
    return findings, exempt


def main() -> int:
    findings, exempt = scan()
    for f in findings:
        print(f)
    if findings:
        print(f"\nFAIL: {len(findings)} line(s) use raw colors, fonts or corners. Use a token from docs/tokens.css "
              "(see docs/THEMING.md).")
    else:
        print("PASS: theme check, every page and renderer uses tokens.")
    if exempt:
        print("Exempt (not checked): " + ", ".join(f"{k} {v} [{EXEMPT[k]}]" for k, v in exempt.items()))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
