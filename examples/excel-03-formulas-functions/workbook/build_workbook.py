#!/usr/bin/env python3
"""Build the Excel 3 practice workbook so its numbers match the narrative.

Writes, next to this script:
  crew-bonus-start.xlsx  data sheets plus empty work columns: what Eli opened
  crew-bonus-key.xlsx    the same workbook with every formula the story uses filled in

The data is generated from a fixed seed and then tuned until the story's numbers
come out exactly (crew average 41.3, median 44, mode 45, the $412.6875 example,
a $9,840 total with Marco's ID typo, and so on). STORY below is the contract:
the script fails if the data can't meet it. verify_with_libreoffice() then
recalculates the key workbook and checks Excel-style results cell by cell.

Usage: .venv/bin/python examples/excel-03-formulas-functions/workbook/build_workbook.py
Needs openpyxl; verification needs LibreOffice (soffice) on PATH.
"""
from __future__ import annotations

import datetime as dt
import random
import shutil
import subprocess
import tempfile
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.formula import ArrayFormula

HERE = Path(__file__).resolve().parent
Q_START, Q_END = dt.date(2026, 7, 1), dt.date(2026, 9, 30)
FORKLIFT_WEEK = (dt.date(2026, 8, 10), dt.date(2026, 8, 14))  # the hydraulic-line week

# Numbers the narrative states. The build fails if the data can't produce them.
STORY = {
    "crew_average": 41.3,      # AVERAGE of every weekly pallets-per-hour value, 1 decimal
    "crew_median": 44,
    "crew_mode": 45,
    "tyler_week1": 4,
    "seniors_over_60": 3,
    "example_raw": 412.6875,   # Bonus!K2
    "total_with_typo": 9840,   # SUM(L2:L38*M2:M38) with Marco's base zeroed by IFERROR
    "marco_bonus": 415,
    "marco_days": 64,
    "marco_pph": 48,
    "payout_date": dt.date(2026, 10, 14),  # WORKDAY(quarter end, 10)
}

TIERS = [(0, 0, 1.00), (38, 1, 1.10), (44, 2, 1.25), (52, 3, 1.50)]  # cutoff, tier, multiplier
BASE = {"Loader": 285.40, "Forklift operator": 330.15, "Receiving clerk": 298.60}

NIGHT = [
    # name, role, level (target pallets/hour), status
    ("Dale Ostrander", "Forklift operator", 45, ""),          # row 2: the $412.6875 example
    ("Ana Ferreira", "Forklift operator", 65, ""),
    ("Curt Bessler", "Forklift operator", 64, ""),
    ("Lou Tran", "Forklift operator", 68, ""),
    ("Marco Reyes", "Forklift operator", 48, ""),
    ("Tyler Brooks", "Loader", 36, ""),                       # new hire, 4 pallets his first week
    ("Jenna Kowalski", "Loader", 45, "Light duty"),
    ("Ray Mulcahy", "Loader", 44, "Light duty"),
    ("Sofia Aguilar", "Receiving clerk", 42, "Leave"),
    ("Pete Lindgren", "Loader", 45, ""),
    ("Hollis Wade", "Loader", 46, ""),
    ("Mei Chen", "Forklift operator", 50, ""),
    ("Grant Ruiz", "Loader", 43, ""),
    ("Darnell Hayes", "Forklift operator", 47, ""),
    ("Kim Sorensen", "Loader", 45, ""),
    ("Luis Ortega", "Loader", 39, ""),
    ("Bree Halverson", "Receiving clerk", 41, ""),
    ("Sam Okonkwo", "Loader", 44, ""),
    ("Nate Pierce", "Forklift operator", 49, ""),
    ("Jo Whitcomb", "Loader", 45, ""),
    ("Arturo Vega", "Loader", 40, ""),
    ("Casey Dunn", "Loader", 46, ""),
    ("Rich Albers", "Forklift operator", 52, ""),
    ("Tess Mahoney", "Loader", 44, ""),
    ("Omar Haddad", "Loader", 38, ""),
    ("Kyle Banks", "Loader", 42, ""),               # new hire
    ("Lena Novak", "Receiving clerk", 45, ""),      # new hire
    ("Ben Ashby", "Loader", 45, ""),
    ("Vic Duran", "Forklift operator", 46, ""),
    ("Ruby Clark", "Loader", 43, ""),
    ("Gus Petrakis", "Loader", 45, ""),
    ("Ivy Nakamura", "Loader", 44, ""),
    ("Wes Thornton", "Forklift operator", 48, ""),
    ("Dee Fontaine", "Loader", 41, ""),
    ("Hector Salas", "Loader", 45, ""),
    ("June Albright", "Loader", 42, ""),
    ("Paul Engstrom", "Day lead", 44, ""),          # the one base the tuner may set
]
NEW_HIRES = {"Tyler Brooks": dt.date(2026, 7, 20), "Kyle Banks": dt.date(2026, 7, 6),
             "Lena Novak": dt.date(2026, 8, 3)}
