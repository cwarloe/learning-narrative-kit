---
name: new-unit
description: Author a new learning-narrative unit for this kit — pick the term set, build one forcing situation, and write narrative.md, glossary.yaml, unit.yaml and review.yaml under examples/<unit_id>/. Use when starting a new chapter, lesson, module or exam cluster, or drafting a candidate chapter from a brief or course plan.
argument-hint: "[unit-id]"
allowed-tools: Read Grep Glob
---

## Existing units to clone file shapes from

```!
ls -1 examples/ 2>/dev/null
```

## Authoring contract

The full contract is `schema/README.md`, and it **wins over anything in this skill**. Track canon:

- Portland Desk (Security+) — `examples/PORTLAND_DESK.md`
- ITM — `examples/itm310-vanguard-edge/` as the specimen

Read the contract and the relevant track file before writing. Don't work from what a sibling unit happens to do; the sibling is for file *shapes*.

## Starting from a brief (candidate mode)

If the job has a brief (`briefs/<id>.brief.yaml`), the chapter is a **candidate**: write it in `workshop/<id>/candidates/<unit_id>/`, never directly in `examples/`, and never over an accepted chapter.

1. `.venv/bin/python tools/author.py brief-check briefs/<id>.brief.yaml`. For a course plan, also run `plan-check --chapter chNN`. Don't draft past a failed gate unless the author says to, and if they do, record it in `status.yaml`.
2. Write the four files (below), taking the situation from the plan.
3. Review, revise (no more than `max_revisions` times, default 2), validate, and preview:
   ```bash
   .venv/bin/python tools/author.py review workshop/<id>/candidates/<unit_id> --brief briefs/<id>.brief.yaml --chapter chNN --out workshop/<id>/reviews/chNN-r1.md
   .venv/bin/python tools/validate_unit.py workshop/<id>/candidates/<unit_id>
   .venv/bin/python tools/render_unit.py workshop/<id>/candidates/<unit_id> --out workshop/<id>/preview
   ```
4. Do your own editorial pass, in the report under its own heading, separate from the automated results. Cover test, accuracy against each definition, and continuity against the canon and the accepted chapters. The review's continuity list is a prompt for this pass, not a substitute.
5. Update `status.yaml` and stop. The author accepts, asks for a revision, or rejects. Publishing is `/ship-unit`, and only on their say-so.

## Build it

The unit id is `$0` when given; otherwise agree one with the author before creating files. It must match the folder name and the Pages path.

1. **Collect the term set** that genuinely belongs together — one exam or lesson cluster, not an arbitrary slice.
2. **Choose one forcing situation** where those ideas must interact. Build each beat as goal / complication / pivot, with the marked terms landing on the complication or the pivot, per `schema/README.md` → Beat structure.
3. **Create** `examples/<unit_id>/` by copying the nearest sibling's file shapes.
4. **Write `narrative.md` first.** The story is the learning object; the glossary coheres inside it. Marks are `[[term_id|surface text]]`.
5. **Write `glossary.yaml`** — every id used at least once in the narrative.
6. **Write `unit.yaml`** (`unit_id` matches the folder) and **`review.yaml`** (cards from the glossary, each with a `tier`).

## The bar

**The cover test is what matters.** Strip every `[[...]]` mark; the story must still teach how the concepts depend on each other. A unit that only works with tooltips on has failed, even when validation is green.

**Don't let the situation resolve tidily.** Beat structure asks what the pivot *costs*; answer it. The fix shouldn't work the first time, the vendor shouldn't be helpful, and the user shouldn't comply just because someone explained the reason well. A chapter where the ticket closes clean and the queue empties has taught the terms and told a lie about the work — and the shape of a narrative teaches as surely as its marked terms do. Escalated, deferred, mitigated with a tradeoff, or fixed-and-the-user-is-still-annoyed are all better endings. `schema/VOICE.md` → The structural tell has the full list.

Two tiers when used: `exam` = study targets, `support` = readability jargon, flavor unmarked. Tooltips carry `definition` plus optional `context` only — `refs` stay in the sidebar.

**Don't invent port numbers, exam definitions, or vendor specifics.** If the course source doesn't state it, ask. A confidently wrong Security+ fact inside a study narrative is worse than a gap, because the story makes it memorable.

When the files are written, run `/ship-unit` to validate, render and publish.
