#!/usr/bin/env python3
"""Browser smoke checks for shared decks in unit pages and Docsify.

Install requirements-browser.txt and run playwright install chromium first.
Set CHROMIUM_EXECUTABLE to use an existing Chromium. No repository files are written.
External web fonts are deliberately excluded; checks exercise layout with fallbacks.
CDN scripts/styles are fetched over HTTPS through the inherited proxy.
"""

import functools
import http.server
import json
import os
import sys
import threading
import traceback
import urllib.request
from pathlib import Path

from playwright.sync_api import sync_playwright
from _workbench import check_workbench
from _accessibility import check_deck_accessibility, check_deck_contrast

ROOT = Path(__file__).resolve().parent.parent
failures = 0


class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


s = http.server.ThreadingHTTPServer(
    ("127.0.0.1", 0), functools.partial(Quiet, directory=str(ROOT / "docs"))
)
threading.Thread(target=s.serve_forever, daemon=True).start()
base = f"http://127.0.0.1:{s.server_port}"
cache = {}
external = []


def route(r):
    u = r.request.url
    if u.startswith(base):
        return r.continue_()
    if "fonts.googleapis.com/" in u or "fonts.gstatic.com/" in u:
        return r.abort()
    u = u.replace("http://", "https://", 1)
    try:
        if u not in cache:
            with urllib.request.urlopen(u, timeout=25) as res:
                cache[u] = (
                    res.read(),
                    res.headers.get("Content-Type", "application/octet-stream"),
                )
        body, mime = cache[u]
        r.fulfill(status=200, body=body, content_type=mime)
    except Exception as e:
        external.append((u, str(e)))
        r.abort()


