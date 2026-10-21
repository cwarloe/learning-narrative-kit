#!/usr/bin/env python3
import re
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent

for path in [KIT_ROOT / "portland-desk" / "index.html", KIT_ROOT / "docs" / "portland-desk" / "index.html"]:
    html = path.read_text(encoding="utf-8")

    # 1. Update tooltip HTML
    if '<div class="tt-link" id="tt-link">' not in html:
        html = html.replace(
            '<div class="tt-context" id="tt-context"></div>',
            '<div class="tt-context" id="tt-context"></div>\n    <div class="tt-link" id="tt-link">Click to view in Master Glossary &rarr;</div>'
        )

    # 2. Update term markup from <span> to <a>
    html = html.replace(
        'return `<span class="term ${cat}" id="term-${id}" data-term="${id}">${displayText}</span>`;',
        'return `<a class="term ${cat}" href="#/glossary?id=term-${id}" id="term-${id}" data-term="${id}">${displayText}</a>`;'
    )

    # 3. Update click behavior
    old_click = """              el.addEventListener('click', function(e) {
                if (window.innerWidth <= 768) {
                  if (activeTouchTerm === el && tooltip.style.display === 'block') {
                    hideTooltip();
                    activeTouchTerm = null;
                  } else {
                    activeTouchTerm = el;
                    showTooltip(el, e);
                  }
                }
              });"""

    new_click = """              el.addEventListener('click', function(e) {
                if (window.innerWidth <= 768) {
                  if (activeTouchTerm !== el) {
                    e.preventDefault();
                    activeTouchTerm = el;
                    showTooltip(el, e);
                  } else {
                    hideTooltip();
                    activeTouchTerm = null;
                  }
                } else {
                  hideTooltip();
                }
              });"""

    if old_click in html:
        html = html.replace(old_click, new_click)

    # 4. Add auto-scroll handler
    if 'Auto-scroll and highlight target term in Master Glossary' not in html:
        scroll_code = """
            // Auto-scroll and highlight target term in Master Glossary
            const currentHash = window.location.hash || '';
            if (currentHash.indexOf('glossary') !== -1) {
              const urlParts = currentHash.split('?');
              if (urlParts.length > 1) {
                const urlParams = new URLSearchParams(urlParts[1]);
                const targetId = urlParams.get('id');
                if (targetId) {
                  setTimeout(function() {
                    const el = document.getElementById(targetId);
                    if (el) {
                      el.scrollIntoView({ behavior: 'smooth', block: 'center' });
                      el.classList.add('story-highlight');
                      setTimeout(function() { el.classList.remove('story-highlight'); }, 2500);
                    }
                  }, 180);
                }
              }
            }
"""
        html = html.replace(
            '// Smooth scroll and pulse on term anchors',
            scroll_code + '            // Smooth scroll and pulse on term anchors'
        )

    path.write_text(html, encoding="utf-8")
    print(f"Updated {path}")
