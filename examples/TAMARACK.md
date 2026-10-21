# Tamarack Feed & Supply Company — track canon (MIS + Excel/BI)

One company, one cast, one fiscal year. Each unit stands alone, but the world stays
the same so that terms from earlier modules can show up later without re-introduction.

Source of terms: the MindTap course glossary export (`mindtap_glossary_by_module.csv`),
one unit per module. Definitions are copied from that export; the narrative does not
supply rival definitions. Where the export has an obvious error, the unit notes it in
`unit.yaml` rather than quietly rewriting it.

## The company

**Tamarack Feed & Supply Company** is a fictional, family-owned farm-and-hardware
retailer: eleven stores across eastern Washington and north Idaho, a distribution center
(the DC) and head office in Spokane Valley. It sells feed, fencing, seed, tools, work
clothes, and propane. It has a loyalty program, a small web store, and a lot of habits
older than its software.

Walt Brandvold's grandfather opened it in the 1940s as a feed mill and store beside a
stand of tamaracks outside Colville. (The tamarack is the western larch, the conifer
that turns gold and drops its needles every fall.) The full name is on the cover, the
letterhead, and the trucks. In dialogue and narration, everyone just says "Tamarack."

### Stores

Eleven stores through May 3, 2027; twelve from May 4, 2027, when Davenport opens. Check a
new chapter's store names against this list. "Established" means a chapter already uses
the store; the rest are named here so later chapters have somewhere to go, and can be
renamed until one does.

| Store | State | Status | Known for (chapter) |
|---|---|---|---|
| Colville | WA | Established | The original store, next to the old feed mill. Curtis is the manager. The inventory pilot starts here (MIS 1). Gordon Ashby's four mailers (MIS 3). |
| Kettle Falls | WA | Established | The parking-lot video (MIS 4). Gordon also shops here (MIS 3). |
| Republic | WA | Established | At the end of a rural line that fails every winter. Got 400 chicks it hadn't ordered in the Chick Days mix-up; Arlo Nygaard ran it until he retired in June 2026 (MIS 7). The edge server and the October 2026 outage (MIS 10). |
| Chewelah | WA | Established | The Counter Assistant clerk (MIS 9). The manager who read his login to a "vendor" (MIS 5). |
| Deer Park | WA | Established | The "Q2 Payroll" USB stick (MIS 5). Monthly count file (Excel 5). |
| Spokane Valley | WA | Established | Same town as the DC and head office. Got 100 of the 300 chicks it ordered in the Chick Days mix-up (MIS 7). Leaky time-clock app (MIS 5). |
| Springdale | WA | Named, not yet used | |
| Cheney | WA | Named, not yet used | |
| Rathdrum | ID | Named, not yet used | |
| Priest River | ID | Named, not yet used | |
| Bonners Ferry | ID | Named, not yet used | |
| Davenport | WA | Established, opens May 4, 2027 | Chosen over Sandpoint (MIS 8). Break-even (Excel 8). Opening and first-month sales (Excel 10). |

There is no store in Sandpoint, Newport, or Ritzville: all three were candidates for the twelfth store that lost to Davenport (MIS 8), and Newport already had a competitor.

**Other dealers in the same towns.** Small towns hold competitors, so a Tamarack store and an
independent dealer can share a town:

- **Palmer's Feed & Seed** (Gene Palmer), Kettle Falls: buying-group member (ITM Week 7).
- **Grange Supply** (Linda Ostby), Deer Park: buying-group member; drops out (ITM Week 7).
- **Northland Farm Supply**: a chain that opened two stores in Tamarack's territory (MIS 1).
- An unnamed dealer in **Omak** that signed with the cattle association (MIS 10).
"Feed" stayed in the name after the fencing, propane, and web store arrived, and Walt
will defend that.

## Cast

| Person | Role | Notes |
|--------|------|-------|
| Dana Okafor | Business systems analyst, about a year in | Point-of-view character for the MIS units. Competent, not yet trusted with the big calls. |
| Ruth Halvorsen | Chief operating officer | Dana's manager. Mostly says operational things; is wrong sometimes. |
| Walt Brandvold | Owner and CEO, third generation | Decides on instinct, pays for it, occasionally right anyway. |
| Teo Vasquez | IT manager | Runs a two-person IT team plus an outside MSP. Tired. |
| Marcy Lund | Head buyer / merchandising | Lives in spreadsheets; distrusts anything she can't sort. |
| Eli Mendez | DC shift lead | Point-of-view character for the Excel/BI units. Mid-thirties, taking an evening business course at the community college that uses SAM. Dana sometimes helps. |
| Hank Pruitt | Controller | Owns the books, the bank, and the loan schedule. |

