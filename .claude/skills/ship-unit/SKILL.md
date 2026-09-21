---
name: ship-unit
description: Validate, render and publish a learning-narrative unit — runs validate_unit.py and render_unit.py, adds the landing card to docs/index.html, and commits source plus generated output. Use when a unit's files are written and it needs to go live on Pages.
argument-hint: "[unit-id]"
allowed-tools: Bash(python3 tools/*) Bash(.venv/bin/python tools/*) Bash(git add *) Bash(git status *) Bash(git diff *) Read Grep Glob
---

## Python to use

```!
if [ -x .venv/bin/python ]; then echo ".venv/bin/python"; elif [ -x examples/secplus-ports-helpdesk/.venv/bin/python ]; then echo "examples/secplus-ports-helpdesk/.venv/bin/python"; else python3 -c "import yaml" 2>/dev/null && echo "python3 (PyYAML present)" || echo "NONE — create one: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt"; fi
```

Use whichever the line above names. The commands below write `python3`; substitute it.

## Ship it

The unit is `$1` when given; otherwise ask which one.

**1. Validate — must PASS.**

```bash
python3 tools/validate_unit.py examples/<unit_id>
```

A `warn` is not a pass-with-notes to argue past. Fix it, or state plainly why it stands. Density is reported rather than enforced — read the number and judge it, don't ignore it.

**2. Render.**

```bash
python3 tools/render_unit.py examples/<unit_id>
```

This writes `docs/<unit_id>/`. **Never hand-edit anything under `docs/`** — the one exception is `docs/index.html`, which the renderer does not touch.

**3. Landing card — by hand.**

The renderer will not do this. Add a card to `docs/index.html` under the right track heading (`ITM track` or `Portland Desk track`), matching the existing shape:

```html
<li>
  <a class="card" href="<unit_id>/">
    <span class="title">Portland Desk — Title Of The Unit</span>
    <span class="meta">Short topic description · <unit_id></span>
  </a>
</li>
```

**4. Commit** `examples/<unit_id>/`, `docs/<unit_id>/`, and `docs/index.html` together. Pages serves `/docs`, so a render that isn't committed isn't shipped.

Live at `https://cwarloe.github.io/learning-narrative-kit/<unit_id>/`.

## Voice pass

Before shipping, run the reading aid:

```bash
python3 tools/voice_check.py examples/<unit_id>/narrative.md
```

Report what it flags — it's heuristic and produces false positives, so never rewrite just to move a number. Then answer the one thing it can't see: **read the last beat and say in one sentence what the pivot cost.** If the answer is "nothing," the chapter is tidy and needs reopening before it ships. `schema/VOICE.md` → The structural tell.

## Done means

Validate PASS, render succeeded, landing card present, **cover test passes** (strip the `[[...]]` marks and the story still teaches the relationships), the sticky teaching beats can each be named in one sentence, the ending cost something you can name, and `docs/` is pushed.

Report the validate output rather than summarising it as "passed" — the density and tier counts are worth the author seeing.
