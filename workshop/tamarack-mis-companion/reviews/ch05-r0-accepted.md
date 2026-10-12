# Review: Tamarack — The Invoice That Changed Its Bank

Candidate: `examples/mis-05-security` · 2026-10-12

This report separates three things. **Automated checks** are mechanical and either pass or fail. **Heuristic flags** are patterns that often mean a problem; each one needs a person to look, and a passage that reads well and is accurate stays as it is (schema/README.md rule 9). **Editorial review** is judgment, and **learning effectiveness** is not measured here at all.

## 1. Automated checks

```
Words (cover-stripped): 2338
Marks: 49 unique=49 glossary=49
Mark density: 2.10 marks per 100 words
Tiers: exam=49 support=0
Headings: 3, scene breaks: 1
RESULT: PASS
```

Voice metrics (reading aid; ITM control: mean 19.7w, sd 14.0, 11% short): `sentences=139  mean=16.5w  sd=10.3  short(<=6w)=19%  em-dash/1k=0.9` `fragments=8  frag-runs=1  no-determiner=17  aphorisms=0  antithesis=1  tricolon=2`

Plan ch05: 49/49 planned terms marked
Builds on 6 earlier term(s); 5 mentioned in the text (data, Information, computer, server, operating system (OS))

## 2. Heuristic flags (need a person to look)

- **Definition echo:** 0 mark(s) sit in a sentence that restates most of the glossary definition. Fine when a character explains because the scene needs it (schema/README.md rule 8); many in a row is the vocabulary-parade pattern.
- **Inline glosses:** 11 of 49 marks (22%) are followed at once by their explanation ("X meant…", "X, a…", "X: …"). Context only: this did not separate strong from weak chapters in calibration.
- **Longest exposition run:** 5 consecutive paragraphs each introduce a new term with no dialogue. Five or more is the tour-guide pattern (a booth, a term, the next booth).
- **Mark clusters:** 4 paragraph(s) with 4+ marked terms (a list wearing prose).
  - In January Hank had needed to convert a PDF to a spreadsheet and had downloaded a free converter from a site t…
  - The testers took it apart in a sandbox. It contained a macro virus, written in the spreadsheet program's own m…
  - The vendor bank-change process got a real fix. Tamarack would accept bank changes only through a signed form f…
  - The DC already used fingerprint readers on the time clock, a form of biometric security. The vendor's sales re…
- **Marks near decisions or dialogue:** 49% of marks are in paragraphs with dialogue or a decision word. Low numbers suggest terms in exposition rather than at the complication or pivot (schema/README.md → Beat structure).
- **Ending** (does it charge a cost? schema/VOICE.md → The structural tell): "g. In June the seed company's real accounts-receivable office received an email, from an address with one letter doubled, asking whether Tamarack's bank had changed. Karen forwarded it to Hank with one line: "Is this you?" Hank called her back at the number on the paper invoice.
"

## 3. Continuity (for the author to confirm)

- **Names and proper nouns not in the canon or any accepted chapter:** Karen, Payroll. New characters or places are allowed; confirm each is intended, and add recurring ones to the canon.
- **Dated statements to check against the track timeline:** 11
  - She asked whether Tamarack had paid the February invoice to the new account, because their February payment had never arrived.
  - Fourteen thousand two hundred dollars, sent on February 19 to an account in another state, following an earlier email about the same "bank c
  - In January Hank had needed to convert a PDF to a spreadsheet and had downloaded a free converter from a site that ranked well in search.
  - There was also a bundle of adware that tracked his browsing to serve ads, which explained the pop-ups Hank had been complaining about and ig
  - In November a stranger had emailed Tamarack's general inbox.
  - The contractor who wrote it in 2004 had left a backdoor: a hard-coded username and password that bypassed the program's login, presumably so
  - Its CPU had been pinned at ninety-eight percent since a public-facing service was exposed in December.
  - Besides the bank-change email, the attacker had sent a second message in February with a spreadsheet attached, "updated seed pricing."
  - The bank's fraud desk called Hank back in April.
  - The receiving account had been emptied the day after the February deposit.
  - In June the seed company's real accounts-receivable office received an email, from an address with one letter doubled, asking whether Tamara
- **Figures stated** (each should come from a calculation, schema/README.md → Prove the story): $500, $86,240, forty minutes, hundred dollars, ninety-eight percent, two days, two months, two stores

## 4. Editorial review (judgment; fill in)

- [ ] **Cover test:** read the marks-stripped text (`*.cover.txt` next to this report). Do the concepts' relationships still come through?
- [ ] **Concepts matter:** each major term changes a goal, complication, decision, or consequence; none is decoration.
- [ ] **Instructional accuracy:** every claim about a concept matches its glossary definition or a cited source; nothing unverified is stated as fact.
- [ ] **Continuity:** names, dates, numbers, and standing facts agree with the canon and accepted chapters.
- [ ] **Explanations are earned:** any technical explanation has a reason in the scene and reads as an exchange, not a lecture (schema/README.md rule 8).
- [ ] **The pivot costs something,** and the ending doesn't explain the chapter.
- [ ] **Voice:** reads like a person, not a generator (schema/VOICE.md).

## 5. Not measured

Whether readers learn more with this chapter alongside their course materials than without it. The chapter supports the course; it doesn't replace it. Finding out needs readers: for example a short pre/post question set on the chapter's relationships, given to a few students.
