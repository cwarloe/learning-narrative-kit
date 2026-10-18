# Learning Narrative Kit (LNK) — Template & Authoring Guide

> **A Universal, Zero-Build Framework for Operational Story-First Technical Learning.**  
> Package high-stakes narrative immersion and rigorous hands-on engineering practice into an instant, static web platform.

---

## 1. What is the Learning Narrative Kit?

The **Learning Narrative Kit (LNK)** is an open architecture for technical education derived from battle-tested instructional engineering at scale. It replaces fragmented slides, dry documentation, and ungrounded flashcards with a cohesive **dual-track system**:

```
                     ┌────────────────────────────────┐
                     │    LEARNING NARRATIVE KIT      │
                     └───────────────┬────────────────┘
                                     │
            ┌────────────────────────┴────────────────────────┐
            ▼                                                 ▼
┌──────────────────────┐                           ┌──────────────────────┐
│   NARRATIVE TRACK    │  ==== [ Bridge Card ] ==> │   WORKBENCH TRACK    │
│       (Story)        │                           │      (Practice)      │
├──────────────────────┤                           ├──────────────────────┤
│ • Human tension      │                           │ • Concrete formulas  │
│ • 3-Beat Engine      │                           │ • Micro-drills       │
│ • [[term_id]] marks  │                           │ • Prediction gates   │
│ • Friction decisions │                           │ • Scored deliverables│
└──────────────────────┘                           └──────────────────────┘
            │                                                 │
            └────────────────────────┬────────────────────────┘
                                     │
                                     ▼
                     ┌────────────────────────────────┐
                     │   STANDALONE ZERO-BUILD SHELL  │
                     │  (Docsify + KaTeX + Prism)     │
                     └────────────────────────────────┘
```

### The Core Pedagogical Axioms
1. **The narrative is the primary learning object.** The vocabulary gains its meaning from the operational crisis and human decisions in the story.
2. **The habit is the complication; the replacement is the pivot.** People arrive carrying what they learned at old shops; the lesson is negotiating that habit into a new, disciplined decision.
3. **Commit before you inspect.** Learners predict observable outcomes in writing before revealing answers, eliminating hindsight bias.
4. **Zero-build accessibility.** No complex Node pipelines or toolchains; any author can clone, edit Markdown, and deploy instantly to GitHub Pages.

---

## 2. Template Directory Structure

The starter template is organized cleanly into four functional areas:

```
template/
├── index.html                 # Standalone Docsify shell, KaTeX, Prism, & plugins
├── README.md                  # Course homepage & curriculum overview
├── _sidebar.md                # Dual-track sidebar navigation
├── TEMPLATE_GUIDE.md          # This authoring manual
├── .nojekyll                  # Bypasses Jekyll on GitHub Pages
│
├── assets/
│   ├── lnk-theme.css          # High-contrast 2-column dark theme (#0f172a / #1e293b)
│   ├── lnk-shell.js           # Mode switcher, docked glossary drawer, hover popovers
│   └── glossary.json          # Starter domain vocabulary database
│
├── narrative/                 # Track 1: Narrative chapters
│   └── 01-chapter-sample.md   # Specimen 3-beat chapter with bridge card
│
├── workbench/                 # Track 2: Technical exercises
│   └── 01-workbench-sample.md # Specimen workbench with prediction gates & rubric
│
└── tools/
    └── check-links.py         # Zero-dependency relative link & anchor validator
```

---

## 3. Step-by-Step Customization Workflow

Follow these six steps to adapt this template to any engineering, data, healthcare, or business domain:

### Step 1: Branding & Metadata Configuration
1. Open `index.html`:
   - Update `<title>` and `<meta name="description">`.
   - In `$docsify`, update `name` to your course title (e.g., `"Cloud Resilience Academy"`).
   - If using a GitHub repository, set `repo: 'https://github.com/your-org/your-repo'`.
2. Open `README.md` and customize the course title, lead summary, and target competencies.
3. Open `_sidebar.md` and adjust the table of contents.

### Step 2: Establish Your Domain Vocabulary (`assets/glossary.json`)
Every term marked in prose must exist in `assets/glossary.json`.

```json
{
  "circuit_breaker": {
    "title": "Circuit Breaker Pattern",
    "category": "architecture",
    "definition": "A defensive design pattern that automatically halts outbound calls to a failing remote dependency once an error threshold is crossed.",
    "context": "Prevents catastrophic cascading failures across microservices during network partition events."
  }
}
```

#### Glossary Schema Guidelines
- **`title`**: Canonical display title shown in the tooltip and drawer.
- **`category`**: Category tag for filtering (e.g. `telemetry`, `architecture`, `analytical`, `pedagogy`, `transport`, `security`, `finance`).
- **`definition`**: 1–2 punchy, exact sentences explaining the concept.
- **`context`**: *(Optional)* An operational nuance or desk translation clarifying how practitioners think about it.

### Step 3: Authoring Narrative Chapters (`narrative/`)
Create chapters named `01-<slug>.md`, `02-<slug>.md`, etc.

