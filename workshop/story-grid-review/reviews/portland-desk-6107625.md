# Portland Desk — Five Commandments review

**Status:** review complete; proposed narrative revisions await author prioritization. Recording this review does not mean its recommendations have been implemented.

## Scope and basis

Reviewed all thirteen narrative source files, Episodes 00–12, fully at commit `6107625085d43d6b8871148eb8b088505bffe864`. This matched remote `main` at the start and end of the review. The Story Grid review agent considered the complete Book 0 formation arc, each chapter's main arc, and its constituent scenes/vignettes. It read the reviewer definition, verified reference notes, and the supplied full 12-page Tim Grahl PDF directly via `pdftotext`. The live webpage was not fetched. It also consulted `AGENTS.md`, `schema/README.md`, `schema/VOICE.md`, the Learning Narrative Framework, Portland timeline, and author bible. Adjacent chapters were read to verify continuations. No lab, glossary, or plan was used to supply a missing narrative event. No story files were changed and no mechanical or reader-learning result is claimed by this editorial review.

Assessment words describe evidence: **clear**, **partial**, **not found**, **outside scope**. A diagnosis is not automatically a crisis; a recorded retrospective decision still counts as an action. Professional delegation is legitimate. Its structural question is whether Ethan's consequential choice remains identifiable, not whether he personally executes every command.

`E00` through `E12` below abbreviate the corresponding episode source in `docs/portland-desk/narrative/`. The chapter sections give the full source paths. An abbreviated reference such as `E12:124` identifies a source line, not a line in this report.

## Verdict

**Targeted revision recommended**, especially if the intent is for every chapter to operate as a complete Story Grid arc. This is already a substantially connected professional-formation story: mistakes cost people time and trust, and later chapters collect those costs. Its main weakness is that several diagnostic sequences establish complications and results more clearly than an incompatible, consequential choice for Ethan. That is different from lacking stakes or needing larger incidents. No new must-address factual/causal contradiction comparable to the five repaired defects was identified under this structural lens.

## What works

1. **Partial fixes genuinely expose deeper failures.** The hosts cleanup fails and reveals the resolver problem in `docs/portland-desk/narrative/04-the-name-is-not-the-number.md:56–60`; restored flood hardware exposes DHCP exhaustion in `docs/portland-desk/narrative/06-the-portland-flood.md:105–140`. These are causal complications, not merely harder vocabulary.
2. **Costs persist across episodes.** Maya's copied closure notes in `docs/portland-desk/narrative/02-the-live-board.md:125` recur in `docs/portland-desk/narrative/03-the-default-gateway-doesnt-care.md:9`. The tone complaint/promotion loss in `docs/portland-desk/narrative/08-prove-who-you-are.md:114–118` carries into `docs/portland-desk/narrative/09-dont-click-that.md:9` and `docs/portland-desk/narrative/10-something-on-the-box.md:9`. These are actual changes in conduct and opportunity.
3. **The revised late chapters have paid choices and useful endings.** Ethan deliberately keeps scanners offline despite dock costs in `docs/portland-desk/narrative/11-the-air-is-shared.md:86–90`; his containment choice and incomplete remote capture are distinguished correctly in `docs/portland-desk/narrative/12-when-the-ticket-escalates.md:124–126`. His final application enacts accountability rather than ending with a congratulatory speech (same file, lines 134–136).

## Prioritized findings

### A. Author decision — choose what completeness means at book and chapter scale

**Evidence:** `docs/portland-desk/narrative/00-the-four-rubber-bands.md:17–19` establishes the retake problem; it resolves at line 175, while the permanent desk goal resolves in `docs/portland-desk/narrative/02-the-live-board.md:129`. The security application arrives in `docs/portland-desk/narrative/12-when-the-ticket-escalates.md:130–136`. Thus Book 0 changes concrete goals as Ethan advances; it does not maintain one external problem for all thirteen chapters.

**Interpretation:** this works as linked apprenticeship/formation, but is only partially evidenced as a single five-commandment external plot. Decide whether the intended form is an episodic formation book with a larger internal arc, or a novel with one book-length forcing goal. Do not invent an overarching villain or rewrite thirteen chapters merely to satisfy the latter model.

### B. Consider — distinguish a diagnostic question from a crisis in weaker chapter arcs

**Evidence:** `docs/portland-desk/narrative/03-the-default-gateway-doesnt-care.md:159–173` diagnoses and removes a duplicate-IP printer; `docs/portland-desk/narrative/05-the-wire-has-two-ends.md:152–168` diagnoses exhaustion and adopts both pooling and a timeout adjustment. Both show competent repairs, but neither passage clearly shows Ethan choosing between two incompatible, costly alternatives. The fact that the two mitigations in Episode 05 are compatible is not a technical defect; it simply cannot be used as evidence of a binary dilemma.

