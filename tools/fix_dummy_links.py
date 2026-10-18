from pathlib import Path
import re

for base_dir in [Path('portland-desk'), Path('docs/portland-desk')]:
    if not base_dir.exists():
        continue
    for md_file in base_dir.rglob('*.md'):
        content = md_file.read_text(encoding='utf-8')
        # Replace [`xxx`](#) with `xxx`
        new_content = re.sub(r'\[`([^`]+)`\]\(#\)', r'`\1`', content)
        # Also check for [xxx](#)
        new_content = re.sub(r'\[([^\]]+)\]\(#\)', r'\1', new_content)
        if new_content != content:
            md_file.write_text(new_content, encoding='utf-8')
            print(f"Cleaned (#) in {md_file}")

print("Done cleaning dummy anchors.")
