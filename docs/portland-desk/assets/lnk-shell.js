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
            <span class="glossary-badge" style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; font-weight: 700; color: #38bdf8; background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.3); border-radius: 4px; padding: 2px 8px;">INDEX</span>
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
      const container = textarea.closest('.scratchpad-container');
      const title = container && container.querySelector('.scratchpad-title');
      if (title) {
        title.id = id + '-label';
        textarea.setAttribute('aria-labelledby', title.id);
      }
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

      // Keyboard controls when the deck has focus. (This used to be a document-level
      // listener added per deck on every page render, so they piled up across visits.)
      if (!deck.hasAttribute('tabindex')) deck.setAttribute('tabindex', '0');
      deck.addEventListener('keydown', function(e) {
        if (e.target.closest('button')) return;
        if (e.code === 'Space' || e.code === 'Enter') {
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
     Ethan's 3x5 Kitchen Table Trivia Deck Engine (Full Canvas Comic)
     ========================================================================== */

  const storyTriviaDeck = [
    {
      num: '#01',
      tag: 'TRIVIA',
      q: 'What are the six stages of the laser printing electrophotographic (EP) cycle in exact order?',
      hint: 'Memory trick: People Can Easily Do The Fix...',
      a: 'Processing -> Charging -> Exposing -> Developing -> Transferring -> Fusing',
      r1: '- Charging applies -600V DC to photosensitive drum using primary corona wire or roller.',
      r2: '- Exposing uses laser to write electrostatic latent image by discharging drum to -100V.',
      trap: 'Exam trap: Cleaning happens before Processing or after Fusing to scrape remnant toner.'
    },
    {
      num: '#02',
      tag: 'TRIVIA',
      q: 'Toner smudges off a freshly printed page onto your fingers like loose charcoal dust. What part failed?',
      hint: 'Toner is plastic powder that must be melted into paper fibers...',
      a: 'The Fuser Assembly',
      r1: '- Failed to reach ~200°C (~390°F) to melt plastic toner resin into paper fibers.',
      r2: '- Pressure roller failed to squeeze melted resin into the grain.',
      trap: 'Exam trap: Faded page = empty toner or transfer roller. Smearing loose powder = cold fuser.'
    },
    {
      num: '#03',
      tag: 'TRIVIA',
      q: 'What are the pin counts for a legacy parallel printer cable on PC vs. printer?',
      hint: 'DB-25 has screws, Centronics has wire spring clips...',
      a: '25-pin DB-25 on PC, 36-pin Centronics on Printer',
      r1: '- IEEE 1284 standard for legacy bidirectional parallel communications.',
      r2: '- Maximum certified cable length is strictly 10 feet (3 meters).',
      trap: 'Exam trap: Serial is 9-pin (DB-9) or 25-pin (DB-25); Parallel printer is always 36-pin Centronics.'
    },
    {
      num: '#04',
      tag: 'TRIVIA',
      q: 'What DC voltages correspond to Orange, Red, and Yellow wires on a standard ATX power harness?',
      hint: 'Black is always Ground (0V)...',
      a: 'Orange = +3.3V, Red = +5V, Yellow = +12V',
      r1: '- Orange (+3.3V): Logic chips, chipset, PCIe signaling, RAM.',
      r2: '- Red (+5V): Legacy chips, USB ports, SATA logic.',
      trap: 'Exam trap: Yellow (+12V) drives motors, fans, and CPU VRMs. Blue is -12V.'
    },
    {
      num: '#05',
      tag: 'TRIVIA',
      q: 'What is the maximum certified channel distance for a Cat5e or Cat6 UTP Ethernet run?',
      hint: 'Includes solid structural horizontal run plus stranded patch cords...',
      a: '100 meters (328 feet total)',
      r1: '- 90 meters solid-core horizontal run from patch panel to wall jack.',
      r2: '- 10 meters total stranded patch cables (5m in closet + 5m at desk).',
      trap: 'Exam trap: Beyond 100m causes signal attenuation and Ethernet collision timing failures.'
    },
    {
      num: '#06',
      tag: 'TRIVIA',
      q: 'Power cuts abruptly during an office outage. Does data in dynamic RAM survive the drop?',
      hint: 'Compare capacitors needing refresh cycles to magnetic/NAND storage...',
      a: 'No. Dynamic RAM is Volatile',
      r1: '- DRAM bits are stored as microscopic electrical charges in capacitors.',
      r2: '- Without power delivering refresh cycles every few milliseconds, charge leaks to zero.',
      trap: 'Exam trap: Non-volatile storage (SSD, HDD, NVMe, USB) retains bits; RAM collapses instantly.'
    },
    {
      num: '#07',
      tag: 'TRIVIA',
      q: 'A workstation powers on, fans spin loudly, monitor shows "No Signal", and BIOS emits 1 long beep + 2 short beeps. What failed?',
      hint: 'Standard AMI/Award BIOS power-on self test video alert...',
      a: 'Display / Video Adapter Fault (GPU)',
      r1: '- POST completed CPU check, but failed to initialize video adapter hardware.',
      r2: '- Immediate action: Reseat the PCIe graphics card and verify auxiliary power harness.',
      trap: 'Exam trap: Continuous long beeps = RAM missing/unseated. 1 Long + 2 Short = Video error.'
    }
  ];

  let currentTriviaIdx = 0;

  function renderTriviaCard() {
    const stage = document.getElementById('storyTriviaCardStage');
    if (!stage) return;
    const card = storyTriviaDeck[currentTriviaIdx];
    if (!card) return;

    const flipper = document.getElementById('storyTriviaFlipper');
    if (flipper) flipper.classList.remove('is-flipped');

    const numFront = document.getElementById('storyCardNumFront');
    const numBack = document.getElementById('storyCardNumBack');
    const qEl = document.getElementById('storyCardQ');
    const hintEl = document.getElementById('storyCardHint');
    const aEl = document.getElementById('storyCardA');
    const r1El = document.getElementById('storyCardR1');
    const r2El = document.getElementById('storyCardR2');
    const trapEl = document.getElementById('storyCardTrap');
    const counterEl = document.getElementById('storyCardCounter');

    if (numFront) numFront.textContent = card.num;
    if (numBack) numBack.textContent = card.num;
    if (qEl) qEl.textContent = card.q;
    if (hintEl) hintEl.textContent = card.hint;
    if (aEl) aEl.textContent = card.a;
    if (r1El) r1El.textContent = card.r1;
    if (r2El) r2El.textContent = card.r2;
    if (trapEl) trapEl.textContent = card.trap;
    if (counterEl) counterEl.textContent = 'CARD ' + (currentTriviaIdx + 1) + ' OF ' + storyTriviaDeck.length;
  }

  function initStoryTriviaDeck() {
    const stage = document.getElementById('storyTriviaCardStage');
    if (!stage) return;
    if (stage._initialized) return;
    stage._initialized = true;

    const flipper = document.getElementById('storyTriviaFlipper');
    const prevBtn = document.getElementById('storyCardPrevBtn');
    const nextBtn = document.getElementById('storyCardNextBtn');
    const flipBtn = document.getElementById('storyCardFlipBtn');
    const shuffleBtn = document.getElementById('storyCardShuffleBtn');

    if (flipper) {
      flipper.addEventListener('click', function() {
        flipper.classList.toggle('is-flipped');
      });
    }

    if (flipBtn) {
      flipBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        if (flipper) flipper.classList.toggle('is-flipped');
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        currentTriviaIdx = (currentTriviaIdx - 1 + storyTriviaDeck.length) % storyTriviaDeck.length;
        renderTriviaCard();
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        currentTriviaIdx = (currentTriviaIdx + 1) % storyTriviaDeck.length;
        renderTriviaCard();
      });
    }

    if (shuffleBtn) {
      shuffleBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        let nextIdx;
        do {
          nextIdx = Math.floor(Math.random() * storyTriviaDeck.length);
        } while (nextIdx === currentTriviaIdx && storyTriviaDeck.length > 1);
        currentTriviaIdx = nextIdx;
        renderTriviaCard();
      });
    }

    document.addEventListener('keydown', function(e) {
      const activeStage = document.getElementById('storyTriviaCardStage');
      if (!activeStage) return;
      if (e.code === 'Space' && activeStage.matches(':hover')) {
        e.preventDefault();
        if (flipper) flipper.classList.toggle('is-flipped');
      } else if (e.code === 'ArrowRight' && activeStage.matches(':hover')) {
        e.preventDefault();
        currentTriviaIdx = (currentTriviaIdx + 1) % storyTriviaDeck.length;
        renderTriviaCard();
      } else if (e.code === 'ArrowLeft' && activeStage.matches(':hover')) {
        e.preventDefault();
        currentTriviaIdx = (currentTriviaIdx - 1 + storyTriviaDeck.length) % storyTriviaDeck.length;
        renderTriviaCard();
      }
    });

    renderTriviaCard();
  }


  /* ==========================================================================
     Ethan's 4x6 Taped Field Slates Deck Engine (Flippable Physical 3-Card Deck)
     ========================================================================== */

  const storySlatesDeck = [
    {
      band: 'THE ANATOMY SLATE (GREEN BAND)',
      tagColor: 'rgba(34, 197, 94, 0.45)',
      tagTextColor: '#14532d',
      frontHtml: `
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.92rem; font-weight: 700; color: #0f172a; margin-bottom: 0.65rem;">SIDE A: THE FOUR UNCHANGING MACHINE SUBSYSTEMS</div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">1. CPU (Central Processing Unit)</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Executes serialized instructions. Reads from cache/RAM. Halted if clock or power rail ripples.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #15803d; margin-top: 4px;">[Core Engine]</div>
          </div>
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">2. RAM (Volatile Memory)</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Ephemeral workspace for OS kernel and running programs. Drops to zero the moment current stops.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #b91c1c; margin-top: 4px;">[Volatile Workspace]</div>
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; margin-top: 0.75rem;">
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">3. Non-Volatile Storage</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Magnetic platters (HDD) or NAND cells (SSD). Preserves OS files, logs, and registry across reboots.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #15803d; margin-top: 4px;">[Persistent State]</div>
          </div>
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">4. System Bus & POST Firmware</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Motherboard circuit paths. UEFI/BIOS runs power-on self-test before handing off to the boot loader.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #0284c7; margin-top: 4px;">[Physical Interconnect]</div>
          </div>
        </div>
      `,
      backHtml: `
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.92rem; font-weight: 700; color: #0f172a; margin-bottom: 0.65rem;">SIDE B: HARDWARE DIAGNOSTICS & TELLS</div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">Capacitor Vent Inspection</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Inspect silver cylinders near CPU socket. Flat top = Healthy. Domed top or crusty brown vent = Blown voltage regulator.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #b91c1c; margin-top: 4px;">[Visual Tell: Voltage Ripple]</div>
          </div>
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">Flea Power Residual Drain</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Power supply capacitors hold residual DC charge. Pull wall AC cord, hold power button for 30s to bleed circuits to ground.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #0284c7; margin-top: 4px;">[Action: 30-Second Ground Bleed]</div>
          </div>
        </div>
        <div style="margin-top: 0.75rem; padding: 0.65rem 0.85rem; background: #fff; border: 1.5px solid #0f172a; border-radius: 4px;">
          <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a; margin-bottom: 3px;">POST Tell Cheat-Sheet (AMI/Award):</div>
          <div style="font-size: 0.72rem; color: #334155; font-family: 'JetBrains Mono', monospace;">
            &bull; 1 Short Beep: Normal boot &bull; Continuous Beeps: Memory unseated<br>
            &bull; 1 Long + 2 Short: Video/GPU fault &bull; Fans Max / No Beep: Dead VRM / CPU power unplugged
          </div>
        </div>
      `
    },
    {
      band: 'THE IDENTITY SLATE (YELLOW BAND)',
      tagColor: 'rgba(234, 179, 8, 0.45)',
      tagTextColor: '#713f12',
      frontHtml: `
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.92rem; font-weight: 700; color: #0f172a; margin-bottom: 0.65rem;">SIDE A: THE THREE NETWORK IDENTITY BOUNDARIES</div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">Layer 2: Physical MAC Address</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">48-bit hex stamped on NIC. Directs Ethernet frames across the immediate wire or switch port.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #0284c7; margin-top: 4px;">CLI: getmac /v &bull; ipconfig /all</div>
          </div>
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">Layer 3: Logical IP Address</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">32-bit IPv4 address assigned by DHCP or static lease. Dictates location in routed topology.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #0284c7; margin-top: 4px;">CLI: ipconfig /renew</div>
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; margin-top: 0.75rem;">
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">Layer 4: Transport Port Number</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">16-bit software doorway directing segments to the right application socket buffer.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #0284c7; margin-top: 4px;">CLI: netstat -ano</div>
          </div>
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">The Default Gateway Boundary</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Local router interface door. If gateway is dead, host talks to local roommates but cannot reach outside.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #0284c7; margin-top: 4px;">CLI: ping [gateway_ip]</div>
          </div>
        </div>
      `,
      backHtml: `
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.92rem; font-weight: 700; color: #0f172a; margin-bottom: 0.65rem;">SIDE B: IDENTITY DIAGNOSTICS & PING LADDER</div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">The APIPA 169.254 Tell</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Host has 169.254.x.x. Layer 1/2 copper link is up, but DHCP lease timed out (scope exhausted or VLAN wrong).</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #b91c1c; margin-top: 4px;">[Symptom: DHCP Unreachable]</div>
          </div>
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">The Loopback 127.0.0.1 Invariant</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Tests internal host TCP/IP software stack. Successful ping proves OS driver works; does NOT test physical wire.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #15803d; margin-top: 4px;">[Invariant: Stack Self-Test]</div>
          </div>
        </div>
        <div style="margin-top: 0.75rem; padding: 0.65rem 0.85rem; background: #fff; border: 1.5px solid #0f172a; border-radius: 4px;">
          <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a; margin-bottom: 3px;">The 4-Step Ping Ladder (Shop Binary Search):</div>
          <div style="font-size: 0.72rem; color: #334155; font-family: 'JetBrains Mono', monospace;">
            1. ping 127.0.0.1 (Internal OS Stack) &rarr; 2. ping [Local_IP] (NIC Binding)<br>
            3. ping [Default_Gateway] (Local Wire/Switch) &rarr; 4. ping 8.8.8.8 (External Internet)
          </div>
        </div>
      `
    },
    {
      band: 'THE TRIAGE COMPASS (BLUE BAND)',
      tagColor: 'rgba(2, 132, 199, 0.45)',
      tagTextColor: '#0c4a6e',
      frontHtml: `
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.92rem; font-weight: 700; color: #0f172a; margin-bottom: 0.65rem;">SIDE A: THE 6-STEP TROUBLESHOOTING ORDER OF OPERATIONS</div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">1. Identify the Problem</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Question user, identify symptoms, review environmental changes, determine if anything changed before failure.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #0284c7; margin-top: 4px;">[Rule: Question the user first]</div>
          </div>
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">2. Establish Theory of Cause</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Question the obvious. Consider multiple approaches. Establish a single testable theory of probable cause.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #0284c7; margin-top: 4px;">[Rule: Simplest explanation first]</div>
          </div>
        </div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem; margin-top: 0.75rem;">
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">3. Test Theory to Determine Cause</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Run simplest non-destructive test. If confirmed, determine next steps. If disproven, establish new theory.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #0284c7; margin-top: 4px;">[Rule: Never guess blindly]</div>
          </div>
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">4. Plan of Action & Resolution</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Establish plan to resolve problem and implement solution. Identify potential unintended side-effects.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #0284c7; margin-top: 4px;">[Rule: Change one variable at a time]</div>
          </div>
        </div>
      `,
      backHtml: `
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.92rem; font-weight: 700; color: #0f172a; margin-bottom: 0.65rem;">SIDE B: VERIFICATION, DOCUMENTATION & HANK'S RULES</div>
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.75rem;">
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">5. Verify Full Functionality</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Verify complete system functionality and implement preventive measures to stop recurrence.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #15803d; margin-top: 4px;">[Rule: Customer signs off]</div>
          </div>
          <div style="border: 1.5px solid #0f172a; padding: 0.65rem 0.85rem; background: #fff; border-radius: 4px;">
            <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a;">6. Document Everything</div>
            <div style="font-size: 0.72rem; color: #334155; line-height: 1.35; margin-top: 3px;">Document findings, actions, and outcomes in ticket passdown notes for team handoff.</div>
            <div style="font-size: 0.68rem; font-weight: 700; color: #0284c7; margin-top: 4px;">[Rule: If not documented, it didn't happen]</div>
          </div>
        </div>
        <div style="margin-top: 0.75rem; padding: 0.65rem 0.85rem; background: #fff; border: 1.5px solid #0f172a; border-radius: 4px;">
          <div style="font-weight: 700; font-size: 0.82rem; color: #0f172a; margin-bottom: 3px;">Hank's Machine Shop Law:</div>
          <div style="font-size: 0.72rem; color: #334155; font-family: 'JetBrains Mono', monospace;">
            &bull; "Power comes in, signal goes out. If copper don't have clean ground, the circuit is blind."<br>
            &bull; Never adjust three adjustments at once out of panic. One change &rarr; Test &rarr; Verify.
          </div>
        </div>
      `
    }
  ];

  let currentSlateIdx = 0;

  function renderSlateCard() {
    const stage = document.getElementById('storySlateCardStage');
    if (!stage) return;
    const slate = storySlatesDeck[currentSlateIdx];
    if (!slate) return;

    const flipper = document.getElementById('storySlateFlipper');
    if (flipper) flipper.classList.remove('is-flipped');

    const markerFront = document.getElementById('slateMarkerFront');
    const markerBack = document.getElementById('slateMarkerBack');
    const numFront = document.getElementById('slateNumFront');
    const numBack = document.getElementById('slateNumBack');
    const frontContent = document.getElementById('slateFrontContent');
    const backContent = document.getElementById('slateBackContent');
    const counter = document.getElementById('slateCounter');

    if (markerFront) {
      markerFront.textContent = slate.band;
      markerFront.style.background = slate.tagColor;
      markerFront.style.color = slate.tagTextColor;
    }
    if (markerBack) {
      markerBack.textContent = slate.band;
      markerBack.style.background = slate.tagColor;
      markerBack.style.color = slate.tagTextColor;
    }
    if (numFront) numFront.textContent = 'SIDE A';
    if (numBack) numBack.textContent = 'SIDE B';
    if (frontContent) frontContent.innerHTML = slate.frontHtml;
    if (backContent) backContent.innerHTML = slate.backHtml;
    // textContent shows entities literally, so use the bullet character itself, and the real deck length
    if (counter) counter.textContent = '[ CARD ' + (currentSlateIdx + 1) + ' OF ' + storySlatesDeck.length + ' \u2022 CLICK OR SPACEBAR TO FLIP TO SIDE B ]';
  }

  function initStorySlatesDeck() {
    const stage = document.getElementById('storySlateCardStage');
    if (!stage) return;
    if (stage._initialized) return;
    stage._initialized = true;

    const flipper = document.getElementById('storySlateFlipper');
    const prevBtn = document.getElementById('slatePrevBtn');
    const nextBtn = document.getElementById('slateNextBtn');
    const flipBtn = document.getElementById('slateFlipBtn');

    if (flipper) {
      flipper.addEventListener('click', function() {
        flipper.classList.toggle('is-flipped');
      });
    }

    if (flipBtn) {
      flipBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        if (flipper) flipper.classList.toggle('is-flipped');
      });
    }

    if (prevBtn) {
      prevBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        currentSlateIdx = (currentSlateIdx - 1 + storySlatesDeck.length) % storySlatesDeck.length;
        renderSlateCard();
      });
    }

    if (nextBtn) {
      nextBtn.addEventListener('click', function(e) {
        e.stopPropagation();
        currentSlateIdx = (currentSlateIdx + 1) % storySlatesDeck.length;
        renderSlateCard();
      });
    }

    renderSlateCard();
  }

  /* ==========================================================================
     Taped Field Slate Tab & Side Switcher
     ========================================================================== */

  function initTapedSlates() {
    document.querySelectorAll('.taped-field-slate').forEach(function(slate) {
      if (slate._initializedTaped) return;
      slate._initializedTaped = true;

      const tabBtns = slate.querySelectorAll('.slate-tab-btn');
      const sideBtns = slate.querySelectorAll('.slate-side-btn');
      let currentBand = 'green';
      let currentSide = 'a';

      function updateView() {
        slate.querySelectorAll('.slate-sheet').forEach(function(s) {
          const band = s.getAttribute('data-band');
          const side = s.getAttribute('data-side');
          s.classList.toggle('active', band === currentBand && side === currentSide);
        });
        tabBtns.forEach(function(b) {
          b.classList.toggle('active', b.getAttribute('data-band') === currentBand);
        });
        sideBtns.forEach(function(b) {
          b.classList.toggle('active', b.getAttribute('data-side') === currentSide);
        });
      }

      tabBtns.forEach(function(b) {
        b.addEventListener('click', function(e) {
          e.preventDefault();
          currentBand = b.getAttribute('data-band');
          updateView();
        });
      });

      sideBtns.forEach(function(b) {
        b.addEventListener('click', function(e) {
          e.preventDefault();
          currentSide = b.getAttribute('data-side');
          updateView();
        });
      });

      updateView();
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
        // ```lnk-deck decks build themselves: docs/lnk-deck.js watches for new placeholders.
        initJobAidTabs();
        initTapedSlates();
        initStoryTriviaDeck();
        initStorySlatesDeck();

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