**Impact:** the chapter can become “identify fault, apply appropriate remedy, learn afterward what it cost” rather than “a failing strategy forces a choice that incurs this cost.”

**Smallest useful direction:** identify the actual decision already latent in each situation and its supported competing stakes. If the text supplies none, retain a useful diagnostic vignette and mark the deliberate structural departure rather than fabricating a dilemma. Do not give the breakroom printer an invented critical role or add arbitrary danger.

### C. Consider — keep Ethan's decision identifiable when experts diagnose or execute a fix

**Evidence:** Jules points directly to Event Viewer in `docs/portland-desk/narrative/02-the-live-board.md:113`; Lena spots the VPN error and later pushes the correction in `docs/portland-desk/narrative/04-the-name-is-not-the-number.md:108` and line 118. Ethan does perform meaningful work: he apologizes and changes approach in E02:60, and takes evidence to the authorized owner in E04:118.

**Impact:** the technical result is clear; the character-level price or alternative facing Ethan at the decisive moment is less clear. This is not a request to silence mentors or have a junior change someone else's gateway.

**Smallest useful direction:** center his evidence-based recommendation/escalation and the existing pressure around it, especially the professional disagreement with Jared in E04:122–128. Preserve Lena's authority and shared expertise.

### D. Consider — Episode 08's refusal is present, but its cost is not a forced security-versus-service dilemma

**Evidence:** `docs/portland-desk/narrative/08-prove-who-you-are.md:114` reports Ethan's written refusal; line 116 shows Jules being both polite and unmoving; line 118 says the complaint was one contributor to the lost promotion.

**Impact:** the story's actual lesson concerns curtness and communication as well as control enforcement. Do not retroactively treat “be secure or be courteous” as irreconcilable goods: Jules demonstrates that both are possible. The action is not missing merely because it is narrated retrospectively.

**Smallest useful direction:** if a complete crisis scene is wanted, let the already-existing exception exchange expose Ethan's actual pressure and alternatives. Preserve the nuance that tone contributed to the consequence; do not claim promotion loss was an unavoidable price of enforcing MFA.

### E. Consider — give Episode 09's wire sequence a distinct decision/closure

**Evidence:** `docs/portland-desk/narrative/09-dont-click-that.md:56–58` already has the real-number callback, CFO denial, AP freeze, and Ethan's SOC escalation. The Wire Run at line 90 reprises the callback/denial and cancellation; the broader batch-verification cost appears at line 92.

**Impact:** this is not necessarily a continuity contradiction—provisional freeze and final cancellation can differ—but the later passage does not clearly establish a new Ethan decision or changed uncertainty. Much of the costly choice to hold the batch is owned by AP/Marisol, appropriately for their roles.

**Smallest useful direction:** clarify what remains pending after the first freeze, distinguish provisional hold from final clearance, and identify Ethan's actual recommendation/escalation. Keep Marisol's finance authority; do not transfer it to Ethan to manufacture a hero climax.

### F. Consider, lower priority — Episode 12's decisive operational action is disclosed after the live incident

**Evidence:** `docs/portland-desk/narrative/12-when-the-ticket-escalates.md:104` shows collection; line 110 reports containment; line 124 first supplies Ethan's cable-pull choice and its interrupted-stream consequence.

**Impact:** the chapter contains the crisis and action; this is weaker immediate dramatization, not absent evidence or a fresh RAM/isolation error. The after-action review is doing double duty by introducing the very act it then evaluates.

**Smallest useful direction:** consider showing the already-established cable pull in the live incident before line 110, then let the review explain its cost. Preserve prompt containment and the repaired distinction between a broken remote transfer and powered RAM. No additional incident or altered outcome is required.

## Overall Book 0 map

| Commandment | Assessment | Evidence and judgment |
|---|---|---|
| Inciting incident | Partial at whole-book scale; clear locally | The causal failure of Ethan's brute-force study method is exposed at E00:17–19, with his fear of remaining on the dock at E00:34. This begins a formation need, but the concrete retake goal resolves in E00:175, and the desk goal in E02:129. |
| Turning Point Progressive Complication | Partial as one book plot; clear as a learning/relationship sequence | E01's failed guessing and damaged equipment (E01:23–69), E02's re-image threat (E02:46–54), E08's promotion loss (E08:114–118), and E10's reassurance to Ken (E10:171–181) repeatedly defeat the idea that correct facts or confidence alone make him trustworthy. These are related tests of a standing flaw, but not one continuously escalating external strategy. |
| Crisis | Partial | The final operational best-bad choice is supported in E12:104 and E12:124: finish the remote snapshot while spread continues, or contain immediately and interrupt collection. For the whole career arc, choosing candid accountability over self-protective presentation is suggested by E12:134–136; the job stakes are real, but the text does not fully establish those as incompatible goods, especially since Nia explicitly requests the failure account at E12:132. Do not invent a global binary to certify a pass. |
| Climax | Clear for Ethan's formation | E12:124 reports his containment act, and E12:134–136 shows him choosing the failed capture as his application subject and deleting his self-justifying sentence before submitting. The latter is an identifiable act revealing changed self-presentation. |
| Resolution | Clear for Book 0's formation boundary; outside scope for the new-job offer | He has moved from wanting paper proof of competence (E00:11, E01:11) to accounting for an imperfect decision in E12:134–136. The application is submitted; the offer belongs to Book 1 under the approved canon. Missing an offer here is not a defect. |

