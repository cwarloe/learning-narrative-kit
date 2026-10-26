#!/usr/bin/env python3
"""Strict QA/QC Gatekeeper: Zero-Emoji and AI Slop Linter.

Fails (exit code 1) if any Unicode emoji glyph or forbidden AI slop marker
is present in learner-facing markdown, HTML, CSS, or JS files.

Usage:
    python tools/check_cleanliness.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

# Fix Windows console UTF-8 output
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Regex matching Unicode emoji ranges:
# - Miscellaneous Symbols and Pictographs: \U0001F300-\U0001F5FF
# - Emoticons: \U0001F600-\U0001F64F
# - Transport and Map Symbols: \U0001F680-\U0001F6FF
# - Supplemental Symbols and Pictographs: \U0001F900-\U0001F9FF
# - Symbols and Pictographs Extended-A: \U0001FA70-\U0001FAFF
# - Dingbats: \u2700-\u27BF
# - Miscellaneous Symbols: \u2600-\u26FF
# - Geometric Shapes Extended: \U0001F780-\U0001F7FF
EMOJI_PATTERN = re.compile(
    r"[\U0001F300-\U0001F5FF"
    r"\U0001F600-\U0001F64F"
    r"\U0001F680-\U0001F6FF"
    r"\U0001F900-\U0001F9FF"
    r"\U0001FA00-\U0001FAFF"
    r"\u2600-\u26FF"
    r"\u2700-\u27BF"
    r"\u2702-\u27B0"
    r"]",
    re.UNICODE,
)

# Common AI slop decorative glyphs
SLOP_GLYPHS = re.compile(r"[✓✔✕✖✗★☆⚡✨🔥💡🎯🚀]", re.UNICODE)

EXCLUDED_DIRS = {
    ".git",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".venv",
    "venv",
    "scratch",
}

INCLUDED_EXTENSIONS = {".md", ".html", ".css", ".js", ".json", ".yaml", ".yml"}

def check_file(path: Path) -> list[tuple[int, str, list[str]]]:
    errors = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return []

    lines = text.splitlines()
    for idx, line in enumerate(lines, start=1):
        # Ignore comments or regex definitions inside python linter files themselves
        if path.name == "check_cleanliness.py" or path.name == "purge_all_emojis.py":
            continue
            
        emoji_matches = EMOJI_PATTERN.findall(line)
        slop_matches = SLOP_GLYPHS.findall(line)
        matches = emoji_matches + slop_matches
        if matches:
            errors.append((idx, line.strip(), list(set(matches))))
    return errors

def main() -> int:
    root = Path(__file__).resolve().parent.parent
    scan_targets = [root / "docs", root / "portland-desk", root / "examples"]

    total_errors = 0
    checked_files = 0

    print("======================================================================")
    print("QA/QC LINTER: SCANNING FOR EMOJIS & AI SLOP GLYPHS")
    print("======================================================================")

    for target in scan_targets:
        if not target.exists():
            continue
        for p in target.rglob("*"):
            if not p.is_file():
                continue
            if any(part in EXCLUDED_DIRS for part in p.parts):
                continue
            if p.suffix.lower() not in INCLUDED_EXTENSIONS:
                continue

            checked_files += 1
            file_errors = check_file(p)
            if file_errors:
                total_errors += len(file_errors)
                rel_path = p.relative_to(root)
                print(f"\n[FAIL] {rel_path}:")
                for line_no, content, matches in file_errors:
                    print(f"  Line {line_no:4d} | Disallowed glyphs: {matches} | {content[:80]}")

    print("----------------------------------------------------------------------")
    print(f"Checked {checked_files} files.")
    if total_errors > 0:
        print(f"[REJECTED] Found {total_errors} violations across scanned files.")
        print("Violation of Strict Zero-Emoji & Professional Engineering Standard.")
        return 1
    else:
        print("[PASSED] Zero emojis or AI slop glyphs detected. Clean engineering baseline.")
        return 0

if __name__ == "__main__":
    sys.exit(main())
