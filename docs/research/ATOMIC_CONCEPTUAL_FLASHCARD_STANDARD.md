# Atomic Conceptual Flashcard Standard (The Goldilocks Specification)

**Project:** Portland Desk / Learning Narrative Kit (LNK)  
**Document Purpose:** Cognitive Science & Research-Backed Specification for Courseware Flashcard Design  
**Governing Research:** Cognitive Load Theory (Sweller), Minimum Information Principle (Wozniak), The Testing Effect (Roediger & Karpicke), Conceptual vs. Detail Card Efficacy Studies  
**Status:** Approved Pedagogical Standard  

---

## 1. Executive Summary & Core Philosophy

Flashcards in technical education fail when they fall into two traps:
1. **The "Too Simple" Trap (Term-and-Definition):** Rote memorization of glossary definitions (`"What is DVI-I?"`). Students memorize surface text without understanding how or when to apply it.
2. **The "Too Long" Trap (Wall of Text / Story Recitation):** Dumping multi-sentence paragraphs, historical trivia, full code blocks, or narrative plot dialogue onto the back of a card. Students skim, fool themselves into thinking they knew it, and fail to build retrieval pathways.

**The Solution: The "Goldilocks" Atomic Conceptual Card.**
Cards must test **one single abstract invariant or decision boundary** in a way that takes **under 10 seconds to read aloud**.

---

## 2. The 4 Core Research Rules

### Rule 1: The "One Idea, Under 10 Seconds" Rule
* **Minimum Information Principle:** Every card tests strictly **one idea** or decision boundary.
* **The 10-Second Audit:** Read the answer out loud. If it takes longer than 10 seconds to say at conversational speed, the card is overloaded.
* **The Triad Architecture:** Complex technical topics must never be condensed into one mega-card. Instead, break them into a **Triad of 3 Atomic Cards**:
  1. **The Invariant / Cause Card:** Why the physical or protocol phenomenon happens.
  2. **The Comparison / Boundary Card:** How it contrasts with its closest confusing alternative (e.g., DVI-I vs DVI-D, TCP RST vs Drop).
  3. **The Edge Case / Trap Card:** The specific failure state, diagnostic indicator, or CompTIA exam trap.

---

### Rule 2: Upgraded Question Prompts ("How/Why" & Boundary Decisions)
Students studying conceptual prompt cards score significantly higher than those studying definition cards. All flashcard questions must fit into one of three prompt templates:

| Prompt Template | Bad (Rote / Wall of Text) | Goldilocks Atomic Conceptual Card |
| :--- | :--- | :--- |
| **Application & Boundary** *(Yes/No + Why)* | *"What is volatile memory?"* | **Front:** *"Power cuts out during an outage. Does RAM keep its data? (Yes/No and why)"*<br>**Back:** *"No. Dynamic RAM is volatile and requires electrical refresh cycles to hold bits."* |
| **Diagnostic Symptom** *(Tool / Symptom Tell)* | *"What does a fuser do in a laser printer?"* | **Front:** *"Toner smudges off a printed page onto your fingers like loose dust. What part failed?"*<br>**Back:** *"The Fuser Assembly. It didn't reach ~200°C to melt toner resin into the paper fibers."* |
| **Compare & Contrast** *(Single Key Distinction)* | *"List the pinouts and differences between DVI types."* | **Front:** *"A monitor has only VGA analog pins. Which DVI port can drive it with a passive pin adapter?"*<br>**Back:** *"DVI-I (Integrated). Only DVI-I has the 4 analog pins around the flat blade."* |

---

### Rule 3: Keep Narrative Story & Multi-Step Procedures Off the Answer Side
* **Story Disassociation:** Ethan and Jules encounter the problem in the story, but the flashcard **never tests the story's plot or character dialogue**. It tests the abstract engineering invariant so the learner can transfer knowledge to new, unseen jobs.
* **No Procedural Cards:** Never use flashcards to practice multi-step sequences (e.g. 7 steps of CompTIA troubleshooting, writing PowerShell scripts, crimping RJ-45). 
  * *Procedures belong in:* Checklists, worked examples, and interactive lab drills.
  * *Flashcards are strictly for:* Facts, physical boundaries, and decision rules.

---

### Rule 4: System-Level Retrieval Mechanics (Retrieve, Re-Order, Repeat)
* **Pre-Made Authoritative Decks:** Learners spend 80% of their energy making flashcards and only 20% studying them. Our courseware delivers curated, validated conceptual cards ready to study.
* **Active Retrieval Before Flip:** The UI must encourage learners to formulate the answer before flipping (verbalize or commit).
* **Interleaving (Re-Order):** When studying Episode 05, the deck shuffles in 2–3 cards from Episodes 00–04. Interleaving forces the brain to reload schema context and doubles long-term retention.
* **The 3-to-5 Correct Rule:** A card is not mastered upon its first correct answer. It remains in the review rotation until recalled successfully across 3 to 5 separate study sessions.

---

## 3. Agent Ownership & Action Matrix

| Agent Role | Responsibility & Mandate |
| :--- | :--- |
| **Instructional Designer** (`helpdesk_curriculum_designer`) | Authors all flashcards strictly using the **3 Prompt Templates** (Boundary, Diagnostic, Compare) and splits topics into **Triads**. Audits answers against the **10-Second Rule**. |
| **Narrative Author** (`portland_narrative_architect`) | Ensures Ethan's break-room study cards reference real workplace physics without testing story plot or dialogue quotes. |
| **Design Technologist / UI Architect** (`design_technologist`) | Builds UI deck controls: **Interleaving shuffle**, **Say it / Commit gate**, and compact 3x5 high-contrast layouts. |
| **Adversarial Nitpicker** (`technical_nitpicker`) | Verifies that flashcard rules are 100% technically invariant with zero over-simplifications that create bad shop habits. |
