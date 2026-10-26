#!/usr/bin/env python3
"""Check month and season words in Portland Desk episodes against PORTLAND_TIMELINE.md.

Checks, per episode:
- Months: only the episode's own month, unless the line is marked <!-- date-ok -->
  (use the marker for deliberate back-references such as "the posting I missed in October").
- Seasons: season words must fit the episode month.
- Weekdays: the lab may only name weekdays the chapter names; if the chapter names
  none, the lab may name at most one.
- IDs (rule 13): INC/ESC/EVD IDs carry no year, are unique to one episode, and increase by episode.
- date-ok markers must give a reason; the cast registry (bible 3.4) fixes surnames;
  'burst into' and repeated carried-'like a' entrances are flagged (rules 11 and 14).
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

YEAR_OF_EP = {"00": 1, "01": 2, "02": 2, "03": 2, "04": 3, "05": 3, "06": 3, "07": 3, "08": 3, "09": 3, "10": 4, "11": 4, "12": 4}
YEAR_ZERO = 2022  # Year 4 of Book 0 is 2026 (Ep 12 is June 2026)

def check_iso_dates():
    """Every YYYY-MM-DD date in an episode's chapter or lab must fall in that episode's year and month."""
    bad = 0
    exp = episode_months()
    for p in sorted(glob.glob(str(ROOT / "docs/portland-desk/*/[01][0-9]-*.md"))):
        ep = Path(p).name[:2]
        if ep not in exp:
            continue
        want = (YEAR_ZERO + YEAR_OF_EP[ep], exp[ep] + 1)
        for ln, line in enumerate(Path(p).read_text().splitlines(), 1):
            if "date-ok" in line:
                continue
            for m in re.finditer(r"\b(20\d\d)-(\d\d)-(\d\d)\b", line):
                if (int(m.group(1)), int(m.group(2))) != want:
                    print(f"{p[len(str(ROOT))+1:]}:{ln}: {m.group(0)} but Ep {ep} is {want[0]}-{want[1]:02d}")
                    bad += 1
    return bad

ID_EP_OF_ARTIFACT = {"tickets.csv": "07", "tickets.json": "07", "sample_spoofed_cfo_payroll.eml": "09"}

def id_sources():
    """(episode, path) pairs for every file whose identifiers belong to one episode."""
    out = []
    for p in sorted(glob.glob(str(ROOT / "docs/portland-desk/*/[01][0-9]-*.md"))):
        out.append((Path(p).name[:2], p))
    for p in glob.glob(str(ROOT / "docs/portland-desk/artifacts/**/*"), recursive=True):
        if Path(p).name in ID_EP_OF_ARTIFACT:
            out.append((ID_EP_OF_ARTIFACT[Path(p).name], p))
    return out

def check_ids():
    """Ticket, escalation, and evidence IDs: no year, unique to one episode, increasing by episode."""
    bad = 0
    seen = {}  # id -> episode
    for ep, p in id_sources():
        text = Path(p).read_text()
        rel = p[len(str(ROOT))+1:]
        for m in re.finditer(r"\b(?:INC|ESC|EVD|HD|SEC)-?(?:[A-Z]+-)?20\d\d-\d+\b|\bHD-\d+\b", text):
            print(f"{rel}: {m.group(0)} carries a year or old format; use one counter like INC0048192"); bad += 1
        for m in re.finditer(r"\b(INC|ESC|EVD)(\d{7})\b", text):
            seen.setdefault(m.group(0), set()).add(ep)
    for i, eps in seen.items():
        if len(eps) > 1:
            print(f"{i} is used in more than one episode: {sorted(eps)}"); bad += 1
    for prefix in ("INC", "ESC", "EVD"):
        rng = {}
        for i, eps in seen.items():
            if i.startswith(prefix):
                for ep in eps:
                    lo, hi = rng.get(ep, (10**9, -1))
                    rng[ep] = (min(lo, int(i[3:])), max(hi, int(i[3:])))
        prev = None
        for ep in sorted(rng):
            if prev and rng[ep][0] <= rng[prev][1]:
                print(f"{prefix} IDs in Ep {ep} start at {rng[ep][0]} but Ep {prev} reaches {rng[prev][1]}"); bad += 1
            prev = ep
    return bad

def check_date_ok_reasons():
    bad = 0
    for p in sorted(glob.glob(str(ROOT / "docs/portland-desk/*/[01][0-9]-*.md"))):
        for ln, line in enumerate(Path(p).read_text().splitlines(), 1):
            for m in re.finditer(r"<!--\s*date-ok(.*?)-->", line):
                if not re.match(r"\s*:\s*\S", m.group(1)):
                    print(f"{p[len(str(ROOT))+1:]}:{ln}: date-ok marker needs a reason (<!-- date-ok: why -->)"); bad += 1
    return bad

def cast_registry():
    bible = (ROOT / "docs/research/PORTLAND_AUTHOR_BIBLE.md").read_text()
    sec = bible.split("### 3.4 Cast Registry", 1)[1].split("\n---", 1)[0]
    reg = {}
    for m in re.finditer(r"^\| ([A-Z][a-z]+) \| ([A-Za-z]+) \|", sec, re.M):
        if m.group(1) != "First":
            reg.setdefault(m.group(1), set()).add(m.group(2))
    return reg

def check_cast():
    """Rule 14: a registered first name may only be paired with its registered surname."""
    bad = 0
    reg = cast_registry()
    surnames = {s for v in reg.values() for s in v if s != "none"}
    files = [p for _, p in id_sources()] + glob.glob(str(ROOT / "docs/portland-desk/artifacts/**/*.*"), recursive=True)
    files += [str(ROOT / "tools/generate_helpdesk_artifacts.py")]
    for p in sorted(set(files)):
        try:
            text = Path(p).read_text()
        except (UnicodeDecodeError, IsADirectoryError):
            continue
        rel = p[len(str(ROOT))+1:]
        for m in re.finditer(r"\b([A-Z][a-z]+) ([A-Z][a-z]+)\b", text):
            first, last = m.groups()
            if first in reg and last in surnames and last not in reg[first]:
                print(f"{rel}: '{m.group(0)}' but the cast registry says {first} {'/'.join(sorted(reg[first]))}"); bad += 1
        for m in re.finditer(r"\b([a-z]+)\.([a-z]+)@harrowmere\.", text):
            first, last = m.group(1).title(), m.group(2).title()
            if first in reg and last in surnames and last not in reg[first]:
                print(f"{rel}: {m.group(0)} but the cast registry says {first} {'/'.join(sorted(reg[first]))}"); bad += 1
    return bad

def check_staging():
    """Rule 11: no 'burst into' entrances, and no carried-'like a' entrance twice in one act."""
    bad = 0
    acts = {"I": "000102", "II": "03040506", "III": "070809101112"}
    for act, eps in acts.items():
        hits = []
        for ep in [eps[i:i+2] for i in range(0, len(eps), 2)]:
            for p in glob.glob(str(ROOT / f"docs/portland-desk/narrative/{ep}-*.md")):
                for ln, line in enumerate(Path(p).read_text().splitlines(), 1):
                    if re.search(r"\bburst(s)? into\b", line):
                        print(f"{p[len(str(ROOT))+1:]}:{ln}: 'burst into' entrance (rule 11)"); bad += 1
                    if re.search(r"\b(holding|carrying|clutching|cradling) (his|her|their|a|the) \w+ like a\b", line):
                        hits.append(f"{p[len(str(ROOT))+1:]}:{ln}")
        if len(hits) > 1:
            print(f"Act {act}: carried-'like a' entrance used {len(hits)} times: {hits} (rule 11)"); bad += 1
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
    bad += check_iso_dates()
    bad += check_ids()
    bad += check_date_ok_reasons()
    bad += check_cast()
    bad += check_staging()
    print(f"{bad} date finding(s)")
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
