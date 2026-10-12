# Review: Tamarack — The Closet Gets Too Hot

Candidate: `examples/mis-10-emerging` · 2026-10-12

This report separates three things. **Automated checks** are mechanical and either pass or fail. **Heuristic flags** are patterns that often mean a problem; each one needs a person to look. **Editorial review** is judgment, and **learning effectiveness** is not measured here at all.

## 1. Automated checks

```
Words (cover-stripped): 1917
Marks: 42 unique=42 glossary=42
Mark density: 2.19 marks per 100 words
Tiers: exam=42 support=0
Headings: 2, scene breaks: 1
RESULT: PASS
```

Voice metrics (reading aid; ITM control: mean 19.7w, sd 14.0, 11% short): `sentences=114  mean=16.5w  sd=9.2  short(<=6w)=9%  em-dash/1k=1.6` `fragments=3  frag-runs=0  no-determiner=15  aphorisms=0  antithesis=0  tricolon=4`

Plan ch10: 42/42 planned terms marked
Builds on 5 earlier term(s); 5 mentioned in the text (process, object, data, computer, Information)

## 2. Heuristic flags (need a person to look)

- **Definition echo:** 3 mark(s) sit in a sentence that restates most of the glossary definition. Some are fine (a character explaining to another); many in a row is the vocabulary-parade pattern.
  - public_cloud: "A public cloud meant connecting over the Internet to a provider's off-site infrastructure, shared with its other custome"
  - private_cloud: "A private cloud ran the same kind of services on a private network for one organization."
  - cryptocurrency: "A different booth wanted to let customers pay in cryptocurrency, digital money created from computer code and tracked by"
- **Inline glosses:** 17 of 42 marks (40%) are followed at once by their explanation ("X meant…", "X, a…", "X: …"). A few help; a high share means the prose is defining terms rather than using them.
- **Longest exposition run:** 5 consecutive paragraphs each introduce a new term with no dialogue. Five or more is the tour-guide pattern (a booth, a term, the next booth).
- **Mark clusters:** 2 paragraph(s) with 4+ marked terms (a list wearing prose).
  - At the top was software as a service: the vendor ran the whole application and Tamarack used it through a brow…
  - A forklift manufacturer offered virtual reality training: a headset with computer-generated 3D scenes that mad…
- **Marks near decisions or dialogue:** 52% of marks are in paragraphs with dialogue or a decision word. Low numbers suggest terms in exposition rather than at the complication or pivot (schema/README.md → Beat structure).
- **Ending** (does it charge a cost? schema/VOICE.md → The structural tell): "the Republic store's internet went down for six hours during the first snow, and its edge server, which had been installed only two weeks earlier, kept the registers running until the line came back. Then it took eleven hours to sync, and two loyalty customers got double points.
"

## 3. Continuity (for the author to confirm)

- **Names and proper nouns not in the canon or any accepted chapter:** Boise, Oregon, Seattle, Founders, Herd. New characters or places are allowed; confirm each is intended, and add recurring ones to the canon.
- **Dated statements to check against the track timeline:** 3
  - In the second week of July, the window air conditioner in the feed-room closet quit during a heat wave, and by two in the afternoon the ther
  - The QR codes went on the feed tags in September.
  - In October the Republic store's internet went down for six hours during the first snow, and its edge server, which had been installed only t
- **Figures stated** (each should come from a calculation, schema/README.md → Prove the story): eleven hours, ninety-seven degrees, six hours, twenty minutes, two weeks

## 4. Editorial review (judgment; fill in)

- [ ] **Cover test:** read the marks-stripped text (`*.cover.txt` next to this report). Do the concepts' relationships still come through?
- [ ] **Concepts matter:** each major term changes a goal, complication, decision, or consequence; none is decoration.
- [ ] **Instructional accuracy:** every claim about a concept matches its glossary definition or a cited source; nothing unverified is stated as fact.
- [ ] **Continuity:** names, dates, numbers, and standing facts agree with the canon and accepted chapters.
- [ ] **The pivot costs something,** and the ending doesn't explain the chapter.
- [ ] **Voice:** reads like a person, not a generator (schema/VOICE.md).

## 5. Not measured

Whether readers actually learn more from this chapter than from the glossary alone. That needs readers: for example a short pre/post question set on the chapter's relationships, given to a few students.
