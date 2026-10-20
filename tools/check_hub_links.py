from pathlib import Path
import re

html_path = Path('docs/index.html')
content = html_path.read_text(encoding='utf-8')
links = re.findall(r'href=["\']([^"\']+)["\']', content)

print(f"Total links found in docs/index.html: {len(links)}")
broken = 0
for l in links:
    if l.startswith('http') or l.startswith('#'):
        continue
    target = l.split('#')[0]
    full_target = Path('docs') / target
    if not full_target.exists():
        print(f"BROKEN: {l} -> {full_target}")
        broken += 1
    else:
        # print(f"OK: {l}")
        pass

if broken == 0:
    print("ALL internal relative links in docs/index.html are 100% VALID!")
else:
    print(f"Found {broken} broken links.")
