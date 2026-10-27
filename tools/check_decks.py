#!/usr/bin/env python3
"""Check Docsify markdown for the two ways flashcard decks have broken.

1. HTML that markdown will show as a code block. A blank line ends a markdown HTML
   block; a following line indented 4+ spaces that starts with "<" is then rendered as
   a code block, so the raw HTML shows up as text. This is what reduced the Episode 00
   workbench deck to one card. Write decks as ```lnk-deck fences instead.
2. Malformed ```lnk-deck fences: no cards, a card without Q: or A:, an unknown size or
   band, or an unknown field. An unknown field is usually a continuation line that
   happens to start with "Word:"; its text would be dropped from the card.

Usage:
  python3 tools/check_decks.py [paths...]     (default: docs/portland-desk)
Exits 1 if any problem is found.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

KEY = re.compile(r"^([A-Za-z_]+):\s?(.*)$")
CARD_KEYS = {"q", "a", "why", "tag", "back_tag", "band", "hint"}
HEAD_KEYS = {"title", "meta", "size", "band"}
SIZES = {"3x5", "4x6"}
BANDS = {"red", "green", "yellow", "blue"}


def check_deck(path: Path, start: int, body: list[str]) -> list[str]:
    problems = []
    sections, cur, cur_start = [], [], start + 1
    for i, line in enumerate(body, start + 1):
        if re.match(r"^---[ \t]*$", line):
            sections.append((cur_start, cur))
            cur, cur_start = [], i + 1
        else:
            cur.append((i, line))
    sections.append((cur_start, cur))

    def fields(lines, allowed, where):
        out = {}
        for n, line in lines:
            m = KEY.match(line)
            if m:
                key = m.group(1).lower()
                if key not in allowed:
                    problems.append(f"{path}:{n}: unknown field '{m.group(1)}' in {where}. If this is a "
                                    "continuation of the line above, reword it so it doesn't start with 'Word:'")
                out[key] = m.group(2).strip()
        return out

    head_line, head = sections[0]
    h = fields(head, HEAD_KEYS, "deck header")
    if h.get("size", "3x5") not in SIZES:
        problems.append(f"{path}:{head_line}: size must be 3x5 or 4x6, not '{h['size']}'")
    if h.get("band", "red") not in BANDS:
        problems.append(f"{path}:{head_line}: band must be red, green, yellow, or blue, not '{h['band']}'")
    cards = 0
    for line_no, lines in sections[1:]:
        c = fields(lines, CARD_KEYS, "card")
        if not lines or not any(l.strip() for _, l in lines):
            continue
        cards += 1
        if not c.get("q"):
            problems.append(f"{path}:{line_no}: card has no Q:")
        if not c.get("a"):
            problems.append(f"{path}:{line_no}: card has no A:")
        if c.get("band") and c["band"] not in BANDS:
            problems.append(f"{path}:{line_no}: band must be red, green, yellow, or blue, not '{c['band']}'")
    if cards == 0:
        problems.append(f"{path}:{start}: lnk-deck has no cards (separate cards with a line of ---)")
    return problems


def check_file(path: Path) -> tuple[list[str], int]:
    lines = path.read_text(encoding="utf-8").splitlines()
    problems, decks = [], 0
    in_fence, fence_lang, fence_start, fence_body = False, "", 0, []
    prev_blank = True
    for n, line in enumerate(lines, 1):
        fence = re.match(r"^\s*(```+|~~~+)\s*([\w-]*)", line)
        if fence and not in_fence:
            in_fence, fence_lang, fence_start, fence_body = True, fence.group(2), n, []
            continue
        if fence and in_fence and line.strip().startswith(("```", "~~~")):
            if fence_lang == "lnk-deck":
                decks += 1
                problems += check_deck(path, fence_start, fence_body)
            in_fence = False
            prev_blank = False
            continue
        if in_fence:
            fence_body.append(line)
            continue
        if prev_blank and re.match(r"^ {4,}<", line):
            problems.append(f"{path}:{n}: indented HTML after a blank line will render as a code block, "
                            "not HTML. Remove the blank line or the indentation (for flashcards, use ```lnk-deck)")
        prev_blank = not line.strip()
    if in_fence and fence_lang == "lnk-deck":
        problems.append(f"{path}:{fence_start}: lnk-deck fence is never closed")
    return problems, decks


def main(argv: list[str]) -> int:
    roots = [Path(a) for a in argv] or [Path("docs/portland-desk")]
    files = [f for r in roots for f in ([r] if r.is_file() else sorted(r.rglob("*.md")))]
    problems, decks = [], 0
    for f in files:
        p, d = check_file(f)
        problems += p
        decks += d
    for p in problems:
        print("FAIL", p)
    print(f"{len(files)} files, {decks} lnk-deck fences, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
