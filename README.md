# Learning Narrative Kit

## The point

Take a cohesive set of terms and concepts from a learning chunk (a class module, an exam section, a lesson) and weave them into **one story that actually makes sense**.

Same move as:
- 8th-grade vocab: “use every word in a sentence/paragraph”
- Eli Goldratt’s *The Goal*: operations concepts inside a plant story
- NADF’s narrative track: analytical ideas inside Ethan’s first tickets

The story is not decoration. It is the thing that supplies **connectedness** — why these words belong together, how they depend on each other, what decision they inform. Definitions alone stay floating; a story makes them load-bearing.

Interactive glosses (hover, sidebar) and review cards are optional layers for lookup and later retrieval. They are not the pedagogy.

## Hand this to an LLM

**Start here:** [`AGENTS.md`](AGENTS.md) — full ship checklist, validate/render commands, copy-paste prompt, and links to track canon.

Authoring contract (density, tiers, tooltips, QA): [`schema/README.md`](schema/README.md).

Portland Desk (Security+) voice and sizing: [`examples/PORTLAND_DESK.md`](examples/PORTLAND_DESK.md).

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
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python tools/validate_unit.py examples/<unit_id>
.venv/bin/python tools/render_unit.py examples/<unit_id>
```

That writes `docs/<unit_id>/` (from `unit.yaml`’s `unit_id`). Then **manually** add a card to `docs/index.html` (the renderer does not update the landing page). Commit `examples/` + `docs/` and push `main`.

Local scratch HTML under `examples/` stays gitignored; **`docs/` is committed** for GitHub Pages.

## GitHub Pages

Repo Settings → Pages → Source: **Deploy from a branch** → Branch: **main** → folder: **/docs** (once).

Landing: https://cwarloe.github.io/learning-narrative-kit/

Re-render + push updates the same unit URLs.

## Generation order (story-first)

1. Collect the term set that belongs together (slides, notes, flashcards, lesson vocab).
2. Decide the **situation** that would force those ideas to interact.
3. Write `narrative.md` so each term earns its place.
4. Attach short definitions in `glossary.yaml` (exam-faithful when studying a class).
5. Run the authoring QA checklist in `schema/README.md` (cover test, density, tiers).
6. `validate_unit.py` → `render_unit.py` → update `docs/index.html` → commit & push.

## Specimens

### ITM track

| Folder | Title |
|--------|--------|
| `examples/itm310-vanguard-edge/` | The Goal of Vanguard Edge |

### Portland Desk track (Security+ precursor)

| Folder | Title |
|--------|--------|
| `examples/secplus-ports-helpdesk/` | The Port That Is Open |
| `examples/secplus-auth-helpdesk/` | Prove Who You Are |
| `examples/secplus-phishing-helpdesk/` | Don't Click That |
| `examples/secplus-malware-helpdesk/` | Something on the Box |
| `examples/secplus-wireless-helpdesk/` | The Air Is Shared |
| `examples/secplus-physical-helpdesk/` | Badge, Lock, Eyes |
| `examples/secplus-crypto-helpdesk/` | Trust on Paper |
| `examples/secplus-ir-helpdesk/` | When the Ticket Escalates |

Track rules: [`examples/PORTLAND_DESK.md`](examples/PORTLAND_DESK.md).

## Research

Background notes that shaped the contract live in `research/` (including the Sep 2026 Perplexity pass). **Schema wins** if notes disagree.
