#!/usr/bin/env python3
"""
check-links.py — Zero-dependency relative link validator for Docsify / LNK templates.

Features:
- Validates Markdown links [label](path) and HTML <a href="path">.
- Supports Docsify hash-routing links (e.g., '#/narrative/01-chapter-sample' -> checks 'narrative/01-chapter-sample.md').
- Checks standard relative file paths and asset references.
- Validates on-page and cross-page anchor fragments (#anchor).
- Excludes external URLs (http://, https://, mailto:).
- Returns exit code 0 on success, 1 on broken links.
"""

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

# ANSI Color Codes for clean terminal output
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"


def find_anchors_in_file(file_path: Path) -> set:
    """Extract all potential anchor IDs from headings and HTML id attributes."""
    anchors = set()
    try:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return anchors

    # 1. HTML id/name attributes: id="xyz" or id='xyz'
    for match in re.finditer(r'''\b(?:id|name)=["']([^"']+)["']''', content, re.IGNORECASE):
        anchors.add(match.group(1))

    # 2. In-text term spans: id="term-xyz" or [[xyz|...]]
    for match in re.finditer(r'`?\[\[([a-zA-Z0-9_-]+)(?:\|[^\]]+)?\]\]`?', content):
        anchors.add(f"term-{match.group(1)}")
        anchors.add(match.group(1))

    # 3. Markdown Headings (# Heading Name -> heading-name)
    for line in content.splitlines():
        line = line.strip()
        if line.startswith("#"):
            heading_text = re.sub(r"^#+\s*", "", line)
            # Remove inline markdown links/markup
            heading_text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", heading_text)
            heading_text = re.sub(r"[^\w\s-]", "", heading_text).strip().lower()
            slug = re.sub(r"[-\s]+", "-", heading_text)
            if slug:
                anchors.add(slug)

    return anchors


def resolve_docsify_hash_target(root_dir: Path, current_file: Path, hash_target: str):
    """
    Resolves a Docsify hash path (e.g. '#/narrative/01-chapter-sample')
    to an actual file on disk relative to the root_dir.
    """
    clean_path = hash_target.lstrip("#").lstrip("/")
    # Extract fragment if present inside the hash: #/path/to/page#anchor
    fragment = None
    if "#" in clean_path:
        parts = clean_path.split("#", 1)
        clean_path = parts[0]
        fragment = parts[1]

    # Candidate 1: clean_path.md
    c1 = root_dir / f"{clean_path}.md"
    if c1.is_file():
        return c1, fragment

    # Candidate 2: clean_path (already has extension or is exact file)
    c2 = root_dir / clean_path
    if c2.is_file():
        return c2, fragment

    # Candidate 3: clean_path/README.md
    c3 = root_dir / clean_path / "README.md"
    if c3.is_file():
        return c3, fragment

    # Candidate 4: root README.md if clean_path is empty
    if not clean_path:
        c4 = root_dir / "README.md"
        if c4.is_file():
            return c4, fragment

    return None, fragment


