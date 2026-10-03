# Tamarack Supply — track canon (MIS + Excel/BI)

One company, one cast, one fiscal year. Each unit stands alone, but the world stays
the same so that terms from earlier modules can show up later without re-introduction.

Source of terms: the MindTap course glossary export (`mindtap_glossary_by_module.csv`),
one unit per module. Definitions are copied from that export; the narrative does not
supply rival definitions. Where the export has an obvious error, the unit notes it in
`unit.yaml` rather than quietly rewriting it.

## The company

**Tamarack Supply** is a fictional, family-owned farm-and-hardware retailer: eleven
stores across eastern Washington and north Idaho, a distribution center (the DC) and
head office in Spokane Valley. It sells feed, fencing, seed, tools, work clothes, and
propane. It has a loyalty program, a small web store, and a lot of habits older than
its software.

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

## Rules

- Third-person past tense, ITM-style sentences (see `schema/VOICE.md`).
- Each chapter ends with a cost: a deferred decision, a tradeoff, a person who stays
  unconvinced. Nothing closes clean.
- Excel units describe Excel behavior accurately. If a glossary definition and real
  Excel behavior disagree, write the scene so it is consistent with both, and flag the
  definition in `unit.yaml`.
- Don't use Priya or Harrowmere (validator rule inherited from Portland Desk).
