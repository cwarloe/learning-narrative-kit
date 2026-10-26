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


## 2. The Story-to-Lab Model (decision of Charles, 2026-10-26)

This model replaces the four gated handoff models (Parallel Ticket, Cliffhanger Handoff, Co-Pilot, and Incident Commander) that used to sit in this section. Nothing in the story is held back to protect the lab.

1. **The chapter is a complete story.** Write each chapter as the best standalone story it can be. It may end on a cliffhanger or not, as the story needs. It may, and usually will, show Ethan finding and applying the answer, and it shows what the fix cost.
2. **The lab opens with a worked example of the same incident.** The worked example is exactly the incident Ethan worked in the chapter, with the solution known, walked through step by step as training and demonstration. This is the Worked Example Effect (Sweller): the learner studies a solved problem before solving one.
3. **The lab then practices the steps.** The reference material, drills, ticket notes, and checklist sections practice the steps of the worked example.
4. **The lab ends with one transfer problem.** The transfer problem works on the same principle as the incident but looks different on the surface: a different device, user, symptom, or setting.
5. **No "what would you do" handoffs before training.** Neither the chapter nor the lab asks the learner to solve the incident before the worked example has shown how.
6. **No lab epilogues and no story Easter eggs.** Everything that matters to the story, including every cost, lives in the chapter. A lab may refer to the story ("as Ethan found on Line 4") to aid learning, but it holds no story content the chapter lacks.

The phases (Phase 1 is Ep 00 to 02, Phase 2 is Ep 03 to 06, Phase 3 is Ep 07 to 10, and Phase 4 is Ep 11 to 12) now describe only how much support the drills and the transfer problem give. Phase 1 transfer problems come with more hints. Phase 4 transfer problems give the learner only the scenario.

> **Terms.** "Phase" means a level of lab support. "Act" means story structure only, and the acts are defined in `PORTLAND_TIMELINE.md`.

---

## 3. Authoring Checklist for Content Creators
1. **Write the chapter to the end of the incident.** Do not stop the prose to protect a lab answer.
2. **Mentors may give rules of thumb or answers,** as a real lead would. Jules is still a working lead, not an oracle.
3. **The worked example must match the story exactly.** Hostnames, IP addresses, error codes, and symptoms in the lab must match what Ethan saw.
4. **The transfer problem must share the principle, not the surface.**
5. **Costs and consequences belong in the chapter.** If a cost exists only in a lab, it does not count.

