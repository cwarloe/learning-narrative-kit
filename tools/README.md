# Tools

Setup (from repo root): `python3 -m venv .venv && .venv/bin/pip install -r requirements.txt`.
`.venv` at the repo root is the supported location (gitignored). If system `python3` already has PyYAML you can run the tools with `python3` directly.

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
| `Priya` or `Harrowmere` in narrative (Portland Desk rule) | fail |
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
- **Does not** update `docs/index.html` — add landing cards by hand

Markdown/YAML remain source of truth; never hand-edit generated HTML under `docs/<unit_id>/`.

**Preview a candidate without publishing it:** `--out DIR` writes `DIR/<unit_id>/` plus copies of `unit.css` and `unit.js`, and swaps the track navigation for a "Candidate preview: not published" banner. It refuses any path under `docs/`.

```bash
.venv/bin/python tools/render_unit.py workshop/<job>/candidates/<unit_id> --out workshop/<job>/preview
cd workshop/<job>/preview && python3 -m http.server 8000   # then open /<unit_id>/
```

Local wrapper: `examples/secplus-ports-helpdesk/build_preview.py` calls this and also writes a gitignored scratch HTML next to the unit.

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
