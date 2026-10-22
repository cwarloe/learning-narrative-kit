# Portland Desk Visual Production Audit: Literary & Prose Critic Review
**Repository:** `learning-narrative-kit`  
**Reviewer:** Cynical Literary & Prose Critic (`prose_critic`)  
**Target Document:** `docs/research/PROPOSED_VISUALS_AUDIT.md` (Digital Art Director)  
**Governing Standards:** `docs/research/TECHNICAL_NARRATIVE_AUTHORING_PRINCIPLES.md`, `docs/research/PLAIN_ENGLISH_STYLE_GUIDE.md`, `docs/research/PORTLAND_TIMELINE.md`, `docs/research/PORTLAND_AUTHOR_BIBLE.md`

---

## 1. Executive Verdict: The Grounded Eye vs. The Comic Book Trap

The Digital Art Director's proposed catalog (`docs/research/PROPOSED_VISUALS_AUDIT.md`) represents a major structural leap forward for the Portland Desk courseware. The commitment to **The Absolute Zero-Text Rule** (allowing generative AI to handle materials, light, and geometry while SVG/Docsify overlays handle typography and telemetry) is an architectural necessity that will save learners from the uncanny valley of hallucinated lettering.

Furthermore, the decision to enforce **One Primary Visual Anchor Per Episode** (13 total plates) is literarily and cognitively correct. In narrative pedagogy, every image creates visual drag. If an author peppers a chapter with four or five generic illustrations, the reading rhythm shatters, the text feels like an elementary school primer, and the technical gravity evaporates. A single, high-leverage visual plate per episode gives the learner a distinct mental landmark without cognitive clutter.

However, from the perspective of prose craft, dialogue realism, and plain-English style, the proposal has three serious failure modes that must be corrected before production:

1. **The Superhero Action-Comic Trap (Figure 10.1):** Figure 10.1 degenerates into campy Hollywood melodrama. Having a 51-year-old warehouse supervisor back away with "hands raised" as if staring down an armed gunman, while Ethan "reaches down with authority" and yanks a network cord until the plastic clip flexes, is cartoonish. It completely violates the working-class procedural tone of Harrowmere Equipment Group.
2. **The "Static Catalog Still-Life" Risk (Figures 0.1 and 8.1):** While Ligne Claire cutaways are welcome, Figures 0.1 and 8.1 risk looking like isolated hardware catalog spreads rather than dramatic narrative beats. They must be tethered to Ethan's immediate physical reality and the active friction of the scene.
3. **Internal & Learner-Facing Jargon Creep:** Despite the existence of `PLAIN_ENGLISH_STYLE_GUIDE.md`, the document is laced with internal instructional design jargon (`scaffolding`, `pedagogical role` repeated 13 times), and several learner-facing badges and captions slip into stiff university computer-science dialect (`diagnostic binary search`, `cryptographic enclave`, `IOC`).

---

## 2. Pedagogical Weight & Pacing: Pivot vs. Complication Audit

