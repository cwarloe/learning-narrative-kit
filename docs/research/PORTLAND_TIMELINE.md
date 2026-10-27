# Portland Desk Master Timeline & Canon Continuity Guide
**Repository:** `learning-narrative-kit`  
**Protagonist:** Ethan Mercer (20 at Ep 00; 23 by Ep 12)  
**Lead Mentor:** Jules Brooks (Lead Support Specialist, Harrowmere Portland Regional Operations Center)  
**Employer:** Harrowmere Equipment Group (the same company as NADF, Books 1–2)  
**Setting:** East Portland, Harrowmere's Gresham distribution warehouse, & Harrowmere's Portland Regional Operations Center (Hawthorne Bridge overlook). Ethan never relocates; he stays in the Portland area through NADF.  
**Purpose:** The top-ranked source for Portland Desk facts (see `AGENTS.md` precedence) and the chronological anchor for all authoring, editing, visual prompts, and lab environments across CompTIA A+, Network+, and Security+ modules.

---

## 0. Acts and phases (decided 2026-10-26)

- **Acts are story structure.** Act I is Ep 00 to 02 (getting in: dock to desk, A+). Act II is Ep 03 to 06 (the wire: Net+). Act III is Ep 07 to 12 (identity, threats, and escalation: Sec+, with the Tier 2 promotion in January, between Ep 09 and Ep 10). These match the published hub.
- **Phases are the story-to-lab handoff models** in `PEDAGOGICAL_AGENCY_ARCHITECTURE.md`: Phase 1 is Ep 00 to 02, Phase 2 is Ep 03 to 06, Phase 3 is Ep 07 to 10, and Phase 4 is Ep 11 to 12.
- Use "act" only for story and "phase" only for the handoff model.

## 1. Ethan's Professional & Pedagogical Arc

The 13 episodes document Ethan's transformation from an exhausted warehouse laborer studying on a scarred kitchen table to a disciplined Incident Commander:

