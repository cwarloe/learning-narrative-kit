@AGENTS.md

## Claude-specific notes

`AGENTS.md` above is the shared playbook every coding agent reads; it is the source of truth for the ship checklist and validate/render commands, and its "Which document wins" section sets precedence. Story canon lives in `docs/research/PORTLAND_TIMELINE.md` and `PORTLAND_AUTHOR_BIBLE.md`.

This file exists so the playbook still loads in contexts where `AGENTS.md` isn't read directly — in particular, a Claude Code project that clones several repositories, where each clone is attached as an additional directory and only `CLAUDE.md` loads from it. Keep Claude-only instructions below this line.

- **Portland Desk source:** Edit `docs/portland-desk/` directly; it is the single source and the published courseware. Do not recreate the archived root copy.
- **Validate before render, render before commit:** `validate_unit.py` and `template/tools/check-links.py` must PASS; a warn is not a pass-with-notes to argue past, it's a thing to fix or explain.
- **Plain-English Standard (MANDATORY):** Adhere strictly to `docs/research/PLAIN_ENGLISH_STYLE_GUIDE.md`. Banned terms include "invariant/invariants", "falsifiable hypothesis", "rubric", "pedagogy", "heuristic" (in general prose), and "scaffolding". All courseware must read in natural spoken English accessible to a U.S. high school graduate.
- **Story and lab:** Follow the approved model in `AGENTS.md` and `docs/research/PEDAGOGICAL_AGENCY_ARCHITECTURE.md`. Chapters may show the answer; labs open with worked examples and end with a transfer problem. Do not withhold story answers or put story resolutions in lab epilogues.
- **Visual Art & Technical Panels:** Follow `docs/research/VISUAL_ART_DIRECTION.md`. All AI images must have ZERO text/letters. Use reference photos (Img2Img) for hardware accuracy, and overlay text using the browser.
- **Interactive Components:** Author terminals using the ````lnk-terminal` syntax and panels with ````callout-panel` per `docs/research/INTERACTIVE_COMPONENTS_SPEC.md`.
- **The cover test is the real bar:** Strip every `[[...]]` mark and the story must still teach how the concepts depend on each other. A unit that only works with tooltips on has failed, even if validation is green.
- **Don't invent port numbers, exam definitions, or vendor specifics.** If the course source doesn't state it, ask rather than supply it — a confidently wrong Sec+ fact in a study narrative is worse than a gap.
- `research/` is background, not contract. `archive/` is never a source. See the precedence list in `AGENTS.md`.
