#!/usr/bin/env python3
"""Check that every script in tools/ is listed in the Tool index in tools/README.md.

A script counts as listed when its file name appears in backticks anywhere in
tools/README.md (for example `refactor_episode_02.py`). The point is that each
new script gets sorted into "use it", "generator" or "one-shot, do not rerun"
when it is committed, so nobody has to open it to find out.

    python3 tools/check_tools_index.py           # exit 1 if any script is unlisted
    python3 tools/check_tools_index.py --warn    # report only (exit 0); CI uses this

Standard library only.
"""
import pathlib
import sys

TOOLS = pathlib.Path(__file__).resolve().parent


def main() -> int:
    warn_only = "--warn" in sys.argv[1:]
    readme = (TOOLS / "README.md").read_text(encoding="utf-8")
    scripts = sorted(p.name for p in TOOLS.glob("*.py"))
    missing = [name for name in scripts if f"`{name}`" not in readme]
    listed_but_gone = sorted(
        name for name in _backticked_py(_index_section(readme))
        if "/" not in name and not (TOOLS / name).exists()
    )

    for name in missing:
        msg = f"tools/{name} is not listed in tools/README.md (add it to the Tool index)"
        print(f"::warning file=tools/{name}::{msg}" if warn_only else f"MISSING: {msg}")
    for name in listed_but_gone:
        msg = f"tools/README.md lists `{name}` but tools/{name} does not exist"
        print(f"::warning file=tools/README.md::{msg}" if warn_only else f"STALE: {msg}")

    problems = len(missing) + len(listed_but_gone)
    if problems == 0:
        print(f"Tool index OK: {len(scripts)} scripts in tools/, all listed in tools/README.md.")
        return 0
    print(f"{problems} tool index problem(s).")
    return 0 if warn_only else 1


def _index_section(readme: str) -> str:
    """The "## Tool index" section only, so prose elsewhere can name a retired script."""
    start = readme.find("## Tool index")
    if start < 0:
        return readme
    end = readme.find("\n## ", start + 1)
    return readme[start:] if end < 0 else readme[start:end]


def _backticked_py(text: str):
    parts = text.split("`")
    for i in range(1, len(parts), 2):
        token = parts[i].strip()
        if token.endswith(".py") and len(token) > 3 and " " not in token:
            yield token


if __name__ == "__main__":
    sys.exit(main())
