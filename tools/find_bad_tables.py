import glob, re
from pathlib import Path

for f in sorted(glob.glob('docs/portland-desk/**/*.md', recursive=True)):
    with open(f, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
    
    for i in range(1, len(lines)):
        line = lines[i]
        # Check if line is a table delimiter
        if re.match(r'^\s*\|?\s*[-:]+[-| :]+\s*\|?\s*$', line):
            header = lines[i-1]
            if '|' in header:
                # header is a table row. check line before header
                if i >= 2:
                    before_header = lines[i-2]
                    if before_header.strip() and not before_header.strip().startswith('#') and not before_header.strip().startswith('---'):
                        print(f"{f}:{i} Table '{header.strip()[:35]}' preceded by text: '{before_header.strip()[:35]}'")