$$\text{Laborer / Student} \longrightarrow \text{IT Rotation} \longrightarrow \text{Frontline Help Desk} \longrightarrow \text{NOC / Network Tech} \longrightarrow \text{Incident Responder}$$

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                                PORTLAND DESK CHRONOLOGY                                │
├─────────┬──────────────────────┬─────────────┬─────────────────────────────────────────┤
│ Episode │ Title & Focus        │ Month (age) │ Narrative Context & Employment State    │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 00   │ The Four Rubber      │ Year 1:     │ About 7 months on the graveyard dock at │
│         │ Bands (A+ Prologue)  │ Late July   │ Harrowmere Gresham, unloading 80 lb     │
│         │                      │ (20)        │ bags of Quikrete Concrete Mix. Studies  │
│         │                      │             │ flashcards on his night off at the      │
│         │                      │             │ kitchen table. Failed Core 1 six weeks  │
│         │                      │             │ ago (592); passes the retake next       │
│         │                      │             │ morning with 690.                       │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 01   │ The Paper Cert (A+   │ Year 2:     │ Graveyard dock, ~14 months in. Sorting  │
│         │ Core 1 Hardware)     │ February    │ Line 4; multimeter and Kapton tape. Ken │
│         │                      │ (21)        │ writes an internal referral to regional │
│         │                      │             │ IT.                                     │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ (skip)  │ IT rotation, ~6 mo   │ Late Feb to │ Off-page. Day shift at a slight pay     │
│         │ (covered in Ep 02)   │ August (21) │ cut: imaging bench, deployments, desk-  │
│         │                      │             │ side, one overnight week. Not an        │
│         │                      │             │ internship.                             │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 02   │ The Live Board (A+   │ Year 2:     │ Practical that closes the rotation at   │
│         │ Core 2 Software)     │ Late August │ the Portland ROC. Dual-headset trial    │
│         │                      │ (21)        │ with Jules; cracks Maya's payroll       │
│         │                      │             │ crash; joins the desk at ~$24/hr.       │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 03   │ Default Gateway      │ Year 2:     │ 2 months on the desk. Works the queue   │
│         │ Doesn't Care (Net+)  │ October     │ solo; rogue static IPs and broadcast    │
│         │                      │ (22)        │ boundaries.                             │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 04   │ The Name Is Not the  │ Year 3:     │ 7 months on the desk. Flashcards moved  │
│         │ Number (Net+ DNS)    │ March       │ to the desk drawer. Split-horizon DNS   │
│         │                      │ (22)        │ and a stale hosts file.                 │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 05   │ The Wire Has Two     │ Year 3:     │ 8 months on the desk. Cable plant,      │
│         │ Ends (Net+           │ April (22)  │ console rollovers, half-duplex          │
│         │ Transport)           │             │ collisions in a wiring closet.          │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 06   │ The Portland Flood   │ Year 3:     │ 9 months on the desk. Spring storm      │
│         │ (Net+ Capstone)      │ Late May    │ floods the sub-basement; broadcast loop │
│         │                      │ (22)        │ and Spanning Tree rescue with Jules.    │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 07   │ The Port That Is     │ Year 3:     │ 1 year on the desk. Jared's Telnet      │
│         │ Open (Sec+ Ports)    │ August (22) │ script; protocol hardening.             │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 08   │ Prove Who You Are    │ Year 3:     │ 14 months on the desk. MFA push-bombing │
│         │ (Sec+                │ October     │ and AD lockouts. Misses the October     │
│         │ Authentication)      │ (23)        │ Tier 2 round.                           │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 09   │ Don't Click That     │ Year 3:     │ 16 months on the desk, still Tier 1.    │
│         │ (Sec+ Phishing)      │ December    │ Phishing headers, typo domains,         │
│         │                      │ (23)        │ SPF/DKIM/DMARC.                         │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 10   │ Something on the Box │ Year 4:     │ 18 months on the desk. Ken calls from   │
│         │ (Sec+ Malware)       │ February    │ Gresham with an infected logistics      │
│         │                      │ (23)        │ laptop.                                 │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 11   │ The Air Is Shared    │ Year 4:     │ 20 months on the desk. Rogue APs, evil  │
│         │ (Sec+ Wireless)      │ April (23)  │ twins, deauth storms hitting barcode    │
│         │                      │             │ guns.                                   │
├─────────┼──────────────────────┼─────────────┼─────────────────────────────────────────┤
│ Ep 12   │ When the Ticket      │ Year 4:     │ 22 months on the desk. Capstone         │
│         │ Escalates (Sec+ IR)  │ Late June   │ incident; CSIRT handoff. Ends with      │
│         │                      │ (23)        │ Ethan applying for the security ops     │
│         │                      │             │ analyst role. Offer opens Book 1.       │
└─────────┴──────────────────────┴─────────────┴─────────────────────────────────────────┘
```

---

## 2. Canonical Recurring Cast & Entities

### Ethan Mercer
* **Identity:** 20 at Ep 00, 21 when he joins the desk, 23 by Ep 12. Son of a retired East Portland precision machinist. Pragmatic, hands-on, scars on his knuckles from warehouse freight.
* **Gear:** Worn canvas Carhartt-style jacket, grey heather hoodie, dark jeans, work boots. Stainless steel 0.5mm drafting pencil clipped in chest pocket (father's graduation gift).
* **Quirk:** Carries 300 handmade flashcards bundled with four thick colored rubber bands (Red = trivia, Green = hardware anatomy, Yellow = network identity, Blue = diagnostic troubleshooting reflex). Started in a mug on his kitchen table; now lives in his top center desk drawer.

### Jules Brooks
* **Identity:** 34-year-old female Lead Support Specialist, Harrowmere's Portland Regional Operations Center. Nine years at the operations center.
* **Voice:** Measured, wry, calm under fire. Acts as a diagnostic compass rather than a cheat sheet. Never commands panic; uses Socratic questions to teach binary search.
* **Gear:** Commutes by bicycle regardless of weather (steel Kona Rove commuter bike locked to vertical bullpen pipe; matte silver commuter helmet clipped to secondary monitor arm; rain shell drying over chair). Worn ceramic coffee mug.
* **Motto:** Yellow sticky note on the corner of her monitor bezel: *Which decision?*

### Supporting Characters
* **Ethan's Father:** 61-year-old retired industrial machinist (East Portland tool-and-die). Stoic, observant, smells of cutting oil and flannel. Teaches Ethan that every machine on earth has the same anatomy.
* **Ken:** 51-year-old frantic logistics shift supervisor at Harrowmere's Gresham distribution warehouse. Career measured in outbound trailer tonnage. Demands proof of paper certifications, but recognizes genuine competence and writes Ethan's internal referral to regional IT.
* **Maya Lin:** Supervisor of regional accounting, Harrowmere Portland. Experienced financial administrator, under relentless biweekly payroll deadlines. Demanding but deeply grateful when technicians treat her time and system settings with respect.
* **Jared:** Senior Network Operations technician. Old-school network engineer who racks gear, writes automated shell scripts, and clings to habits formed in Hillsboro tech campuses a decade ago. Grumbles at modern security requirements, but respects anyone who proves a better way once.

---

## 3. Standing Rules of Continuity

1. **The Employer is Always Harrowmere Equipment Group:**
   * The desk is Harrowmere's Portland Regional Operations Center (PROC), the internal IT help desk for every Portland-area Harrowmere site: the Gresham distribution warehouse, the Willamette River plant, the Rivergate parts & service center, and the regional offices. It reports up to Central IT in Chicago. Never call it an MSP or a city agency.
   * Ethan never relocates. Chicago is where central IT and the SOC leadership sit; Ethan works from Portland in Book 0 and in NADF.
2. **The Internal Transfer Law:**
   * Ethan does **not** take live tickets solo as an unscreened walk-in candidate.
   * After Ken's internal referral (Ep 01), Ethan spends about six months in a day-shift IT rotation at a slight pay cut. In Episode 02, Jules runs the supervised practical that closes the rotation, using a dual-headset training bridge. He moves onto the desk the next Monday. No resignation and no notice: it is the same company.
   * Overnight desk coverage is a rotation everyone works, not a promotion.
3. **The Index Cards Progress with Ethan:**
   * In Ep 00: Scattered on the kitchen linoleum floor in despair, then sorted into four colored bands.
   * In Ep 01: In his pocket on the freight pallet.
   * In Ep 02: In his backpack; his portfolio holds the A+ certificate, rotation sign-off, and Ken's referral.
   * In Ep 04–07: Kept in the top center drawer of Workstation 14 as an anchor for nerve control during triage, not as a novice crutch.
4. **Ken's Loop Closes in Episode 10:**
   * When the malware outbreak strikes the logistics network in Episode 10, the infected laptop belongs to Ken in Gresham—creating a satisfying narrative echo of Episode 01.

---

## 4. Ethan's Backstory (approved 2026-10-21; durations synced 2026-10-26)

**Book 0 spans about three years**: Ep 00 is late July of Year 1, and Ep 12 is late June of Year 4. Ethan is 20 at Ep 00, 21 at Ep 01 and 02, 22 from Ep 03 to 07, and 23 from Ep 08 to 12. He turns 24 in September after Book 0, as NADF Book 1 begins.

**Ep 00 job detail (real-world):** the dock moves 80 lb bags of Quikrete Concrete Mix (Model 110180), stacked 42 bags to a pallet (3,360 lb). Home Depot's listed price was $6.47 a bag ($271.74 a pallet) as of 2026. Ethan unloads concrete mix, not mortar.

Most of this is off the page. It exists so every episode and NADF agree on how Ethan got here. Source: Writing Bot's "Ethan Mercer — Backstory Bible v3" (Charles's Drive). Assumes a September birthday, so he graduates high school in June at 18.

| When | Age | Stage | Certs | Pay (approx.) | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| June, year of graduation | 18 | Graduates high school; no money for college | — | — | Off |
| Up to 2 years | 18–20 | Restaurant job (line cook, later shift lead). Drift: the pay is fine, the future is not | — | ~$18–23/hr | Off (Ep 00 memory) |
| ~14 months | 20–21 | Non-technical graveyard dock job, Harrowmere Gresham distribution warehouse; studies by day and on nights off | A+ Core 1: failed first attempt in mid-June of Year 1 (592), passed the retake in late July (690). Core 2 followed before Ep 01 | ~freight median ($22.17) + night differential | Ep 00–01 |
| February | 21 | Line 4 sorting-line fix; Ken writes the internal referral | — | — | Ep 01 |
| ~6 months | 21 | IT rotation on day shift (imaging bench, deployments, desk-side, one overnight week). Quasi-apprenticeship, not a formal internship | Net+ study begins | ~$20–21/hr: a slight cut, traded for day shift | Covered at the start of Ep 02 |
| Late August | 21 | Passes Jules's practical; joins the desk | — | ~$24/hr | Ep 02 |
| ~22 months on the desk | 21–23 | Help desk (Tier 1, Ep 02 to 09), then Tier 2 from January of Year 4 (Ep 10 to 12). Overnight is a rotation | Net+ (~13 months into IT); Security+ (~29 months into IT, just after Ep 12) | ~$24 → ~$28/hr in steps | Ep 02–12 (Book 0 ends ~22 months into the desk) |
| End of Ep 12 (late June, Year 4) | 23 | Applies for the analyst opening on Harrowmere security operations | — | — | Ep 12 |
| August, Year 4 | 23, turning 24 | Offer and move upstairs to the analyst role, still in Portland. This is the opening of Book 1. | — | — | NADF Book 1 |

Pay benchmarks: BLS OEWS, Portland-Vancouver-Hillsboro, May 2025. The rotation pay, night differential, and raise sizes are estimates, not sourced figures.

His father is a retired precision machinist (East Portland tool-and-die, 34 years).

### Open questions (not decided)

None right now. Leah's age (36) and Ep 00's job (the Harrowmere dock) were settled on 2026-10-21.
