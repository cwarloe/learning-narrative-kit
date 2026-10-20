#!/usr/bin/env python3
"""Check callout-panel blocks and panel artwork in the Portland Desk courseware.

Fails when:
  - a callout-panel sets `image:` but has no `alt:` (or an empty one)
  - an `image:` points at a file that does not exist
  - an image in assets/panels/ has no sidecar .yaml next to it
  - portland-desk/ and docs/portland-desk/ panel folders or chapters differ

Run from the repo root:  python3 tools/check_panels.py
"""
from __future__ import annotations

import filecmp
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MIRRORS = [ROOT / "portland-desk", ROOT / "docs" / "portland-desk"]
FENCE = re.compile(r"^```callout-panel\s*\n(.*?)^```", re.S | re.M)
IMAGE_EXT = {".webp", ".png", ".jpg", ".jpeg"}


def field(block: str, key: str) -> str:
    m = re.search(rf"^{key}:\s*(.+)$", block, re.M)
    return m.group(1).strip().strip("\"'").strip() if m else ""


def main() -> int:
    errors: list[str] = []
    panels = 0
    for mirror in MIRRORS:
        if not mirror.is_dir():
            continue
        for md in sorted(mirror.rglob("*.md")):
            text = md.read_text(encoding="utf-8")
            for m in FENCE.finditer(text):
                panels += 1
                block = m.group(1)
                line = text[: m.start()].count("\n") + 1
                where = f"{md.relative_to(ROOT)}:{line}"
                image = field(block, "image")
                if not image:
                    continue
                if not field(block, "alt"):
                    errors.append(f"{where}: callout-panel has image: but no alt:")
                if not (mirror / image).is_file():
                    errors.append(f"{where}: image not found: {(mirror / image).relative_to(ROOT)}")
        panel_dir = mirror / "assets" / "panels"
        if panel_dir.is_dir():
            for img in sorted(panel_dir.rglob("*")):
                if img.suffix.lower() in IMAGE_EXT and not img.with_suffix(".yaml").is_file():
                    errors.append(f"{img.relative_to(ROOT)}: missing sidecar {img.with_suffix('.yaml').name}")

    a, b = MIRRORS
    for sub in ["assets/panels", "narrative"]:
        pa, pb = a / sub, b / sub
        if pa.is_dir() != pb.is_dir():
            errors.append(f"mirror mismatch: {sub} exists in only one of portland-desk/ and docs/portland-desk/")
            continue
        if not pa.is_dir():
            continue
        files_a = {p.relative_to(pa) for p in pa.rglob("*") if p.is_file()}
        files_b = {p.relative_to(pb) for p in pb.rglob("*") if p.is_file()}
        for rel in sorted(files_a ^ files_b):
            errors.append(f"mirror mismatch: {sub}/{rel} is in only one mirror")
        for rel in sorted(files_a & files_b):
            if not filecmp.cmp(pa / rel, pb / rel, shallow=False):
                errors.append(f"mirror mismatch: {sub}/{rel} differs between mirrors")

    for e in errors:
        print(f"FAIL: {e}")
    if errors:
        return 1
    print(f"PASS: {panels} callout-panel blocks checked; panel art and mirrors OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