**Inferred controlling idea, not an author-established genre/theme:** professional trust grows when knowledge is tested against evidence and the technician accepts the consequences of imperfect decisions. The book supports that value movement more firmly than it supports one overarching incident plot.

## Chapter maps and scene inventories

Each chapter declares its exact source path. `L` anchors in that section refer to that file's line numbers at `6107625`. These are chapter-level maps with scene inventories and selected scene-level concerns, not separate five-row maps for every vignette.

### Episode 00 — The Four Rubber Bands

Source: `docs/portland-desk/narrative/00-the-four-rubber-bands.md`.

Scene inventory: kitchen failure/father exchange (L5–60); sorting and field-slate preparation (L62–122, with embedded learning widgets); timed exam (L157–175); departure/residue (L177–183). The widgets/tables are teaching exhibits, not additional complete scenes.

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear | Causal: Ethan's chosen brute-force study method produces another practice failure, L15–19; the next morning's paid retake is already scheduled, L13. The result destabilizes his confidence and demands a different way to pass. |
| Turning Point Progressive Complication | Clear | Revelatory: his father's catalog/mechanism comparison, L48, becomes Ethan's recognition that memorized cadence does not explain machines, L60. In the exam, the eight minutes lost on the router and the remaining 68 questions, L163, defeat an exhaustive first-pass approach. These are linked study and examination scenes rather than one uninterrupted action. |
| Crisis | Clear in the exam scene; partial in the study scene | Best Bad Choice, supported implicitly at L163–167: remain on the difficult simulation and risk insufficient time for the rest, or leave points unresolved and move on without assurance he can return. The kitchen's “keep cramming versus change method” is less fully presented as two costly alternatives. |
| Climax | Clear | Ethan flags the router and moves forward, L167, applies the frameworks, L169, then returns and commits his remaining answers, L171. He acts rather than receiving the exam's solution from his father. |
| Resolution | Clear | He passes narrowly at 690, L175–177, while the earlier lost voucher, overtime, and dock situation remain, L11–13 and L181. Do not attribute specific lost points to the flagged question; the text does not establish that. |

Value change: panicked possession of facts → limited but usable understanding and a narrow pass. Preserve the timed-exam choice. The father's exchange is a catalyst, not by itself a full five-commandment scene.

### Episode 01 — The Paper Cert

Source: `docs/portland-desk/narrative/01-the-paper-cert.md`.

Scene inventory: line stop and reckless reset (L13–35); failed RAM guess and Rosa's measurement (L43–91); ribbon repair reveals serial failure (L95–136); clock-setting repair and late freight (L144–159); manual cleanup/referral/residue (L161–165). The successive failures form one extended repair sequence.

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear | Coincidental mechanical line failure, L13, interrupts Ethan's freight job; Ken's trailers and ultimatum establish a restoration goal and public pressure, L19 and L35. |
| Turning Point Progressive Complication | Clear | Ethan's reset loses data, L23–29; his RAM guess breaks the latch without helping, L55–69; ribbon repair brings the console back but exposes serial corruption, L95–105. The revelation that his own reset changed the baud rate, L134–136, defeats treating the remaining fault as merely the bent pin. |
| Crisis | Partial | Best Bad Choice is suggested by Ken's “show me…or grab a hand truck” and the costly contractor, L35, plus the fragile-pin risk, L120, and deadline, L130. Continued intervention risks further harm; stepping back leaves an outage and the dispatch deadline. But these pressures are not assembled into one clearly evidenced final dilemma at the baud-rate turning point. The risk of a repair is not automatically a separate crisis at every step. |
| Climax | Clear | Ethan reads the silkscreen, works out the timings, and changes the switches/restarts the daemon, L144–146. Rosa's bounded assistance does not take this action away from him. |
| Resolution | Clear | The line runs, but hand reweighing delays Seattle 51 minutes and leaves Ken with the report, L155–159. The referral still names the loss, L163; this does not erase it. |