def validate_file(root_dir: Path, md_file: Path, anchor_cache: dict) -> list:
    """Scans a single markdown file for links and checks their validity."""
    broken = []
    try:
        content = md_file.read_text(encoding="utf-8", errors="ignore")
    except Exception as e:
        broken.append((0, "file-read-error", f"Could not read file: {e}"))
        return broken

    # Regex patterns for Markdown links and HTML anchor tags
    md_link_pattern = re.compile(r'\[([^\]]*)\]\(([^)]+)\)')
    html_link_pattern = re.compile(r'<a\s+[^>]*href=["\']([^"\']+)["\']', re.IGNORECASE)

    links_to_check = []

    for line_idx, line in enumerate(content.splitlines(), start=1):
        # Markdown links
        for match in md_link_pattern.finditer(line):
            raw_url = match.group(2).strip()
            links_to_check.append((line_idx, raw_url))

        # HTML links
        for match in html_link_pattern.finditer(line):
            raw_url = match.group(1).strip()
            links_to_check.append((line_idx, raw_url))

    for line_num, raw_url in links_to_check:
        parsed = urlparse(raw_url)
        # Skip external web protocols and mailto
        if parsed.scheme in ("http", "https", "mailto", "ftp", "javascript"):
            continue

        url_path = unquote(parsed.path)
        fragment = parsed.fragment

        # Case 1: Docsify Hash Route (e.g. #/narrative/01-chapter-sample)
        if raw_url.startswith("#/"):
            target_file, sub_fragment = resolve_docsify_hash_target(root_dir, md_file, raw_url)
            if target_file is None:
                broken.append((line_num, raw_url, "Docsify hash route does not resolve to an existing markdown file"))
                continue
            if sub_fragment:
                if target_file not in anchor_cache:
                    anchor_cache[target_file] = find_anchors_in_file(target_file)
                if sub_fragment not in anchor_cache[target_file]:
                    # Note: We emit warning or flag if anchor missing
                    broken.append((line_num, raw_url, f"Anchor '#{sub_fragment}' not found in {target_file.name}"))
            continue

        # Case 2: Pure in-page anchor fragment (e.g. #term-telemetry_stream or #overview)
        if raw_url.startswith("#") and not raw_url.startswith("#/"):
            anchor_name = raw_url.lstrip("#")
            if md_file not in anchor_cache:
                anchor_cache[md_file] = find_anchors_in_file(md_file)
            if anchor_name not in anchor_cache[md_file]:
                broken.append((line_num, raw_url, f"In-page anchor '#{anchor_name}' not found in {md_file.name}"))
            continue

        # Case 3: Relative file path (e.g. 'narrative/01-chapter-sample.md' or '../assets/style.css')
        if url_path:
            # Check relative to current file's directory
            candidate_local = (md_file.parent / url_path).resolve()
            # Also check relative to root directory
            candidate_root = (root_dir / url_path.lstrip("/")).resolve()

            target_resolved = None
            if candidate_local.exists():
                target_resolved = candidate_local
            elif candidate_root.exists():
                target_resolved = candidate_root

            if target_resolved is None:
                broken.append((line_num, raw_url, f"Target file does not exist (checked {candidate_local} and {candidate_root})"))
                continue

            # If anchor is present on the target file
            if fragment and target_resolved.suffix == ".md":
                if target_resolved not in anchor_cache:
                    anchor_cache[target_resolved] = find_anchors_in_file(target_resolved)
                if fragment not in anchor_cache[target_resolved]:
                    broken.append((line_num, raw_url, f"Anchor '#{fragment}' not found in target file {target_resolved.name}"))

    return broken


def main():
    # Base directory to check defaults to template root (parent of tools/)
    script_dir = Path(__file__).resolve().parent
    template_root = script_dir.parent

    if len(sys.argv) > 1:
        target_dir = Path(sys.argv[1]).resolve()
    else:
        target_dir = template_root

    print(f"\n{BOLD}{CYAN}=== LNK Link Validator (Zero-Dependency) ==={RESET}")
    print(f"Target Directory: {target_dir}\n")

    md_files = list(target_dir.rglob("*.md"))
    if not md_files:
        print(f"{YELLOW}No Markdown files found in {target_dir}{RESET}")
        sys.exit(0)

    anchor_cache = {}
    total_files = len(md_files)
    total_broken = 0
    checked_count = 0

    for md_file in sorted(md_files):
        # Exclude .git or node_modules if present
        if any(part.startswith(".") and part != "." for part in md_file.parts):
            continue

        rel_path = md_file.relative_to(target_dir)
        broken = validate_file(target_dir, md_file, anchor_cache)
        checked_count += 1

        if broken:
            total_broken += len(broken)
            print(f"{RED}[FAIL]{RESET} {BOLD}{rel_path}{RESET}")
            for line_num, link, reason in broken:
                print(f"  {RED}-> Line {line_num}:{RESET} {link} ({YELLOW}{reason}{RESET})")
        else:
            print(f"{GREEN}[OK]{RESET}   {rel_path}")

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    print("\n" + "=" * 50)
    if total_broken == 0:
        print(f"{GREEN}{BOLD}[PASS] SUCCESS:{RESET} All relative links and anchors in {checked_count} files are 100% valid!\n")
        sys.exit(0)
    else:
        print(f"{RED}{BOLD}[FAIL] FAILED:{RESET} Found {total_broken} broken link(s) across {checked_count} file(s).\n")
        sys.exit(1)


if __name__ == "__main__":
    main()

