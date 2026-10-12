---
name: plan-course
description: Plan a multi-chapter learning narrative from a whole course glossary (or several unit glossaries) — check the brief, map every term to the chapter that introduces, applies or revisits it, report gaps, and propose the story architecture for the author to approve. Use before drafting any chapter of a course companion.
argument-hint: "[brief-id]"
allowed-tools: Bash(.venv/bin/python tools/author.py *) Bash(python3 tools/author.py *) Read Grep Glob Edit Write
---

## Briefs in this repo

```!
ls -1 briefs/ 2>/dev/null
```

The brief is `briefs/$0.brief.yaml` when given; otherwise ask which one, or help the author write one from `schema/BRIEF.md`. The brief format and the author's decision points in `schema/BRIEF.md` win over this skill.

## 1. Check the brief

```bash
.venv/bin/python tools/author.py brief-check briefs/<id>.brief.yaml
.venv/bin/python tools/author.py status briefs/<id>.brief.yaml --init
```

Stop and ask the author about anything under **NEEDS A DEFINITION**, **PROPOSED** or **CONFLICT**. You may propose a definition (`status: proposed`, with where it came from), but only the author can make it `confirmed`. Never let a chapter rest on a definition you supplied.

## 2. Generate the plan

```bash
.venv/bin/python tools/author.py plan briefs/<id>.brief.yaml
```

This writes `workshop/<id>/plan.yaml` and `plan.md`: one chapter per group in course order, every term's introducing chapter, suggested dependencies, revisits found in accepted chapters, and gaps. The computed parts are suggestions. Read the forward references and catalog risks yourself.

## 3. Propose the architecture

Fill the author's parts of `plan.yaml` (they survive `--refresh`):

- `story`: premise, setting, cast, through_line. With a track, the canon file wins.
- Each chapter's `situation`: pov, goal, complication, decision, cost, carries_forward. **carries_forward is what makes it a companion and not ten short stories:** name the consequence a later chapter inherits.
- `status`: `accepted` for chapters that already exist, `planned` or `revise` otherwise, with a `notes` line saying why.

Only claim a link between chapters that the text supports. Where you want one that isn't there yet, write it as a question for the author.

## 4. Hand it to the author

Run `plan-check` and give the author `plan.md`. List the decisions that are theirs: definitions, conflicts, the architecture, which chapter to draft first. **Do not set `approved: true` yourself.** Record where things stand in `workshop/<id>/status.yaml` (stages, open issues, next action).

After approval, draft one chapter at a time with `/new-unit` (candidate mode). Each chapter goes through review and preview before the next one starts.