Value change: paper-based assurance → conditional trust earned through evidence and help. The technical escalation is strong; a larger confrontation is unnecessary. If tightening, clarify which existing commitment Ethan knowingly accepts after his guesses fail.

### Episode 02 — The Live Board

Source: `docs/portland-desk/narrative/02-the-live-board.md`.

Scene inventory: supervised practical and call setup (L7–21); re-image mistake and apology (L32–60); Safe Mode/BitLocker boundary (L62–97); eighteen-service decision and log diagnosis (L101–121); payroll verification and conditional desk entry (L123–131).

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear | Causal: Jules chooses a live payroll case for the final practical, L11–21. Ethan wants the permanent desk seat, L9, while Maya needs payroll working before noon, L21. |
| Turning Point Progressive Complication | Clear, with a qualified final link | Re-imaging threatens unsynced data, L46–54; the Safe Mode test introduces a recovery-key permission barrier, L72–91. Eighteen services and the deadline make blind elimination unattractive, L105–115. Jules identifies Event Viewer as the better next step, L113; this is a diagnostic pivot, not by itself a crisis. |
| Crisis | Partial | A character-level Best Bad Choice is implicit in the move from defensive “quick fix” to admitting error and starting careful inquiry, L44–60, under the one-strike warning, L54. The final eighteen-service passage does not establish two incompatible valued options; reading logs is a sensible method, not a demonstrated sacrifice. Do not invent a quitting option. |
| Climax | Clear | Ethan apologizes and changes approach, L60, and performs the two-stage application/driver correction, L119–123. Jules's teaching can remain; the scene need not turn into an unsupervised junior intervention. |
| Resolution | Clear | Payroll works, Maya copies Jules and remains distrustful, L125; Ethan receives the desk assignment without the damaged trust being erased, L127–131. |

Value change: anticipated certification-style proof → practical competence with scrutiny. The crisis is weaker than the mistakes and consequence; the smallest useful revision would center Ethan's actual decision and pressure rather than add technical danger.

### Episode 03 — The Default Gateway Doesn't Care

Source: `docs/portland-desk/narrative/03-the-default-gateway-doesnt-care.md`.

Scene inventory: storm/APIPA and trunk repair (L22–66); separate pump-subnet repair (L70–111); duplicate-IP printer investigation and restoration (L115–173); packet explanation and static-sprawl coda (L175–177). These are related diagnostic service vignettes, not all failures of one attempt.

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear | Coincidental storm/power-transfer disruption produces the warehouse outage, L5–11 and L22. Ken's blocked manifests give Ethan an immediate goal. |
| Turning Point Progressive Complication | Partial at chapter scale | APIPA reveals the local configuration failure, L41–51; the renewed network then exposes the duplicate-IP symptom, L117. The pump's contractor-configured mask/gateway problem, L74–111, is a separate fault, not a consequence of Ethan's first failed strategy. Jared owns the trunk repair, L51; Ethan owns the subnet and printer corrections, L111 and L173. |
| Crisis | Not found for a single chapter-level Ethan arc | The text supports diagnosis and repair, but no clear Best Bad Choice or Irreconcilable Goods decision for Ethan before unplugging/reserving the printer, L167–173. Ken's freight hold, L169, is consequential, but should not be silently repurposed as Ethan's own enacted dilemma. |
| Climax | Clear technically; partial as crisis payoff | Ethan removes the conflicting drop and sets the reservation, L173, answering the later printer problem. That is a real action, but it cannot answer a binary crisis not yet evidenced. |
| Resolution | Clear | The pings stabilize, L173; two trailers load late, L169; Ethan spends two unapproved extra hours tagging newly found statics, L177. The next chapter carries the unfinished list, E04:7. |

Value change: a supposed broken external circuit → differentiated local faults, with documentation debt. A useful diagnostic chapter does not have to be falsely certified as a complete Story Grid scene. Author decision: retain this episodic form, or give one existing incident the chapter's principal decision.

### Episode 04 — The Name Is Not the Number

Source: `docs/portland-desk/narrative/04-the-name-is-not-the-number.md`.

Scene inventory: carrier-blame dispute (L22–34); stale-hosts cleanup (L38–60); deeper resolver/profile investigation (L64–112); authorized correction and Jared escalation (L118–128); missed-queue consequence (L130–132).

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear | Causal: a changed VPN profile produces remote-user failures, L11, with the maintenance choice revealed at L108. Ethan's immediate task is restoring Greg's payroll access, L28. |
| Turning Point Progressive Complication | Clear | Removing the hosts entries fails, L56–60, so the first discovered anomaly cannot explain all the calls, L64–66. The home-router DNS reply, L78, and profile discrepancy, L108, force the investigation beyond the initial local fix. This is a strong revelatory turning point. |
| Crisis | Partial | Ethan must take evidence to the owner rather than simply keep tweaking Greg's machine, L118. A further conflict is whether to record the uncomfortable zone/design finding despite Jared's reaction, L122–128. The professional pressure is credible, but the chapter does not clearly establish those as a forced binary with both costs before the choice. Classification as Best Bad Choice remains interpretive. |
| Climax | Clear as collaborative resolution | Ethan takes the evidence to Lena and sends the client steps, L118–120; Lena legitimately owns and pushes the gateway/profile change. His fact-based escalation and response to Jared, L122–126, are also real choices. Delegation is not a missing climax. |
| Resolution | Clear | Users recover, L120; Jared's replies shrink for two weeks, L128, and four of Ethan's tickets miss response targets, L132. Those are specific prices for his involvement. |