A visual earns its place on the page only if it anchors a genuine **Complication** (where the learner's assumptions crash into a stubborn physical reality) or an actionable **Pivot** (the decisive operational turning point where the diagnostic fork is taken). 

Here is the beat-by-beat verdict across all 13 proposed plates:

| Episode | Proposed Plate | Proposed Role | Critic Verdict | Editorial Remediation |
| :--- | :--- | :--- | :--- | :--- |
| **Ep 00** | Motherboard Anatomy & Leaking Capacitors | Pivot (Hardware vs Trivia) | **Pass with Note:** Highly effective contrast between healthy and bulging capacitors. However, Ethan is sitting at his kitchen table in East Portland studying index cards. | Ensure the caption or framing indicates this is the physical anatomy Ethan visualizes from his Green Rubber Band cards, not a high-end corporate workbench he doesn't yet have access to. |
| **Ep 01** | DB-9 Serial Pin Realignment | Pivot (Layer 1 Mechanics) | **Strong Pass:** Superb dramatic pivot. Anchors the moment Ethan stops guessing on multiple-choice cards and uses his father's 0.5mm drafting pencil to realign Pin 2. | Perfect tactile granularity. Perfectly timed at the sorting-line climax. |
| **Ep 02** | Workstation 14 Dual-Headset Bridge | Complication (Live Triage) | **Pass with Acting Fix:** The physical setup (dual-headset splitter, secondary monitor, Hawthorne Bridge view) earns its place. | Needs character acting correction. Jules is too relaxed sipping coffee during a live payroll outage; Ethan needs more visible tension. |
| **Ep 03** | /26 Subnet Boundary & Gateway | Complication (Off-link Route) | **Strong Pass:** Excellent visual explanation of why two servers on the same physical switch cannot communicate without crossing the router boundary. | Solves the classic student confusion around CIDR boundaries without a wall of math. |
| **Ep 04** | Split-Horizon DNS Resolution Race | Complication (DNS Leak) | **Strong Pass:** Demonstrates the race condition between the fast domestic 4ms NXDOMAIN and the slow corporate 20ms VPN answer. | Clean, dynamic, and directly explains why the internal domain name fails. |
| **Ep 05** | TCP State Machine & Port Exhaustion | Pivot (Socket Depletion) | **Pass:** Contrasts server RST with client-side TIME_WAIT pool saturation. | Ensure the visual clearly highlights the unthrottled 500ms retry script as the culprit. |
| **Ep 06** | Sub-Basement Vault Flood Restoration | Capstone Pivot (Physical DR) | **Exceptional Pass:** The undisputed visual triumph of the catalog. Perfectly captures the physical grit of IT work. | Eight inches of floodwater, milk crate perch, Cat6 bundles, and rack elevation 4U above water line. Zero decorative fluff. |
| **Ep 07** | Perimeter Protocol Hardening | Pivot (Cleartext to VPN) | **Conditional Pass:** Currently too abstract. Glowing red and blue conduits entering a generic firewall appliance look like a corporate sales deck. | Ground the cutaway in Leah Moreno's water treatment plant: show the plant gateway protecting the Modbus/DNP3 telemetry from Jared's open Telnet path. |
| **Ep 08** | Authentication Factor Triad & TPM 2.0 | Pivot (MFA Classification) | **Borderline (Risk of Still-Life):** A phone, a notebook, and a token resting on a mat feels like a stock photo layout. | Reframe around an active incident: contrast an incoming MFA push-bomb on the phone display with the physical hardware token and TPM. |
| **Ep 09** | Email MIME Envelope Architecture | Complication/Pivot (Spoofing) | **Strong Pass:** Using translucent nested envelopes to separate RFC 5321 (transmission sender) from RFC 5322 (display header) is brilliant narrative pedagogy. | Makes the technical mechanism of Business Email Compromise immediately obvious. |
| **Ep 10** | Physical Host Cable Isolation | Pivot (Worm Containment) | **Pedagogically Strong, Dramatically Broken:** The decision to pull the cable to save RAM is the correct pivot, but the acting in the prompt is melodramatic comic-book absurdity. | Full prompt rewrite required (see Section 3). |
| **Ep 11** | RF Spectrum Interference & Rogue AP | Complication (RF Contention) | **Pass:** Visualizes the invisible: 2.4 GHz channel overlap (1, 6, 11) vs 5 GHz capacity, pinned to the rogue travel router and microwave. | Clean, technical, and directly explains why warehouse barcode scanners drop connections. |
| **Ep 12** | Live Forensic Bench & Volatility | Capstone Pivot (RFC 3227) | **Strong Pass:** Ethan at the bench capturing volatile RAM with a hardware write-blocker before powering down. | Perfect culmination of Ethan's growth from dock laborer to disciplined Incident Responder. |

---

## 3. Working-Class Pacific Northwest Realism & Character Acting

The core aesthetic of the Learning Narrative Kit is grounded, working-class procedural realism: the smell of diesel exhaust, hydraulic oil, rain drumming against casement windows, buzzing ballast lamps, cold coffee, stained workwear, and exhausted apprentices under production pressure.

When reviewing the three primary human-centered narrative spreads, significant adjustments are required to protect this voice:

### Figure 2.1: The Dual-Headset Triage Station at Workstation 14
* **The Setting:** The fourth-floor PROC bullpen overlooking the rain-blurred Hawthorne Bridge trusses, the matte silver commuter helmet clipped to the monitor, and the yellow *"Which decision?"* sticky note are spot-on. They anchor the scene firmly in Portland IT culture.
* **The Character Acting Failure:**  
  The prompt describes Jules Brooks as:  
  > *"calmly watching his screen... holding a ceramic coffee mug..."*  
  This is a direct violation of `TECHNICAL_NARRATIVE_AUTHORING_PRINCIPLES.md` (Principle 4: AI Crutch-Word Kill List: *"chipped ceramic mug / lukewarm tea"*, *"calm deliberation"*).  
  In Episode 02, Maya Lin's payroll run is frozen with biweekly direct deposit deadlines expiring in minutes. Accounting is on the line. Jules is not lounging in a coffee shop observing a casual demo; she is conducting a high-stakes live trial. 
* **The Fix:**  
  Jules should be leaning in with intense focus, one hand on her headset ear-cup, listening to Maya's distress while her eyes bore into Ethan's screen. Ethan should not be passively "typing"; his posture should show apprentice strain—shoulders tight, fingers poised over the mechanical keyboard, hesitating at the fork between Safe Mode and destructive recovery.

### Figure 6.1: The Sub-Basement Telecommunications Vault Restoration
* **The Literary Assessment:**  
  This scene is **flawless**. It is the gold standard for how technical narrative illustration should be executed.
* **Why It Works:**  
  It completely resists the temptation of superhero fantasy. Ethan is not wading heroically through chest-deep rapids; he is uncomfortably balanced on an overturned milk crate, shivering in insulated coveralls and mud boots, carefully balancing a ruggedized laptop on his knees so he doesn't drop his light-blue console cable into the murky water. Jules in her yellow cycling rain jacket holding a halogen beam onto the printed wiring schematic captures the exact unglamorous, exhausted teamwork of municipal IT disaster recovery.

### Figure 10.1: Living-Off-The-Land Worm Triage & Physical Host Isolation
* **The Literary Catastrophe (Melodrama & Superhero Posturing):**  
  Figure 10.1 suffers from acute comic-book exaggeration:
  1. *"Ken, an alarmed 51-year-old supervisor, backs away from his desk with hands raised as his laptop cooling fan whines at maximum speed."*  
     Ken has spent twenty years on industrial loading docks managing freight tonnage. When an office laptop freezes or runs hot, an experienced warehouse supervisor does **not** surrender with his hands raised like an armed suspect in a police standoff. He leans over the desk, curses at the screen, slams the mouse, or frantically stabs at the power button.
  2. *"In sharp foreground focus, the steady hand of Ethan Mercer reaches down with authority and firmly yanks a blue RJ-45 Ethernet cable out of the laptop's side network port, the clear plastic retention clip flexing as it disconnects."*  
     - **Crutch Word:** *"steady hand"* is explicitly quarantined on our kill list (Principle 4).  
     - **Superhero Tone:** *"reaches down with authority and firmly yanks"* turns Ethan into a Marvel action hero defusing a bomb.  
     - **Mechanical Hardware Blunder:** You do **not** "yank" an RJ-45 cable until the clip flexes. If a technician yanks an 8P8C modular connector without depressing the retention tab, they snap the plastic tab off inside the jack or rip the surface-mount modular connector pins off the laptop motherboard! A real technician presses the thumb-tab firmly before pulling.
  3. *"On the illuminated laptop display, a branching process tree diagram showing a central process spawning aggressive sub-processes suddenly turns amber and halts at the severed boundary."*  
     This is pure Hollywood sci-fi UI fantasy. In the real world, Process Explorer does not display glowing amber animations halting at an illustrated boundary. Local PowerShell processes keep thrashing in memory until they time out trying to reach unreachable network shares.
* **Mandatory Prompt Rewrite for Figure 10.1:**
  ```text
  Dramatic graphic novel scene in Pacific Northwest silicon noir style, crisp uniform ink linework, high contrast clean lines, authentic industrial warehouse office atmosphere. Inside a cramped shipping dispatch office, Ken, an exhausted 51-year-old supervisor in a hi-vis vest, leans over his cluttered laminate desk in frustration, one hand aggressively reaching toward the laptop power button. In sharp foreground focus, 22-year-old technician Ethan Mercer steps in, his thumb firmly depressing the clear plastic release tab of a blue RJ-45 patch cable and cleanly sliding the connector out of the laptop's side port to isolate the machine. On the laptop screen, a standard Windows task manager and console terminal display unmoving, dense text log lines. On the desk sits a spiral incident notepad, a clip-on company badge, and a half-empty mug. Outside the window behind them, grey Pacific Northwest rain streaks the industrial loading bay. Crisp mechanical accuracy, grounded procedural drama, no text, no letters, no words, no numbers, no speech bubbles, no watermarks. 16:9 ratio.
  ```

---

## 4. Banned Jargon & Plain-English Style Guide Audit

An audit against `docs/research/PLAIN_ENGLISH_STYLE_GUIDE.md` reveals both internal meta-jargon and several learner-facing phrases that violate the high-school readability standard.

### 4.1 Internal Document Sanitization
* **"Scaffolding" (Lines 11 & 356 in Audit):** Strictly prohibited under the style guide. Replace with: *"active visual anchor"* or *"operational mental model"*.
* **"Pedagogical Role" (Repeated 13 times):** Academic instructional-design jargon. Replace throughout the taxonomy and subheaders with: **"Operational Teaching Beat"** or **"Incident Turning Point"**.

### 4.2 Learner-Facing Badges, Titles, Captions & Pin Callouts

Every badge, title, caption, and pin will be rendered directly in Docsify over the illustrations. The following table identifies academic/architect jargon in the Art Director's draft and provides mandatory plain-English replacements:

| Figure | Proposed Element | Current Wording (Draft) | Flaw / Violation | Plain-English Replacement |
| :--- | :--- | :--- | :--- | :--- |
| **Fig 2.1** | Caption | *"Jules enforces diagnostic binary search via Safe Mode..."* | "Binary search" sounds like a computer science data structures exam. | *"Jules guides Ethan through a disciplined process of elimination using Safe Mode..."* |
| **Fig 2.1** | Pin 2 | `Desk Lead Compass: "Which Decision?"` | Slightly abstract/poetic. | `Desk Lead Reminder: "Which Decision?"` |
| **Fig 7.1** | Pin 3 | `Encrypted Cryptographic Enclave: SSH (22) & IPsec VPN` | "Cryptographic Enclave" is heavy enterprise marketing buzz. | `Encrypted Remote Management: SSH (22) & Secure VPN Tunnel` |
| **Fig 8.1** | Pin 1 | `Something You Know: NIST SP 800-63B Passphrase` | Dropping formal NIST publication numbers in a beginner pin creates exam anxiety. | `Something You Know: Memorized Multi-Word Passphrase (NIST Guideline)` |
| **Fig 8.1** | Pin 3 | `Hardware Root of Trust: Asymmetric Private Key Storage` | Stiff academic abstraction. | `Hardware Security Anchor (TPM 2.0): Tamper-Proof Key Storage` |
| **Fig 10.1** | Pin 3 | `Incident Evidence Log & Initial IOC Capture` | "IOC" is unexplained acronym jargon for an apprentice. | `Incident Evidence Log: Tracking Suspicious Hashes & IPs` |
| **Fig 12.1** | Title | `FIGURE 12.1: FORENSIC BENCH & ORDER OF VOLATILITY (RFC 3227)` | RFC number in main figure title is intimidating. | `FIGURE 12.1: FORENSIC BENCH & ORDER OF VOLATILITY` |
| **Fig 12.1** | Pin 1 | `Volatile System RAM (RFC 3227 Priority 1)` | Stiff formal citation. | `Live System RAM: Fleeting Memory (Capture Before Power Down)` |

---

## 5. Continuity & Character Arc Sanity Check (14-Month Timeline)

The 13 visual proposals were audited against `docs/research/PORTLAND_TIMELINE.md` and `docs/research/PORTLAND_AUTHOR_BIBLE.md` to ensure character ages, gear, and relationship dynamics match canon:

### 5.1 Dynamic Fading Apprenticeship (Mentor Dynamic)
The visual presence of Jules Brooks perfectly tracks the fading scaffolding progression established in `docs/research/PEDAGOGICAL_AGENCY_ARCHITECTURE.md`:
* **Episodes 00–01:** Jules is completely absent. Ethan is struggling on the dock and studying at home.
* **Episode 02 (Figure 2.1):** Jules is seated shoulder-to-shoulder on the dual-headset training bridge, actively guiding Ethan's triage during his closing IT rotation practical.
* **Episodes 03–05:** Jules steps back into the bullpen background as Ethan takes solo queue tickets.
* **Episode 06 (Figure 6.1):** Jules reappears beside him as a trusted operational partner during the physical crisis of the sub-basement flood.
* **Episodes 07–11:** Ethan operates independently in the field and at his desk. In Episode 10, Ethan is dispatched solo back to Gresham to save Ken's laptop.
* **Episode 12 (Figure 12.1):** Ethan is alone at the forensic bench as the de facto Incident Commander, escalating directly to Chicago CSIRT Lead Nia Alvarez. Jules has successfully faded, leaving Ethan fully self-reliant.

### 5.2 Gear & Character Detail Tracking
* **The 0.5mm Drafting Pencil:** Correctly tracked as a persistent tactile anchor across the arc. It appears in Figure 1.1 (used to straighten DB-9 Pin 2) and reappears in Figure 12.1 (logging cryptographic evidence on the forensic bench). This honors the gift from his machinist father.
* **The Four Rubber Bands / Index Cards:** Established in Episode 00. Note: Ensure Figure 2.1 shows the top center drawer of Workstation 14 slightly cracked to reveal the rubber-banded cards, representing his quiet anchor under fire rather than a discarded crutch.
* **Character Ages:** Verified. Ethan progresses from a 20-year-old laborer (Ep 00) to a 21-year-old apprentice (Ep 01–02), a 22-year-old frontline technician (Ep 10), and a 23-year-old Tier 2 lead (Ep 12). Jules remains the 34-year-old steady hand.

---

## 6. Actionable Recommendations for the Art Director

Before generating final image assets or freezing the visual production catalog, the following revisions must be applied to `docs/research/PROPOSED_VISUALS_AUDIT.md`:

1. **Replace the Prompt for Figure 10.1:**  
   Purge the armed-robbery surrender pose and the cable-yanking melodrama. Use the revised procedural prompt provided in Section 3 of this review.
2. **Adjust Character Acting in Figure 2.1:**  
   Replace Jules's passive coffee-sipping posture with active, focused triage posture appropriate for an impending payroll deadline.
3. **Ground Figures 0.1, 7.1, and 8.1:**  
   - Frame Figure 0.1 explicitly as the anatomical mental model from Ethan's Green Rubber Band flashcards.  
   - Ground Figure 7.1 around Leah Moreno's treatment plant PLC cabinet.  
   - Anchor Figure 8.1 around an active authentication challenge rather than an inert tabletop spread.
4. **Sanitize Titles, Badges, and Pins:**  
   Adopt the plain-English replacements detailed in Section 4.2 to eliminate academic and software-architect jargon.
5. **Update Taxonomy Terminology:**  
   Replace `Pedagogical Role` with `Operational Teaching Beat` across the master table and all episode headers.

---
*Review complete. Forwarding to Lead Curriculum Architect and Digital Art Director for immediate implementation.*