INCIDENTS = [("2026-07-28", "Hollis Wade", "Strained back lifting a torn bag"),
             ("2026-08-19", "Luis Ortega", "Pallet jack ran over foot; first aid only"),
             ("2026-09-02", "Hollis Wade", "Cut hand on banding strap")]
DAY_CREW = 20


def mround(x: float, m: int) -> int:
    return int((Decimal(str(x)) / m).quantize(Decimal(1), rounding=ROUND_HALF_UP) * m)


def xround(x: float, n: int = 0) -> float:
    q = Decimal(1).scaleb(-n)
    return float(Decimal(str(x)).quantize(q, rounding=ROUND_HALF_UP))


def weekdays(a: dt.date, b: dt.date) -> list[dt.date]:
    return [a + dt.timedelta(i) for i in range((b - a).days + 1) if (a + dt.timedelta(i)).weekday() < 5]


def weeks() -> list[dt.date]:
    d = Q_START - dt.timedelta(days=Q_START.weekday())
    out = []
    while d <= Q_END:
        out.append(d)
        d += dt.timedelta(days=7)
    return out


def tier_for(pph: int) -> tuple[int, float]:
    t = TIERS[0]
    for row in TIERS:
        if pph >= row[0]:
            t = row
    return t[1], t[2]


def median(v):
    s = sorted(v)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2


def mode_counts(v):
    c = {}
    for x in v:
        c[x] = c.get(x, 0) + 1
    return c


def generate(seed: int):
    rng = random.Random(seed)
    ids = list(range(1101, 1101 + len(NIGHT)))
    ids[[n for n, *_ in NIGHT].index("Marco Reyes")] = 1147
    people = []
    for eid, (name, role, level, status) in zip(ids, NIGHT):
        hire = NEW_HIRES.get(name, dt.date(2015 + rng.randrange(10), rng.randrange(1, 13), 1))
        people.append(dict(id=eid, name=name, role=role, level=level, status=status, hire=hire))

    # Shifts: weekdays from hire date, minus absences; status people miss more.
    for p in people:
        days = weekdays(max(p["hire"], Q_START), Q_END)
        if p["name"] == "Marco Reyes":
            drop = len(days) - STORY["marco_days"]
        elif p["status"]:
            drop = rng.randrange(14, 24)
        else:
            drop = rng.choice([0, 1, 2, 2, 3, 4, 5, 6, 8])
        p["shifts"] = sorted(rng.sample(days, len(days) - drop))

    # Weekly pallets per hour, whole numbers, one value per week worked.
    for p in people:
        vals = {}
        for w in weeks():
            if not any(w <= s < w + dt.timedelta(7) for s in p["shifts"]):
                continue
            v = p["level"] + rng.choice([-3, -2, -1, 0, 0, 1, 2, 3])
            if w == dt.date(2026, 8, 10):
                v -= rng.randrange(14, 22)      # forklift down
            vals[w] = max(v, 1)
        p["weekly"] = vals
    tyler = next(p for p in people if p["name"] == "Tyler Brooks")
    first = min(tyler["weekly"])
    tyler["weekly"][first] = STORY["tyler_week1"]
    return people


