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
        <div class="glossary-header-bar">
          <div class="glossary-title-wrap">
            <span class="glossary-icon">📚</span>
            <div>
              <h3>Active Domain Glossary & Technical Concept Index</h3>
              <div class="sidebar-meta" id="term-count">Loading terms…</div>
            </div>
          </div>
          <div class="glossary-filter-controls">
            <div class="filter-bar" role="group" aria-label="Vocabulary Category Filter">
              <button type="button" class="filter-btn active" data-cat="all">All</button>
              <button type="button" class="filter-btn" data-cat="telemetry">Telemetry</button>
              <button type="button" class="filter-btn" data-cat="architecture">Architecture</button>
              <button type="button" class="filter-btn" data-cat="analytical">Analytical</button>
              <button type="button" class="filter-btn" data-cat="pedagogy">Pedagogy</button>
            </div>
            <input type="text" id="search-box" placeholder="Filter terms or concepts…" autocomplete="off">
          </div>
        </div>
        <div class="glossary-split-deck">
          <div class="term-list" id="term-list"></div>
          <div class="detail-panel empty" id="detail-panel">Select a highlighted term in prose or from the index to inspect its formal engineering definition.</div>
        </div>
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
      el.addEventListener('click', function (e) {
        e.preventDefault();
        const id = el.getAttribute('data-term');
        selectTerm(id, false);

        const detailPanel = document.getElementById('detail-panel');
        if (detailPanel) {
          detailPanel.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      });
    });
  }

  /* ==========================================================================
     Interactive Scratchpads (Hypothesis Prediction & Ticket Drafting)
     ========================================================================== */

  function initScratchpads() {
    document.querySelectorAll('.scratchpad-body textarea').forEach(function (textarea) {
      const id = textarea.id;
      if (!id) return;
      const storageKey = 'lnk_scratchpad_' + id;
      const saved = localStorage.getItem(storageKey);
      if (saved && !textarea.value) {
        textarea.value = saved;
      }

      // Auto-save on input
      textarea.addEventListener('input', function () {
        localStorage.setItem(storageKey, textarea.value);
        const container = textarea.closest('.scratchpad-container');
        if (container) {
          const indicator = container.querySelector('.scratchpad-save-indicator');
          if (indicator) {
            indicator.textContent = 'Saving…';
            indicator.style.opacity = '1';
            clearTimeout(textarea._saveTimer);
            textarea._saveTimer = setTimeout(function () {
              indicator.textContent = 'Saved to browser';
              setTimeout(function () {
                indicator.style.opacity = '0.7';
              }, 1200);
            }, 300);
          }
        }
      });
    });
  }

  window.copyScratchpad = function (id) {
    const textarea = document.getElementById(id);
    if (!textarea) return;
    const text = textarea.value;
    if (!text.trim()) {
      alert('The scratchpad is empty. Type your notes or prediction first!');
      return;
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(function () {
        const btn = event && event.target ? event.target : null;
        if (btn) {
          const orig = btn.textContent;
          btn.textContent = 'Copied!';
          setTimeout(function () { btn.textContent = orig; }, 1800);
        }
      }).catch(function () {
        fallbackCopy(textarea);
      });
    } else {
      fallbackCopy(textarea);
    }
  };

  function fallbackCopy(textarea) {
    textarea.select();
    document.execCommand('copy');
    const btn = event && event.target ? event.target : null;
    if (btn) {
      const orig = btn.textContent;
      btn.textContent = 'Copied!';
      setTimeout(function () { btn.textContent = orig; }, 1800);
    }
  }

  
  /* ==========================================================================
     Multi-Card Flashcard Deck Engine
     ========================================================================== */

  function initPassportDecks() {
    document.querySelectorAll('.passport-deck-container').forEach(function(deck) {
      if (deck._initialized) return;
      deck._initialized = true;

      const cards = deck.querySelectorAll('.passport-card');
      if (cards.length === 0) return;

      let activeIdx = 0;
      const currIdxEl = deck.querySelector('.deck-curr-idx');
      const totalCountEl = deck.querySelector('.deck-total-count');
      const dotsContainer = deck.querySelector('.passport-progress-dots');

      if (totalCountEl) totalCountEl.textContent = cards.length;

      // Populate dots if empty
      if (dotsContainer && dotsContainer.children.length === 0) {
        cards.forEach(function(_, i) {
          const dot = document.createElement('span');
          dot.className = 'dot' + (i === 0 ? ' active' : '');
          dot.addEventListener('click', function(e) {
            e.stopPropagation();
            showCard(i);
          });
          dotsContainer.appendChild(dot);
        });
      }

      function showCard(idx) {
        activeIdx = (idx + cards.length) % cards.length;
        cards.forEach(function(c, i) {
          c.classList.remove('active', 'flipped');
          if (i === activeIdx) c.classList.add('active');
        });
        if (dotsContainer) {
          const dots = dotsContainer.querySelectorAll('.dot');
          dots.forEach(function(d, i) {
            d.classList.toggle('active', i === activeIdx);
          });
        }
        if (currIdxEl) currIdxEl.textContent = activeIdx + 1;
      }

      // Card click anywhere to flip
      cards.forEach(function(card) {
        card.addEventListener('click', function(e) {
          if (e.target.tagName !== 'BUTTON' && !e.target.closest('button')) {
            card.classList.toggle('flipped');
          }
        });
      });

      // Dedicated flip button
      const flipBtn = deck.querySelector('.flip-btn');
      if (flipBtn) {
        flipBtn.addEventListener('click', function(e) {
          e.stopPropagation();
          const activeCard = deck.querySelector('.passport-card.active');
          if (activeCard) activeCard.classList.toggle('flipped');
        });
      }

      // Next / Prev buttons
      const nextBtn = deck.querySelector('.next-btn');
      if (nextBtn) {
        nextBtn.addEventListener('click', function(e) {
          e.stopPropagation();
          showCard(activeIdx + 1);
        });
      }

      const prevBtn = deck.querySelector('.prev-btn');
      if (prevBtn) {
        prevBtn.addEventListener('click', function(e) {
          e.stopPropagation();
          showCard(activeIdx - 1);
        });
      }

      // Shuffle button
      const shuffleBtn = deck.querySelector('.shuffle-btn');
      if (shuffleBtn) {
        shuffleBtn.addEventListener('click', function(e) {
          e.stopPropagation();
          if (cards.length > 1) {
            let nextRand;
            do {
              nextRand = Math.floor(Math.random() * cards.length);
            } while (nextRand === activeIdx);
            showCard(nextRand);
          }
        });
      }

      // Keyboard controls when hovering deck
      let isHovered = false;
      deck.addEventListener('mouseenter', function() { isHovered = true; });
      deck.addEventListener('mouseleave', function() { isHovered = false; });

      document.addEventListener('keydown', function(e) {
        if (!isHovered) return;
        if (e.code === 'Space') {
          e.preventDefault();
          const activeCard = deck.querySelector('.passport-card.active');
          if (activeCard) activeCard.classList.toggle('flipped');
        } else if (e.code === 'ArrowRight') {
          e.preventDefault();
          showCard(activeIdx + 1);
        } else if (e.code === 'ArrowLeft') {
          e.preventDefault();
          showCard(activeIdx - 1);
        }
      });

      // Show initial card
      showCard(0);
    });
  }

  /* ==========================================================================
     Job Aid Dual-Face Tab Switcher
     ========================================================================== */

  function initJobAidTabs() {
    document.querySelectorAll('.lnk-job-aid-card').forEach(function(card) {
      if (card._initializedTabs) return;
      card._initializedTabs = true;

      const tabBtns = card.querySelectorAll('.aid-tab-btn');
      const faceA = card.querySelector('.aid-face.side-a');
      const faceB = card.querySelector('.aid-face.side-b');

      tabBtns.forEach(function(btn) {
        btn.addEventListener('click', function(e) {
          e.preventDefault();
          const target = btn.getAttribute('data-target');
          tabBtns.forEach(function(b) {
            b.classList.remove('active');
            b.setAttribute('aria-pressed', 'false');
          });
          btn.classList.add('active');
          btn.setAttribute('aria-pressed', 'true');

          if (target === 'side-a') {
            if (faceA) faceA.classList.add('active');
            if (faceB) faceB.classList.remove('active');
          } else {
            if (faceB) faceB.classList.add('active');
            if (faceA) faceA.classList.remove('active');
          }
        });
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
        initScratchpads();
        initPassportDecks();
        initJobAidTabs();

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

