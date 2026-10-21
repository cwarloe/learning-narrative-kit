"""Landing-page (docs/index.html) drift check.

Run from anywhere:  python3 tools/check_hub_links.py [--strict]

Fails (exit 1) when:
  * docs/index.html no longer matches what tools/build_hub_index.py writes
    (someone hand-edited the generated page, or edited the builder without re-running it);
  * a relative link on docs/index.html points at a file that does not exist.

Reports (and fails only with --strict):
  * rendered pages docs/<dir>/index.html that cannot be reached by following
    links from docs/index.html (a unit with no landing card or track entry).
"""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
HUB = DOCS / "index.html"
HREF_RE = re.compile(r"""href=["']([^"']*)["']""")


def load_builder_html() -> str:
    spec = importlib.util.spec_from_file_location("build_hub_index", ROOT / "tools" / "build_hub_index.py")
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module.HTML_CONTENT


def local_target(page: Path, href: str) -> Path | None:
    """Resolve a relative href on `page` to a file path, or None for external/anchor-only links."""
    parts = urlsplit(href)
    if parts.scheme or parts.netloc or href.startswith(("mailto:", "javascript:")):
        return None
    path = unquote(parts.path)
    if not path:
        return None  # "#anchor" or docsify "#/route" on the same page
    target = (page.parent / path).resolve()
    if path.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


def html_links(page: Path) -> list[str]:
    return HREF_RE.findall(page.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--strict", action="store_true", help="also fail on rendered pages unreachable from the hub")
    args = parser.parse_args()

    failures = 0

    # 1. Generated page matches its builder.
    hub_text = HUB.read_text(encoding="utf-8")
    if hub_text != load_builder_html():
        print("DRIFT: docs/index.html differs from tools/build_hub_index.py output.")
        print("       Edit HTML_CONTENT in tools/build_hub_index.py, then run: python3 tools/build_hub_index.py")
        failures += 1
    else:
        print("OK: docs/index.html matches tools/build_hub_index.py")

    # 2. Every relative link on the hub resolves.
    links = html_links(HUB)
    broken = 0
    for href in links:
        target = local_target(HUB, href)
        if target is not None and not target.exists():
            print(f"BROKEN: {href} -> {target.relative_to(ROOT)}")
            broken += 1
    print(f"Checked {len(links)} links on docs/index.html; {broken} broken.")
    failures += broken

    # 3. Every rendered docs/<dir>/index.html is reachable from the hub.
    seen: set[Path] = set()
    queue = [HUB.resolve()]
    while queue:
        page = queue.pop()
        if page in seen:
            continue
        seen.add(page)
        for href in html_links(page):
            target = local_target(page, href)
            if target is None or target.suffix != ".html" or not target.exists():
                continue
            if DOCS.resolve() in target.parents and target not in seen:
                queue.append(target)

    rendered = sorted(p.resolve() for p in DOCS.glob("*/index.html"))
    orphans = [p for p in rendered if p not in seen]
    if orphans:
        label = "ORPHAN" if args.strict else "warning: unlinked"
        print(f"{len(orphans)} rendered page(s) not reachable from docs/index.html:")
        for p in orphans:
            print(f"  {label}: {p.parent.relative_to(DOCS)}/")
        if args.strict:
            failures += len(orphans)
    else:
        print(f"All {len(rendered)} rendered docs/<dir>/index.html pages are reachable from the hub.")

    if failures:
        print(f"FAIL ({failures} problem(s))")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