def person_pph(p) -> int:
    v = list(p["weekly"].values())
    return int(xround(sum(v) / len(v), 0))


def tune(people, rng):
    """Nudge weekly values (never protected people's averages) until the crew stats match."""
    protected = {"Marco Reyes", "Dale Ostrander", "Ana Ferreira", "Curt Bessler", "Lou Tran", "Tyler Brooks"}
    cells = [(p, w) for p in people if p["name"] not in protected for w in p["weekly"]]

    def score():
        v = [x for p in people for x in p["weekly"].values()]
        c = mode_counts(v)
        top = max(c.values())
        modes = [k for k, n in c.items() if n == top]
        s = abs(round(sum(v) / len(v), 1) - STORY["crew_average"]) * 10
        s += abs(median(v) - STORY["crew_median"]) * 3
        s += 0 if modes == [STORY["crew_mode"]] else 2 + abs(c.get(STORY["crew_mode"], 0) - top - 1)
        return s

    best = score()
    for _ in range(40000):
        if best == 0:
            break
        p, w = rng.choice(cells)
        old = p["weekly"][w]
        p["weekly"][w] = max(1, old + rng.choice([-1, 1, -2, 2]))
        s = score()
        if s <= best:
            best = s
        else:
            p["weekly"][w] = old
    return best


def fix_protected(people):
    for p in people:
        if p["name"] == "Marco Reyes":
            ks = sorted(p["weekly"])
            vals = [48] * len(ks)
            vals[ks.index(dt.date(2026, 8, 10))] = 31
            # lift a few weeks so the average is 48 again despite the forklift week
            short = 48 * len(ks) - sum(vals)
            i = 0
            while short > 0:
                if ks[i] != dt.date(2026, 8, 10):
                    vals[i] += 1
                    short -= 1
                i = (i + 1) % len(ks)
            p["weekly"] = dict(zip(ks, vals))


def compute(people, lead_base):
    rows = []
    incidents = {}
    for _, name, _ in INCIDENTS:
        incidents[name] = incidents.get(name, 0) + 1
    for p in people:
        base = lead_base if p["role"] == "Day lead" else BASE[p["role"]]
        pph = person_pph(p)
        tier, mult = tier_for(pph)
        days = len(p["shifts"])
        inc = incidents.get(p["name"], 0)
        elig = (days >= 60 and inc == 0) or p["status"] in ("Light duty", "Leave")
        raw = base * mult
        rows.append(dict(p=p, base=base, pph=pph, tier=tier, mult=mult, days=days, inc=inc,
                         elig=elig, raw=raw, bonus=mround(raw, 5)))
    return rows


def solve(seed: int):
    rng = random.Random(seed * 7 + 1)
    people = generate(seed)
    fix_protected(people)
    if tune(people, rng) != 0:
        return None
    rows = compute(people, 0)
    lead = next(r for r in rows if r["p"]["role"] == "Day lead")
    if not lead["elig"]:
        return None
    rest = sum(r["bonus"] for r in rows if r["elig"] and r["p"]["name"] != "Marco Reyes" and r is not lead)
    need = STORY["total_with_typo"] - rest
    if not 300 <= need <= 600:
        return None
    lead_base = round(need / lead["mult"] - 0.37, 2)       # odd cents, still rounds to `need`
    rows = compute(people, lead_base)
    try:
        check(people, rows)
    except AssertionError:
        return None
    return people, rows, lead_base


