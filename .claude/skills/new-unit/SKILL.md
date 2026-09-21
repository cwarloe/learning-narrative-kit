---
name: new-unit
description: Author a new learning-narrative unit for this kit — pick the term set, build one forcing situation, and write narrative.md, glossary.yaml, unit.yaml and review.yaml under examples/<unit_id>/. Use when starting a new chapter, lesson, module or exam cluster for the Portland Desk or ITM tracks.
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

## Build it

The unit id is `$1` when given; otherwise agree one with the author before creating files. It must match the folder name and the Pages path.

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
