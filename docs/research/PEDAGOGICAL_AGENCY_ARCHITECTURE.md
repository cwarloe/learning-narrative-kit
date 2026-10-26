# Pedagogical Agency Architecture: Resolving the "Already Solved" Dilemma
**Repository:** `learning-narrative-kit`  
**Theoretical Anchor:** Collins, Brown, & Holum's Cognitive Apprenticeship Model & Constructivist Whole-Task Learning (4C/ID)

---

## 1. The Core Tension: Dramatic Fallacy vs. Passive Playback

In narrative-driven technical courseware, there is a fundamental clash between **Classical Fiction Storytelling** and **Constructivist Learning**:

1. **The Dramatic Fallacy:** In traditional fiction, the reader derives emotional satisfaction from seeing the hero (Ethan) face an impossible obstacle, synthesize clues, apply cleverness, and triumph through his own agency.
2. **The Pedagogical Fallacy (Passive Playback):** If Ethan solves the entire incident in the story text (isolating the bad RAM, running the CLI fix, and getting praised by his boss) *before* the learner opens the lab, **the cognitive mystery is dead**. The learner's dopamine of discovery has already been spent vicariously on Ethan. The lab becomes a compliance chore—what video game designers call *"quick-time event typing"*.
3. **The Cognitive Overload Trap:** Conversely, dropping a raw career-switcher directly into an open-ended terminal failure without prior modeling triggers panic and paralysis.

---

> **Terms.** "Phase" means one of the four story-to-lab handoff models below. "Act" means story structure only, and the acts are defined in `PORTLAND_TIMELINE.md`. The two do not line up one to one.

## 2. The Solution: The "Dynamic Fading Apprenticeship" (4-Phase Arc)

Using any single narrative pattern across all 13 modules causes learner fatigue (13 cliffhangers feels like a soap opera; 13 parallel tickets feels like double homework).

Instead, we align the relationship between story and lab to the **Cognitive Apprenticeship progression**:
$$\text{Modeling} \longrightarrow \text{Scaffolding} \longrightarrow \text{Coaching} \longrightarrow \text{Fading} \longrightarrow \text{Independent Mastery}$$

```
┌─────────────────────────────────────────────────────────────────────────────────────────┐
│                      THE 13-EPISODE NARRATIVE & AGENCY PROGRESSION                      │
├───────────────────┬──────────────────────┬──────────────────────────────────────────────┤
│ Progression       │ Structural Model     │ Narrative & Learner Dynamic                  │
├───────────────────┼──────────────────────┼──────────────────────────────────────────────┤
│ Phase 1 (Ep 00–02)│ Symmetrical Ticket   │ MODELING: Ethan works Case A in full story.  │
│ The Greenhorn     │ (Isomorphic Case)    │ Parallel Ticket B drops on queue for learner │
│                   │                      │ with the same core failure mode but different clues. │
├───────────────────┼──────────────────────┼──────────────────────────────────────────────┤
│ Phase 2 (Ep 03–06)│ Cliffhanger Handoff  │ SCAFFOLDING: Story breaks at the Crucible.   │
│ In the Trenches   │ (The Interleaved Cut)│ Ethan is STUCK. Learner solves it in lab.    │
│                   │                      │ Part 2 story resumes with fallout & debrief. │
├───────────────────┼──────────────────────┼──────────────────────────────────────────────┤
│ Phase 3 (Ep 07–10)│ Co-Pilot / Dispatch  │ DISTRIBUTED COGNITION: Ethan is on the floor │
│ The Outages       │ (Radio Dispatcher)   │ with cables; learner is at the NOC console   │
│                   │                      │ running remote diagnostics & directing him.  │
├───────────────────┼──────────────────────┼──────────────────────────────────────────────┤
│ Phase 4 (Ep 11–12)│ Clinical CPC / Lead  │ FADING TO MASTERY: Full triage matrix, multi-│
│ Capstone Mastery  │ Incident Commander   │ stage kill-chain, and formal CSIRT handoff.  │
└───────────────────┴──────────────────────┴──────────────────────────────────────────────┘
```

---

## 3. Detailed Anatomy of the Four Models

### Model 1: The Symmetrical Parallel Ticket (Phase 1: Episodes 00–02)
* **How It Works:** Ethan diagnoses Case A in the narrative prose. The learner observes his mental model, how he formulates a testable prediction, and how he avoids panic.
* **The Handoff:** Just as Case A is resolved, a second ticket (Ticket B) lands on the Portland help desk queue. It shares the exact same core failure mode (e.g., an unseated expansion card or power rail drop) but with different surface symptoms.
* **Why It Works for Novices:** Maximum safety and zero test anxiety. Leverages Sweller's **Worked Example Effect**.

### Model 2: The Interleaved Cliffhanger Handoff (Phase 2: Episodes 03–06)
* **Part 1 (The Inciting Incident & The Wall):** Ethan encounters an ambiguous ticket under heavy business pressure. Standard textbook steps fail. His supervisor drops a rule of thumb, not the answer. Ethan is paralyzed by conflicting telemetry.
* **The Handoff Gate:** The prose halts at peak suspense:  
  > *"The conveyor is cold, Ken is counting trailers, and the scale is streaming corrupted bytes. Step up to Station 01 on the Workbench. Match the clock divider and prove the fix before the 05:00 AM dispatch."*
* **The Workbench Lab:** The learner enters the lab, uses the interactive terminal, runs the diagnostics, and finds the root cause.
* **Part 2 (The Shift Resolution & Epilogue):** Placed at the end of the lab (Section 6), the learner unlocks the story's resolution: Ethan executes the verified fix and pays a realistic cost for it. The learner's satisfaction comes from solving it in the lab, not from a clean ending for Ethan (decision of 2026-10-26).

### Model 3: The Co-Pilot / Radio Dispatcher (Phase 3: Episodes 07–10)
* **The Dynamic:** Distributed cognition. Ethan is physically on the floor (in the unventilated wiring closet, under a desk, or in the warehouse annex with cables and a flashlight). The learner sits at the central console.
* **The Interaction Loop:** Ethan reports physical observations ("Link light is amber, fan is screaming at 100%"); the learner runs the remote CLI diagnostics (`netstat`, `nmap`, Event Viewer) and directs the physical remediation.

### Model 4: The Incident Commander / Clinical CPC (Phase 4: Episodes 11–12)
* **The Dynamic:** Modeled after the New England Journal of Medicine clinicopathological conference.
* **The Flow:** Ethan and the learner act as lead investigators assembling a multi-stage forensic dossier: preserving volatile order, calculating SHA-256 evidence hashes, and presenting a formal handoff to Senior CSIRT.

---

## 4. Authoring Checklist for Content Creators
1. **Never write past the turning point in Part 1** of a Cliffhanger episode. Leave the mystery open.
2. **Mentors offer rules of thumb, never solutions.** Jules Brooks is a compass, not a cheat sheet.
3. **The Lab must match the story state exactly.** Hostnames, IP addresses, error codes, and symptoms in the interactive terminal must match what Ethan observed in the prose.
4. **Epilogues explore human consequences, not mechanics.** Show user gratitude or pushback, supervisor feedback, documentation hygiene, and what the fix cost Ethan or someone else (see `docs/craft/learning-narrative-framework.md`).
