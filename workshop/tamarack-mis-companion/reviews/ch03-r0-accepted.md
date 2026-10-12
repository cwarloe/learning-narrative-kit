# Review: Tamarack — One Customer, Four Records

Candidate: `examples/mis-03-data-bi` · 2026-10-12

This report separates three things. **Automated checks** are mechanical and either pass or fail. **Heuristic flags** are patterns that often mean a problem; each one needs a person to look, and a passage that reads well and is accurate stays as it is (schema/README.md rule 9). **Editorial review** is judgment, and **learning effectiveness** is not measured here at all.

## 1. Automated checks

```
Words (cover-stripped): 2309
Marks: 47 unique=47 glossary=47
Mark density: 2.04 marks per 100 words
Tiers: exam=47 support=0
Headings: 2, scene breaks: 1
RESULT: PASS
```

Voice metrics (reading aid; ITM control: mean 19.7w, sd 14.0, 11% short): `sentences=141  mean=16.1w  sd=9.1  short(<=6w)=18%  em-dash/1k=0.0` `fragments=8  frag-runs=1  no-determiner=20  aphorisms=0  antithesis=0  tricolon=2`

Plan ch03: 47/47 planned terms marked
Builds on 4 earlier term(s); 4 mentioned in the text (data, process, Information, server)

## 2. Heuristic flags (need a person to look)

- **Definition echo:** 1 mark(s) sit in a sentence that restates most of the glossary definition. Fine when a character explains because the scene needs it (schema/README.md rule 8); many in a row is the vocabulary-parade pattern.
  - sequential_access_file_structure: "It stored customers in a sequential access file structure: records in the order they were entered, read from top to bott"
- **Inline glosses:** 18 of 47 marks (38%) are followed at once by their explanation ("X meant…", "X, a…", "X: …"). Context only: this did not separate strong from weak chapters in calibration.
- **Longest exposition run:** 3 consecutive paragraphs each introduce a new term with no dialogue. Five or more is the tour-guide pattern (a booth, a term, the next booth).
- **Mark clusters:** 2 paragraph(s) with 4+ marked terms (a list wearing prose).
  - The stores lost internet a few times a year, usually in winter. Teo proposed a distributed database so each st…
  - The web store's vendor ran an object-oriented database. In it, a product was an object that held its own data …
- **Marks near decisions or dialogue:** 49% of marks are in paragraphs with dialogue or a decision word. Low numbers suggest terms in exposition rather than at the complication or pivot (schema/README.md → Beat structure).
- **Ending** (does it charge a cost? schema/VOICE.md → The structural tell): "Walt approved the merchandising data mart and declined the full warehouse until next fiscal year. Marcy's mineral-feed test was still running. The spring mailer went out again to the corrected list, two weeks late, after most of the fencing season had started.
"

## 3. Continuity (for the author to confirm)

- **Names and proper nouns not in the canon or any accepted chapter:** Ashby, Gordon, Gordons, Tableau. New characters or places are allowed; confirm each is intended, and add recurring ones to the canon.
- **Dated statements to check against the track timeline:** 6
  - In April he walked into the Colville store holding four identical envelopes, each one a spring mailer with a twenty-dollar coupon for fencin
  - Ranchers got fencing, backyard flocks got feed, people who'd bought a pressure washer in October got a coupon for a new one in April.
  - Tamarack's first loyalty program, from 2009, had been run by a vendor that sent nightly files.
  - The 2009 vendor's export had been arranged in a hierarchical model: each store at the top, customers underneath as children, purchases under
  - Teo said, "if anybody had used it in 2014.
  - Data-mining analysis on the merged purchase history found a pattern Marcy hadn't known: customers who bought T-posts in March bought mineral
- **Figures stated** (each should come from a calculation, schema/README.md → Prove the story): 1,940, four customers, nineteen days, six weeks, three weeks, two stores, two weeks

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