Value change: borrowed blame → accountable evidence and strained working relationships. Preserve the failed partial fix and Lena's authority. If strengthening the arc, connect Ethan's existing recommendation/escalation to the competing pressure, not to unauthorized technical heroics.

### Episode 05 — The Wire Has Two Ends

Source: `docs/portland-desk/narrative/05-the-wire-has-two-ends.md`.

Scene inventory: two desk symptoms/shortcut correction (L24–54); stopped service and restoration (L58–102); catch-up script exposes client exhaustion (L106–156); fix plus missed-alert accountability (L162–174). The second failure is causally linked to catching up after the first.

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear | Coincidental reported service failure at L7, L13, and L24, later traced to a file-lock crash at L75, disrupts Jared's backups and Ken's intake. The subsequent unpooled retry storm is causal—Jared's chosen catch-up method, L106 and L148. |
| Turning Point Progressive Complication | Clear | Fixing the stale shortcut produces the same refusal rather than success, L52–54; restoring the service appears to solve it, L91–102, but the catch-up run fails, L106–119. Healthy server evidence and client TIME_WAIT records reveal that the new failure is on Jared's own workstation, L133–154. |
| Crisis | Not found as a binary choice | The audit deadline, L156, is pressure, but the text does not show Ethan choosing between mutually exclusive costly alternatives. Pooling and the timeout adjustment are both used, L168. Their compatibility is fine engineering, but not evidence of an Irreconcilable Goods crisis. |
| Climax | Clear technically; partial as crisis payoff | Jared rewrites the pool and Ethan changes the workstation setting, L168. The action solves the initiating backup problem; a choice-level consequence for Ethan is less connected to that instant. |
| Resolution | Clear | The run completes, L168; missed backups require Jared's evening sweep and Ethan stays until nine, L170–174. His earlier decision not to raise the alert is acknowledged, L172, rather than hidden behind Jared's error. |

Value change: blaming the distant server → accepting local/own responsibility. Keep the two-ended diagnostic reversal. If a strict five-commandment arc is desired, identify a real existing decision around the alert, recovery, or ownership; do not invent false incompatibility between compatible fixes.

### Episode 06 — The Portland Flood

Source: `docs/portland-desk/narrative/06-the-portland-flood.md`.

Scene inventory: flood call/site safety (L5–34); attempted hardware reset and replacement (L36–46); VLAN/trunk construction and verification (L50–105); mass restart reveals DHCP failure (L109–140); mostly-restored verification/cost/duty (L144–152).

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear | Coincidental flood and surge, L5–9 and L24, force a recovery before opening, L30. |
| Turning Point Progressive Complication | Clear | Resetting the power supplies fails, L38–42. Rebuilt links look healthy, L105, but the morning restart strands users, L111–138. The revelation that the address pool is exhausted defeats treating physical restoration as complete recovery. |
| Crisis | Partial | Irreconcilable Goods is suggested by restoring critical billing/telemetry/dispatch before eight, L30 and L52, versus restoring every shipping printer. The lack of time to move their patch cord is reported at L150. The competing service values are present, but the priority choice is not clearly located before the result. |
| Climax | Clear | Ethan clears stale leases and changes duration, L144; he walks the actual application-level verification, L146. This is his enacted recovery, supported by the team. |
| Resolution | Clear | Critical services return, but twelve printers remain unavailable until ten and the pooling window slips, L150. The overnight assignment, L152, changes future duties rather than making the recovery a cost-free victory. |

Value change: a rebuilt but unusable network → explicitly partial service restoration and greater responsibility. If tightening, a small clarification of the existing service-priority choice is sufficient; no bigger flood is needed.

### Episode 07 — The Port That Is Open

Source: `docs/portland-desk/narrative/07-the-port-that-is-open.md`.

