"""lnk-deck fences: parse the fence text and emit the placeholder docs/lnk-deck.js builds.

Same format and rules as the Docsify parser in docs/portland-desk/index.html
(spec: docs/research/INTERACTIVE_COMPONENTS_SPEC.md, section 4):

    ```lnk-deck
    title: Module 5 key terms
    meta: Bidgoli Module 5
    size: 3x5            # or 4x6
    band: red            # red | green | yellow | blue
    ---
    Q: Front of the card
    A: Back of the card
    why: optional line under the answer
    tag: optional label on the front
    ---
    Q: ...
    ```

A line that does not start with `word:` continues the previous field.
tools/check_decks.py checks fences for unknown fields, sizes and bands.
"""
from __future__ import annotations

import html
import json
import re
from urllib.parse import quote

_FIELD = re.compile(r"^([A-Za-z_]+):\s?(.*)$")
_SEP = re.compile(r"^---[ \t]*$", re.M)


def _fields(text: str) -> dict:
    out: dict = {}
    last = None
    for line in text.split("\n"):
        m = _FIELD.match(line)
        if m:
            last = m.group(1).lower()
            out[last] = m.group(2).strip()
        elif last and line.strip():
            out[last] += " " + line.strip()
    return out


def parse_deck(block: str) -> dict:
    sections = _SEP.split(block)
    head = _fields(sections[0] if sections else "")
    cards = [c for c in (_fields(s) for s in sections[1:]) if c.get("q") or c.get("a")]
    return {
        "title": head.get("title") or "Flashcards",
        "meta": head.get("meta", ""),
        "size": head.get("size") or "3x5",
        "band": head.get("band") or "red",
        "cards": cards,
    }


def deck_placeholder(block: str) -> str:
    """The element docs/lnk-deck.js turns into a deck (encodeURIComponent-compatible)."""
    data = json.dumps(parse_deck(block), ensure_ascii=False, separators=(",", ":"))
    return f'<div class="lnk-deck" data-deck="{html.escape(quote(data, safe=""))}"></div>'