def check(people, rows):
    v = [x for p in people for x in p["weekly"].values()]
    c = mode_counts(v)
    top = max(c.values())
    assert round(sum(v) / len(v), 1) == STORY["crew_average"], sum(v) / len(v)
    assert median(v) == STORY["crew_median"]
    assert [k for k, n in c.items() if n == top] == [STORY["crew_mode"]]
    assert sum(1 for r in rows if r["pph"] > 60) == STORY["seniors_over_60"]
    assert rows[0]["raw"] == STORY["example_raw"], rows[0]["raw"]
    marco = next(r for r in rows if r["p"]["name"] == "Marco Reyes")
    assert marco["pph"] == STORY["marco_pph"] and marco["days"] == STORY["marco_days"]
    assert marco["elig"] and marco["bonus"] == STORY["marco_bonus"]
    typo_total = sum(r["bonus"] for r in rows if r["elig"] and r is not marco)
    assert typo_total == STORY["total_with_typo"], typo_total
    tyler = next(p for p in people if p["name"] == "Tyler Brooks")
    assert tyler["weekly"][min(tyler["weekly"])] == STORY["tyler_week1"]


# ---------------------------------------------------------------- workbook

BOLD = Font(bold=True)
HEAD_FILL = PatternFill("solid", fgColor="DDE7D0")
WORK_FILL = PatternFill("solid", fgColor="FFF6D5")


def header(ws, cols, fill=HEAD_FILL):
    for i, c in enumerate(cols, 1):
        cell = ws.cell(row=1, column=i, value=c)
        cell.font = BOLD
        cell.fill = fill
    ws.freeze_panes = "A2"


