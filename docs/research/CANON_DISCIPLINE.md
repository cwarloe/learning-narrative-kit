# Canon Discipline & Narrative Grounding Laws
**Project:** Portland Desk (Book 0: Zero-to-One) & Learning Narrative Kit (LNK)  
**Heritage:** Ported and adapted from `novel-builder` (`KERNEL.md`, `VOICE-TELLS.md`, `auditor.system.md`)  
**Status:** Canonical Law for all Authors, Instructional Designers, and Agents  

---

## 1. Executive Mandate

You are building authentic, grounded workplace operational fiction—not sci-fi, not an ARG murder-mystery game, and not an educational cartoon. Ethan Brooks is a tired twenty-year-old dock laborer in an East Portland duplex trying to survive on $14 an hour. He is not a superhero, he does not have innate genius, and he cannot download skills like Neo in *The Matrix*.

The following non-negotiable laws govern all narrative drafting, workbench design, and agent reviews.

---

## 2. The Core Laws

### Law 1: Plausible ≠ Canon (The Anti-Superhero Rule)
> *Default modern life, default history, default family structure, default technical skills are `[UNKNOWN]` until locked. Plausible detail is not canon.*

* **The Rule:** The LLM must never fill gaps with "plausible invention." 
* **Application:** Ethan cannot suddenly possess graphic design skills, advanced scripting abilities, or sophisticated pedagogical theories. If Ethan uses a tool or a structured layout, he must have **acquired it externally**:
  - Found on an old IT forum / Reddit thread.
  - Taught to him on the shop floor by a mentor (Frank, Hank, Jules).
  - Cobbled together from salvaged scrap, manufacturer manuals, or community templates.

### Law 2: Epistemic Leaks Are Banned (POV Horizon Lock)
> *The protagonist cannot know, deduce, or name what they have not yet touched, observed, or been taught.*

* **The Rule:** Authors must never write Ethan with the hindsight of the certification syllabus or a senior engineer's mental model.
* **Application:** If the reader (a career switcher or beginner) is confused, Ethan must be equally confused. He cannot make intuitive diagnostic leaps across protocol layers. Every diagnostic step must be grounded in observable telemetry (multimeter display, LED blink code, terminal error string).

### Law 3: Resolution Must Be Paid For
> *A problem cannot wrap up neatly in the same scene without a genuine cost charged.*

* **The Tells:**
  - A technical fault introduced in a scene is resolved five minutes later with zero fallout.
  - A mentor explains a principle once, and Ethan executes it flawlessly on the first try.
  - The scene ends on a summarizing moral line explaining what Ethan learned.
* **The Fix:**
  - **Charge for it:** If Ethan solves an issue, something must be spent: skin scraped off knuckles, $4.20 in glove-compartment gas money, blown fuses, lost sleep, or workplace reprimand.
  - **Let tension carry:** Most scenes should end with the pressure still running.
  - **Cut the last line:** Delete the concluding fortune-cookie moral sentence. The scene almost always lands stronger ending on an unresolved physical action.

### Law 4: Ordinary Inventory on the Ledger
> *Objects, tools, vehicles, and hardware exist in the scene only if their provenance is accounted for.*

* **The Rule:** No magical toolboxes. If Ethan reaches for an instrument, its physical origin, condition, and limitations must be accounted for:
  - *The Laptop:* A battered 2012 Lenovo ThinkPad T430 bought for $65 cash, with a duct-taped battery release and worn trackpoint.
  - *The Meter:* A cheap analog or secondhand digital multimeter from an auto parts store or Hank's loaner.
  - *The 3x5 Cards:* $1.19 pack of Walgreens index cards bound with a celery rubber band.
  - *The 4x6 Slates:* Downloaded forum text template printed on 65lb cardstock at the 24-hr FedEx on 82nd Ave, laminated with 2-inch Scotch packing tape.

### Law 5: The Anti-Epigram Rule (Boring Operational Realism)
> *Characters who speak only in epigrams make dialogue unreadable. Real people say boring operational things.*

* **The Rule:** Mentors (Jules Brooks, Frank Mercer, Hank) are working professionals, not Zen monks or fortune-cookie dispensers.
* **Application:** Strip out endless philosophical aphorisms. Real technicians speak in direct, practical, task-oriented language:
  - *"Did you check if the link light is on?"*
  - *"Hand me the 10mm socket."*
  - *"Don't touch three adjustments at once; change one variable and test."*

### Law 6: No Pretentious Classification or ARG Markings
> *This is an East Portland logistics warehouse, not a military black site or a cyberpunk murder mystery.*

* **The Rule:** Strictly ban bracketed classification headers such as `[ ARTIFACT // ETHAN'S KITCHEN TABLE — 02:45 AM ]` or `LEVEL 3 // TELEMETRY DOSSIER`.
* **Application:** Use clean, honest, plain-English headings: `### Ethan's 3x5 Trivia Cards`, `### The 4x6 Taped Field Slates`, `### Jules' Passdown Notes`.

---

## 3. Review Agent Enforcement

The `prose_critic` and `ui_standards_inspector` agents will strictly enforce these laws on every candidate chapter and component before code or prose is accepted into main.