Scene inventory: Jared's Telnet request (L24–40); Maya's mail profile (L44–60); Dale's transfer and Leah's plant request (L64–96, two related calls); HR change-ticket fragment (L100–102); Sam's RDP request (L106–122); legacy-switch workaround and Saturday rupture (L126–136). Several are short service vignettes. The Saturday incident is a separate, causally linked scene, not merely another port example.

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear for the opening service scene | Causal: Jared asks to use the Telnet script to repair a VLAN, L24–26. Ethan is pressed to approve a familiar method; other callers extend the workday's competing requests. |
| Turning Point Progressive Complication | Partial at chapter scale | The remembered captured password, L32, invalidates the easy approval. Dale's unsupported SFTP proposal, L72, genuinely complicates that separate transfer. The six switches that cannot run SSH without firmware, L126, complicate standardization. These are not all failures of one strategy; the calls share a theme and queue rather than a single causal chain. |
| Crisis | Partial for the day's main arc; clearer in the Saturday scene | Standards versus callers' speed/convenience is a credible pressure, but “allow an exposed service or use an available secure substitute” is not automatically a meaningful binary crisis. In the Saturday scene, an implicit Best Bad Choice is supported at L130: keep waiting while a switch is down or risk acting without the uplink information. The on-call alternative is revealed afterward, L132, so do not pretend Ethan knowingly rejected it at the time. |
| Climax | Clear for the choices actually shown | Ethan refuses public RDP and specifies the constrained alternative, L122. In the consequence scene, he guesses and shuts the wrong port, L130. These are enacted choices, but they belong to different local arcs rather than one continuous port-ticket climax. |
| Resolution | Clear | Secure configurations and an acknowledged legacy workaround result, L124–128. The shortcut costs the Gresham station 35 minutes and damages the Jared relationship, L130–136. E08:11 collects that relationship through a later ordinary call, consistent with the author's action-based exception. |

Value change: confident policy correction → recognition of the operational and relational debt left by a workaround. Preserve the Saturday scene and its flawed choice. Decide whether the chapter is intentionally a queue montage or should foreground the Jared thread more clearly; do not force every phone call into the same incident.

### Episode 08 — Prove Who You Are

Source: `docs/portland-desk/narrative/08-prove-who-you-are.md`.

Scene inventory: Nora's password/reset (L22–38); Todd's factor misconception/enrollment plus Rita's token alternative (L42–76); Dev's script lockout and Lila's Hello question (L80–94); Reggie's physical-access inquiry (L98–104); resolutions and the manager's exception/complaint/promotion sequence (L108–120). The short Rita/Lila exchanges are teaching vignettes; the manager exchange is reported retrospectively rather than absent.

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear as a composite service-day setup | User actions create causal problems: Todd wipes his phone, L42; Dev's script reuses a secret, L80–82; Nora also faces timed policy expiration, L22–26. The lockout wave, L7, gives Ethan a task. A single chapter-wide forcing incident is less distinct than the individual service triggers. |
| Turning Point Progressive Complication | Partial at chapter scale | Todd's two-secrets claim must be corrected, L44–56, and unlocking Dev without fixing the source would repeat the failure, L84. The requested quarter-end exception, L114, introduces genuine authority/communication pressure. The cases themselves do not successively defeat one Ethan strategy. |
| Crisis | Partial, not absent action | The manager's desired exception versus enforcement is evidenced at L114; a Best Bad Choice could involve control risk versus professional friction. However, the text specifically charges Ethan's curtness, and Jules is both polite and firm at L116. Security and courtesy are therefore not demonstrated irreconcilable goods. Do not invent a false binary from the later penalty. |
| Climax | Clear, in retrospective narration | Ethan says no in writing, L114; the narrated action counts. He also fixes Dev's actual lockout source and verifies the zero counter, L108. A live email scene might sharpen the choice, but its absence is not a missing action. |
| Resolution | Clear | The fixes work, L108–112, but the complaint contributes to his lost promotion, L114–118. Reggie's investigation remains uncertain, L120; it is not falsely presented as a solved physical case. The promotion thread continues in E09:9 and E10:9. |

Value change: technical certainty → professional constraint caused partly by manner. Preserve the fact that being correct did not excuse being curt. If stronger crisis structure is desired, use the existing exchange to show Ethan's actual pressure and decision rather than claiming secure service and empathy cannot coexist.

### Episode 09 — Don't Click That

Source: `docs/portland-desk/narrative/09-dont-click-that.md`.

