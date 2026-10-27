#!/usr/bin/env python3
"""Build the comprehensive Master Technical Glossary for Portland Desk.

Reads docs/portland-desk/assets/glossary.json and generates docs/portland-desk/glossary.md
with searchable, categorized, anchorable entries. docs/portland-desk/ is the only copy
(the root portland-desk/ duplicate is archived), so nothing is written outside it.
"""

import json
from pathlib import Path

KIT_ROOT = Path(__file__).resolve().parent.parent
GLOSSARY_JSON = KIT_ROOT / "docs" / "portland-desk" / "assets" / "glossary.json"
TARGET_DOCS = KIT_ROOT / "docs" / "portland-desk" / "glossary.md"

def build_glossary():
    if not GLOSSARY_JSON.exists():
        raise FileNotFoundError(f"Missing {GLOSSARY_JSON}")

    with open(GLOSSARY_JSON, "r", encoding="utf-8") as f:
        terms_dict = json.load(f)

    # Sort terms by title (case-insensitive)
    sorted_terms = sorted(terms_dict.values(), key=lambda t: t.get("title", t["id"]).lower())

    # Collect alphabet letters
    letters = sorted(list(set(t.get("title", t["id"])[0].upper() for t in sorted_terms if t.get("title", t["id"])[0].isalpha())))

    md = []
    md.append("# Master Technical Glossary & Domain Reference\n")
    md.append("*Comprehensive Tier 1 IT Support & Security Operations Reference • CompTIA A+, Network+, and Security+ Alignments*\n")
    md.append("> [!TIP]\n")
    md.append("> Use **Ctrl+F** to search instantly, or click a letter below to jump directly to a concept section. Clicking any highlighted term in an incident narrative or hands-on lab navigates directly to its entry below.\n\n")

    # Letter jump index
    md.append("### Alphabetical Index\n\n")
    letter_links = [f"[{letter}](#{letter.lower()})" for letter in letters]
    md.append(" · ".join(letter_links) + "\n\n---\n\n")

    # Group by first letter
    current_letter = ""
    for term in sorted_terms:
        title = term.get("title", term["id"])
        first_char = title[0].upper() if title[0].isalpha() else "#"

        if first_char != current_letter:
            current_letter = first_char
            md.append(f"## {current_letter}\n\n")

        tid = term["id"]
        category = term.get("category", term.get("tier", "telemetry")).upper()
        definition = term.get("definition", "").strip()
        context = term.get("context", "").strip()
        refs = term.get("refs", [])
        tags = term.get("tags", [])

        md.append(f'<div class="glossary-entry-card" id="term-{tid}">\n\n')
        md.append(f'### {title} <span class="glossary-card-badge">{category}</span>\n\n')
        if definition:
            md.append(f"**Definition:** {definition}\n\n")
        if context:
            md.append(f"**Operational Context:** *{context}*\n\n")
        if refs:
            md.append("**Certification & Domain Reference:**\n")
            for r in refs:
                md.append(f"- {r}\n")
            md.append("\n")
        if tags:
            tag_badges = " ".join([f"`#{tag}`" for tag in tags])
            md.append(f"**Tags:** {tag_badges}\n\n")
        md.append("</div>\n\n---\n\n")

    content = "".join(md)

    TARGET_DOCS.parent.mkdir(parents=True, exist_ok=True)
    TARGET_DOCS.write_text(content, encoding="utf-8")
    print(f"Wrote {len(sorted_terms)} terms to {TARGET_DOCS}")

if __name__ == "__main__":
    build_glossary()
