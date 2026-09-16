# Learning Narrative Kit

## The point

Take a cohesive set of terms and concepts from a learning chunk (a class module, an exam section, a lesson) and weave them into **one story that actually makes sense**.

Same move as:
- 8th-grade vocab: “use every word in a sentence/paragraph”
- Eli Goldratt’s *The Goal*: operations concepts inside a plant story
- NADF’s narrative track: analytical ideas inside Ethan’s first tickets

The story is not decoration. It is the thing that supplies **connectedness** — why these words belong together, how they depend on each other, what decision they inform. Definitions alone stay floating; a story makes them load-bearing.

Interactive glosses (hover, sidebar) and review cards are optional layers for lookup and later retrieval. They are not the pedagogy.

## Unit shape

| File | Role |
|------|------|
| `unit.yaml` | What this chunk is for, sources, constraints |
| `glossary.yaml` | The term set that must cohere |
| `narrative.md` | The story that uses them with real meaning |
| `review.yaml` | Optional flashcards derived from the glossary |

Marks in prose: `[[term_id|surface text]]`

## Generation order (story-first)

1. Collect the term set that belongs together (slides, notes, flashcards, lesson vocab).
2. Decide the **situation** that would force those ideas to interact (a plant crisis, a first ticket, an exam-relevant decision).
3. Write the narrative so each term earns its place — used as someone would use it when thinking, not as a checklist.
4. Attach short definitions for lookup (exam-faithful when studying a class; analytical when teaching a framework).
5. Validate: every required term appears; every mark has a definition; the story still reads if you hide the marks.
6. Optionally render HTML and emit a review deck.

## Specimens

- `examples/itm310-vanguard-edge/` — disciplined class study narrative (ITM 310), glossary-first, Goldratt-shaped plant story.
- `examples/secplus-ports-helpdesk/` — Security+ SY0-701 ports/protocols help-desk precursor (*Portland Desk*). Two-tier glossary (exam + support), tooltip = definition + optional context, refs on sidebar only. Open `portland-desk.html` or rebuild with `python build_preview.py` (needs PyYAML).
- Earlier NADF prologue HTML was a one-shot smoke test without a prebuilt glossary.

See `schema/README.md` for the authoring contract.
