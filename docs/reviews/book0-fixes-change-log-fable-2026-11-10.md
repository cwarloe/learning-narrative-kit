# Book 0 fixes: change log

Date: 2026-11-10. Writer: Claude (Fable 5.2). Work order: `docs/reviews/book0-book1-canon-handoff-fable-2026-11-10.md` (findings 1 to 13 and the handoff checklist), with Charles's five approved decisions. Nothing is committed. The NADF repo was read, not edited.

Short names: **PD** = `docs/portland-desk/`, **nar** = `PD/narrative/`, **wb** = `PD/workbench/`, **art** = `PD/artifacts/`. Line numbers are for the files as they now stand. "F" numbers are the work order's findings.

## (b) Canon file edits (read these first)

### `docs/research/PORTLAND_TIMELINE.md`

The Timeline did forbid Nia's move: section 3 rule 1 said Chicago is "where central IT and the SOC leadership sit". I recorded the approved move as a dated exception and left the rest of the rule alone.

| Lines | Change | Finding |
|---|---|---|
| 120 | Added: Harrowmere makes and distributes industrial equipment; write the plant in plain plant language, never as a water or wastewater utility; the product is not specified. | F12, decision 4 |
| 121 | "SOC leadership sit" now reads "sit through Ep 12", followed by the exception: Nia moves to Portland with her promotion to Security Operations Manager right after Ep 12 and runs security operations from the Portland pod in NADF; in Ep 12 she is still in Chicago, by bridge only. | F4, F5, decision 2 |
| 152 | Security+ cell: added "neither exam is taken on the page". The 29-month figure is unchanged. | F10 |
| 153 | End-of-Ep-12 row: "late June to early July"; Nia is "moving from Chicago to Portland with the job". | F4, F11 |
| 154 | August row: Leah made the same move "a few weeks ahead of him". Pay cell changed from "—" to "Not stated". | F2, F10 |
| 162 to 164 | Open-questions paragraph: recorded the three 2026-11-10 settlements; listed two things still open (what the plant makes; Ethan's analyst pay). Removed "None right now." | F12, F10 |

### `docs/research/PORTLAND_AUTHOR_BIBLE.md`

| Lines | Change | Finding |
|---|---|---|
| 9 | "Tier 2 Help Desk Lead at Harrowmere Equipment Group's" operations center is now "Tier 2 support technician at Harrowmere Northwest's" operations center, and "He is never the desk lead; Jules is." | F13 |
| 16 | "a wastewater pump to keep running" is now "a production line to keep running". | F12 |
| 19 | Security Operations is run from Chicago "through Ep 12". Added the passing-contact rule for the Portland pod (badges, one signature, one voice; he has not worked with them). | F4, decision 5 |
| 20 | Leah: "Senior Plant Systems Specialist" is now "Plant Operations Lead"; "a few months" is now "a few weeks"; added that she says in the Ep 12 review she is leaving in three weeks. | F2, F13 |
| 22 | Nia: "Tier 1/2 escalation dossier ... earns him a seat at the enterprise security table" is now "Tier 2 escalation dossier catches her attention"; she is on the bridge from Chicago for all of Ep 12; she moves to Portland with the promotion. | F4, F5, F10 |
| 31 | Reconcile item 4 (Leah's role, resolved 2026-10-29): title revised to Plant Operations Lead with a controls and SCADA background; a few weeks ahead of Ethan; no finance or inventory history in Book 0. **This overrides the 2026-10-29 wording "Senior Controls Tech". See open item 2.** | F2, F13 |
| 64 | Cast diagram: Leah's label is "Plant Operations Lead". | F13 |
| 89 | Security+ "about twenty-six months into IT" is now "about twenty-nine months into IT (just after Ep 12; it is not earned on the page in Book 0)". | F10 |
| 102 | Jules: the referral is to "the parent's security operations" (was "Chicago's"). Added the on-page cost, matching Ep 12 (see section c). | F3 |
| 104 to 105 | Leah heading and role line: Plant Operations Lead; came up through controls and SCADA. | F13 |
| 107 to 109 | Leah: clipboard holds "line drawings and wiring diagrams" (was piping diagrams); the "hundreds of thousands of gallons ... effluent overflow ... pump seals" sentence is now a stopped line, scrapped work and overtime, product not specified; "staunchest operational ally" is replaced by what the shipped chapters show (she calls him directly; wary and tired by Ep 12; they know each other and are not close). | F12, F13 |
| 136 | Nia (3.3): "and moves to Portland with the job". | F4 |
| 145 | Registry, Ethan: "dock, then Tier 1 desk, then Tier 2 from January of Year 4". | F10 |
| 165 | Registry, Nia: "(moves to Portland after Ep 12)". | F4 |
| 170 to 172 | Registry: Carlos Gomez is now "Gresham shipping clerk (Ep 03; ticket artifact)"; new rows for Lila (surname none, human resources, Ep 08) and Dana Shah (in Book 0 only a signature on a ticket reply, Ep 09). | F13, decision 5 |
| 193, 354 | Ep 09 carry-forward, matrix and card: "The phishing campaign is a scout for what comes in Ep 12" is replaced. Ethan starts saving indicators nobody asked for; in Ep 12 none match; the Ep 09 phish is not a scout. The card notes the reply signed D. Shah. | F13 |
| 385 | Card 12 cast: added one unnamed voice from the Portland pod on the bridge. | F4 |
| 390 | Card 12 carry-forward: Nia is "newly promoted and moving to Portland". | F4 |

Not changed in the Bible: the cast diagram still groups Nia under "Chicago Central IT" (true through Ep 12). Section 3.3 is still titled "The Chicago Presence".

## (a) Every other file changed

### Narrative

| File and lines | Change | Finding |
|---|---|---|
| `nar/03` l.7 | "logistics annex and water pump station two miles south" is now "logistics annex two miles south, and the mechanical room beside it". | F12 |
| `nar/03` l.11 | "automated pump loggers" is now "the building-systems loggers". | F12 |
| `nar/03` l.70, 72 | "water pump annex ... intake turbines", "water pressure telemetry logger", "pump house" are now the mechanical room beside the warehouse, air handlers, "building-systems logger". Reggie's Bible role (building management systems, HVAC) is the source. | F12 |
| `nar/03` l.74, 82, 111 | Hostnames `PDX-PUMP-LOG02` and `PDX-PUMP-DB01` renamed `PDX-BMS-LOG02` and `PDX-BMS-DB01`. Addresses unchanged. | F12, rule 13 |
| `nar/03` l.117 to 175 (11 places) | Dock clerk "Frank" renamed "Carlos" (Carlos Gomez, already in the registry as warehouse shipping). Frank is Ethan's father. | F13, rule 14 |
| `nar/05` l.126, 136 | Prompt `PS C:\Users\jvance>` on Jared's workstation is now `PS C:\Users\jlindqvist>`. | F13, rule 13 |
| `nar/06` l.52 | "twenty for intake telemetry" and "an intake logger" are now "plant telemetry" and "a telemetry logger". | F12 |
| `nar/06` l.59 | VLAN name `CORP_WATER_BILLING` is now `CORP_ORDER_BILLING`. | F12, rule 13 |
| `nar/07` l.82 | "called from the treatment facility down by the river" is now "called from the Willamette River plant". "Leah ran plant ops" is kept. | F12, F13 |
| `nar/07` l.84, 88, 92, 94 | "industrial pumps humming" is "the plant floor loud"; "overflow alarms" is "line alarms" (twice); "reading tank levels ... a malicious valve command" is "reading sensor values ... a command to a machine on your line"; "touches the pumps" is "touches the line"; "treatment line" is "production line". Drill 1 is not in this file. | F12 |
| `nar/08` l.24 | Nora's passwords "Spring2024!, Summer2024!" are now "Spring2025!, Summer2025!" (the episode is October 2025). | F11 |
| `nar/09` l.94 | Added three sentences: the security team's one-line reply to his escalation, signed D. Shah (about 60 new words). | F4, decision 5 |
| `nar/11` l.84 | "Security brought a radio-shielding pouch" is now someone sent down from the floor above, wearing an Equipment Group badge, who leaves without asking who found it (about 25 new words). | F4, decision 5 |
| `nar/12` l.22 to 24 | Maya's entrance rewritten. Gone: the carried "like a wet umbrella" entrance and "standup ... in twelve minutes". She now opens on what changed since February: she walked it over without calling, installed nothing, uses the portal, and has her spreadsheets on the share. New `date-ok` marker with a reason. | F13 (rules 7, 11) |
| `nar/12` l.76 to 82 | Todd's USB: the stick is marked "carrier rates" in marker (was "Client Deck Final"); the file is `rate_sheet_Q3.pdf.exe` (was `SOW_final.pdf.exe`, which stays in Ep 10). Two new lines call back Sam's February stick. New `date-ok` marker with a reason. | F13 (rule 7) |
| `nar/12` l.106 to 110 | Upstairs beat: Ethan asks about upstairs; Jules says why nobody is coming down; one unknown man's voice says the Portland pod is on the bridge (about 115 new words). New `date-ok` marker with a reason. | F4, decision 5 |
| `nar/12` l.116 | "treatment line" is now "production line". | F12 |
| `nar/12` l.128 | New paragraph: Leah says she is leaving the plant (about 50 new words). | F2, decision 3 |
| `nar/12` l.134 | Two sentences added to Nia's ruling so the lost capture stays charged. | F3, rule 1 |
| `nar/12` l.140 to 144 | The posting scene: Jules's cost for the referral, and Nia's move (about 95 new words; the old paragraph's other sentences are kept). | F3, F4, rule 9 |
| `nar/12` l.146 | Added: "Under certifications I typed Security+ and then *scheduled*, because scheduled was all it was." | F10, checklist |
| `nar/12` l.161 | Glossary table: "Tier 1 desk technicians" is now "Desk technicians". | F10 |

Total new prose in Ep 12 is about 330 words across six places. No single scene took more than about 150.

### Workbench (labs)

| File and lines | Change | Finding |
|---|---|---|
| `wb/02` l.225, 246 | Event timestamps `2026-08-14` are now `2024-08-22` (the lab's own date at l.509). | F11 |
| `wb/02` l.414 | "Water Bureau service counter" is now "Rivergate parts counter". | F12 |
| `wb/03` l.3, 50, 52, 261 to 263, 545 to 547, 568 | Pump station, pump house and pump loggers are now the Gresham logistics annex, the mechanical room and building-systems loggers; hostnames renamed to `PDX-BMS-LOG02` and `PDX-BMS-DB01` to match the chapter. | F12, rule 13 |
| `wb/03` l.23 to 598 (9 places) | "Frank" is now "Carlos". | F13 |
| `wb/04` l.109 | Example SOA serial `2026101801` is now `2025031101` (the lab is dated 2025-03-11). | F11 |
| `wb/06` l.95, 111, 157 | `CORP_WATER_BILLING` is now `CORP_ORDER_BILLING`. | F12, rule 13 |
| `wb/06` l.96, 112, 261, 298, 300 | "River Intake Modbus Loggers", "river level sensors", "river telemetry sensor intake", "Water Accounting", "SCADA Intake Pressure Loggers" are now plant, line, order-billing and telemetry wording. | F12 |
| `wb/07` l.137, 175 | **Drill 1 touched.** Login password `C1sco_Sw!tch_2026` is now `C1sco_Sw!tch_2025` (frame 122 keystroke `6` is now `5`). The episode is August 2025. Capture regenerated; see checks. | F11 |
| `wb/07` l.385, 396, 477, 486 | Leah's ticket: "East Treatment Line", pump and valve controllers, valve commands and "water level telemetry ... environmental" hazard are now "East Production Line", line controllers, commands to line equipment and sensor telemetry. Ports unchanged. | F12 |
| `wb/08` l.51, 105, 514 | `Spring2024!`, `Summer2024!` are now `Spring2025!`, `Summer2025!`. | F11 |
| `wb/10` l.4, 542, 605 | "Your Role" and the two note signatures: Tier 1 is now Tier 2. | F10 |
| `wb/10` l.229 | Event time `2026-10-22T10:17:42` is now `2026-02-12T10:17:42`. | F11 |
| `wb/11` l.4, 478, 530 | "Your Role" and the two note signatures: Tier 1 is now Tier 2. | F10 |
| `wb/12` l.3, 4, 141, 320, 544, 551, 660 | Tier 1 labels for Ethan and the learner's role are now Tier 2, or "the desk" where no tier is needed. | F10 |
| `wb/12` l.50, 434, 563 | USB wording matches the chapter ("carrier rates"). | F13, rule 13 |
| `wb/12` l.306, 310, 434, 564, 595 to 596 | Dropper file is `rate_sheet_Q3.pdf.exe`, with a new SHA-256 (`4B7E19C2...6A14`). The lab had reused Ep 10's file name and Ep 10's hash, which contradicted the chapter's "none of my saved hashes matched". | F13, rule 13 |
| `wb/12` l.490 | Maya's adware is `CouponBlast.exe`, as in the chapter (the lab said `couponbar.dll`, which is Ep 10's). | rule 13 |
| `wb/12` l.570 to 571 | "Willamette River Water Treatment Facility" is now "the Willamette River plant". | F12 |
| `wb/12` l.619, 668 | "EDR Alert 2026-1022-991" and "Case-2026-1022" (an October date in a June lab) are now "EDR Alert 0624-991" and "Case-INC0075950". | F11, rule 13 |
| `wb/12` l.707 | "Tier 2 analysts" is now "SOC analysts", so it is not read as Ethan's tier. | F10 |

### Artifacts and tools

| File | Change | Finding |
|---|---|---|
| `art/tickets.csv`, `art/tickets.json` | All 39 timestamps moved from `2026-10-20` to `2025-08-12` (this is the Ep 07 queue: `INC0063140` to `INC0063153`, and wb/07's note already carries 2025-08-12 15:25:12). "Tier 1 Service Desk" is now correct for that date and is unchanged. Attachment `INV_Oct2026_9942.pdf.iso` is now `INV_Aug2025_9942.pdf.iso`. Leah's ticket: water pump, valve, "East Treatment Line" and overflow wording replaced; the doubled word "Telemetry telemetry" fixed. | F11, F12 |
| `art/ipconfig_all.txt`, `art/terminal_dumps/ipconfig_all.txt` | Lease dates are now Tuesday, August 12, 2025 and Wednesday, August 13, 2025 (linked from wb/07). | F11 |
| `art/gpresult.txt`, `art/terminal_dumps/gpresult.txt` | Dates moved to August 12, 2025; copyright year and the GPO name suffix changed from 2026 to 2025. | F11 |
| `art/sample_legit_payroll.eml`, `art/sample_phish_invoice.eml`, `art/sample_spoofed_exec.eml`, and the same three under `art/eml_samples/` | Header dates moved from Tue, 20 Oct 2026 to Tue, 12 Aug 2025; message IDs and the attachment name follow. | F11 |
| `art/phishing_samples.json` | Attachment name follows the email. | F11 |
| `art/security_events.json` | `2026-10-20` is now `2025-10-20` (linked from wb/08, which is dated 2025-10-20). | F11 |
| `art/eml_samples/sample_credential_harvest_urgent.eml`, `art/eml_samples/sample_legit_internal_auth.eml` | Wed, 21 Oct 2026 -0700 is now Wed, 10 Dec 2025 -0800 (the Ep 09 date; a Wednesday). | F11 |
| `art/phishing_iocs.json` | `incident_date` is now `2025-12-10T08:12:12-08:00`; `investigation_id` "SEC-PHISH-2026-1021" is now `ESC0006820`, the Ep 09 lab's own escalation ID. | F11, rule 13 |
| `art/powershell_event_4104.json`, `art/event_7045_dump.txt`, `art/autoruns_dump.txt` | `2026-10-22` is now `2026-02-12` (linked from wb/10). | F11 |
| `art/jared-telnet-capture.pcap` | Regenerated: new password keystroke and capture time 2025-08-12 08:44:12 UTC (was 2026-10-13). | F11 |
| `tools/generate_ep07_telnet_capture.py` l.25, 112 | Capture start date and the password string, to match the drill. | F11 |

## (c) Facts Book 1 must now match

All quotes are exact, from the narrative files.

**1. What the referral costs Jules** (`nar/12` l.140 to 144).
- Jules comes to his desk "with her coffee and two printouts".
- Ethan: "You don't give Chicago anything."
- Jules: "She won't be Chicago much longer. She's moving out here to run it."
- The second printout "was a backfill request for a Tier 2 seat, routed to Central IT, with her signature already on it."
- Jules: "These people are. They've waited two quarters for me to finish their agent rollout, and they'll sit on this until I do. If you get the job, your overnights are mine until they sign."
- So the facts are: Jules has delayed a Central IT agent rollout for two quarters; her backfill for Ethan's Tier 2 seat depends on Central IT signing; she works his overnight shifts until they do. She does not thank him and does not explain. The scene still ends "I did not get to ask her why."
- Nia "still wants the application, and she wants the second capture in it."

**2. Leah** (title: `nar/07` l.82; departure: `nar/12` l.128).
- One title in Book 0: **plant operations lead**, Willamette River plant. On the page: "Leah Moreno from Portland plant operations called from the Willamette River plant. Leah ran plant ops with a steel clipboard and zero patience for corporate drift". Labs and tickets say "Portland Plant Operations Lead". The registry row is unchanged ("Willamette River plant operations lead").
- Departure line, in the after-action review: "Not mine," Leah said. "I'm off the plant in three weeks. I took a job with Equipment Group's applications team. Whoever gets my crew gets a gateway they have never seen go dark and a playbook nobody has written." She looked at me when she said it, and then she looked at her clipboard.
- "Not mine" answers Nia's note *plant isolation playbook, owner TBD*. Leah has a crew. Where the applications team sits is not stated.
- Dates: the lab dates the incident Wednesday 2026-06-24, so the review ("the following Tuesday") is 30 June 2026 and "three weeks" puts her start at about 21 July. Ethan's day 1 in Book 1 is about 10 August. That is about three weeks ahead of him.
- Where they stand: she holds him to account ("I found out my gateway was going dark from a phone call, not from a plan", l.122, unchanged), she is tired, not angry (l.116, unchanged), and she looks at him when she names the dark gateway. They know each other. They are not friends.
- Book 0 gives her no finance or inventory history.

**3. The upstairs team** (three touches; Ethan has never worked with any of them).
- Ep 09 (December 2025), `nar/09` l.94: "The reply on my escalation came back two days later from the parent company's security team, the people with the Equipment Group badges one floor up. It was one line, *Received, blocked at the gateway*, signed *D. Shah*. I had shared an elevator with that team for more than a year and could not have picked D. Shah out of it." Dana is only this signature. Ethan does not know her first name, her face, or her gender.
- Ep 11 (April 2026), `nar/11` l.84: "Security sent someone down from the floor above with a radio-shielding pouch. He wore an Equipment Group badge, sealed the device inside for the incident team, and left without asking who had found it". He is unnamed, and they do not speak.
- Ep 12 (24 June 2026), `nar/12` l.106 to 110: "What about upstairs?" I asked. "The parent company's security team had the floor above ours. I knew them as Equipment Group badges in the elevator and as one signature, *D. Shah*, on a one-line reply in December. I had never worked a ticket with any of them." Jules: "They answer to Nia, not to me, and they work from their own consoles. They'll be on the bridge. Nobody is coming down the stairs to hold your hand, so start the capture." Then, on the bridge: "A man's voice I did not know said the Portland pod was on. He was one floor above my head, and it was the first time I had heard any of them speak."
- The man on the bridge is unnamed. Book 1 may make him Owen or Cal, or leave him. Nothing in Book 0 says the Ep 11 man and the Ep 12 voice are the same person.
- Nobody teaches Ethan to separate what he saw from what he thinks. His one-breath attack story (`nar/12` l.70) is unchanged and unchallenged.

**4. Nia's move.**
- In Ep 12 she is in Chicago throughout: "Senior CSIRT Lead Nia Alvarez and the incident command team from Chicago are bridging onto our operations floor" (l.102), "Nia joined the bridge at 2:52" (l.110), "with Nia on the bridge from Chicago" (l.120).
- The move is stated once, by Jules, on the Monday after the review (6 July 2026 by the lab's date): "She's running security operations now." and "She won't be Chicago much longer. She's moving out here to run it." (l.140, 144). She has not arrived when Book 0 ends. The date she arrives is not stated.
- Canon: Timeline l.121 and l.153; Bible l.22 and l.136.
- What Nia has seen of Ethan (l.134): she ruled that stopping the spread came first, told him to write down why he pulled the cable, and said: "And I am still short the one capture that would have shown me what that machine was doing when it found the shares. I don't get that one back." It went into lessons learned "with my name on it".

**5. The plant.**
- It is "the Willamette River plant". It has a "plant floor", a "production line", "line alarms", a telemetry gateway (`GW-PLANT-04`, "the SCADA edge gateway"), a control network, and a crew of operators who can run the line "on manual override" (`nar/07` l.82 to 94; `nar/12` l.90, 116).
- The lab names an "East Production Line" in Building 4 (`wb/07` l.385).
- No product is named anywhere. No water, treatment, pump-station, or city-agency wording remains in `PD/`.
- In Ep 12 the gateway was isolated, "three operators were working a double because of it", and it "came back nine days later, after Jared rebuilt it" (l.116, unchanged).
- Renamed identifiers: `CORP_WATER_BILLING` is `CORP_ORDER_BILLING`; `PDX-PUMP-LOG02` and `PDX-PUMP-DB01` are `PDX-BMS-LOG02` and `PDX-BMS-DB01` (these two are in the mechanical room beside the Gresham warehouse, not at the plant).

**6. Ethan's tier and certificates.**
- Tier 2 since January 2026 (`nar/10` l.9, unchanged: "It was my third week as Tier 2, a month later than I had wanted it"). No Ep 10 to 12 chapter or lab now calls him Tier 1. The backfill Jules files is "for a Tier 2 seat" (`nar/12` l.144).
- Security+ is not earned in Book 0: "Under certifications I typed Security+ and then *scheduled*, because scheduled was all it was." (`nar/12` l.146). The exam date is not stated on the page; the Timeline says about 29 months into IT, just after Ep 12 (late July 2026).
- Network+ is not shown as earned on any page of Book 0 and is not mentioned in Ep 12. The Timeline says he earned it about 13 months into IT.
- His pay upstairs: not stated (Timeline l.154).
- Book 0 ends with the application submitted and no offer, no raise and no thanks.

**7. The interrupted capture, for Book 1 to collect** (`nar/12` l.132 to 134, 146 to 148).
- He pulled Todd's network cable while a second memory dump was streaming to a remote collector. The first dump was complete and hashed. The second file was incomplete. A later local dump was taken under isolation.
- Nia's two asks: write down why, and have ready next time "local capture, or a tested containment channel that keeps the collector reachable".
- He wrote about it in the application and "cut the sentence where I explained that it had been a defensible call".

**8. Small facts that changed.**
- The Ep 12 USB: marked "carrier rates", file `rate_sheet_Q3.pdf.exe`, found by Todd on the shipping office floor. Sam's February stick (`CLIENT_DECK`, `SOW_final.pdf.exe`) is a different stick, and Ethan and Jules both remember it.
- The Gresham dock clerk in Ep 03 is Carlos (Gomez). The only Frank is Ethan's father.
- Jared's workstation login is `jlindqvist`.
- Maya in Ep 12: she uses the software portal since February, keeps her spreadsheets on the share, and presents to the VP at nine.

## (d) Open items for the author

1. **Product not specified.** What the Willamette River plant makes is still not stated. I used only "production line", "plant floor" and "line". Leah's Book 1 job depends on the answer.
2. **Leah's title overrides a dated decision.** The Bible's 2026-10-29 resolution said "Senior Controls Tech". The shipped Ep 07 ("ran plant ops"), Ep 12 (she has a crew and speaks for the plant) and the registry all say she leads plant operations, so I picked Plant Operations Lead and kept controls and SCADA as her background. NADF's cast file still says "Senior Controls & SCADA Technician" and "a few months".
3. **DNP3 in Ep 07.** Leah's request still names Modbus (502) and DNP3 (20000). DNP3 is mostly a utility protocol. I left it because the port lesson and the lab are built on it. Charles decides whether a factory plant keeps it.
4. **"SCADA" stays.** Factories use it, so I kept "SCADA edge gateway". Say so if it should go.
5. **Jules's cost uses two new details**: a Central IT "agent rollout" she has delayed "two quarters", and the backfill request. The Bible supports the habit (she delays Chicago's rollouts) but not the specifics. Confirm or reword.
6. **Ep 03's pump house became a mechanical room** with building-systems loggers, on the strength of Reggie's Bible role. A warehouse fire-pump house would also have been plausible; the decision named "water pump station" for removal, so I removed it. The hostnames are new.
7. **Network+ is never earned on the page.** I did not add it. Book 1 assumes it.
8. **The unnamed voice from the pod.** Book 1 should decide who he is, or that it does not matter.
9. **`tools/generate_helpdesk_artifacts.py` is stale and was not edited.** It still carries 2026-10-20 dates, `jvance@portland-ops.local`, and the water-pump ticket. The published artifacts had already been hand-edited away from it. Rerunning it into `art/` would undo these fixes.
10. **Labs for Ep 10 and Ep 11 keep "Tier 1" in generic headings** (for example "Tier 1 Host Infection Isolation & Containment Ticket Note", "Level 1 Service Desk Terminal"). I changed only the lines that name Ethan or the learner's role.
11. **Ep 10's lab has a practice ticket (`wb/10` l.423) where a warehouse clerk finds an unlabeled USB in the shipping bay.** It is marked "not from the chapter", so I left it, but it reads close to Ep 12's Todd beat.
12. **The scheduled task name `CacheCleanup` appears in both Ep 10 and the Ep 12 lab.** Not in the work order; not changed.
13. **Offer timing** (F11: about ten days from offer to start) is a Book 1 and Timeline question. Not changed.
14. **`gpresult.txt` copyright year.** I changed 2026 to 2025 to keep the date inside Book 0. The real tool prints its own fixed year; I did not look it up.
15. **Ep 12's title for Nia** is still "Senior CSIRT Lead" on the page; canon says Senior Incident Response Lead. Not in the work order; not changed.

## (e) Check results

| Check | Result |
|---|---|
| `python3 tools/check_dates.py` | PASS, "0 date finding(s)". Run after all edits. Four new `date-ok` markers, each with a reason. |
| `python3 tools/check_decks.py` | PASS, "57 files, 14 lnk-deck fences, 0 problems". |
| `python3 template/tools/check-links.py docs/portland-desk` | PASS, 29 files, all links and anchors valid. (Run with no argument it checks only the template: also PASS, 5 files.) |
| `tools/generate_ep07_telnet_capture.py`, then `python3 tools/check_ep07_capture.py` | Regenerated with scapy 2.8.0 from a throwaway virtual environment outside the repo. Check PASS: "137 frames; Telnet frames 101-137 match the drill table (37 rows); answer-key passwords match the keystrokes." Frame 101 is stamped 2025-08-12 08:44:12 UTC. |
| `python3 tools/find_bad_tables.py` | 2 findings, both in `nar/10` `gui` fences (l.43, l.144). Same 2 before my edits; I did not touch those lines. |
| `python3 tools/check_cleanliness.py` | PASS. |
| `python3 tools/voice_check.py` on `nar/12` | Reading aid, not a gate. Mean sentence length 17.5 words; no fragment runs. Its one "section-final aphorism" flag is a line I did not write (l.110, "I read out the first hash..."). |
| JSON artifacts | All five `art/*.json` files still parse. |
| `validate_unit.py`, `render_unit.py` | Not run: no folder under `examples/` changed. |
| `tools/check_decks_browser.py` and the headless page check | **Not run.** Playwright is not installed here. No deck or terminal fence was restructured; hostnames inside lab text were renamed consistently. |
| Leftover search | No match in `PD/` for water bureau, treatment, pump station, pump house, `CORP_WATER`, `PDX-PUMP`, `jvance`, or any date after June 2026. |