Scene inventory: Maya's broad phish (L22–36); Sam's targeted lure and the CFO impersonation (L42–58); Todd's SMS vignette (L62–66); Dev's fatigue incident (L70–76); certificate/vendor verification (L80–86); wire-run closure, saved indicators, secondhand vishing, and lost Friday (L90–98). These are related social-engineering cases, not proof that one failed local response caused every next case.

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear | Causal attacker messages: the mailbox lure, L22, and especially the forged CFO request, L48–54, pressure recipients toward unsafe action before close of business. |
| Turning Point Progressive Complication | Partial at chapter scale | Personal detail defeats Sam's “too informed to be spam” assumption, L42–46; the valid certificate does not establish the vendor's identity, L80–86. Those are useful revelatory pivots. But the CFO spoof has already been recognized, checked by phone, and frozen at L56–58, so later cases are not all escalation of an unresolved initial strategy. |
| Crisis | Partial | Holding legitimate business while verifying fraud creates competing goods, evidenced by the stated business deadline, L48, and the three-hour batch hold/payment delay, L92. The passage does not clearly locate Ethan's own forced decision between the alternatives. Marisol/AP legitimately own the finance hold; do not silently assign that authority to Ethan. |
| Climax | Clear for local protective actions; partial as one late chapter climax | Ethan directs trusted-number verification and escalates with headers, L56–58; Marisol performs the callback and AP freezes. These are supported collaborative actions. The Wire Run at L90 mostly reprises the same confirmation and cancellation rather than clearly adding a distinct Ethan decision. |
| Resolution | Clear | The wire change is cancelled and the malicious archive purged, L90. Verification delays real payments, L92, and costs Ethan his requested Friday, L98. His indicator collection, L94, later proves nondecisive in E12:122, an intentional limitation rather than an unpaid setup. |

Value change: reassurance by logos/authority → verification that protects money but inconveniences legitimate work. Preserve Marisol's complementary expertise. Clarify provisional hold versus final clearance if a stronger central wire arc is wanted, rather than inventing a still-moving fraudulent payment.

### Episode 10 — Something on the Box

Source: `docs/portland-desk/narrative/10-something-on-the-box.md`.

Scene inventory: Maya's unwanted bundle (L33–64); Sam's USB triage (L68–93); Todd's share-spreading host (L97–128); Rina's ransomware response (L134–161); Ken's certificate/reassurance failure (L165–171); SOC resolution and Ethan's incident note (L175–181). The chapter presents a set of malware cases; Ken's sub-arc carries the principal relationship cost.

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear | Causal installations/delivery choices create cases: Maya installed a bundled utility, L35; Todd copied material to a share, L101; Ken's similar installer appears at L165. Ethan's immediate goal is safe triage/containment under the SOC instruction, L7. |
| Turning Point Progressive Complication | Clear locally; partial as one chapter strategy | The pattern grows from one noisy installation to share spread, L97–126. For Ken's arc, revocation information defeats Ethan's assurance based on a valid-looking signature, L167–171. The other cases are not all consequences of the Maya cleanup failing. |
| Crisis | Partial at chapter scale | Todd's unfinished renewal proposal versus immediate isolation supplies a credible local Best Bad Choice, L126–128: lose the business copy's continuity or leave active spread connected. Ethan issues the instruction and Todd enacts it. Ken's revocation revelation does not show an equally explicit binary response for Ethan before the later re-image/report. Do not invent a temptation to conceal the mistake. |
| Climax | Clear for the recorded actions | Ethan orders the interruption, L126–128; SOC containment/removal and re-images occur, L175–177; he writes the incident note with his own two minutes, L179. Jules requiring the note does not mean Ethan's action is absent, though it is less self-initiated than the final application in Episode 12. |
| Resolution | Clear | Rina regains the previous backup but loses edits, L175. Ken loses local notes and trust, L177–181; Ethan must own the reassurance that contributed to it. E11:9 and E11:90 continue that relationship through changed behavior. |

Value change: apparent assurance from signatures → responsibility for verification limits. The costly Ken arc is worth preserving; if revising, make its actual response to the revealed mistake clearer rather than adding another infection.

### Episode 11 — The Air Is Shared

Source: `docs/portland-desk/narrative/11-the-air-is-shared.md`.

Scene inventory: Maya's failed connection and wired workaround (L22–34); Todd's hotel/WEP vignette (L38–50); Rita's separate rogue router (L54–60); Dev's deauth symptoms (L64–72); physical lobby investigation (L76–80); distinct device containment, scanner-profile choice, and dock cost (L84–92). The hotel call remains contextual, not a complication caused by the local attack.

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear | Causal impersonation: an unknown radio duplicates the corporate SSID, L26, later found deliberately placed under the bench, L76. Maya's failed connection and Ken's prior safety question, L9 and L11, give Ethan a concrete access-and-trust problem. |
| Turning Point Progressive Complication | Clear for the central wireless-safety arc | Wired docking is a temporary workaround, L32–34; deauth reports and the lobby device expand the problem, L68 and L76. Crucially, removing the device is not enough: legacy scanner profiles still fail server-identity validation, L86. That revelation defeats “remove this radio and resume as before.” |
| Crisis | Clear, implicit Best Bad Choice | At L86 Ethan can return devices to work with profiles still capable of trusting another impostor, or keep affected scanners off wireless until corrected. The stated ongoing vulnerability and known dock dependence supply both costs; L90 confirms the throughput/time price rather than inventing one. |
| Climax | Clear | Ethan calls Ken and keeps the affected scanners offline until their profiles are replaced, L86. Security's separate pouching of the attack device, L84, is appropriate delegation and does not replace his scanner decision. |
| Resolution | Clear | The duplicate signal disappears, L84; managed profiles are enforced, L90, but dock work is manual until noon and Ethan loses Saturday. The unfilled camera and kept baseline, L88–92, carry into E12:9 and E12:120. |

