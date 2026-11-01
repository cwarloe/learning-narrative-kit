# Editorial & QA Review Agents

This directory contains definitions for the project's specialized adversarial review subagents.

## Agents

### 1. `ui_standards_inspector`
- **Definition:** [`ui_standards_inspector.md`](ui_standards_inspector.md)
- **Role:** The ruthless Design Systems Auditor & UI/UX QA Inspector. Enforces the strict zero-emoji mandate across all CSS, JS, HTML, and markdown files. Eliminates "AI slop" tropes (emojis, raw `<details>` dropdowns, broken code fences, unstyled buttons) and enforces high-density, engineering-grade typography (`JetBrains Mono`, clean monospace tokens `[PREDICTION GATE]`, `[OK]`, `[VERIFIED]`). Runs `tools/check_cleanliness.py`.

### 2. `technical_nitpicker`
- **Definition:** [`technical_nitpicker.md`](technical_nitpicker.md)
- **Role:** The pedantic senior systems architect / protocol SME. Pushes his glasses up his nose, finds RFC discrepancies, flags corner cases, verifies subnet calculations, and ensures packet traces and telemetry are mathematically and topologically sound.

### 3. `prose_critic`
- **Definition:** [`prose_critic.md`](prose_critic.md)
- **Role:** The blunt, cynical literary editor and dialogue coach. Eliminates wooden "AI-sounding" dialogue, flags pacing stalls and melodramatic tropes, catches word repetitions, and enforces the plain-English style guide (`docs/research/PLAIN_ENGLISH_STYLE_GUIDE.md`).

### 4. `story_grid_reviewer`
- **Definition:** [`story_grid_reviewer.md`](story_grid_reviewer.md)
- **Role:** Reviews causal story structure using the Five Commandments: inciting incident, progressive complications/turning point, crisis, climax, and resolution. Cites story evidence, distinguishes scenes from chapters, and recommends proportionate changes without rewriting.
- **Reference:** [Story Grid article supplied by the author](https://storygrid.com/articles/five-commandments-of-storytelling). Current article text was blocked by the setup environment; the definition identifies its working paraphrases and requires honest source reporting.

## How to Invoke in Antigravity

In any conversation turn, you can ask the assistant to invoke these reviewers:
- *"Have the UI standards inspector audit Module 01 for zero-emoji compliance and layout cleanliness."*
- *"Have the technical nitpicker review Episode 07's packet trace."*
- *"Have the prose critic audit the dialogue in Episode 03."*

## Story Grid review

For any assistant, load `tools/agents/story_grid_reviewer.md` and supply the target:

> Use the Story Grid reviewer on `docs/portland-desk/narrative/11-the-air-is-shared.md`. Review the chapter arc and its individual scenes. Report findings; do not rewrite it.

Claude Code also has a native read-only agent in
`.claude/agents/story-grid-reviewer.md` and a matching skill:

```text
/review-story-grid docs/portland-desk/narrative/11-the-air-is-shared.md
```

The review is an editorial judgment, not a CI gate or an automatic rewrite.
The caller can save its report under `workshop/` when requested. A pilot report
is in `workshop/story-grid-pilot/reviews/episode11.md`.
