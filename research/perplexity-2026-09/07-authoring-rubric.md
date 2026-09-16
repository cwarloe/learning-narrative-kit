# Prompt 7 — Authoring Rubric

- **Title:** QA rubric for a learning narrative kit
- **Model used:** Claude Sonnet 5
- **URL:** https://www.perplexity.ai/search/e17735a1-6532-4c33-b5af-9191759bdf8f

## Full answer

Two-page QA rubric? Wait: one-page QA rubric.

### Purpose and scope

Define the learning narrative kit goals: cohesive term set, interaction scenario, story-first with marks, short definitions, cover test, and HTML/review secondary.

Audience and use: authors, editors, reviewers; align with contract requirements.

### Content quality criteria

**Cohesive term set (terms, definitions, and relationships)**

- Consistency: uniform terminology, clear scope, unambiguous labels.
- Traceability: each term linked to at least one learning objective and to story elements.

**Interaction scenario**

- Relevance: one situation that forces term interplay; stakes and context clearly motivate term use.
- Plausibility: scenario is domain-appropriate and comprehensible without extraneous jargon.

**Story-first with [[id|text]] marks**

- Marks syntax: exact format, unique IDs, deterministic rendering.
- Information density: marks integrated naturally, not forced; no leakage of non-target terms.

**Short definitions**

- Brevity and clarity: 1–2 sentences max; concrete examples where helpful.
- Placement: immediately accessible but not disruptive to narrative flow.

**Cover test (marks hidden)**

- Blind evaluation: story coherent without seeing marks; definitions still support comprehension.
- Recovery test: readers can infer term meanings from context when marks hidden.

**HTML/review secondary**

- Accessibility: semantic HTML, accessible markup, readable without JS.
- Review workflow: clear diff/annotation process; versioning and approval checkpoints.

### Failure modes authors should watch

- **Term drift or collision:** overlapping definitions cause ambiguity; resolve via glossary governance.
- **Mark invisibility drift:** marks render incorrectly in some pipelines; require deterministic escaping and templating.
- **Density misalignment:** too dense (~2 marks per 100 words) or too sparse; calibrate against reading time and cognitive load.
- **Narrative-fragmentation:** marks disrupt flow; ensure narrative beats remain intact with/without marks.
- **Coverage gaps:** essential terms not exercised by the interaction scenario; add an alternate path to exercise.
- **Accessibility gaps:** color/text contrasts; non-visual readers cannot discern marks or definitions.
- **HTML rendering fragility:** broken links, malformed anchors, or broken markup across editors.
- **Review bottlenecks:** unclear rubrics for exam vs. support tiers; ensure consistent scoring across reviewers.

### Governance of density and tiers

**Density target:** approximately 2 marks per 100 words; adjust per genre or audience but document rationale.

**Tier definitions**

- **Exam tier:** high-stakes evaluation of term mastery; stricter criteria, explicit rubrics, reproducible scoring, and stricter alignment to objectives.
- **Support tier:** formative feedback; looser criteria, richer narrative exploration, allowances for partial mastery, and guidance instead of penalties.

### Scoring framework

Map each mark to a learning objective; use a fixed rubric with thresholds for mastery (e.g., 0–100 scale, with bands).

Ensure inter-rater reliability: train reviewers with exemplars; compute agreement metrics.

**Calibration**

Periodic audits: sample stories, measure density, term usage, and error rates; adjust definitions and thresholds accordingly.

### Revision protocol

If density or tier criteria fail, trigger revision sprint: terminology glossary update, scenario rewrite, and re-run of cover test.

### One-page QA checklist (condensed)

- Are all terms defined consistently with no collisions?
- Does the interaction scenario compel term interplay in a plausible way?
- Are all [[id|text]] marks correct, unique, and renderable across tools?
- Do definitions appear short, clear, and correctly placed?
- Does the cover test allow comprehension with marks hidden?
- Is HTML accessible, semantically structured, and review-friendly?
- Is the density near 2 marks per 100 words, justified if not?
- Are exam and support tier criteria distinct, documented, and applied consistently?
- Are failure modes addressed with concrete mitigations?
- Is there a governance log for changes to terms, definitions, and rubrics?

**Sources:** 10 sources were cited in the answer.