def write_workbook(people, rows, lead_base, key: bool) -> Workbook:
    rng = random.Random(99)
    wb = Workbook()

    # Timeclock export: night crew and day crew.
    tc = wb.active
    tc.title = "Timeclock"
    header(tc, ["Emp ID", "Date", "Clock in", "Clock out", "Crew", "Month", "Hours", "Overtime"])
    shifts = []
    for p in people:
        for d in p["shifts"]:
            start = dt.time(22, rng.choice([0, 0, 0, 15, 30]))
            if rng.random() < 0.12:
                start = dt.time(0, rng.choice([15, 30]))       # late starts after midnight
            hours = rng.choice([8, 8, 8.5, 8.5, 9, 9.5, 10, 10.5, 11, 11.5])
            if FORKLIFT_WEEK[0] <= d <= FORKLIFT_WEEK[1]:
                hours = rng.choice([3, 3.5, 4, 5])
            end = (dt.datetime.combine(d, start) + dt.timedelta(hours=hours)).time()
            shifts.append((p["id"], d, start, end, "Night"))
    for k in range(DAY_CREW):
        eid = 1201 + k
        for d in weekdays(Q_START, Q_END):
            if rng.random() < 0.06:
                continue
            start = dt.time(6, rng.choice([0, 0, 30]))
            hours = rng.choice([8, 8, 8.5, 9, 10])
            end = (dt.datetime.combine(d, start) + dt.timedelta(hours=hours)).time()
            shifts.append((eid, d, start, end, "Day"))
    shifts.sort(key=lambda s: (s[1], s[4] != "Night", s[2] < dt.time(12), s[0]))
    assert shifts[0][4] == "Night" and shifts[0][2] >= dt.time(22), shifts[0]
    for r, (eid, d, a, b, crew) in enumerate(shifts, 2):
        tc.cell(r, 1, eid)
        tc.cell(r, 2, d).number_format = "mm/dd/yyyy"
        tc.cell(r, 3, a).number_format = "h:mm AM/PM"
        tc.cell(r, 4, b).number_format = "h:mm AM/PM"
        tc.cell(r, 5, crew)
        tc.cell(r, 6, d.strftime("%b"))
        tc.cell(r, 7, f"=IF(D{r}<C{r},D{r}+1-C{r},D{r}-C{r})*24" if key else None).number_format = "0.00"
        tc.cell(r, 8, f"=MAX(0,G{r}-8)" if key else None).number_format = "0.00"
    for col, w in zip("ABCDEFGH", [9, 12, 11, 11, 8, 8, 9, 10]):
        tc.column_dimensions[col].width = w
    for c in ("G1", "H1"):
        tc[c].fill = WORK_FILL
    n_tc = len(shifts) + 1

    # Warehouse system: weekly pallets per hour, night crew.
    wms = wb.create_sheet("WMS")
    header(wms, ["Emp ID", "Week of", "Crew", "Pallets/hr"])
    r = 2
    for w in weeks():
        for p in people:
            if w in p["weekly"]:
                wms.cell(r, 1, p["id"])
                wms.cell(r, 2, w).number_format = "mm/dd/yyyy"
                wms.cell(r, 3, "Night")
                wms.cell(r, 4, p["weekly"][w])
                r += 1
    n_wms = r - 1
    for col, wd in zip("ABCD", [9, 12, 8, 11]):
        wms.column_dimensions[col].width = wd

    # HR list, with Marco's ID mistyped.
    hr = wb.create_sheet("HR")
    header(hr, ["Emp ID", "Name", "Role", "Base bonus", "Hire date", "Status"])
    for r, p in enumerate(people, 2):
        hr.cell(r, 1, 1174 if p["name"] == "Marco Reyes" else p["id"])
        hr.cell(r, 2, p["name"])
        hr.cell(r, 3, p["role"])
        base = lead_base if p["role"] == "Day lead" else BASE[p["role"]]
        hr.cell(r, 4, base).number_format = "$#,##0.00"
        hr.cell(r, 5, p["hire"]).number_format = "mm/dd/yyyy"
        hr.cell(r, 6, p["status"] or None)
    for col, wd in zip("ABCDEF", [9, 18, 18, 11, 12, 11]):
        hr.column_dimensions[col].width = wd

    # Safety log.
    sf = wb.create_sheet("Safety")
    header(sf, ["Date", "Emp ID", "What happened"])
    ids = {p["name"]: p["id"] for p in people}
    for r, (d, name, what) in enumerate(INCIDENTS, 2):
        sf.cell(r, 1, dt.date.fromisoformat(d)).number_format = "mm/dd/yyyy"
        sf.cell(r, 2, ids[name])
        sf.cell(r, 3, what)
    sf.column_dimensions["C"].width = 42

    # Tier table from Ruth.
    tt = wb.create_sheet("Tiers")
    header(tt, ["Pallets/hr at least", "Tier", "Multiplier"])
    for r, (cut, t, m) in enumerate(TIERS, 2):
        tt.cell(r, 1, cut)
        tt.cell(r, 2, t)
        tt.cell(r, 3, m).number_format = "0.00"
    tt.column_dimensions["A"].width = 20

    # Bonus sheet: the work.
    bs = wb.create_sheet("Bonus", 0)
    cols = ["Emp ID", "Name", "Base", "Pallets/hr", "Tier name", "Days worked", "Incidents",
            "Status", "Eligible", "Tier", "Raw bonus", "Bonus", "Paid?", "Full weeks"]
    header(bs, cols)
    for c in range(2, len(cols) + 1):
        bs.cell(1, c).fill = WORK_FILL
    for r, p in enumerate(people, 2):
        bs.cell(r, 1, p["id"])
        look = "VLOOKUP(A{r},HR!$A:$F,{c},FALSE)"
        formulas = {
            2: f"=IFERROR({look.format(r=r, c=2)},0)",
            3: f"=IFERROR({look.format(r=r, c=4)},0)",
            4: f"=ROUND(AVERAGEIF(WMS!A:A,A{r},WMS!D:D),0)",
            5: f'=_xlfn.IFS(J{r}=3,"Gold",J{r}=2,"Silver",J{r}=1,"Bronze",J{r}=0,"Base")',
            6: f"=COUNTIF(Timeclock!A:A,A{r})",
            7: f"=COUNTIF(Safety!B:B,A{r})",
            8: f'=IFERROR({look.format(r=r, c=6)}&"",0)',
            9: f'=OR(AND(F{r}>=60,G{r}=0),H{r}="Light duty",H{r}="Leave")',
            10: f"=VLOOKUP(D{r},Tiers!$A$2:$C$5,2,TRUE)",
            11: f"=C{r}*VLOOKUP(D{r},Tiers!$A$2:$C$5,3,TRUE)",
            12: f"=MROUND(K{r},5)",
            13: f"=IF(I{r},1,0)",
            14: f"=INT(F{r}/5)",
        }
        fmts = {3: "$#,##0.00", 11: "$#,##0.0000", 12: "$#,##0"}
        for c, f in formulas.items():
            cell = bs.cell(r, c, f if key else None)
            if c in fmts:
                cell.number_format = fmts[c]
    bs["K40"], bs["K40"].font = "Total payout", BOLD
    if key:
        bs["L40"] = ArrayFormula("L40", "=SUM(L2:L38*M2:M38)")
    bs["L40"].number_format = "$#,##0"
    bs["L40"].font = BOLD
    for col, wd in zip("ABCDEFGHIJKLMN", [9, 18, 11, 10, 10, 12, 10, 11, 9, 6, 12, 9, 7, 11]):
        bs.column_dimensions[col].width = wd

    # Checks: Ruth's and Hank's questions.
    ck = wb.create_sheet("Checks", 1)
    ck.column_dimensions["A"].width = 46
    ck.column_dimensions["B"].width = 16
    ck.column_dimensions["C"].width = 60
    tc_g, tc_e, tc_f, tc_h = "Timeclock!G:G", "Timeclock!E:E", "Timeclock!F:F", "Timeclock!H:H"
    wms_d = "WMS!D:D"
    items = [
        ("Ruth: what is a normal pallets/hr?", None, None),
        ("Crew average (AVERAGE)", f"=AVERAGE({wms_d})", "0.0"),
        ("Crew median (MEDIAN)", f"=MEDIAN({wms_d})", "0"),
        ("Crew mode (MODE.MULT)", f"=_xlfn.MODE.MULT({wms_d})", "0"),
        ("Hank: overtime", None, None),
        ("Night overtime hours (SUMIF)", f'=SUMIF({tc_e},"Night",{tc_h})', "0.0"),
        ("Shifts over 10 hours (COUNTIF)", f'=COUNTIF({tc_g},">10")', "0"),
        ("Average night shift (AVERAGEIF)", f'=AVERAGEIF({tc_e},"Night",{tc_g})', "0.00"),
        ("Night overtime, September (SUMIFS)", f'=SUMIFS({tc_h},{tc_e},"Night",{tc_f},"Sep")', "0.0"),
        ("Night shifts over 10 hrs, September (COUNTIFS)", f'=COUNTIFS({tc_e},"Night",{tc_f},"Sep",{tc_g},">10")', "0"),
        ("Average night shift, September (AVERAGEIFS)", f'=AVERAGEIFS({tc_g},{tc_e},"Night",{tc_f},"Sep")', "0.00"),
        ("Longest night shift, September (MAXIFS)", f'=_xlfn.MAXIFS({tc_g},{tc_e},"Night",{tc_f},"Sep")', "0.00"),
        ("Shortest night shift, August (MINIFS)", f'=_xlfn.MINIFS({tc_g},{tc_e},"Night",{tc_f},"Aug")', "0.00"),
        ("Rounding the $412.6875 example (Bonus!K2)", None, None),
        ("ROUND to cents", "=ROUND(Bonus!K2,2)", "$#,##0.00"),
        ("ROUNDDOWN to dollars", "=ROUNDDOWN(Bonus!K2,0)", "$#,##0.00"),
        ("MROUND to $5", "=MROUND(Bonus!K2,5)", "$#,##0.00"),
        ("Practice: ROUNDDOWN(-1.9,0)", "=ROUNDDOWN(-1.9,0)", "0"),
        ("Practice: INT(-1.9)", "=INT(-1.9)", "0"),
        ("Dates", None, None),
        ("Quarter end", None, "mm/dd/yyyy"),
        ("Payout date (WORKDAY, 10 working days)", "=WORKDAY(B21,10)", "mm/dd/yyyy"),
        ("Possible days: Tyler Brooks (NETWORKDAYS)", "=NETWORKDAYS(HR!E7,B21)", "0"),
        ("Possible days: Kyle Banks", "=NETWORKDAYS(HR!E27,B21)", "0"),
        ("Possible days: Lena Novak", "=NETWORKDAYS(HR!E28,B21)", "0"),
        ("Calculated as of", None, "mm/dd/yyyy"),
        ("This file", '=CELL("filename",A1)', None),
    ]
    for r, (label, formula, fmt) in enumerate(items, 1):
        a = ck.cell(r, 1, label)
        if formula is None and fmt is None:
            a.font = BOLD
            continue
        if label == "Quarter end":
            ck.cell(r, 2, Q_END).number_format = fmt
            continue
        if label == "Calculated as of":
            ck.cell(r, 2, dt.date(2026, 10, 6) if key else None).number_format = fmt
            ck.cell(r, 3, "Typed, not =TODAY(): TODAY is volatile and changes every day." if key else None)
            continue
        cell = ck.cell(r, 2, formula if key else None)
        if fmt:
            cell.number_format = fmt
        ck.cell(r, 2).fill = WORK_FILL
    assert ck["A21"].value == "Quarter end"
    for ws in wb.worksheets:
        for row in ws.iter_rows(min_row=1, max_row=1):
            for c in row:
                c.alignment = Alignment(wrap_text=False)
    return wb


