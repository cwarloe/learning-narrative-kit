#!/usr/bin/env python3
"""Check month and season words in Portland Desk episodes against PORTLAND_TIMELINE.md.

Checks, per episode:
- Months: only the episode's own month, unless the line is marked <!-- date-ok -->
  (use the marker for deliberate back-references such as "the posting I missed in October").
- Seasons: season words must fit the episode month.
- Weekdays: the lab may only name weekdays the chapter names; if the chapter names
  none, the lab may name at most one.
- Desk tenure: "N months on the desk" (or "N months into my tenure") must match the
  timeline row for that episode.
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

DAYS = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
NUM = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty twenty-one twenty-two twenty-three twenty-four".split())}

def tenure_from_timeline():
    out, cur = {}, None
    for line in TL.splitlines():
        m = re.match(r"│ Ep (\d\d)\s+│", line)
        if m:
            cur = m.group(1); out[cur] = ""
        if cur and line.startswith("│"):
            cells = line.split("│")
            if len(cells) > 4:
                out[cur] += " " + cells[4].strip()
        if line.startswith("├") or line.startswith("└"):
            cur = None
    res = {}
    for ep, t in out.items():
        m = re.search(r"(\d+|~\d+) months on the desk", t) or re.search(r"(\d+) months? on the", t)
        if m:
            res[ep] = int(m.group(1).lstrip("~"))
        elif re.search(r"1 year on the desk", t):
            res[ep] = 12
    return res

def tenure_mentions(text):
    for m in re.finditer(r"\b([A-Za-z-]+|\d+) months (?:on the (?:Portland )?(?:service )?desk|into my tenure)", text):
        w = m.group(1).lower()
        n = NUM.get(w, int(w) if w.isdigit() else None)
        if n is not None:
            yield n, m.group(0)

def strip_ok(text):
    out, fenced = [], False
    for l in text.splitlines():
        if l.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if not fenced and "date-ok" not in l:
            out.append(l)
    return "\n".join(out)

def check_weekdays_and_tenure():
    bad = 0
    ten = tenure_from_timeline()
    for p in sorted(glob.glob(str(ROOT / "docs/portland-desk/narrative/[01][0-9]-*.md"))):
        ep = Path(p).name[:2]
        nar = strip_ok(Path(p).read_text())
        labs = glob.glob(str(ROOT / f"docs/portland-desk/workbench/{ep}-*.md"))
        lab = strip_ok(Path(labs[0]).read_text()) if labs else ""
        nd = {d for d in DAYS if re.search(rf"\b{d}\b", nar)}
        ld = {d for d in DAYS if re.search(rf"\b{d}\b", lab)}
        if nd and not ld <= nd:
            print(f"Ep {ep}: lab names {sorted(ld - nd)} but the chapter names {sorted(nd)}"); bad += 1
        if not nd and len(ld) > 1:
            print(f"Ep {ep}: lab names several weekdays {sorted(ld)} and the chapter names none"); bad += 1
        if ep in ten:
            for txt in (nar, lab):
                for n, phrase in tenure_mentions(txt):
                    if n != ten[ep]:
                        print(f"Ep {ep}: '{phrase}' but the timeline says {ten[ep]} months"); bad += 1
    return bad

def main():
    exp = episode_months()
    bad = 0
    for kind in ("narrative", "workbench"):
        for p in sorted(glob.glob(str(ROOT / f"docs/portland-desk/{kind}/[01][0-9]-*.md"))):
            ep = Path(p).name[:2]
            if ep not in exp:
                continue
            m0 = exp[ep]
            allowed = {m0}
            seas_ok = {(m0 - 1) % 12, m0, (m0 + 1) % 12}
            for ln, line in enumerate(Path(p).read_text().splitlines(), 1):
                if "date-ok" in line:
                    continue
                for i, name in enumerate(MONTHS):
                    if re.search(rf"\b{name}\b", line) and i not in allowed:
                        print(f"{p[len(str(ROOT))+1:]}:{ln}: '{name}' but Ep {ep} is {MONTHS[m0]}")
                        bad += 1
                for s, ms in SEASON.items():
                    if re.search(rf"\b{s}\b", line, re.I) and not (ms & seas_ok):
                        print(f"{p[len(str(ROOT))+1:]}:{ln}: '{s}' but Ep {ep} is {MONTHS[m0]}")
                        bad += 1
    bad += check_weekdays_and_tenure()
    print(f"{bad} date finding(s)")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