Value change: blanket reassurance → verified, deliberately costly caution. The five recently repaired facts should not be reflagged: the two devices now have distinct dispositions, the profile decision has a cause, and its cost is explicit. This is one of the stronger current chapter-level chains.

### Episode 12 — When the Ticket Escalates

Source: `docs/portland-desk/narrative/12-when-the-ticket-escalates.md`.

Scene inventory: Maya's contained-adware contrast vignette (L22–44); Nora's mailbox/host investigation (L48–70); Todd/jump-host/plant linkage (L76–90); declaration and collection (L94–104); containment cost (L108–110); after-action reconstruction (L114–126); referral/application coda (L130–136). The first benign case is contrast, not proof that all four tickets share one infection.

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear for the main incident | Causal compromise creates Nora's quiet mailbox problem, L48–56. Ethan's local goal changes from routine service to recognizing and stopping an incident. Maya's earlier noise is a separate contrast scene. |
| Turning Point Progressive Complication | Clear | Disabling one forwarding rule, L58, does not explain or stop host beaconing, L66–68; shared jump-host contact and plant egress, L82–88, defeat treating the cases as isolated tickets. The second stream and renewed enumeration create the final operational pressure, established at L104 and reconstructed at L124. These are revelatory complications of the same breach. |
| Crisis | Clear for containment, reported retrospectively | Best Bad Choice at L124: interrupt a remotely streamed snapshot to stop an actively enumerating host, losing that complete earlier state, or leave production exposure while collection continues. Nia correctly makes containment the priority at L126. Knowing which bad option is professionally preferable does not erase its real cost. Do not confuse this with erasing powered RAM; the repaired passage explicitly preserves it. |
| Climax | Clear, with a presentation qualification | Ethan pulls Todd's cable, L124; that action enacts his containment decision. The live sequence at L104 does not show it yet, but retrospective narration is evidence. The later application choice and deletion of self-justification, L134–136, provide a second, character-level decisive act. |
| Resolution | Clear | The breach is contained at the price of plant manual operation and a nine-day gateway rebuild, L110. The incomplete stream, missing playbook, and needed collection preparation are recorded, L120–126. Ethan submits the application, L136; the job offer is intentionally outside Book 0, not missing closure. |

Value change: fast technical response → accountable judgment that includes the limits and costs of a defensible act. Consider locating the cable pull in the live sequence to strengthen immediate crisis/action/consequence linkage; do not rewrite the repaired technical mechanism or make Ethan delay containment. The existing account is structurally supported, not a fresh factual failure.

## Author decisions and limits

- Decide whether every chapter is intended to be a complete Story Grid arc or whether some remain intentionally useful procedural/service vignettes inside an episodic formation book. The repository's higher-ranked schema explicitly treats beat grammar as a quality lever, not an overriding gate. A deliberate departure should be labeled, not falsely counted as a complete crisis.
- If selecting a small first revision pass, start with Episode 03 or 05 to clarify the central decision, then Episode 08 or 09 to clarify which character owns the costly choice. Do not batch-rewrite all thirteen. Preserve clear actions that are already present in retrospective narration.
- Genre and the proposed controlling idea above are interpretations; no new canon, mandated genre, promised job offer, or reader outcome is established here.
- The scene inventory identifies local service cases and fragments; it is not a separate five-row map for every paragraph or side exchange. The five-row maps evaluate each chapter's main arc. A deeper single-scene audit can follow after the author chooses the intended main scene in the partial chapters.
- This is not a new technical accuracy certification, browser audit, or reader study. The recently fixed FTPS, certificate validation, device-disposition, inbox-rule, and memory-transfer facts were read in their repaired form and were not recycled as current defects.
- Reference notes and the supplied PDF were both read. The live Story Grid page was not fetched. No story edits, report writes, commits, pushes, or subagent delegations were performed by the reviewer. The parent assistant saved and checked this report.

**Final verdict: targeted revision recommended.** The current story has substantial earned causality, character continuity, and paid consequences. Its biggest remaining structural opportunity is making consequential choice as clear as diagnosis in the weaker chapter arcs, while retaining the intentionally episodic, proportionate workplace form.