#### The 3-Beat Pedagogical Engine
Structure every chapter into three clear beats:
1. **Beat 1: Goal.** What does the protagonist urgently need to accomplish in the next ten minutes? *(Keep terms out of setup; setup is just human motivation).*
2. **Beat 2: Complication.** What intuitive move, obsolete habit, or friction makes the obvious path fail? **Place marked terms here.**
3. **Beat 3: Pivot.** What gets decided, what replaces the habit, and **what does it cost**? **Place marked terms here.**

#### Marking Prose
Mark technical terms in Markdown prose using the double bracket syntax:
```markdown
Elena ran an emergency query across the [[telemetry_stream|incoming telemetry stream]], 
noticing that the [[cardinality|field cardinality]] on tenant IDs had spiked.
```

#### Scene Artifacts
Use fenced code blocks or HTML cards to show what characters are staring at:
- **Incident Tickets**: `<div class="ticket-chrome"><div class="ticket-bar"><span class="ticket-id">INC-101</span>...</div>...</div>`
- **Terminals**: `<div class="console-body"><span class="cmd">$ kubectl logs ...</span></div>`

#### The Curriculum Bridge Card
Every narrative chapter **must** end with a `.bridge-card` linking directly to its companion workbench:
```html
<div class="bridge-card">
  <div class="bridge-label">Companion Workbench Exercise</div>
  <div class="bridge-title">Workbench 01 — Circuit Breakers & Backpressure Dynamics</div>
  <p class="bridge-desc">Apply Elena's decision in a hands-on sandbox: calculate saturation limits and complete the prediction gate.</p>
  <a href="#/workbench/01-workbench-sample" class="bridge-btn">Open Workbench 01 Practice →</a>
</div>
```

### Step 4: Authoring Technical Workbenches (`workbench/`)
Workbenches translate narrative intuition into rigorous muscle memory. Every workbench includes:
1. **At a Glance Card:** Target capabilities, time required, prerequisite links, and workbench tool requirements.
2. **Technical Heuristics:** Mathematical formulas (using KaTeX `$L = \lambda \cdot W$`), terminal commands, or protocol structures.
3. **Interactive Micro-Drills:** 15-second scenario discrimination checks using `<details class="reveal-gate">`.
4. **The "Commit Before You Inspect" Prediction Gate:**
   Learners must write down their 5 commitments (Explanation, Evidence, Assumption, 3-Part Prediction, Weakener) before clicking:
   ```html
   <div class="prediction-gate">
     <h4>🔒 Stage 1: Commit Before You Reveal</h4>
     <p>Commit your answers in writing before expanding.</p>
     <details class="reveal-gate">
       <summary>🔓 I Have Written All Commitments — Reveal Telemetry</summary>
       <div class="reveal-content">
         ... evidence and expert debrief ...
       </div>
     </details>
   </div>
   ```
5. **Concrete Deliverable Rubric:** A 1-page spec, architecture diagram, or script the student must produce.
6. **4DX Scorecard Table:** Disciplined metric tracking for individual or cohort accountability.

### Step 5: Validating Links with `check-links.py`
Before publishing or opening a pull request, run:

```bash
python tools/check-links.py
```

The script will scan all Markdown files, verify internal relative links, check Docsify hash paths (`#/narrative/01-...`), and confirm on-page anchor targets.

### Step 6: 1-Click Deployment to GitHub Pages
Because LNK is a zero-build client-side Docsify application, deployment takes 60 seconds:
1. Push your repository to GitHub.
2. Navigate to **Settings → Pages**.
3. Under **Build and deployment**:
   - Source: `Deploy from a branch`
   - Branch: `main`
   - Folder: `/ (root)`
4. Click **Save**. Your site is instantly live!

---

## 4. Authoring Rubric & Quality Gates

| Test | Question to Ask | Pass Criteria |
|:---|:---|:---|
| **The Cover Test** | If you hide all `[[...]]` brackets, does the prose still sound like a smart engineer thinking through a crisis? | Passes if it reads like real work. Fails if it reads like a vocab parade. |
| **The Decision Gate** | Where do marked terms sit? | Must sit at the **Complication** or **Pivot**. Fails if terms only appear in setup or aftermath. |
| **The Friction Test** | Did the protagonist's decision cost something? | A free decision teaches nothing. The pivot must cost time, rework, latency, or an admission. |
| **The Falsification Gate** | Does the workbench prediction specify what proves it wrong? | Must declare observable direction, kind, condition, and a specific falsification trigger. |

---

## 5. Anti-Patterns to Avoid

- **The Vocab Parade:** Introducing 10 terms in two paragraphs without a decision forcing them into conflict.
- **Unverified Numbers:** Inventing random metrics. If you say a worker was processing 42,000 events/sec, ensure the math across Little's Law checks out.
- **The Free Lunch Solution:** Characters implementing an architecture change with zero trade-offs or operational costs.
- **Passive Reveals:** Putting terminal logs in the workbench without requiring learners to commit to a prediction first.
