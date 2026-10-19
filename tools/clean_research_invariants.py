import os

base_dir = "C:/Users/charl/learning-narrative-kit"
files = [
    os.path.join(base_dir, 'docs/research/PORTLAND_AUTHOR_BIBLE.md'),
    os.path.join(base_dir, 'docs/research/PORTLAND_CURRICULUM_PLAN.md'),
    os.path.join(base_dir, 'docs/research/PEDAGOGICAL_AGENCY_ARCHITECTURE.md')
]

reps = [
    ('Green Band (The Physical Invariants):', 'Green Band (The Physical Building Blocks):'),
    ('understanding the physical invariants', 'understanding the physical building blocks'),
    ('its 4 invariant components', 'its 4 core components'),
    ('Machine Invariants,', 'Core Machine Building Blocks,'),
    ('Machine Invariants):', 'Core Machine Building Blocks):'),
    ('Architectural Invariants', 'Core Machine Principles'),
    ('4 Invariants of Computing:', '4 Core Building Blocks of Computing:'),
    ('physical and logical invariants', 'physical and logical fundamentals'),
    ('The 4 Machine Invariants', 'The 4 Machine Building Blocks'),
    ('with the same invariant but different clues', 'with the same core failure mode but different clues')
]

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        txt = f.read()
    for old, new in reps:
        txt = txt.replace(old, new)
    with open(p, 'w', encoding='utf-8') as f:
        f.write(txt)
    print(f'Cleaned {p}')
