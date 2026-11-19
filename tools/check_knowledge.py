#!/usr/bin/env python3
"""Check the Portland Desk knowledge ledger against the episodes.

The ledger (docs/research/PORTLAND_KNOWLEDGE_LEDGER.yaml) records, for each marked
term, the episode where Ethan picks it up and where it came from: a named person,
his own cert study (A+, Network+, Security+), a document he read, something he saw,
or what he knew before the story starts.
Contract: docs/research/KNOWLEDGE_LEDGER_STANDARD.md.

Two kinds of finding, kept apart as AGENTS.md asks:

FAIL (automated, exit 1):
  - a ledger entry names a term no episode marks
  - the episode where Ethan picks it up does not mark the term (it has to happen on the page)
  - a person source is not named in the episode where Ethan picks the term up, or
    gives a surname that disagrees with the bible's cast registry (section 3.4)
  - a document source lacks a title, or has a url but no retrieved date
  - a prior source has no note pointing at the timeline backstory
  - a study source names a cert other than A+, Network+ or Security+, or dates
    Network+ study before Ep 02 (the timeline starts it during the IT rotation) or
    Security+ study before Ep 05 (after he passes Network+)
  - duplicate entries, unknown episode numbers, unknown status or kind values

FLAG (a person looks; exit 0 unless --strict):
  - Ethan uses a term, in narration or his own speech, before the episode where he
    picks it up. Lines where another character says the term are treated as hearing
    it, not using it. The speaker guess reads the "Name said" tag in the paragraph, so
    check each flag in the text before changing anything.

REPORT (counts only):
  - terms Ethan uses that have no ledger entry yet

    python3 tools/check_knowledge.py            # FAIL exits 1; FLAG and REPORT print
    python3 tools/check_knowledge.py --strict   # FLAG also exits 1
    python3 tools/check_knowledge.py --list     # also list the terms with no entry

Needs PyYAML.
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
LEDGER = ROOT / "docs/research/PORTLAND_KNOWLEDGE_LEDGER.yaml"
NARRATIVE = ROOT / "docs/portland-desk/narrative"
BIBLE = ROOT / "docs/research/PORTLAND_AUTHOR_BIBLE.md"

MARK = re.compile(r"\[\[([a-z0-9_]+)\|")
KINDS = {"person", "study", "document", "observed", "prior"}
# Off-page kinds: Ethan can pick these up between scenes, so the pickup episode
# need not mark the term.
OFF_PAGE = {"prior", "study"}
CERTS = {"A+", "Network+", "Security+"}
# PORTLAND_TIMELINE.md section 4: Net+ study begins during the IT rotation,
# which is covered at the start of Ep 02. Security+ study starts in Ep 05, after he
# passes Network+ about 13 months into IT (decided 2026-11-18; see the standard).
CERT_EARLIEST = {"Network+": "02", "Security+": "05"}
STATUSES = {"proposed", "confirmed"}
SPEECH_VERBS = (
    "said|says|answered|asked|added|explained|replied|told|realized|admitted|"
    "muttered|called|insisted|continued|pointed out|offered|typed|wrote"
)
SELF_TAG = re.compile(r"\bI (?:" + SPEECH_VERBS + r")\b")


def cast_registry():
    sec = BIBLE.read_text(encoding="utf-8").split("### 3.4 Cast Registry", 1)[1].split("\n---", 1)[0]
    names = {}
    for m in re.finditer(r"^\| ([A-Z][a-z]+) \| ([A-Za-z]+) \|", sec, re.M):
        if m.group(1) != "First":
            names[m.group(1)] = m.group(2)
    return names


def paragraphs(text):
    """Yield story paragraphs, skipping fenced blocks, tables and headings."""
    in_fence = False
    block = []
    for line in text.splitlines():
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            if block:
                yield " ".join(block)
                block = []
            continue
        if in_fence or line.startswith("|") or line.startswith("#"):
            continue
        if not line.strip():
            if block:
                yield " ".join(block)
                block = []
            continue
        block.append(line.strip())
    if block:
        yield " ".join(block)


def classify(paragraph):
    """Return [(term, 'used'|'heard')] for marks in one paragraph."""
    out = []
    pieces = re.split(r'("[^"]*")', paragraph)
    ethan_speaks = bool(SELF_TAG.search(paragraph))
    for piece in pieces:
        quoted = piece.startswith('"') and piece.endswith('"') and len(piece) > 1
        for term in MARK.findall(piece):
            if quoted and not ethan_speaks:
                out.append((term, "heard"))
            else:
                out.append((term, "used"))
    return out


def episodes():
    """{ep: {'marked': set, 'used': set}} for every narrative file."""
    data = {}
    for path in sorted(NARRATIVE.glob("[0-9][0-9]-*.md")):
        ep = path.name[:2]
        text = path.read_text(encoding="utf-8")
        used = set()
        for para in paragraphs(text):
            for term, how in classify(para):
                if how == "used":
                    used.add(term)
        data[ep] = {"marked": set(MARK.findall(text)), "used": used, "file": path.name, "text": text}
    return data


def main() -> int:
    strict = "--strict" in sys.argv[1:]
    show_list = "--list" in sys.argv[1:]
    if not LEDGER.exists():
        print(f"FAIL: {LEDGER.relative_to(ROOT)} not found")
        return 1
    ledger = yaml.safe_load(LEDGER.read_text(encoding="utf-8")) or {}
    entries = ledger.get("entries") or []
    eps = episodes()
    every_mark = set().union(*(e["marked"] for e in eps.values()))
    cast = cast_registry()
    fails, flags = [], []
    seen = set()

    for i, entry in enumerate(entries):
        where = f"entry {i + 1}"
        term = str(entry.get("term", ""))
        where = f"{term or where}"
        if not term:
            fails.append(f"{where}: missing term")
            continue
        if term in seen:
            fails.append(f"{where}: listed twice")
        seen.add(term)
        if term not in every_mark:
            fails.append(f"{where}: no episode marks [[{term}|...]]")
        ep = str(entry.get("acquired", "")).zfill(2)
        if ep not in eps:
            fails.append(f"{where}: acquired '{entry.get('acquired')}' is not an episode number (00-12)")
        elif (entry.get("source") or {}).get("kind") not in OFF_PAGE and term not in eps[ep]["marked"]:
            fails.append(f"{where}: Ethan picks it up in Ep {ep}, but {eps[ep]['file']} never marks it")
        if entry.get("status") not in STATUSES:
            fails.append(f"{where}: status must be one of {sorted(STATUSES)}")
        src = entry.get("source") or {}
        kind = src.get("kind")
        if kind not in KINDS:
            fails.append(f"{where}: source.kind must be one of {sorted(KINDS)}")
        elif kind == "person":
            parts = str(src.get("name", "")).split()
            if not parts:
                fails.append(f"{where}: person source needs a name")
            else:
                first = parts[0]
                if len(parts) > 1 and first in cast and parts[1] != cast[first]:
                    fails.append(f"{where}: '{src['name']}' but the cast registry says {first} {cast[first]}")
                if ep in eps and first not in eps[ep]["text"]:
                    fails.append(f"{where}: {first} is not named in {eps[ep]['file']}")
        elif kind == "document":
            if not src.get("title"):
                fails.append(f"{where}: document source needs a title")
            if src.get("url") and not src.get("retrieved"):
                fails.append(f"{where}: document has a url but no retrieved date")
        elif kind == "study":
            cert = src.get("cert")
            if cert not in CERTS:
                fails.append(f"{where}: study source needs cert: one of {sorted(CERTS)}")
            elif cert in CERT_EARLIEST and ep < CERT_EARLIEST[cert]:
                fails.append(f"{where}: {cert} study starts in Ep {CERT_EARLIEST[cert]} per the timeline, not Ep {ep}")
        elif kind == "prior" and not src.get("note"):
            fails.append(f"{where}: prior knowledge needs a note pointing at the timeline backstory")

        if ep in eps:
            early = [e for e in sorted(eps) if e < ep and term in eps[e]["used"]]
            if early:
                flags.append(
                    f"{term}: Ethan picks it up in Ep {ep}, but it appears in his narration or "
                    f"speech in Ep {', '.join(early)}"
                )

    used_anywhere = set().union(*(e["used"] for e in eps.values()))
    no_entry = sorted(used_anywhere - seen)

    for line in fails:
        print(f"FAIL: {line}")
    for line in flags:
        print(f"FLAG: {line}")
    print(
        f"REPORT: {len(entries)} ledger entries; {len(no_entry)} of {len(used_anywhere)} terms "
        f"Ethan uses have no entry yet"
    )
    if show_list and no_entry:
        print("  " + ", ".join(no_entry))
    if fails or (strict and flags):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