### Recurring and minor characters

People who have appeared in a chapter. Reuse them before inventing new ones; check what a
chapter already said before giving one of them a new detail. Chapter references show where
each is established.

**Tamarack staff**

| Person | Role | Established |
|--------|------|-------------|
| Curtis | Colville store manager, there since the store opened; keeps a notebook he trusts over the screen | MIS 1 |
| Jesse | Colville clerk, nineteen; defended Tamarack online on his own phone and time | MIS 1, MIS 4 |
| Arlo Nygaard | Ran the Republic store through every outage on paper; retired June 2026 | MIS 7, MIS 10 |
| Bud Carlsen | Retired DC night lead; his nine-year damage-log spreadsheet is the one Eli inherits | Excel 1, Excel 12 |
| Rosa | DC receiving clerk; enters vendor returns ("Prarie Wire" is hers, and intentional) | Excel 6, Excel 12 |
| Marco Reyes | Forklift operator, employee 1147 (see Standing facts) | Excel 3 |

**Customers**

| Person | Role | Established |
|--------|------|-------------|
| Gordon Ashby | Rancher outside Republic, a customer for thirty years; shops Colville and Kettle Falls; got four mailers | MIS 3 |
| Dale Hollister Sr. and Dale Hollister Jr. | Run separate operations from one mailing address and don't speak; wrongly merged into one loyalty account | MIS 3, Power Query |

**Vendors, partners, and others**

| Person | Role | Established |
|--------|------|-------------|
| Karen | Accounts-receivable manager at the seed company; six years of invoices with Hank | MIS 5 |
| Dale Kowalchuk | Prairie Wire's fencing rep, Marcy's call for eleven years, until approvals moved to Saskatoon | MIS 6 |
| Corinne | Former regional planner; the site-selection consultant who built the model | MIS 8 |
| Jim Sorensen | Walt's friend in Sandpoint (the fishing trip and the napkin), with a building he'd lease; told to give it a year | MIS 8 |
| Kip Andersen | Reads the board packet and asks about every number in parentheses | Excel 2, Excel 4 |
| Brenda | ERP vendor's sales engineer at the Boise expo | MIS 10 |
| Gene Palmer | Palmer's Feed & Seed, Kettle Falls; buying-group member | MIS 1 (as "Palmer's"), ITM Week 7 |
| Linda Ostby | Grange Supply, Deer Park; buying-group member who drops out | ITM Week 7 |

Two Dales (Hollister and Kowalchuk) already exist. Don't add a third.

## Timeline

Facts that more than one chapter depends on. Check new chapters against this list, and
add to it whenever a chapter fixes a date, a number, or a person's situation that
another chapter could contradict. Two contradictions got through before this list
existed (Davenport opening in March in one chapter and May in another, and Eli's
course length).

**Year one (2026): Dana's year, the MIS chapters**

- Fall 2025: Prairie Wire is bought by a larger group (MIS 6).
- January–February 2026: Hank's laptop is infected; $14,200 goes to the fake account on Feb 19 (MIS 5).
- March 2026: the inventory pilot starts at Colville; the $86,240 invoice is caught (MIS 1, MIS 5).
- April 2026: the duplicate-customer mailer; the mineral coupon test starts in the spring (MIS 3).
- Spring 2026: Chick Days; Arlo Nygaard retires from Republic in June (MIS 7).
- Spring–summer 2026: Davenport is chosen as store twelve; Sandpoint stays on Walt's dashboard (MIS 8).
- May 2026: Counter Assistant pilot (MIS 9).
- July 2026: the feed-room closet hits 97°F; the Boise expo (MIS 10).
- August 2026: the number-two forklift is down for six days, Aug 10–14 (Excel 3, Excel 4).
- October 2026: Republic's internet outage; the edge server keeps the registers up (MIS 10).

**Year two (Sept 2026 – Oct 2027): Eli's year, the Excel and BI chapters**

