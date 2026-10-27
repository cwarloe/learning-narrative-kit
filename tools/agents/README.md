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

## How to Invoke in Antigravity

In any conversation turn, you can ask the assistant to invoke these reviewers:
- *"Have the UI standards inspector audit Module 01 for zero-emoji compliance and layout cleanliness."*
- *"Have the technical nitpicker review Episode 07's packet trace."*
- *"Have the prose critic audit the dialogue in Episode 03."*
