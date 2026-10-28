/* lnk-deck: flip-card decks for any page in the kit.
 *
 * Load lnk-deck.css and this script on a page. Any element
 *   <div class="lnk-deck" data-deck="ENCODED_JSON"></div>
 * becomes a deck, whenever it appears: at page load, after a page fetches its
 * narrative (Tamarack unit pages), or after a Docsify route change (Portland Desk).
 * A MutationObserver finds new placeholders, so no page has to call anything.
 *
 * data-deck is encodeURIComponent(JSON.stringify(deck)), where deck is
 *   { title, meta, size: '3x5' | '4x6', band: 'red'|'green'|'yellow'|'blue',
 *     cards: [{ q, a, why?, tag?, back_tag?, band?, hint? }] }
 * Pages write decks as ```lnk-deck fences; the page's builder (render_unit.py, or
 * the Docsify hook in portland-desk/index.html) turns the fence into the placeholder.
 * Spec: docs/research/INTERACTIVE_COMPONENTS_SPEC.md, section 4.
 *
 * Rules this file keeps (see research/lessons-learned.md, "The flashcard deck that
 * held one card"): card text is plain text, never innerHTML; one click/keydown listener
 * per deck, none on document; this is the only code that binds deck events.
 */
(function () {
  'use strict';

  var BANDS = { red: 1, green: 1, yellow: 1, blue: 1 };

  // Plain text in, with `backticks` rendered as <code>.
  function inline(el, text) {
    el.textContent = '';
    String(text == null ? '' : text).split(/(`[^`]+`)/).forEach(function (part) {
      if (/^`[^`]+`$/.test(part)) {
        var code = document.createElement('code');
        code.textContent = part.slice(1, -1);
        el.appendChild(code);
      } else if (part) {
        el.appendChild(document.createTextNode(part));
      }
    });
  }

  function el(tag, cls, text) {
    var e = document.createElement(tag);
    if (cls) e.className = cls;
    if (text != null) inline(e, text);
    return e;
  }

  function build(root) {
    if (root._lnkDeck) return;
    var data;
    try {
      data = JSON.parse(decodeURIComponent(root.getAttribute('data-deck') || ''));
    } catch (err) {
      root._lnkDeck = true;
      root.textContent = 'This flashcard deck could not be read: ' + err.message;
      return;
    }
    var cards = (data.cards || []).filter(function (c) { return c && (c.q || c.a); });
    if (cards.length === 0) return;
    root._lnkDeck = true;

    var size = data.size === '4x6' ? '4x6' : '3x5';
    var deckBand = BANDS[data.band] ? data.band : 'red';
    root.classList.add('lnk-deck--' + size);
    root.setAttribute('data-band', deckBand);
    root.setAttribute('tabindex', '0');
    root.setAttribute('role', 'region');
    root.setAttribute('aria-label', (data.title || 'Flashcards') +
      '. Space or Enter flips the card; left and right arrows move between cards.');

    var header = el('div', 'lnk-deck__header');
    var titles = el('div', 'lnk-deck__titles');
    titles.appendChild(el('span', 'lnk-deck__badge', data.title || 'Flashcards'));
    if (data.meta) titles.appendChild(el('span', 'lnk-deck__meta', data.meta));
    header.appendChild(titles);
    var counter = el('div', 'lnk-deck__counter');
    var announcement = el('div', 'lnk-deck__announcement');
    announcement.setAttribute('role', 'status');
    announcement.setAttribute('aria-atomic', 'true');
    header.appendChild(counter);

    var stage = el('div', 'lnk-deck__stage');
    var card = el('div', 'lnk-deck__card');
    var front = el('div', 'lnk-deck__face lnk-deck__face--front');
    var back = el('div', 'lnk-deck__face lnk-deck__face--back');
    card.appendChild(front);
    card.appendChild(back);
    stage.appendChild(card);

    var nav = el('div', 'lnk-deck__nav');
    [['prev', '← Previous'], ['flip', 'Flip card'], ['next', 'Next →'], ['shuffle', 'Shuffle']]
      .forEach(function (b) {
        var btn = el('button', 'lnk-deck__btn', b[1]);
        btn.type = 'button';
        btn.setAttribute('data-act', b[0]);
        nav.appendChild(btn);
      });

    var dots = el('div', 'lnk-deck__dots');
    cards.forEach(function (_, i) {
      var dot = el('button', 'lnk-deck__dot');
      dot.type = 'button';
      dot.setAttribute('data-act', 'go');
      dot.setAttribute('data-i', String(i));
      dot.setAttribute('aria-label', 'Card ' + (i + 1));
      dots.appendChild(dot);
    });

    root.textContent = '';
    root.appendChild(announcement);
    root.appendChild(header);
    root.appendChild(stage);
    root.appendChild(nav);
    if (cards.length <= 40) root.appendChild(dots);

    var idx = 0;
    var flipped = false;

    function render(announce) {
      var c = cards[idx];
      var n = 'Card ' + (idx + 1) + ' of ' + cards.length;
      card.setAttribute('data-band', BANDS[c.band] ? c.band : deckBand);

      front.textContent = '';
      if (c.tag) front.appendChild(el('span', 'lnk-deck__tag', c.tag));
      front.appendChild(el('div', 'lnk-deck__q', c.q || ''));
      var ff = el('div', 'lnk-deck__foot');
      ff.appendChild(el('span', null, n));
      ff.appendChild(el('span', null, c.hint || 'Click or press Space to flip'));
      front.appendChild(ff);

      back.textContent = '';
      back.appendChild(el('span', 'lnk-deck__tag', c.back_tag || 'Answer'));
      back.appendChild(el('div', 'lnk-deck__a', c.a || ''));
      if (c.why) back.appendChild(el('div', 'lnk-deck__why', c.why));
      var bf = el('div', 'lnk-deck__foot');
      bf.appendChild(el('span', null, n));
      bf.appendChild(el('span', null, 'Click to flip back'));
      back.appendChild(bf);

      card.classList.toggle('is-flipped', flipped);
      front.setAttribute('aria-hidden', flipped ? 'true' : 'false');
      back.setAttribute('aria-hidden', flipped ? 'false' : 'true');
      counter.textContent = 'CARD ' + (idx + 1) + ' / ' + cards.length;
      nav.querySelector('[data-act="flip"]').setAttribute('aria-pressed', String(flipped));
      if (announce) inline(announcement, n + '. ' + (flipped ? 'Answer: ' + (c.a || '') + (c.why ? '. ' + c.why : '') : 'Question: ' + (c.q || '')));
      var all = dots.querySelectorAll('.lnk-deck__dot');
      for (var i = 0; i < all.length; i++) all[i].classList.toggle('is-active', i === idx);
    }

    function act(name, arg) {
      if (name === 'flip') {
        flipped = !flipped;
      } else if (name === 'next') {
        idx = (idx + 1) % cards.length; flipped = false;
      } else if (name === 'prev') {
        idx = (idx - 1 + cards.length) % cards.length; flipped = false;
      } else if (name === 'go') {
        idx = Math.min(cards.length - 1, Math.max(0, Number(arg) || 0)); flipped = false;
      } else if (name === 'shuffle' && cards.length > 1) {
        for (var i = cards.length - 1; i > 0; i--) {
          var j = Math.floor(Math.random() * (i + 1));
          var t = cards[i]; cards[i] = cards[j]; cards[j] = t;
        }
        idx = 0; flipped = false;
      }
      render(true);
    }

    root.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-act]');
      if (btn && root.contains(btn)) {
        act(btn.getAttribute('data-act'), btn.getAttribute('data-i'));
        return;
      }
      if (e.target.closest('.lnk-deck__card')) act('flip');
    });
    root.addEventListener('keydown', function (e) {
      if (e.target.closest('button')) return; // buttons handle their own Space/Enter
      if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); act('flip'); }
      else if (e.key === 'ArrowRight') { e.preventDefault(); act('next'); }
      else if (e.key === 'ArrowLeft') { e.preventDefault(); act('prev'); }
    });

    render();
  }

  function init(scope) {
    var list = (scope || document).querySelectorAll('.lnk-deck[data-deck]');
    for (var i = 0; i < list.length; i++) build(list[i]);
  }

  window.LnkDeck = { init: init };

  function start() {
    init(document);
    if (window.MutationObserver) {
      new MutationObserver(function (records) {
        for (var i = 0; i < records.length; i++) {
          if (records[i].addedNodes.length) { init(document); return; }
        }
      }).observe(document.body, { childList: true, subtree: true });
    }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