- September 2026: Eli starts the evening course (it runs two terms and into the next summer, ending September 2027); the damage claim (Excel 1).
- Thursday, October 1, 2026: the board packet (Excel 2).
- October 2026: the Q3 crew bonus, paid October 14; Marco's ID typo (Excel 3).
- October 2026: one forklift approved, delivered December 2026, $34,000 at 7.5% for five years (Excel 4, Excel 9).
- November 2026: the eleven-store monthly count (Excel 5).
- December 2026: the vendor-returns reconciliation (Excel 6).
- January 2027: the coupon-test PivotTable (Excel 7).
- February 2027: Davenport break-even, about $121,000 a month (Excel 8).
- March 15, 2027: $260,000 goes out for Davenport's build-out; year-end close (Excel 9).
- May 4, 2027: Davenport opens; twelve stores from here on (Excel 10, Excel 11).
- June–July 2027: 900 propane tank monitors (Power Query).
- August 2027: the receiving app goes live; Eli becomes day-shift supervisor (Excel 12).
- September 2027: the Power BI report; Eli's course ends (Power BI).
- Late October – December 2027: the feed buying group; Deer Park drops out; the mill break is approved at 1,520 tons (ITM 310 Week 7).

**People and standing facts**

- Ruth bought five Power BI licenses: Ruth, Hank, Marcy, the dispatcher, Eli. Walt does not have one.
- Marco Reyes: employee 1147, forklift operator.
- Tamarack's domain is tamarackfeed.com.

## Proving the story

When a chapter's numbers come from a tool (Excel, Power BI, a database), build the
artifact and check every number the story states before the chapter ships. Excel 3
is the model: `examples/excel-03-formulas-functions/workbook/build_workbook.py`
generates the workbook from a fixed seed, recalculates it, and checks the story's
numbers and the recording script's expected values. Building it caught five things
the narrative said that no real workbook could produce.

For chapters without an artifact, still compute every figure in a script, even one
line of arithmetic, and keep the numbers consistent across the chapter. Most of the
errors fixed after the first draft were figures written by feel.

## Headings inside a chapter

A heading has to earn its place. At each section boundary, ask:

1. Did the **place** change?
2. Did **time** jump (a different day, or hours the story skips)?
3. Did the **people in the scene** change?

- **None of these:** no heading. Merge into the previous section, and let a sentence of
  prose carry the transition.
- **Yes, but the new section is short (under ~300 words), or it is a small skip inside
  the same thread:** a scene break, `* * *` on its own line.
- **Yes, and the section runs ~300 words or more:** a heading.

A change of **topic** alone never gets a heading. Moving from lookups to rounding is the
prose's job, not a signpost's. There is no heading at the top of a chapter; the chapter
title does that work. Headings are a ceiling, not a quota: roughly one per 500–700 words
at most, and a chapter that stays in one place may have one or none.

**Style.** Headings name what happens or who it happens to, the way C.S. Lewis and
Tolkien titled chapters: *Teo Takes the Laptop*, *What the Testers Found*, *Marco's Pay
Stub*. Not topics, and not old-fashioned "In which…" summaries. Place and time go in the
prose ("Teo carried Hank's laptop down the hall to his own bench that afternoon").
Use an italic dateline under a heading only when putting it in the prose would break the
narrative; expect to need it rarely, if ever.

## Rules

- `heading_rule: scene` in each unit's `unit.yaml` turns on the validator's heading check,
  which warns on the rule above. List a deliberate exception by heading text under
  `heading_exceptions`.

- Third-person past tense, ITM-style sentences (see `schema/VOICE.md`).
- Each chapter ends with a cost: a deferred decision, a tradeoff, a person who stays
  unconvinced. Nothing closes clean.
- Excel units describe Excel behavior accurately. If a glossary definition and real
  Excel behavior disagree, write the scene so it is consistent with both, and flag the
  definition in `unit.yaml`.
- Don't use Priya or Harrowmere (validator rule inherited from Portland Desk).
- When the course glossary is wrong, quote it exactly in `glossary.yaml`, record the
  problem in `unit.yaml` `source_notes`, and write the scene so it is true either way.
  Never repeat the wrong version in the prose as fact.
- Large, loosely related modules (more than about 30 terms) drift into a tour of the
  term list. Plan two scenes with different stakes, or split the module.
