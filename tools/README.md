# Tools

## `render_unit.py`

Render a unit directory to **GitHub Pages** HTML under `docs/<unit_id>/index.html`.

```bash
# Prefer the ports example venv (has PyYAML), or create tools/.venv
examples/secplus-ports-helpdesk/.venv/bin/python tools/render_unit.py examples/secplus-ports-helpdesk
examples/secplus-ports-helpdesk/.venv/bin/python tools/render_unit.py examples/secplus-auth-helpdesk
```

- Reads `unit.yaml` + `narrative.md` + `glossary.yaml`
- `unit_id` from `unit.yaml` becomes the output folder name
- Soft prose-tint marks (not hyperlink underlines); Exam-only / All; tooltip = definition + context only
- Markdown/YAML remain source of truth; `docs/` artifacts are committed for Pages

Local wrapper: `examples/secplus-ports-helpdesk/build_preview.py` calls this and also writes a gitignored scratch HTML next to the unit.

## `validate_unit.py`

Authoring QA checker for a learning-narrative unit directory.

```bash
examples/secplus-ports-helpdesk/.venv/bin/python tools/validate_unit.py examples/secplus-ports-helpdesk
examples/secplus-ports-helpdesk/.venv/bin/python tools/validate_unit.py examples/secplus-auth-helpdesk
```

**Checks**

| Check | Severity |
|-------|----------|
| Load `glossary.yaml` + `narrative.md` | fail |
| Every glossary id marked ≥1 as `[[id\|text]]` | fail |
| No mark ids missing from glossary | fail |
| Mark density (marks per 100 cover-stripped words) | report |
| If any `tier` present: exam/support counts; warn if a term lacks tier | warn |
| `Priya` or `Harrowmere` in narrative (Portland Desk rule) | fail |

Exits **0** on PASS, **nonzero** on FAIL.