def verify_with_libreoffice(key_path: Path, rows) -> list[str]:
    """Recalculate the key in LibreOffice and compare with the Python model."""
    soffice = shutil.which("soffice")
    if not soffice:
        return ["SKIPPED: soffice not found"]
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([soffice, "--headless", "--calc", "--convert-to", "xlsx", "--outdir", tmp, str(key_path)],
                       check=True, capture_output=True)
        wb = load_workbook(Path(tmp) / key_path.name, data_only=True)
    bs, ck = wb["Bonus"], wb["Checks"]
    out = []

    def expect(label, got, want):
        ok = got == want or (isinstance(want, float) and got is not None and abs(got - want) < 1e-9)
        out.append(f"{'ok ' if ok else 'BAD'} {label}: {got!r} (story: {want!r})")

    expect("crew average (1 dp)", round(ck["B2"].value, 1), STORY["crew_average"])
    expect("crew median", ck["B3"].value, STORY["crew_median"])
    expect("crew mode", ck["B4"].value, STORY["crew_mode"])
    expect("Bonus!K2 raw", bs["K2"].value, STORY["example_raw"])
    expect("ROUND", ck["B15"].value, 412.69)
    expect("ROUNDDOWN", ck["B16"].value, 412)
    expect("MROUND", ck["B17"].value, 415)
    expect("ROUNDDOWN(-1.9,0)", ck["B18"].value, -1)
    expect("INT(-1.9)", ck["B19"].value, -2)
    payout = ck["B22"].value
    expect("WORKDAY payout", payout.date() if hasattr(payout, "date") else payout, STORY["payout_date"])
    expect("total with Marco's typo", bs["L40"].value, STORY["total_with_typo"])
    marco_row = next(i for i, r in enumerate(rows, 2) if r["p"]["name"] == "Marco Reyes")
    expect("Marco name after IFERROR", bs.cell(marco_row, 2).value, 0)
    expect("Marco days", bs.cell(marco_row, 6).value, STORY["marco_days"])
    expect("Marco pallets/hr", bs.cell(marco_row, 4).value, STORY["marco_pph"])
    expect("Marco bonus with typo", bs.cell(marco_row, 12).value, 0)
    for i, r in enumerate(rows, 2):
        if r["p"]["name"] == "Marco Reyes":
            continue
        if bs.cell(i, 12).value != r["bonus"] or bool(bs.cell(i, 9).value) != r["elig"]:
            out.append(f"BAD row {i} {r['p']['name']}: sheet {bs.cell(i, 12).value}/{bs.cell(i, 9).value}, "
                       f"model {r['bonus']}/{r['elig']}")
    out.append(f"info: night OT Sep {ck['B9'].value}, longest Sep shift {ck['B12'].value}, "
               f"shortest Aug shift {ck['B13'].value}, NETWORKDAYS "
               f"{ck['B23'].value}/{ck['B24'].value}/{ck['B25'].value}, G2 night shift {wb['Timeclock']['G2'].value}")
    return out


