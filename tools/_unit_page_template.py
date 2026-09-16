"""HTML page template for tools/render_unit.py (kept separate for maintainability)."""
from __future__ import annotations

import html


def render_html(page_title: str, subtitle: str, body_html: str, gloss_json: str) -> str:
    byline_note = (
        "Story first; hover highlighted terms for short definitions. "
        "Exam refs and tags live in the sidebar."
    )
    # body_html is written separately to narrative.html; index is a thin shell.
    _ = body_html  # kept in signature for call-site compatibility
    _ = gloss_json
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{html.escape(page_title)}</title>
  <link rel="stylesheet" href="../unit.css">
</head>
<body class="filter-exam-only">

<div class="layout">
  <main>
    <h1>{html.escape(page_title)}</h1>
    <div class="byline">{html.escape(subtitle)}</div>
    <div class="byline-note">{html.escape(byline_note)}</div>
    <article id="narrative"><p class="loading">Loading narrative…</p></article>
  </main>

  <aside>
    <h3>Glossary</h3>
    <div class="sidebar-meta" id="term-count"></div>
    <div class="legend">
      <span class="lg-exam">Exam</span>
      <span class="lg-support">Support</span>
    </div>
    <div class="filter-bar" role="group" aria-label="Tier filter">
      <button type="button" id="filter-exam" class="active" data-filter="exam">Exam only</button>
      <button type="button" id="filter-all" data-filter="all">All</button>
    </div>
    <input type="text" id="search-box" placeholder="Filter terms…" autocomplete="off">
    <div class="term-list" id="term-list"></div>
    <div class="detail-panel empty" id="detail-panel">Select a term to see definition, tags, and refs.</div>
  </aside>
</div>

<div id="tooltip" role="tooltip">
  <div class="tt-tier" id="tt-tier"></div>
  <div class="tt-title" id="tt-title"></div>
  <div class="tt-body" id="tt-body"></div>
  <div class="tt-context" id="tt-context"></div>
</div>

<script src="glossary.js"></script>
<script src="../unit.js"></script>
<script>
fetch('narrative.manifest.json')
  .then(function (r) {{ return r.json(); }})
  .then(function (manifest) {{
    return Promise.all(manifest.parts.map(function (p) {{
      return fetch(p).then(function (r) {{ return r.text(); }});
    }}));
  }})
  .then(function (parts) {{
    document.getElementById('narrative').innerHTML = parts.join('');
    window.bootUnitPage();
  }})
  .catch(function (err) {{
    document.getElementById('narrative').innerHTML =
      '<p>Failed to load narrative</p>';
    console.error(err);
  }});
</script>

</body>
</html>
"""
