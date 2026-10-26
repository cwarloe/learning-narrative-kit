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

Starting from material instead of a finished chapter (a term list, a whole course glossary, slides, or the next chapter of a track)? Write a brief and follow **Authoring workflow** in `AGENTS.md`. The format is in [`schema/BRIEF.md`](schema/BRIEF.md), and `workshop/tamarack-mis-companion/` is a worked example. Drafts stay in `workshop/` as candidates until the author publishes them.

Authoring contract (density, tiers, tooltips, QA): [`schema/README.md`](schema/README.md).

Craft standard for every story (earned competence, costed wins, carry-forward endings, pre-draft and pre-merge checklist): [`docs/craft/learning-narrative-framework.md`](docs/craft/learning-narrative-framework.md).

Craft standard for every track: [`docs/craft/learning-narrative-framework.md`](docs/craft/learning-narrative-framework.md).

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

That writes `docs/<unit_id>/` (from `unit.yaml`’s `unit_id`). Then add a card in `tools/build_hub_index.py` and run `python3 tools/build_hub_index.py` to rewrite `docs/index.html` (the renderer does not update the landing page); `python3 tools/check_hub_links.py` checks the result. Commit `examples/` + `docs/` and push `main`.

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

### Portland Desk (Book 0: Ep 00 to 12)

Source: `docs/portland-desk/` (served at `/portland-desk/`). Canon: `docs/research/PORTLAND_TIMELINE.md` and `docs/research/PORTLAND_AUTHOR_BIBLE.md`. The earlier short Security+ units are archived in `archive/examples/` and are not a source.

## Research

Background notes that shaped the contract live in `research/` (including the Sep 2026 Perplexity pass). When documents disagree, follow the precedence list in `AGENTS.md`.
