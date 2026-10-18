/**
 * Learning Narrative Kit (LNK) — Universal Learning Shell
 * 
 * Features:
 * 1. Dual-Track Mode Switcher (Curriculum Guide, Story Reader, Workbench Mode)
 * 2. Docked Right Aside Glossary Drawer with live search & category filters
 * 3. Bidirectional Sync: In-prose term click glides to glossary; glossary click glides to story & flashes
 * 4. Responsive Hover Tooltips with intelligent viewport edge-detection
 */

(function () {
  let selectedId = null;
  let activeFilter = 'all';
  let searchQuery = '';
  let activeTrackMode = localStorage.getItem('lnk_track_mode') || 'curriculum';

  /* ==========================================================================
     Dual-Track Mode Switcher
     ========================================================================== */

  function applyTrackMode(mode) {
    activeTrackMode = mode;
    localStorage.setItem('lnk_track_mode', mode);

    document.body.classList.remove('mode-curriculum', 'mode-reader', 'mode-workbench');
    document.body.classList.add(`mode-${mode}`);

    // Update active button state
    document.querySelectorAll('.lnk-mode-btn').forEach(function (btn) {
      btn.classList.toggle('active', btn.getAttribute('data-mode') === mode);
    });
  }

  function mountModeSwitcher() {
    const sidebar = document.querySelector('.sidebar');
    if (!sidebar || document.querySelector('.lnk-mode-switcher')) return;

    const switcher = document.createElement('div');
    switcher.className = 'lnk-mode-switcher';
    switcher.setAttribute('role', 'group');
    switcher.setAttribute('aria-label', 'Course Track Mode');
    switcher.innerHTML = `
      <button type="button" class="lnk-mode-btn ${activeTrackMode === 'curriculum' ? 'active' : ''}" data-mode="curriculum" title="Balanced Curriculum Guide">Curriculum</button>
      <button type="button" class="lnk-mode-btn ${activeTrackMode === 'reader' ? 'active' : ''}" data-mode="reader" title="Story Reader Mode">Story</button>
      <button type="button" class="lnk-mode-btn ${activeTrackMode === 'workbench' ? 'active' : ''}" data-mode="workbench" title="Hands-On Workbench Practice">Workbench</button>
    `;

    // Insert switcher below app name or search
    const appName = sidebar.querySelector('.app-name');
    if (appName && appName.nextSibling) {
      sidebar.insertBefore(switcher, appName.nextSibling);
    } else {
      sidebar.prepend(switcher);
    }

    switcher.querySelectorAll('.lnk-mode-btn').forEach(function (btn) {
      btn.addEventListener('click', function () {
        const mode = btn.getAttribute('data-mode');
        applyTrackMode(mode);
      });
    });

    applyTrackMode(activeTrackMode);
    tagSidebarLinks();
  }

  function tagSidebarLinks() {
    document.querySelectorAll('.sidebar ul li').forEach(function (li) {
      const a = li.querySelector('a');
      if (!a) return;
      const href = a.getAttribute('href') || '';
      if (href.includes('narrative/') || href.includes('chapter')) {
        li.setAttribute('data-track', 'narrative');
      } else if (href.includes('workbench/') || href.includes('lab') || href.includes('drill')) {
        li.setAttribute('data-track', 'workbench');
      }
    });
  }

  /* ==========================================================================
     Docked Right Aside Glossary Drawer
     ========================================================================== */

  function mountGlossaryAside() {
    const content = document.querySelector('.content');
    if (!content) return;

    let aside = document.getElementById('lnk-glossary-aside');
    if (!aside) {
      aside = document.createElement('aside');
      aside.id = 'lnk-glossary-aside';
      aside.innerHTML = `
        <h3>Domain Glossary</h3>
        <div class="sidebar-meta" id="term-count">Loading terms…</div>
        <div class="filter-bar" role="group" aria-label="Vocabulary Category Filter">
          <button type="button" class="filter-btn active" data-cat="all">All</button>
          <button type="button" class="filter-btn" data-cat="telemetry">Telemetry</button>
          <button type="button" class="filter-btn" data-cat="architecture">Architecture</button>
          <button type="button" class="filter-btn" data-cat="analytical">Analytical</button>
          <button type="button" class="filter-btn" data-cat="pedagogy">Pedagogy</button>
        </div>
        <input type="text" id="search-box" placeholder="Filter terms or concepts…" autocomplete="off">
        <div class="term-list" id="term-list"></div>
        <div class="detail-panel empty" id="detail-panel">Select a highlighted term in prose or list to inspect definition.</div>
      `;
      content.appendChild(aside);

      // Category filters
      aside.querySelectorAll('.filter-btn').forEach(function (btn) {
        btn.addEventListener('click', function () {
          aside.querySelectorAll('.filter-btn').forEach(function (b) { b.classList.remove('active'); });
          btn.classList.add('active');
          activeFilter = btn.getAttribute('data-cat');
          renderGlossaryList();
        });
      });

      // Search input
      const searchInput = aside.querySelector('#search-box');
      searchInput.addEventListener('input', function (e) {
        searchQuery = (e.target.value || '').trim().toLowerCase();
        renderGlossaryList();
      });
    }

    renderGlossaryList();
    bindInStoryTermClicks();
  }

  function renderGlossaryList() {
    const termList = document.getElementById('term-list');
    const termCount = document.getElementById('term-count');
    if (!termList || !termCount) return;

    const glossary = window.__GLOSSARY__ || {};
    const keys = Object.keys(glossary);
    if (keys.length === 0) return;

    const filtered = keys.filter(function (k) {
      const item = glossary[k];
      const cat = (item.category || '').toLowerCase();
      const catMatch = (activeFilter === 'all') || (cat === activeFilter);
      const textMatch = !searchQuery ||
        (item.title && item.title.toLowerCase().includes(searchQuery)) ||
        (item.definition && item.definition.toLowerCase().includes(searchQuery)) ||
        (k.toLowerCase().includes(searchQuery));
      return catMatch && textMatch;
    }).sort(function (a, b) {
      return (glossary[a].title || a).localeCompare(glossary[b].title || b);
    });

    termCount.textContent = `Showing ${filtered.length} of ${keys.length} entries`;

    if (filtered.length === 0) {
      termList.innerHTML = '<div style="padding: 1.25rem; color: #94a3b8; font-size: 0.82rem; text-align: center;">No matching terms found.</div>';
      return;
    }

    let html = '';
    filtered.forEach(function (k) {
      const item = glossary[k];
      const isSelected = selectedId === k;
      const cat = item.category || 'telemetry';
      html += `
        <div class="term-item ${isSelected ? 'selected' : ''}" data-id="${k}">
          <span>${item.title || k}</span>
          <span class="badge ${cat}">${cat}</span>
        </div>
      `;
    });
    termList.innerHTML = html;

    // In-list selection handler
    termList.querySelectorAll('.term-item').forEach(function (el) {
      el.addEventListener('click', function () {
        const id = el.getAttribute('data-id');
        selectTerm(id, true);
      });
    });
  }

  function selectTerm(id, scrollToStory) {
    selectedId = id;
    const glossary = window.__GLOSSARY__ || {};
    const item = glossary[id];
    if (!item) return;

    // Highlight active item in aside
    document.querySelectorAll('.term-item').forEach(function (el) {
      el.classList.toggle('selected', el.getAttribute('data-id') === id);
    });

    // Populate detail panel
    const detailPanel = document.getElementById('detail-panel');
    if (detailPanel) {
      detailPanel.className = 'detail-panel';
      const cat = item.category || 'telemetry';
      detailPanel.innerHTML = `
        <div class="d-tier ${cat}">${cat.toUpperCase()}</div>
        <div class="d-title">${item.title || id}</div>
        <div class="d-def">${item.definition || ''}</div>
        ${item.context ? `<div class="d-context">${item.context}</div>` : ''}
      `;
    }

    // Bidirectional sync: glide to in-story term and pulse amber
    if (scrollToStory) {
      const targetEl = document.getElementById(`term-${id}`) || document.querySelector(`.term[data-term="${id}"]`);
      if (targetEl) {
        targetEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
        targetEl.classList.remove('flash', 'story-highlight');
        void targetEl.offsetWidth; // Trigger DOM reflow
        targetEl.classList.add('flash');
        setTimeout(function () {
          targetEl.classList.remove('flash');
        }, 1400);
      }
    }
  }

  function bindInStoryTermClicks() {
    document.querySelectorAll('.term').forEach(function (el) {
      el.addEventListener('click', function () {
        const id = el.getAttribute('data-term');
        selectTerm(id, false);

        // Mobile responsiveness: scroll to detail panel
        if (window.innerWidth < 1100) {
          const detailPanel = document.getElementById('detail-panel');
          if (detailPanel) {
            detailPanel.scrollIntoView({ behavior: 'smooth', block: 'center' });
          }
        }
      });
    });
  }

  /* ==========================================================================
     Docsify Lifecycle Integration
     ========================================================================== */

  window.$docsify = window.$docsify || {};
  window.$docsify.plugins = (window.$docsify.plugins || []).concat([
    function (hook) {
      hook.doneEach(function () {
        mountModeSwitcher();
        mountGlossaryAside();

        // If glossary.json was in-flight, poll until populated
        if (!window.__GLOSSARY__ || Object.keys(window.__GLOSSARY__).length === 0) {
          let attempts = 0;
          const pollInterval = setInterval(function () {
            attempts++;
            if (window.__GLOSSARY__ && Object.keys(window.__GLOSSARY__).length > 0) {
              clearInterval(pollInterval);
              renderGlossaryList();
            } else if (attempts > 30) {
              clearInterval(pollInterval);
            }
          }, 100);
        }
      });
    }
  ]);
})();
