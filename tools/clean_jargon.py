"""Clean L&D and architect jargon from Portland Desk markdown and docs."""

import os

REPLACEMENTS = [
    # Invariants -> Plain English building blocks / core parts
    ("The 4 Invariants of Computing", "The 4 Core Building Blocks of a Computer"),
    ("the 4 Invariants of Computing", "the 4 core building blocks of a computer"),
    ("4 Invariants of Computing", "4 Core Building Blocks of a Computer"),
    ("The Four Invariants Computing Matrix", "The Four Core Computer Systems Matrix"),
    ("The Four Invariants", "The Four Core Building Blocks"),
    ("the four invariants", "the four core building blocks"),
    ("four physical machine invariants", "four physical computer building blocks"),
    ("physical machine invariants", "core physical computer components"),
    ("Computing Invariants Matrix", "Computer Core Systems Matrix"),
    ("computing invariants matrix", "computer core systems matrix"),
    ("Hardware Invariants", "Core Computer Hardware"),
    ("hardware invariants", "core computer hardware"),
    ("The Five Invariant Ground Truths", "The Five Unbreakable Rules"),
    ("the five invariant ground truths", "the five unbreakable rules"),
    ("Five Invariant Ground Truths", "Five Unbreakable Rules"),
    ("Subnet Masks Draw Invariant Bitwise Borders", "Subnet Masks Draw Strict, Fixed Network Borders"),
    ("Subnet Masks Draw Invariant Bitwise Borders<br/>", "Subnet Masks Draw Strict, Fixed Network Borders<br/>"),
    ("1. INVARIANT & SUBSYSTEM ISOLATION (Which invariant is misbehaving?):", "1. SUBSYSTEM ISOLATION (Which core component is failing?):"),
    ("[ ] Invariant 1: COMPUTE", "[ ] Component 1: COMPUTE"),
    ("[ ] Invariant 2: VOLATILE MEMORY", "[ ] Component 2: MEMORY"),
    ("[ ] Invariant 3: NON-VOLATILE STORAGE", "[ ] Component 3: STORAGE"),
    ("[ ] Invariant 4: COMMUNICATION", "[ ] Component 4: COMMUNICATION"),
    ("Invariant 1 (Compute", "Component 1 (Compute"),
    ("Invariant 2/3 (Memory", "Component 2/3 (Memory"),
    ("Invariant 4 (Network", "Component 4 (Network"),
    ("Invariant 4 (Communication", "Component 4 (Communication"),
    ("Invariant 4 / Layer 4", "Component 4 / Layer 4"),
    ("- **Invariant / Layer:**", "- **Failed Component / Layer:**"),
    ("| **1. Invariant Identification** |", "| **1. Component Identification** |"),
    ("which of the 4 invariants has failed", "which of the 4 core components has failed"),
    ("Which invariant is misbehaving?", "Which core component is failing?"),

    # Falsifiable -> Testable / Test to prove it
    ("Formulate a Falsifiable Hypothesis", "Make a Testable Prediction"),
    ("formulate a falsifiable hypothesis", "make a testable prediction"),
    ("Falsifiable Hypothesis", "Testable Prediction"),
    ("falsifiable hypothesis", "testable prediction"),
    ("Falsifiable Verification Test:", "Verification Test (How to prove it):"),
    ("falsifiable verification test", "verification test to prove it"),
    ("Falsifiable Test:", "Test to Prove It:"),
    ("falsifiable test", "test to prove it"),
    ("falsifiable", "testable"),
    ("Falsifiable", "Testable"),

    # Rubric -> Scoring Criteria / Passing Standards
    ("### Part C: Grading & Evaluation Rubric", "### Part C: Scoring & Passing Standards"),
    ("### Part C: Evaluation Rubric", "### Part C: Scoring & Passing Standards"),
    ("### Evaluation Rubric & Criteria", "### Scoring & Passing Standards"),
    ("### Shift Evaluation Rubric", "### Shift Scoring & Passing Standards"),
    ("### Lead Sign-Off Checklist & Evaluation Rubric", "### Lead Sign-Off Checklist & Scoring Standards"),
    ("Use this objective rubric", "Use this objective scoring guide"),
    ("Use this objective scoring rubric", "Use this objective scoring guide"),
    ("rubric to assess", "scoring guide to assess"),
    ("rubric to evaluate", "scoring guide to evaluate"),
    ("scoring rubric", "scoring guide"),

    # Heuristic -> Rule of Thumb / Decision Guide (except malware signature vs heuristic)
    ("### 2.4 The Triage Heuristic: Syllabus Trivia vs. Diagnostic Reality", "### 2.4 The Technician's Filter: Exam Trivia vs. Diagnostic Reality"),
    ("The Triage Heuristic:", "The Rule of Thumb:"),
    ("### Tier 1 Triage Decision Heuristic", "### Tier 1 Triage Decision Guide"),
    ("The \"Magic Number\" Heuristic:", "The \"Magic Number\" Shortcut:"),
]

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    modified = content
    for old, new in REPLACEMENTS:
        modified = modified.replace(old, new)
    
    if modified != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(modified)
        return True
    return False

def main():
    targets = ['portland-desk', 'docs/portland-desk', 'tools/build_hub_index.py']
    count = 0
    for target in targets:
        if os.path.isfile(target):
            if clean_file(target):
                print(f"Cleaned {target}")
                count += 1
        else:
            for root, _, files in os.walk(target):
                for f in files:
                    if f.endswith(('.md', '.html', '.js')):
                        p = os.path.join(root, f)
                        if clean_file(p):
                            print(f"Cleaned {p}")
                            count += 1
    print(f"Total files cleaned: {count}")

if __name__ == '__main__':
    main()
