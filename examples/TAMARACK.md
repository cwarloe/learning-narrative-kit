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

- Third-person past tense, ITM-style sentences (see `schema/VOICE.md`).
- Each chapter ends with a cost: a deferred decision, a tradeoff, a person who stays
  unconvinced. Nothing closes clean.
- Excel units describe Excel behavior accurately. If a glossary definition and real
  Excel behavior disagree, write the scene so it is consistent with both, and flag the
  definition in `unit.yaml`.
- Don't use Priya or Harrowmere (validator rule inherited from Portland Desk).
