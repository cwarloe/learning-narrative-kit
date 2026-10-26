#!/usr/bin/env python3
"""Check month and season words in Portland Desk episodes against PORTLAND_TIMELINE.md.

Each episode may name its own month, the month before or after, and any month
in a line marked with <!-- date-ok -->. Season words must fit the episode month.
Exit code 1 when a finding is printed.
"""
import glob, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MONTHS = ["January","February","March","April","May","June","July","August","September","October","November","December"]
TL = (ROOT / "docs/research/PORTLAND_TIMELINE.md").read_text()

def episode_months():
    out, cur = {}, None
    for line in TL.splitlines():
        m = re.match(r"│ Ep (\d\d)\s+│", line)
        if m:
            cur = m.group(1)
            out[cur] = ""
        if cur and line.startswith("│"):
            cells = line.split("│")
            if len(cells) > 3:
                out[cur] += " " + cells[3]
        if line.startswith("├") or line.startswith("└"):
            cur = None
    res = {}
    for ep, text in out.items():
        found = [i for i, n in enumerate(MONTHS) if n in text]
        if found:
            res[ep] = found[0]
    return res

SEASON = {"winter": {11, 0, 1}, "spring": {2, 3, 4}, "summer": {5, 6, 7}, "autumn": {8, 9, 10}}

def main():
    exp = episode_months()
    bad = 0
    for kind in ("narrative", "workbench"):
        for p in sorted(glob.glob(str(ROOT / f"docs/portland-desk/{kind}/[01][0-9]-*.md"))):
            ep = Path(p).name[:2]
            if ep not in exp:
                continue
            m0 = exp[ep]
            allowed = {(m0 - 1) % 12, m0, (m0 + 1) % 12}
            for ln, line in enumerate(Path(p).read_text().splitlines(), 1):
                if "date-ok" in line:
                    continue
                for i, name in enumerate(MONTHS):
                    if re.search(rf"\b{name}\b", line) and i not in allowed:
                        print(f"{p[len(str(ROOT))+1:]}:{ln}: '{name}' but Ep {ep} is {MONTHS[m0]}")
                        bad += 1
                for s, ms in SEASON.items():
                    if re.search(rf"\b{s}\b", line, re.I) and not (ms & allowed):
                        print(f"{p[len(str(ROOT))+1:]}:{ln}: '{s}' but Ep {ep} is {MONTHS[m0]}")
                        bad += 1
    print(f"{bad} date finding(s)")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
