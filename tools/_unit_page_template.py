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
  <style>
    :root {{
      --bg: #0f172a;
      --surface: #1e293b;
      --surface-border: #334155;
      --text-main: #e2e8f0;
      --text-muted: #94a3b8;
      --primary: #38bdf8;
      --accent: #f59e0b;
      --exam: #38bdf8;
      --support: #a78bfa;
      --exam-bg: rgba(56, 189, 248, 0.12);
      --support-bg: rgba(167, 139, 250, 0.10);
      --flash: rgba(245, 158, 11, 0.45);
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}

    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.75;
      display: flex;
      justify-content: center;
    }}

    .layout {{
      display: grid;
      grid-template-columns: 1fr 340px;
      max-width: 1280px;
      width: 100%;
      min-height: 100vh;
      gap: 1.75rem;
      padding: 2rem 1.25rem;
    }}

    main {{
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: 12px;
      padding: 2.75rem 2.5rem;
      min-width: 0;
    }}

    h1 {{
      font-size: 2rem;
      color: #fff;
      margin-bottom: 0.4rem;
      letter-spacing: -0.02em;
      line-height: 1.25;
    }}

    .byline {{
      color: var(--text-muted);
      font-size: 0.92rem;
      margin-bottom: 0.65rem;
    }}

    .byline-note {{
      color: var(--text-muted);
      font-size: 0.82rem;
      margin-bottom: 1.75rem;
      border-bottom: 1px solid var(--surface-border);
      padding-bottom: 1.1rem;
    }}

    h2 {{
      font-size: 1.28rem;
      color: var(--primary);
      margin-top: 2.5rem;
      margin-bottom: 1rem;
      padding-bottom: 0.3rem;
      border-bottom: 1px solid rgba(51, 65, 85, 0.6);
      line-height: 1.35;
    }}

    p {{ margin-bottom: 1.2rem; font-size: 1.02rem; }}

    code {{
      background: rgba(0, 0, 0, 0.35);
      padding: 1px 5px;
      border-radius: 4px;
      font-family: Consolas, Monaco, "Courier New", monospace;
      color: #f1f5f9;
      font-size: 0.88em;
      border: 1px solid rgba(255, 255, 255, 0.08);
    }}

    /* Prose marks, not hyperlinks: soft tint only so readers keep sentence context */
    .term {{
      cursor: inherit;
      font-weight: inherit;
      border-radius: 3px;
      padding: 0 2px;
      border-bottom: none;
      text-decoration: none;
      transition: background 0.15s, box-shadow 0.15s;
    }}

    .term.exam {{
      color: inherit;
      background: var(--exam-bg);
    }}

    .term.support {{
      color: inherit;
      background: var(--support-bg);
    }}

    .term.exam:hover {{
      background: rgba(56, 189, 248, 0.28);
    }}

    .term.support:hover {{
      background: rgba(167, 139, 250, 0.22);
    }}

    .term.flash {{
      background: var(--flash) !important;
      box-shadow: 0 0 0 3px var(--flash);
    }}

    /* Exam-only filter: support marks become plain/muted unmarked */
    body.filter-exam-only .term.support {{
      color: inherit;
      background: transparent;
      border-bottom: none;
      cursor: inherit;
      font-weight: inherit;
      padding: 0;
    }}

    body.filter-exam-only .term.support:hover {{
      background: transparent;
    }}

    #tooltip {{
      position: absolute;
      display: none;
      background: #0f172a;
      border: 1px solid var(--primary);
      box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.7);
      border-radius: 8px;
      padding: 0.95rem 1.05rem;
      width: 320px;
      max-width: calc(100vw - 24px);
      z-index: 1000;
      pointer-events: none;
      font-size: 0.88rem;
      line-height: 1.45;
    }}

    #tooltip.tier-support {{
      border-color: var(--support);
    }}

    #tooltip .tt-tier {{
      display: inline-block;
      font-size: 0.68rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      padding: 2px 6px;
      border-radius: 4px;
      margin-bottom: 0.45rem;
      font-weight: 600;
    }}

    #tooltip .tt-tier.exam {{
      background: rgba(56, 189, 248, 0.18);
      color: var(--exam);
    }}

    #tooltip .tt-tier.support {{
      background: rgba(167, 139, 250, 0.18);
      color: var(--support);
    }}

    #tooltip .tt-title {{
      font-weight: 700;
      color: #fff;
      font-size: 0.98rem;
      margin-bottom: 0.35rem;
    }}

    #tooltip .tt-body {{
      color: var(--text-main);
    }}

    #tooltip .tt-context {{
      color: var(--text-muted);
      margin-top: 0.45rem;
      font-size: 0.84rem;
    }}

    aside {{
      position: sticky;
      top: 1.25rem;
      height: calc(100vh - 2.5rem);
      background: var(--surface);
      border: 1px solid var(--surface-border);
      border-radius: 12px;
      padding: 1.25rem;
      display: flex;
      flex-direction: column;
      min-height: 0;
    }}

    aside h3 {{
      font-size: 1.05rem;
      margin-bottom: 0.35rem;
      color: #fff;
    }}

    .sidebar-meta {{
      font-size: 0.78rem;
      color: var(--text-muted);
      margin-bottom: 0.75rem;
    }}

    .filter-bar {{
      display: flex;
      gap: 0.4rem;
      margin-bottom: 0.75rem;
    }}

    .filter-bar button {{
      flex: 1;
      padding: 0.45rem 0.5rem;
      border-radius: 6px;
      border: 1px solid var(--surface-border);
      background: #0f172a;
      color: var(--text-muted);
      font-size: 0.8rem;
      font-weight: 600;
      cursor: pointer;
    }}

    .filter-bar button.active {{
      border-color: var(--primary);
      color: #fff;
      background: rgba(56, 189, 248, 0.15);
    }}

    #search-box {{
      width: 100%;
      padding: 0.55rem 0.7rem;
      background: #0f172a;
      border: 1px solid var(--surface-border);
      border-radius: 6px;
      color: #fff;
      font-size: 0.86rem;
      margin-bottom: 0.75rem;
    }}
    #search-box:focus {{ outline: 1px solid var(--primary); }}

    .term-list {{
      overflow-y: auto;
      flex: 1 1 auto;
      min-height: 0;
      padding-right: 2px;
    }}

    .term-item {{
      padding: 0.45rem 0.5rem;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.84rem;
      color: var(--text-muted);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 0.4rem;
      transition: background 0.15s;
    }}

    .term-item:hover,
    .term-item.selected {{
      background: #334155;
      color: #fff;
    }}

    .term-item .badge {{
      font-size: 0.65rem;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      flex-shrink: 0;
      padding: 1px 5px;
      border-radius: 3px;
      font-weight: 600;
    }}

    .term-item .badge.exam {{
      color: var(--exam);
      background: rgba(56, 189, 248, 0.12);
    }}

    .term-item .badge.support {{
      color: var(--support);
      background: rgba(167, 139, 250, 0.12);
    }}

    .detail-panel {{
      margin-top: 0.75rem;
      padding-top: 0.75rem;
      border-top: 1px solid var(--surface-border);
      flex: 0 0 auto;
      max-height: 42%;
      overflow-y: auto;
    }}

    .detail-panel.empty {{
      color: var(--text-muted);
      font-size: 0.8rem;
    }}

    .detail-panel .d-title {{
      font-weight: 700;
      color: #fff;
      font-size: 0.95rem;
      margin-bottom: 0.25rem;
    }}

    .detail-panel .d-tier {{
      display: inline-block;
      font-size: 0.65rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 1px 6px;
      border-radius: 3px;
      margin-bottom: 0.45rem;
      font-weight: 600;
    }}

    .detail-panel .d-tier.exam {{
      background: rgba(56, 189, 248, 0.18);
      color: var(--exam);
    }}

    .detail-panel .d-tier.support {{
      background: rgba(167, 139, 250, 0.18);
      color: var(--support);
    }}

    .detail-panel .d-def {{
      font-size: 0.84rem;
      margin-bottom: 0.4rem;
    }}

    .detail-panel .d-context {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-bottom: 0.45rem;
    }}

    .detail-panel .d-tags {{
      font-size: 0.72rem;
      color: var(--accent);
      margin-bottom: 0.35rem;
    }}

    .detail-panel .d-refs {{
      font-size: 0.72rem;
      color: var(--text-muted);
      margin-top: 0.35rem;
    }}

    .detail-panel .d-refs li {{
      margin-left: 1rem;
      margin-bottom: 0.2rem;
    }}

    .legend {{
      display: flex;
      gap: 0.85rem;
      font-size: 0.72rem;
      color: var(--text-muted);
      margin-bottom: 0.65rem;
    }}

    .legend span::before {{
      content: "";
      display: inline-block;
      width: 12px;
      height: 12px;
      border-radius: 3px;
      margin-right: 4px;
      vertical-align: middle;
    }}

    .legend .lg-exam::before {{ background: var(--exam-bg); box-shadow: inset 0 0 0 1px var(--exam); }}
    .legend .lg-support::before {{ background: var(--support-bg); box-shadow: inset 0 0 0 1px var(--support); }}

    @media (max-width: 960px) {{
      .layout {{
        grid-template-columns: 1fr;
        padding: 1rem;
      }}
      aside {{
        position: relative;
        top: 0;
        height: auto;
        max-height: none;
      }}
      .term-list {{
        max-height: 280px;
      }}
      main {{
        padding: 1.5rem 1.15rem;
      }}
      h1 {{ font-size: 1.55rem; }}
    }}
  </style>
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

<script type="application/json" id="glossary-data">
{gloss_json}
</script>

<script>
(function () {{
  const glossary = JSON.parse(document.getElementById('glossary-data').textContent);
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
