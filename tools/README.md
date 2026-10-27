# Tools

Setup (from repo root): `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`.
`.venv` at the repo root is the supported location (gitignored). If system `python3` already has PyYAML you can run the tools with `python3` directly.

## Tool index

Every `.py` file in `tools/`, sorted by how to treat it. `python3 tools/check_tools_index.py` checks that this list stays complete (CI runs it as a warning).

### Use these (pipeline and checks)

| Script | What it does | Docs |
|---|---|---|
| `validate_unit.py` | Authoring QA gate for one unit; must PASS before render (CI runs it on every `examples/*/`) | below |
| `render_unit.py` | Unit dir → `docs/<unit_id>/` HTML; `--out` for an unpublished preview | below |
| `render_track.py` | Track manifest → contents page | below |
| `render_glossary.py` | Track → one A-Z glossary page | below |
| `build_hub_index.py` | Writes `docs/index.html` (the landing page) from `HTML_CONTENT` | below |
| `check_hub_links.py` | Landing page matches builder; hub links resolve (CI) | below |
| `check_ep07_capture.py` | Episode 7 Drill 1 table ↔ `jared-telnet-capture.pcap`, plus the `docs/` mirror (CI) | `AGENTS.md` |
| `check_tools_index.py` | This index lists every script in `tools/` (CI, warning only) | this section |
| `author.py` | Authoring bookkeeping: brief → plan → review → status | below |
| `voice_check.py` | Machine-prose tells; a reading aid, not a gate | below |
| `check_decks.py` | Flashcard decks: no indented HTML that Docsify shows as a code block, and every ```` ```lnk-deck ```` fence well formed (CI) | `AGENTS.md` |
| `check_dates.py` | Portland Desk months, seasons, weekdays, incident IDs and desk tenure match `PORTLAND_TIMELINE.md`; run before merge | `AGENTS.md` |
| `check_cleanliness.py` | Strict lint: fails on any emoji or listed AI-slop marker in learner-facing files. Not in CI | — |
| `_track.py`, `_unit_page_template.py`, `_deck.py` | Modules imported by the renderers (`_deck.py` parses `lnk-deck` fences for `render_unit.py`); not run directly | — |

### Generators (safe to rerun; they rebuild output from a source)

| Script | Source → output |
|---|---|
| `generate_ep07_telnet_capture.py` | Drill table → `docs/portland-desk/artifacts/jared-telnet-capture.pcap` (needs `pip install scapy`; deterministic). Then run `check_ep07_capture.py`. |
| `generate_helpdesk_artifacts.py` | Built-in data → ticket queue, terminal dumps, event logs, email headers (`--generate`, `--verify`, `--out-dir`) |
| `build_portland_glossary.py` | `docs/portland-desk/assets/glossary.json` → `docs/portland-desk/glossary.md` |
| `find_bad_tables.py` | Read-only: lists Markdown tables under `docs/portland-desk/` with text directly above the header row (breaks GFM rendering). Run from the repo root. |
| `sync_agy_chats.py` | Not a content tool: exports/imports Antigravity chat history between machines. Root `sync_agy_chats.py` is a wrapper for it. |

### One-shot edits (history only; do not rerun)

These scripts each made one pass over Portland Desk content and are kept as a record of that change. Rerunning one would rewrite current files with the text it carries, undoing later edits. Several also hard-code `C:\Users\charl\learning-narrative-kit` as the repo path, so they only run on that machine.

| Script | The one change it made | Hard-coded Windows path |
|---|---|---|
| `refactor_portland_ui.py` | Shift Briefing cards, emoji removal, scratchpads across all 13 workbenches | yes |
| `upgrade_all_modules.py` | Episodes 00, 02–12 to the interleaved cliffhanger model with terminal simulations | no |
| `refactor_episode_02.py`, `refactor_episode_03.py`, `refactor_episode_04.py`, `refactor_episode_05.py`, `refactor_episode_06.py`, `refactor_episode_07.py` | One episode each to the interleaved cliffhanger handoff model | no |
| `refactor_cliffhangers_act3.py` | Episodes 08–12 to the same model | yes |
| `refactor_episode_01_sorkin.py` | Episode 01 narrative + workbench rewrite | yes |
| `apply_technical_fixes.py` | Technical fixes and cast disambiguation | yes |
| `apply_final_sorkin_sme_overhaul.py` | Final story and SME fixes | yes |
| `clean_jargon.py` | Phrase replacements ("invariants" → "building blocks") in `portland-desk/`, `docs/portland-desk/`, `build_hub_index.py` | no |
| `clean_research_invariants.py` | Same replacements in three `docs/research/` files | yes |
| `clean_vocab_density.py` | Unmarked everyday terms (`[[id\|text]]` → `text`) in Portland narratives | no |
| `fix_dummy_links.py` | Replaced placeholder `[text](#)` links with plain text in `portland-desk/` and `docs/portland-desk/` | no |
| `update_index_glossary.py` | Patched the Portland Desk `index.html` pages so terms link to the Master Glossary | no |
| `sprint1_fixes.py` | Sprint 1 text fixes in narratives 08–11 | yes |
| `sprint1_workbench_fixes.py` | Sprint 1 fixes in workbenches 00, 01, 08, 10, 11 and `artifacts/powershell_event_4104.json` | yes |
| `sprint2_fixes.py` | Sprint 2 terminal blocks in workbenches 02, 08, 10, 11, 12 and narrative 12 | yes |
| `publish_mockup.py`, `publish_handcrafted.py` | Copied `scratch/comic_card_mockup.html` and `scratch/handcrafted_cards_mockup.html` into `docs/` for a Pages preview | yes |

New one-off edit scripts are better kept out of `tools/` (run them, commit the content change, and describe the script in the commit message). If one is committed, add it to this table.

## `validate_unit.py`

Authoring QA checker. **Must PASS before render/ship.**

```bash
.venv/bin/python tools/validate_unit.py examples/<unit_id>
```

| Check | Severity |
|-------|----------|
| Load `glossary.yaml` + `narrative.md` | fail |
| Every glossary id marked ≥1 as `[[id\|text]]` | fail |
| No mark ids missing from glossary | fail |
| Mark density (marks per 100 cover-stripped words) | report |
| If any `tier` present: exam/support counts; warn if a term lacks tier | warn |
| `Priya` in narrative (Portland Desk rule) | fail |
| Heading rule, for units with `heading_rule: scene` in `unit.yaml` (see `examples/TAMARACK.md`) | warn |

Exits **0** on PASS, **nonzero** on FAIL.

## `render_unit.py`

Render a unit directory to **GitHub Pages** HTML under `docs/<unit_id>/`.

```bash
.venv/bin/python tools/render_unit.py examples/<unit_id>
```

- Reads `unit.yaml` + `narrative.md` + `glossary.yaml`
- `unit_id` from `unit.yaml` becomes the output folder name
- Writes: `index.html` (thin shell), `narrative.N.html` parts + `narrative.manifest.json`, `glossary.js`
- Shared assets: `docs/unit.css`, `docs/unit.js`
- Soft prose-tint marks; Exam-only / All; tooltip = definition + context only
- **Does not** update `docs/index.html` — add landing cards in `tools/build_hub_index.py` (see below)

Markdown/YAML remain source of truth; never hand-edit generated HTML under `docs/<unit_id>/`.

**Preview a candidate without publishing it:** `--out DIR` writes `DIR/<unit_id>/` plus copies of `unit.css` and `unit.js`, and swaps the track navigation for a "Candidate preview: not published" banner. It refuses any path under `docs/`.

```bash
.venv/bin/python tools/render_unit.py workshop/<job>/candidates/<unit_id> --out workshop/<job>/preview
cd workshop/<job>/preview && python3 -m http.server 8000   # then open /<unit_id>/
```

The old local wrapper `build_preview.py` was archived with the Security+ shorts (`archive/examples/secplus-ports-helpdesk/`).

## `render_track.py`

Render a track manifest (`tracks/<track>.yaml`: parts, units in reading order, one-line blurbs) to a table-of-contents page.

```bash
.venv/bin/python tools/render_track.py tracks/tamarack.yaml
# → docs/tamarack/index.html
```

`render_unit.py` also reads `tracks/*.yaml`: a unit listed in a track gets a Contents link and Previous / Next links. Units in no track render unchanged.

## `render_glossary.py`

Render one A-Z glossary page for a whole track, from every unit's `glossary.yaml`.

```bash
.venv/bin/python tools/render_glossary.py tracks/tamarack.yaml
# → docs/tamarack/glossary/index.html
```

- Terms with the same name in several chapters merge into one entry, including acronym and spelled-out forms ("ETL" and "Extraction, transformation, and loading (ETL)"). Differing definitions are all shown, each labeled with its chapter.
- Each chapter link opens the chapter at the term: `chapter/#term=<id>` makes `docs/unit.js` open the term, switch to All if it is support-tier, and scroll to its first mark.
- Search box, Exam-only filter, and A-Z jump bar; works without JavaScript except for search and filtering.
- Set `glossary: true` in the track manifest so the contents page and every chapter's top bar link to it. Re-run after any glossary or track change.

## `build_hub_index.py` and `check_hub_links.py`

`docs/index.html` (the landing page) is generated: its full HTML lives in `HTML_CONTENT` in `tools/build_hub_index.py`. Edit the builder, never the page, then:

```bash
python3 tools/build_hub_index.py    # rewrites docs/index.html
python3 tools/check_hub_links.py    # landing-page drift check (CI runs this)
```

`check_hub_links.py` fails if `docs/index.html` differs from the builder's output or if a relative link on it is broken. It also lists rendered `docs/<dir>/index.html` pages that cannot be reached from the landing page (a unit with no card); that is a warning unless you pass `--strict`.

## Full LLM playbook

See [`AGENTS.md`](../AGENTS.md) at the repo root.

## voice_check.py

Flags machine-prose tells (dropped determiners, fragment runs, section-final
aphorisms, antithesis formulas, sentence-length flatness). Heuristic — a reading
aid, not a gate. Contract and repair pass: `schema/VOICE.md`.

```bash
python3 tools/voice_check.py examples/<unit_id>/narrative.md
python3 tools/voice_check.py examples/*/narrative.md --summary
```

## `author.py`

The authoring workflow's bookkeeping: brief → plan → review → status. It never writes narrative. Brief format: `schema/BRIEF.md`; full workflow with examples: `AGENTS.md` → Authoring workflow.

| Subcommand | What it does | Writes |
|---|---|---|
| `brief-check BRIEF` | Required fields, defaults applied, terms per group, definitions that block drafting (bare or `proposed`), conflicting definitions | nothing |
| `plan BRIEF [--refresh]` | Maps every term to the chapter that introduces it; suggests dependencies (a term whose definition names another term); finds revisits in accepted chapter text; lists gaps (missing or conflicting definitions, forward references, catalog-chapter risk) | `workshop/<id>/plan.yaml`, `plan.md` |
| `plan-check BRIEF [--chapter chNN]` | Coverage (every term introduced exactly once) and the drafting gate (plan approved, situation filled in, definitions dependable) | nothing |
| `review UNIT_DIR [--brief B --chapter chNN] [--out FILE]` | One report: validate + voice metrics, plan conformance, heuristic flags, continuity prompts (new names, dated statements, stated figures), an editorial checklist, and what is not measured | report `.md` + marks-stripped `.cover.txt` |
| `status BRIEF [--init]` | Shows or starts the resumable record: stages, revisions used against the cap, open issues, next action | `workshop/<id>/status.yaml` (on `--init`) |

`--refresh` regenerates the computed parts of a plan (term lists, dependencies, gaps) and keeps everything the author wrote: `approved`, `story`, and each chapter's title, status, situation, notes, and any field the author added.

**How far to trust the heuristics.** All of them were calibrated on twelve accepted chapters (MIS 1–10, ITM Week 7, Excel 3, Power Query):

| Signal | Separates weak chapters? |
|---|---|
| Longest exposition run (paragraphs in a row that each introduce a term with no dialogue) ≥ 5 | **Yes.** It flagged exactly MIS 5 and MIS 10, the two chapters already judged to be catalogs by reading them. |
| Mark clusters (4+ marks in one paragraph) | Partly; MIS 5 had 4. |
| Inline-gloss share | **No.** Kept as context, not as a verdict. |
| Marks in or next to a paragraph with dialogue or a decision word (widened October 2026 to count one paragraph either side) | **Partly.** Across sixteen chapters most score 62–100%. The two lowest were the old MIS 10 catalog (52%) and the pre-trial MIS 8 (44%), both already judged weak by reading; the old MIS 5 scored a normal 78% (its list problem shows in the exposition run). Before widening it didn't separate anything (Week 7 scored 21%), because it missed the rule-8 pattern of naming a term in narration and putting the exchange beside it. |
| Definition echo | Low counts everywhere; useful for pointing at specific sentences. |

The dependency map is a suggestion, not an analysis: it matches term titles inside definitions, so "data" and "information" dominate, and a dependency the definition doesn't spell out is missed.
