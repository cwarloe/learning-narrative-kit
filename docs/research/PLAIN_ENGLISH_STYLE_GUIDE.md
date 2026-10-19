# Plain-English & Learner Experience Style Guide
**Repository:** `learning-narrative-kit`  
**Target Audience:** U.S. high-school graduates, career switchers, and entry-level IT/SOC practitioners.

---

## 1. The Core Philosophy: Shop-Floor Reality Over Academic Theory

Portland Desk and all LNK courseware must sound like a real workplace, written in standard, clear, spoken American English. 

Learners are here to learn how to diagnose broken machines and solve security incidents—not study educational psychology, instructional design frameworks, or software architecture abstractions.

### The Golden Rule
> **If a term would not be said out loud by an experienced bench tech, a frantic warehouse supervisor, or an exhausted junior technician on a graveyard shift, it does NOT belong in the courseware.**

---

## 2. Forbidden Terminology & Plain-English Replacements

The following internal, academic, instructional design, and software-architect terms are strictly banned from all learner-facing materials:

| Banned Term | Why It Fails | Plain-English Replacement |
| :--- | :--- | :--- |
| **"Invariant" / "Invariants"** | Academic math/software architecture jargon. Confuses beginners; not standard IT shop language. | **"Core building blocks"**, **"core parts"**, **"unbreakable rules"**, **"strict, fixed borders"**. |
| **"Falsifiable hypothesis"** | Formal scientific/epistemological jargon. Creates test anxiety. | **"Testable prediction"**, **"Call your shot"**, **"Prediction you can test"**. |
| **"Falsifiable verification test"** | Stiff academic language. | **"Verification test"**, **"Test to prove it"**, **"Test how you'll confirm it"**. |
| **"Rubric" / "Evaluation rubric"** | Sounds like high school or university grading bureaucracy. | **"Scoring standards"**, **"Passing criteria"**, **"What good looks like"**, **"Lead sign-off checklist"**. |
| **"Pedagogy" / "Pedagogical"** | Instructional design theory. Completely alien to a help desk tech. | **"How you learn"**, **"training method"**, **"practice progression"** (or omit entirely). |
| **"Heuristic"** (in general prose) | Cognitive science jargon. | **"Rule of thumb"**, **"troubleshooting shortcut"**, **"decision guide"**. *(Note: Preserve only when referring specifically to antivirus behavioral detection on the CompTIA Security+ exam, explained as "behavior-based detection (heuristics)").* |
| **"Diagnostic drill"** | Military / academic jargon. | **"Quick check"**, **"skill rep"**, **"try it yourself"**, **"practice rep"**. |
| **"Substantive schema"** | Cognitive psychology jargon. | **"Mental model"**, **"understanding how the machine actually works"**. |
| **"Formative / Summative"** | Educational testing jargon. | **"Practice checks"** vs **"Final challenge"**. |

---

## 3. High-School Graduate Readability Standard

1. **Vocabulary Introduced In Context (In the Flow of Work):**
   When technical terms (such as `MAC address`, `IP address`, `default gateway`, `subnet mask`, or `POST code`) are introduced, Ethan must encounter them *on the job, during an active incident*.
   - Never halt the story for a dry academic lecture or dictionary definition.
   - Ground the concept immediately in physical, real-world analogies:
     - *MAC Address:* "The factory serial number stamped into the metal at the factory. Never changes."
     - *IP Address:* "The temporary apartment number you get assigned when you move in. Changes when you change rooms."
     - *Port Number:* "The room number inside the apartment. Directs mail to the specific tenant."
     - *Default Gateway:* "The door leading out to the street. If that door is locked, you can talk to your roommates, but you can't reach the outside world."
2. **Cadence and Voice:**
   - First-person past tense ("I traced the cable...", "Ken stepped behind me...").
   - Mean sentence length: 16–20 words.
   - Zero AI-generated staccato bullet-point summaries inside prose. Complete, grounded sentences reflecting authentic physical work.
   - Authentic sensory details: damp concrete, hydraulic oil, buzzing metal-halide lamps, cold coffee, bleeding knuckles, and fan whine.
