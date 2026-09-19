# Agent / LLM handoff — Learning Narrative Kit

Use this file when an LLM (or human) authors a new unit **without** a specialized bot. Schema wins if anything conflicts: `schema/README.md`.

## What this kit is

Story-first pedagogy: a cohesive term set woven into **one** meaningful narrative so the words gain shared context. Hover glossaries and review decks are secondary lookup/retrieval — not the point.

Inspired by: 8th-grade “use the vocab in a paragraph,” Goldratt’s *The Goal*, NADF.

## Repo layout

```
examples/<unit_id>/     # SOURCE — write here
  unit.yaml
  glossary.yaml
  narrative.md
  review.yaml           # optional but expected for exam tracks
docs/<unit_id>/         # GENERATED — never hand-edit; from render_unit.py
docs/index.html         # landing cards — update BY HAND when adding a unit
docs/unit.css, unit.js  # shared Pages assets
schema/                 # authoring contract + informal schema
tools/                  # validate_unit.py, render_unit.py
research/               # background notes (schema wins on conflict)
```

Marks in prose: `[[term_id|surface text]]`

## Setup (once)

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

`.venv` at the repo root is the only supported location — it is gitignored, so a fresh clone has none until you run the above. If your system `python3` already has PyYAML, you can skip the venv and run the tools with `python3` directly; that is the only dependency.

## Add a new unit (ship checklist)

1. **Collect the term set** that belongs together (one exam/lesson cluster).
2. **Choose one forcing situation** where those ideas must interact (ticket plot, plant floor, etc.). Build each beat as goal / complication / pivot, with the marked terms on the complication or the pivot (`schema/README.md` → Beat structure).
3. **Create** `examples/<unit_id>/` by copying the nearest sibling unit’s file shapes.
4. **Write** `narrative.md` (story-first) and `glossary.yaml` (every id used ≥1 in the narrative).
5. **Write** `unit.yaml` (`unit_id` must match folder name and Pages path) and `review.yaml` (cards from glossary; include `tier`).
6. **QA by hand** — cover test, density, tiers, tooltip contract (`schema/README.md`).
7. **Validate (must PASS):**
   ```bash
   .venv/bin/python tools/validate_unit.py examples/<unit_id>
   ```
8. **Render (do not hand-edit HTML):**
   ```bash
   .venv/bin/python tools/render_unit.py examples/<unit_id>
   ```
9. **Landing card** — add a card under the right track in `docs/index.html` (renderer does **not** update the landing page).
10. **Commit** `examples/<unit_id>/`, `docs/<unit_id>/`, and `docs/index.html`. Push `main`. Pages serves `/docs`.

Expected URL: `https://cwarloe.github.io/learning-narrative-kit/<unit_id>/`

## Validate rules (mechanical)

| Check | Severity |
|-------|----------|
| Glossary + narrative load | fail |
| Every glossary id marked ≥1 | fail |
| No mark ids missing from glossary | fail |
| Mark density | report |
| Missing `tier` when any tier present | warn |
| `Priya` or `Harrowmere` in narrative | fail |

## Authoring contract (summary)

Full text: `schema/README.md`. Non-negotiables:

- Narrative is the learning object; glossary coheres inside it.
- Cover test: strip `[[...]]`; story still teaches relationships.
- Tooltip = `definition` + optional `context` only; `refs` stay sidebar.
- Two tiers when used: `exam` = study targets; `support` = readability jargon; flavor unmarked.
- HTML is generated only via `tools/render_unit.py`.

## Track-specific canon

- **Portland Desk (Sec+):** `examples/PORTLAND_DESK.md`
- **ITM:** see `examples/itm310-vanguard-edge/` as specimen

## Copy-paste prompt for a new chapter

Paste into any capable LLM with this repo checked out:

```
You are authoring a learning-narrative unit for this kit.

Read and follow:
- AGENTS.md (this playbook)
- schema/README.md (authoring contract)
- For Portland Desk Sec+: examples/PORTLAND_DESK.md
- Clone file shapes from the nearest examples/<sibling>/

Task: create examples/<UNIT_ID>/ with unit.yaml, glossary.yaml, narrative.md, review.yaml
for topic: <TOPIC / exam cluster>.

Then run validate_unit.py (must PASS), render_unit.py, add a card to docs/index.html,
and commit examples/<UNIT_ID>/ + docs/<UNIT_ID>/ + docs/index.html.

Constraints from the track docs apply. Do not hand-edit generated HTML.
Do not invent port numbers or exam definitions that contradict the course source.
```

## Done definition

A unit is done when: validate PASS, render succeeded, landing card present, cover test passes, sticky teaching beats can be named in one sentence each, and `docs/` is pushed for Pages.
