# Learning Narrative Kit

## The point

Take a cohesive set of terms and concepts from a learning chunk (a class module, an exam section, a lesson) and weave them into **one story that actually makes sense**.

Same move as:
- 8th-grade vocab: “use every word in a sentence/paragraph”
- Eli Goldratt’s *The Goal*: operations concepts inside a plant story
- NADF’s narrative track: analytical ideas inside Ethan’s first tickets

The story is not decoration. It is the thing that supplies **connectedness** — why these words belong together, how they depend on each other, what decision they inform. Definitions alone stay floating; a story makes them load-bearing.

Interactive glosses (hover, sidebar) and review cards are optional layers for lookup and later retrieval. They are not the pedagogy.

## Source of truth

**Markdown + YAML in → HTML out.**

| File | Role |
|------|------|
| `unit.yaml` | What this chunk is for, sources, constraints |
| `glossary.yaml` | The term set that must cohere |
| `narrative.md` | The story that uses them with real meaning |
| `review.yaml` | Optional flashcards derived from the glossary |

Marks in prose: `[[term_id|surface text]]`

Do **not** author chapters as HTML. Render when you want hovers / Exam-only / All:

```bash
# Prefer the ports example venv (has PyYAML)
examples/secplus-ports-helpdesk/.venv/bin/python tools/render_unit.py examples/itm310-vanguard-edge
examples/secplus-ports-helpdesk/.venv/bin/python tools/render_unit.py examples/secplus-ports-helpdesk
examples/secplus-ports-helpdesk/.venv/bin/python tools/render_unit.py examples/secplus-auth-helpdesk
```

That writes `docs/<unit_id>/index.html` (from `unit.yaml`’s `unit_id`). Local scratch HTML under `examples/` stays gitignored; **`docs/` is committed** for GitHub Pages.

## GitHub Pages

Repo Settings → Pages → Source: **Deploy from a branch** → Branch: **main** → folder: **/docs** (once).

Expected URLs after Pages is enabled:

- https://cwarloe.github.io/learning-narrative-kit/
- https://cwarloe.github.io/learning-narrative-kit/itm310-vanguard-edge/
- https://cwarloe.github.io/learning-narrative-kit/secplus-ports-helpdesk/
- https://cwarloe.github.io/learning-narrative-kit/secplus-auth-helpdesk/

Re-render + push updates the same URLs.

## Generation order (story-first)

1. Collect the term set that belongs together (slides, notes, flashcards, lesson vocab).
2. Decide the **situation** that would force those ideas to interact.
3. Write `narrative.md` so each term earns its place.
4. Attach short definitions in `glossary.yaml` (exam-faithful when studying a class).
5. Run the authoring QA checklist in `schema/README.md` (cover test, density, tiers).
6. Optionally render HTML (`tools/render_unit.py`) and emit a review deck.

## Specimens

- `examples/itm310-vanguard-edge/` — ITM 310 class study narrative (markdown unit).
- `examples/secplus-ports-helpdesk/` — Security+ ports help-desk precursor (*Portland Desk — The Port That Is Open*).
- `examples/secplus-auth-helpdesk/` — Security+ identity/auth help-desk precursor (*Portland Desk — Prove Who You Are*).

Validate: `python tools/validate_unit.py examples/<unit>` (see `tools/README.md`).

## Research

Background notes that shaped the contract live in `research/` (including the Sep 2026 Perplexity pass). Schema wins if notes disagree.

See `schema/README.md` for the full authoring contract.
