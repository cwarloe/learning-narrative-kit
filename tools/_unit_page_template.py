"""HTML page template for tools/render_unit.py (kept separate for maintainability)."""
from __future__ import annotations

import html


def render_html(page_title: str, subtitle: str, body_html: str, gloss_json: str) -> str:
    byline_note = (
        "Story first; hover highlighted terms for short definitions. "
        "Exam refs and tags live in the sidebar."
    )
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
    <article id="narrative">
{body_html}
    </article>
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
<script>
(function () {{
  const glossary = window.__GLOSSARY__;
  const tooltip = document.getElementById('tooltip');
  const ttTier = document.getElementById('tt-tier');
  const ttTitle = document.getElementById('tt-title');
  const ttBody = document.getElementById('tt-body');
  const ttContext = document.getElementById('tt-context');
  const termList = document.getElementById('term-list');
  const searchBox = document.getElementById('search-box');
  const termCount = document.getElementById('term-count');
  const detailPanel = document.getElementById('detail-panel');
  const filterExamBtn = document.getElementById('filter-exam');
  const filterAllBtn = document.getElementById('filter-all');

  let filterMode = 'exam'; // 'exam' | 'all'
  let selectedId = null;

  function isMarkVisible(tier) {{
    if (filterMode === 'all') return true;
    return tier === 'exam';
  }}

  function tooltipBody(item) {{
    // STRICT: definition + optional context only — never refs/tags/sources/related
    let text = item.definition || '';
    if (item.context) {{
      return {{ def: text, ctx: item.context }};
    }}
    return {{ def: text, ctx: '' }};
  }}

  function showTooltip(el, e) {{
    const id = el.getAttribute('data-term');
    const tier = el.getAttribute('data-tier');
    if (!isMarkVisible(tier)) return;
    const item = glossary[id];
    if (!item) return;
    const parts = tooltipBody(item);
    ttTier.textContent = item.tier === 'exam' ? 'Exam' : 'Support';
    ttTier.className = 'tt-tier ' + item.tier;
    ttTitle.textContent = item.title || id;
    ttBody.textContent = parts.def;
    if (parts.ctx) {{
      ttContext.textContent = parts.ctx;
      ttContext.style.display = 'block';
    }} else {{
      ttContext.textContent = '';
      ttContext.style.display = 'none';
    }}
    tooltip.className = item.tier === 'support' ? 'tier-support' : '';
    tooltip.style.display = 'block';
    placeTooltip(e);
  }}

  function placeTooltip(e) {{
    const pad = 14;
    let x = e.pageX + pad;
    let y = e.pageY + pad;
    tooltip.style.left = x + 'px';
    tooltip.style.top = y + 'px';
    const rect = tooltip.getBoundingClientRect();
    if (rect.right > window.innerWidth - 8) {{
      x = e.pageX - rect.width - pad;
      tooltip.style.left = Math.max(8, x) + 'px';
    }}
    if (rect.bottom > window.innerHeight - 8) {{
      y = e.pageY - rect.height - pad;
      tooltip.style.top = Math.max(window.scrollY + 8, y) + 'px';
    }}
  }}

  function hideTooltip() {{
    tooltip.style.display = 'none';
  }}

  document.querySelectorAll('#narrative .term').forEach(function (el) {{
    el.addEventListener('mouseenter', function (e) {{ showTooltip(el, e); }});
    el.addEventListener('mousemove', function (e) {{
      if (tooltip.style.display === 'block') placeTooltip(e);
    }});
    el.addEventListener('mouseleave', hideTooltip);
    el.addEventListener('click', function () {{
      selectTerm(el.getAttribute('data-term'), false);
    }});
  }});

  function setFilter(mode) {{
    filterMode = mode;
    document.body.classList.toggle('filter-exam-only', mode === 'exam');
    filterExamBtn.classList.toggle('active', mode === 'exam');
    filterAllBtn.classList.toggle('active', mode === 'all');
    hideTooltip();
    renderList(searchBox.value);
  }}

  filterExamBtn.addEventListener('click', function () {{ setFilter('exam'); }});
  filterAllBtn.addEventListener('click', function () {{ setFilter('all'); }});

  function renderList(filter) {{
    filter = (filter || '').toLowerCase();
    termList.innerHTML = '';
    const keys = Object.keys(glossary).sort(function (a, b) {{
      return glossary[a].title.localeCompare(glossary[b].title);
    }}).filter(function (k) {{
      const t = glossary[k];
      if (filterMode === 'exam' && t.tier !== 'exam') return false;
      const hay = (t.title + ' ' + t.definition + ' ' + (t.tags || []).join(' ')).toLowerCase();
      return !filter || hay.indexOf(filter) !== -1;
    }});

    const totalVisible = Object.keys(glossary).filter(function (k) {{
      return filterMode === 'all' || glossary[k].tier === 'exam';
    }}).length;
    termCount.textContent = 'Showing ' + keys.length + ' of ' + totalVisible +
      (filterMode === 'exam' ? ' exam' : '') + ' terms';

    keys.forEach(function (key) {{
      const item = glossary[key];
      const div = document.createElement('div');
      div.className = 'term-item' + (selectedId === key ? ' selected' : '');
      div.setAttribute('data-id', key);
      const titleSpan = document.createElement('span');
      titleSpan.textContent = item.title;
      const badge = document.createElement('span');
      badge.className = 'badge ' + item.tier;
      badge.textContent = item.tier;
      div.appendChild(titleSpan);
      div.appendChild(badge);
      div.addEventListener('click', function () {{ selectTerm(key, true); }});
      termList.appendChild(div);
    }});
  }}

  function selectTerm(id, scroll) {{
    selectedId = id;
    const item = glossary[id];
    if (!item) return;

    document.querySelectorAll('.term-item').forEach(function (el) {{
      el.classList.toggle('selected', el.getAttribute('data-id') === id);
    }});

    // Sidebar detail MAY show tier, tags, refs
    let html = '<div class="d-tier ' + item.tier + '">' + item.tier + '</div>';
    html += '<div class="d-title"></div>';
    html += '<div class="d-def"></div>';
    detailPanel.className = 'detail-panel';
    detailPanel.innerHTML = html;
    detailPanel.querySelector('.d-title').textContent = item.title;
    detailPanel.querySelector('.d-def').textContent = item.definition || '';

    if (item.context) {{
      const c = document.createElement('div');
      c.className = 'd-context';
      c.textContent = item.context;
      detailPanel.appendChild(c);
    }}
    if (item.tags && item.tags.length) {{
      const tg = document.createElement('div');
      tg.className = 'd-tags';
      tg.textContent = 'Tags: ' + item.tags.join(', ');
      detailPanel.appendChild(tg);
    }}
    if (item.refs && item.refs.length) {{
      const wrap = document.createElement('div');
      wrap.className = 'd-refs';
      const label = document.createElement('div');
      label.textContent = 'Refs';
      wrap.appendChild(label);
      const ul = document.createElement('ul');
      item.refs.forEach(function (r) {{
        const li = document.createElement('li');
        li.textContent = r;
        ul.appendChild(li);
      }});
      wrap.appendChild(ul);
      detailPanel.appendChild(wrap);
    }}

    if (scroll) {{
      const matches = document.querySelectorAll('#narrative .term[data-term="' + CSS.escape(id) + '"]');
      let target = null;
      for (let i = 0; i < matches.length; i++) {{
        const t = matches[i].getAttribute('data-tier');
        if (isMarkVisible(t)) {{ target = matches[i]; break; }}
      }}
      if (!target && matches.length) target = matches[0];
      if (target) {{
        target.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        matches.forEach(function (m) {{
          if (!isMarkVisible(m.getAttribute('data-tier')) && filterMode === 'exam') return;
          m.classList.add('flash');
          setTimeout(function () {{ m.classList.remove('flash'); }}, 1400);
        }});
      }}
    }}
  }}

  searchBox.addEventListener('input', function (e) {{ renderList(e.target.value); }});
  renderList();
}})();
</script>

</body>
</html>
"""
