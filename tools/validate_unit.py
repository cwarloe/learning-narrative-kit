#!/usr/bin/env python3
"""Validate a learning-narrative unit against the authoring QA checklist.

Usage:
  python tools/validate_unit.py <unit_directory>

Checks:
  - glossary.yaml + narrative.md load
  - every glossary id appears >=1 in narrative marks [[id|text]]
  - no mark ids missing from glossary
  - mark density (marks per 100 words)
  - if tiers present: count exam vs support; warn if any term lacks tier
  - fail if Priya or Harrowmere appear in narrative (Portland Desk rule)
  - print PASS/FAIL; exit nonzero on fail
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print(
        "FAIL: PyYAML is required. "
        "See Setup in AGENTS.md: python3 -m venv .venv "
        "&& .venv/bin/pip install -r requirements.txt",
        file=sys.stderr,
    )
    sys.exit(2)

MARK_RE = re.compile(r"\[\[([^|\]]+)\|([^\]]*)\]\]")
WORD_RE = re.compile(r"\b[\w']+\b", re.UNICODE)
FORBIDDEN = ("Priya", "Harrowmere")


def load_glossary(path: Path) -> list[dict]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or "terms" not in data:
        raise ValueError(f"{path}: expected a mapping with 'terms'")
    terms = data["terms"]
    if not isinstance(terms, list) or not terms:
        raise ValueError(f"{path}: 'terms' must be a non-empty list")
    return terms


def extract_marks(text: str) -> list[str]:
    return [m.group(1).strip() for m in MARK_RE.finditer(text)]


def word_count(text: str) -> int:
    # Count words on mark-stripped surface text (cover-test style).
    stripped = MARK_RE.sub(lambda m: m.group(2), text)
    return len(WORD_RE.findall(stripped))


def validate(unit_dir: Path) -> int:
    unit_dir = unit_dir.resolve()
    glossary_path = unit_dir / "glossary.yaml"
    narrative_path = unit_dir / "narrative.md"

    failures: list[str] = []
    warnings: list[str] = []
    lines: list[str] = []

    lines.append(f"Unit: {unit_dir}")

    if not glossary_path.is_file():
        failures.append(f"missing glossary.yaml at {glossary_path}")
    if not narrative_path.is_file():
        failures.append(f"missing narrative.md at {narrative_path}")

    if failures:
        for f in failures:
            lines.append(f"FAIL: {f}")
        lines.append("RESULT: FAIL")
        print("\n".join(lines))
        return 1

    try:
        terms = load_glossary(glossary_path)
    except Exception as e:
        lines.append(f"FAIL: could not load glossary.yaml: {e}")
        lines.append("RESULT: FAIL")
        print("\n".join(lines))
        return 1

    narrative = narrative_path.read_text(encoding="utf-8")

    glossary_ids: list[str] = []
    seen: set[str] = set()
    for t in terms:
        if not isinstance(t, dict) or "id" not in t:
            failures.append(f"glossary term missing id: {t!r}")
            continue
        tid = str(t["id"])
        if tid in seen:
            failures.append(f"duplicate glossary id: {tid}")
        seen.add(tid)
        glossary_ids.append(tid)

    glossary_set = set(glossary_ids)
    mark_ids = extract_marks(narrative)
    mark_set = set(mark_ids)
    mark_counts: dict[str, int] = {}
    for mid in mark_ids:
        mark_counts[mid] = mark_counts.get(mid, 0) + 1

    # Every glossary id appears >=1
    unused = sorted(glossary_set - mark_set)
    if unused:
        failures.append(
            f"{len(unused)} glossary id(s) never marked in narrative: {', '.join(unused)}"
        )

    # No mark ids missing from glossary
    unknown = sorted(mark_set - glossary_set)
    if unknown:
        failures.append(
            f"{len(unknown)} mark id(s) missing from glossary: {', '.join(unknown)}"
        )

    # Density
    words = word_count(narrative)
    total_marks = len(mark_ids)
    density = (total_marks / words * 100.0) if words else 0.0
    lines.append(f"Words (cover-stripped): {words}")
    lines.append(f"Marks: {total_marks} unique={len(mark_set)} glossary={len(glossary_ids)}")
    lines.append(f"Mark density: {density:.2f} marks per 100 words")

    # Tiers
    tiers_present = any(
        isinstance(t, dict) and "tier" in t for t in terms
    )
    if tiers_present:
        exam = support = missing_tier = 0
        missing_ids: list[str] = []
        for t in terms:
            if not isinstance(t, dict):
                continue
            tier = t.get("tier")
            if tier == "exam":
                exam += 1
            elif tier == "support":
                support += 1
            else:
                missing_tier += 1
                missing_ids.append(str(t.get("id", "?")))
        lines.append(f"Tiers: exam={exam} support={support}")
        if missing_tier:
            warnings.append(
                f"{missing_tier} term(s) lack tier: {', '.join(missing_ids)}"
            )

    # Portland Desk rule
    for name in FORBIDDEN:
        if name in narrative:
            failures.append(
                f"Portland Desk rule: '{name}' appears in narrative (forbidden)"
            )

    for w in warnings:
        lines.append(f"WARN: {w}")
    for f in failures:
        lines.append(f"FAIL: {f}")

    if failures:
        lines.append("RESULT: FAIL")
        print("\n".join(lines))
        return 1

    lines.append("RESULT: PASS")
    print("\n".join(lines))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Validate a learning-narrative unit (authoring QA checklist)."
    )
    parser.add_argument(
        "unit_dir",
        type=Path,
        help="Path to unit directory containing glossary.yaml and narrative.md",
    )
    args = parser.parse_args()
    if not args.unit_dir.is_dir():
        print(f"FAIL: not a directory: {args.unit_dir}", file=sys.stderr)
        return 2
    return validate(args.unit_dir)


if __name__ == "__main__":
    sys.exit(main())