RECORDING_INTRO = """# Recording script: The Crew Bonus (Excel 3)

Generated from `steps.yaml` by `build_workbook.py`. Edit the YAML, not this file.

## Before you start

- **Excel:** desktop Excel for Microsoft 365, or Excel 2021. Excel 2019 lacks some
  functions used here.
- **File:** open a fresh copy of `crew-bonus-start.xlsx` each time you record.
- **Screen:** 1920×1080 if you can, Excel maximized, zoom 120% (bottom-right slider).
  Turn off notifications.
- **Privacy:** your name or email shows in Excel's title bar and on the account button.
  Crop or blur it later, or record only the grid area.
- **Recording on Windows:** Win+Alt+R (Xbox Game Bar) records the Excel window; OBS
  works too. **On a Mac:** Cmd+Shift+5.
- **Clips:** either record each clip as its own file (`clip-01.mp4`, `clip-02.mp4`…),
  or record one long take and **hold still for three seconds** before each clip so it
  can be cut apart later.
- **Pace:** type at normal speed and pause about a second after each Enter, so the
  result is on screen long enough to see.
- **Mistakes:** if you mistype, just fix it and keep going. Real fumbles are fine.
"""


def render_recording(steps_path: Path, out_path: Path) -> None:
    import re
    import yaml
    data = yaml.safe_load(steps_path.read_text(encoding="utf-8"))
    story = (HERE.parent / "narrative.md").read_text(encoding="utf-8")
    story = re.sub(r"\[\[[^|\]]+\|([^\]]*)\]\]", r"\1", story)   # cover-strip the marks
    for clip in data["clips"]:
        if clip["passage"] not in story:
            raise SystemExit(f"clip {clip['id']}: passage not found in narrative.md: {clip['passage']!r}")
    lines = [RECORDING_INTRO]
    for clip in data["clips"]:
        lines.append(f"## Clip {clip['id']}: {clip['title']}\n")
        tail = "" if clip["passage"][-1] in ".!?" else "…"
        lines.append(f"*Story passage:* \"{clip['passage']}{tail}\"\n")
        for n, step in enumerate(clip["steps"], 1):
            lines.append(f"{n}. {step['do']}")
            if step.get("expect"):
                lines.append(f"   - **You should see:** {step['expect']}")
        lines.append("")
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    for seed in range(1, 400):
        result = solve(seed)
        if result:
            break
    else:
        raise SystemExit("no seed met the story's numbers")
    people, rows, lead_base = result
    check(people, rows)
    start = HERE / "crew-bonus-start.xlsx"
    key = HERE / "crew-bonus-key.xlsx"
    write_workbook(people, rows, lead_base, key=False).save(start)
    write_workbook(people, rows, lead_base, key=True).save(key)
    print(f"seed {seed}; lead base ${lead_base}; wrote {start.name}, {key.name}")
    eligible = sum(1 for r in rows if r["elig"])
    print(f"{len(rows)} night crew, {eligible} eligible; corrected total "
          f"{STORY['total_with_typo'] + STORY['marco_bonus']}")
    render_recording(HERE / "steps.yaml", HERE / "RECORDING.md")
    print("wrote RECORDING.md")
    for line in verify_with_libreoffice(key, rows):
        print(line)


if __name__ == "__main__":
    main()
