# Learning Narrative Kit (LNK) Starter Template

> **Story-First Pedagogy meets Technical Mastery.**  
> A zero-build, battle-tested Docsify shell for creating dual-track educational curricula in any domain.

---

## Welcome to the LNK Architecture

Traditional technical education suffers from two opposite failure modes:
1. **The Vocabulary Parade:** Endless abstract definitions, slides, and flashcards disconnected from real operational friction.
2. **The Unguided Sandbox:** Exercises where learners blindly follow cookbook steps without developing analytical mental models.

The **Learning Narrative Kit (LNK)** solves this through a **dual-track architecture**:

```
+-------------------------------------------------------------------------+
|                        LEARNING NARRATIVE KIT                           |
+-------------------------------------------------------------------------+
|                                                                         |
|   [ TRACK 1: NARRATIVE (STORY) ]     --->    [ TRACK 2: WORKBENCH ]     |
|   - Real-world high-stakes tension            - Mathematical heuristics |
|   - 3-Beat Pedagogical Engine                 - Interactive micro-drills|
|   - [[term_id|Marked terms]] on friction      - "Commit Before Inspect" |
|   - Interactive Bridge Cards                  - Verifiable deliverables |
|                                                                         |
+-------------------------------------------------------------------------+
|   [ UNIVERSAL ZERO-BUILD SHELL ]                                        |
|   - High-contrast responsive dark theme (#0f172a / #1e293b)             |
|   - KaTeX math support ($...$ and $$...$$)                              |
|   - Dual-track mode switcher (Curriculum, Story, Workbench)             |
|   - Docked right glossary drawer with live search & bidirectional sync  |
|   - Instant deployment to GitHub Pages with 0 build steps               |
+-------------------------------------------------------------------------+
```

---

## The Dual-Track Curriculum at a Glance

| Unit | Track 1: Narrative Chapter (Story) | Track 2: Technical Workbench (Practice) | Primary Concepts |
|:---|:---|:---|:---|
| **01** | [Chapter 01: When the Queue Stood Still](narrative/01-chapter-sample.md) | [Workbench 01: Circuit Breakers & Backpressure](workbench/01-workbench-sample.md) | [[circuit_breaker\|Circuit Breakers]], [[backpressure\|Backpressure]], [[telemetry_stream\|Telemetry]] |

---

## Core Pedagogical Mechanisms

### 1. The Three-Beat Pedagogical Engine
Every narrative chapter in LNK follows a strict 3-beat rhythm:
- **Beat 1: Goal:** What does the character urgently need to accomplish in the next ten minutes?
- **Beat 2: Complication:** The intuitive or obsolete habit meets reality. **Marked technical terms sit here.**
- **Beat 3: Pivot:** The replacement decision and what it costs in trade-offs. **Marked technical terms sit here.**

### 2. "Commit Before You Inspect" Prediction Gates
In the Workbench track, learners are never shown answers passively. Through interactive `<details class="reveal-gate">` containers, learners are forced to write down:
1. Current Explanation
2. Evidence Basis
3. Material Assumption
4. 3-Part Observable Prediction (Direction, Kind, Condition)
5. Falsification Condition

Only after committing do they reveal the simulated or real telemetry.

### 3. Ambient Interrupt Literacy
Terms are authored as `[[term_id|Surface Text]]`. Hovering displays a concise definition and operational context without breaking reading flow. Clicking any term opens the docked right glossary drawer with bidirectional gliding.

---

## Quick Start (Zero Build Required)

This repository is **100% static**. There are no webpack, node_modules, or compiler dependencies required to view or publish it.

### Option A: Python Built-In Server
```bash
# From inside the template/ directory:
python3 -m http.server 3000
# Open http://localhost:3000 in your browser
```

### Option B: Docsify CLI
```bash
# If you have Node.js installed:
npx docsify-cli serve .
```

### Option C: Instant GitHub Pages Deploy
1. Push this folder to a GitHub repository.
2. In GitHub repository settings, go to **Pages**.
3. Set Source to **Deploy from a branch**, select branch `main`, folder `/` (or `/docs`), and save.
4. Your interactive curriculum is live worldwide in under 60 seconds!

---

## Validating Your Links

Before publishing, verify all relative markdown and asset links using the built-in zero-dependency validator:

```bash
python tools/check-links.py
```

---

## Authoring Guide

To adapt this template to your company, university, or technical course, read the complete [Template Authoring Guide](TEMPLATE_GUIDE.md).