with sync_playwright() as pw:
    b = pw.chromium.launch(
        executable_path=os.environ.get("CHROMIUM_EXECUTABLE") or None
    )
    for width in [1280, 390]:
        ctx = b.new_context(
            viewport={"width": width, "height": 900}, reduced_motion="reduce"
        )
        ctx.route("**/*", route)
        for path, expected_decks in [
            ("/exam2-knaflic-board/", 2),
            ("/itm310-exam2-cards/", 11),
            ("/portland-desk/#/workbench/00-the-four-rubber-bands", 1),
        ]:
            p = ctx.new_page()
            errors = []
            p.on("pageerror", lambda e, sink=errors: sink.append(str(e)))
            try:
                p.goto(base + path, wait_until="domcontentloaded", timeout=60000)
                p.locator(".lnk-deck__card").first.wait_for(timeout=45000)
                decks = p.locator(".lnk-deck[data-deck]")
                n = decks.count()
                assert (
                    n == expected_decks
                ), f"Expected {expected_decks} decks, found {n}"
                cards = 0
                for i in range(n):
                    d = decks.nth(i)
                    data = d.evaluate(
                        "(e)=>JSON.parse(decodeURIComponent(e.dataset.deck))"
                    )
                    check_deck_accessibility(d)
                    check_deck_contrast(d)
                    count = len(data["cards"])
                    cards += count
                    assert d.locator(".lnk-deck__q").text_content() == data["cards"][0][
                        "q"
                    ].replace(chr(96), ""), repr(
                        (
                            d.locator(".lnk-deck__q").text_content(),
                            data["cards"][0]["q"],
                        )
                    )
                    d.locator("[data-act=flip]").click()
                    assert "is-flipped" in d.locator(".lnk-deck__card").get_attribute(
                        "class"
                    )
                    assert d.locator(".lnk-deck__a").text_content() == data["cards"][0][
                        "a"
                    ].replace(chr(96), "")
                    d.locator("[data-act=next]").click()
                    assert (
                        d.locator(".lnk-deck__counter").inner_text()
                        == f"CARD {2 if count>1 else 1} / {count}"
                    )
                    assert "is-flipped" not in d.locator(
                        ".lnk-deck__card"
                    ).get_attribute("class")
                    d.locator("[data-act=prev]").click()
                    assert d.locator(".lnk-deck__q").text_content() == data["cards"][0][
                        "q"
                    ].replace(chr(96), ""), repr(
                        (
                            d.locator(".lnk-deck__q").text_content(),
                            data["cards"][0]["q"],
                        )
                    )
                    d.focus()
                    p.keyboard.press("Space")
                    assert (
                        d.locator(".lnk-deck__face--back").get_attribute("aria-hidden")
                        == "false"
                    )
                    p.keyboard.press("ArrowLeft")
                    assert (
                        d.locator(".lnk-deck__counter").inner_text()
                        == f"CARD {count} / {count}"
                    )
                    d.locator("[data-act=shuffle]").click()
                    assert (
                        d.locator(".lnk-deck__counter").inner_text()
                        == f"CARD 1 / {count}"
                    )
                    # Visit both faces of every card and check card/face overflow.
                    layout = d.evaluate("""e => {
                            const source = JSON.parse(decodeURIComponent(e.dataset.deck)).cards;
                            const issues = [], seen = [];
                            for (let i = 0; i < source.length; i++) {
                                seen.push([
                                    e.querySelector('.lnk-deck__q').textContent,
                                    e.querySelector('.lnk-deck__a').textContent
                                ]);
                                for (const face of e.querySelectorAll('.lnk-deck__face')) {
                                    if (face.scrollWidth > face.clientWidth + 2 ||
                                        face.scrollHeight > face.clientHeight + 2) issues.push(i);
                                }
                                e.querySelector('[data-act=next]').click();
                            }
                            // Shuffle must preserve every question/answer pair exactly once.
                            const expected = source.map(c => [
                                c.q.replace(/`/g, ''), c.a.replace(/`/g, '')
                            ]);
                            if (JSON.stringify(seen.sort()) !== JSON.stringify(expected.sort())) {
                                throw new Error('Navigation or shuffle lost/duplicated card content');
                            }
                            return issues;
                        }""")
                    assert not layout, f"deck {i} overflowing cards {layout}"
                overflow = p.evaluate(
                    "document.documentElement.scrollWidth > innerWidth+2"
                )
                assert not overflow, "Page overflows viewport"
                # Table wrappers can hide clipping from the document-width check.
                assert p.locator(".table-wrap").evaluate_all(
                    "(els)=>els.every(e=>e.scrollWidth<=e.clientWidth+2)"
                ), "Reference table needs horizontal scrolling"
                assert not errors, f"JavaScript errors: {errors}"
                print(
                    json.dumps(
                        {
                            "path": path,
                            "width": width,
                            "decks": n,
                            "cards": cards,
                            "page_overflow": overflow,
                            "errors": errors,
                            "result": "PASS",
                        }
                    ),
                    flush=True,
                )

            except Exception as e:
                failures += 1
                traceback.print_exc()
                print(
                    json.dumps(
                        {
                            "path": path,
                            "width": width,
                            "result": "FAIL",
                            "error": str(e),
                            "errors": errors,
                        }
                    ),
                    flush=True,
                )
                artifacts = Path(
                    os.environ.get("BROWSER_ARTIFACTS", "/tmp/lnk-browser-failures")
                )
                artifacts.mkdir(parents=True, exist_ok=True)
                p.screenshot(path=str(artifacts / f'{width}-{path.split("/")[1]}.png'))
            p.close()
        for source in sorted((ROOT / "docs/portland-desk/workbench").glob("*.md")):
            p = ctx.new_page()
            errors = []
            p.on("pageerror", lambda e, sink=errors: sink.append(str(e)))
            try:
                result = check_workbench(p, source, base)
                assert not errors, f"JavaScript errors: {errors}"
                print(json.dumps(dict(result, width=width, result="PASS")), flush=True)
            except Exception as e:
                failures += 1
                traceback.print_exc()
                print(f"FAIL {source.name} at {width}px: {e}", flush=True)
                artifacts = Path(
                    os.environ.get("BROWSER_ARTIFACTS", "/tmp/lnk-browser-failures")
                )
                artifacts.mkdir(parents=True, exist_ok=True)
                p.screenshot(path=str(artifacts / f"{width}-{source.stem}.png"))
            finally:
                p.close()
        ctx.close()
    b.close()
s.shutdown()
s.server_close()
print("External failures:", external)

sys.exit(1 if failures or external else 0)
