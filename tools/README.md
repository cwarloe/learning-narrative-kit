# Tools

Setup: `pip install -r requirements.txt` (repo root) or use any venv with PyYAML.

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

Local wrapper: `examples/secplus-ports-helpdesk/build_preview.py` calls this and also writes a gitignored scratch HTML next to the unit.

## Full LLM playbook

See [`AGENTS.md`](../AGENTS.md) at the repo root.
