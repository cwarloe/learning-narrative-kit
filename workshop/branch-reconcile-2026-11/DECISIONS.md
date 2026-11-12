# BRANCH vs ARCHIVE: hunk decisions

November 2026. BRANCH is `claude/loving-bohr-ecp6uy` (last edited 2026-10-21); ARCHIVE is `archive/examples/` on main. The 13 retired standalone Portland units had drifted apart in the two places. A dialogue editor (Sorkin-room brief) chose one side per hunk so the old branch could be deleted. Canon, house style and technical accuracy were decided by rule; dialogue and character were its call. Nothing here is published.

How the hunks were cut: a line-level diff between BRANCH and ARCHIVE. Each changed paragraph counts as one hunk, and a block of added or removed lines also counts as one. I chose one side per hunk. Hunk numbers (H#) count changed paragraphs from the top of each file. Each winner was rebuilt from ARCHIVE with only the BRANCH hunks listed below swapped in, and the winners now replace the files in `archive/examples/`.

Tags: [canon] = timeline/bible, [style] = house style or paths, [dialogue] = craft call, [tech] = technical accuracy.

Rule applied to bridge-card `target:` fields: the archived units sit in `archive/examples/<unit>/` with `workbench.md` beside `narrative.md`. That makes BRANCH's `target: workbench.md` the correct path. ARCHIVE's `workbench/0N-....md` was copied from the live series and does not resolve from the archive folder. Titles and badges keep ARCHIVE's "Hands-On Lab", which matches the live series.

Totals: 198 hunks. BRANCH won 23 (14 dialogue, 6 style, 2 tech, 1 canon). ARCHIVE won 175 (32 canon, 68 style, 29 tech, 46 dialogue). 50 of ARCHIVE's style wins are emoji removed from workbench `<summary>` lines.

---

## a-plus-foundations-prologue.narrative

| H | Hunk (BRANCH / ARCHIVE) | Winner | Reason |
|---|---|---|---|
| 1 | "home improvement warehouse… nineteen… mortar" / "Harrowmere's distribution… twenty… Quikrete concrete mix" | ARCHIVE | [canon] Employer, age 20 at Ep 00, and concrete mix all match the timeline. |
| 2 | "swept my right arm across the table, scattering all three hundred" / "shoved the cards away… two stacks tumbling" | BRANCH | [dialogue] Two lines later the father sees "three hundred cards carpeting the linoleum". ARCHIVE's two stacks contradict that. |
| 3 | (none) / FIGURE 0.1 motherboard callout-panel | ARCHIVE | [style] Uses the house callout-panel syntax with no text in the image. The swollen-capacitor subject does not fit a kitchen scene. |
| 4 | "loses its clock pulse" / "loses its refresh cycle" | ARCHIVE | [tech] DRAM loses data without a refresh, not without a clock pulse. |
| 5 | "A computer shares very little with a milling machine" / "isn't like a milling machine, Dad" | ARCHIVE | [dialogue] A tired kid talking to his father uses contractions and "Dad". BRANCH reads like an essay. |
| 6 | "Something… holds the temporary state" / "You've got what does the work, what holds the work while the motor's running" | ARCHIVE | [dialogue] It sounds like a machinist talking. "Temporary state" is software talk. |
| 7 | "kept turning in my head like an uncalibrated lathe spindle" / "What moves, and what stays still." | ARCHIVE | [dialogue] The father's own words land harder than BRANCH's overwritten simile. |
| 8 | "physical invariants" / "building blocks" | ARCHIVE | [style] "Invariants" is a banned word. |
| 9 | "factory-burned… packets… colliding in memory" / "48-bit… segments… socket buffer" | ARCHIVE | [tech] Packets do not "collide in memory", and Layer 4 carries segments. "Socket buffer" is jargon, but it is correct. |
| 10 | "physical invariants" / "four core building blocks" | ARCHIVE | [style] Banned word. |
| 11 | "switches strip it away… hits a router gateway" / "the local router de-encapsulates and discards the frame" | ARCHIVE | [tech] The router discards the frame. Switches do not strip MAC addresses. |
| 12 | "Hands-on Workbench:" / "Hands-On Lab:" | ARCHIVE | [style] Matches the live series label. |
| 13 | `target: workbench.md` / `workbench/00-the-four-rubber-bands.md` | BRANCH | [style] This is the correct path for the archived unit. |
| 14 | badge "Hands-on Workbench" / "Hands-On Lab" | ARCHIVE | [style] Matches the live series label. |

## a-plus-hardware-helpdesk.narrative

| H | Hunk | Winner | Reason |
|---|---|---|---|
| 1 | "early summer… cool" / "late-winter… cold" | ARCHIVE | [canon] Ep 01 is in February. |
| 2 | "nineteen" / "twenty-one" | ARCHIVE | [canon] Ethan is 21 at Ep 01. |
| 3 | Ken: "The Toledo scale deck… cross-dock trailers… depart" / "Scale deck dropped offline… Scanner's kicking every box" | ARCHIVE | [dialogue] Ken talks like a dock boss. In BRANCH he reads like a memo. |
| 4 | "might just be a software service freeze… clean reboot will clear the state" / "Could be a hung driver… A quick power cycle might clear it" | ARCHIVE | [dialogue] Natural speech, and it shows standing struggle #1 (he acts before he has the whole picture). |
| 5 | "I do not need a theoretical lecture on drivers, kid" / "Ken blocked my hand with his clipboard. 'Don't guess, Ethan.'" | ARCHIVE | [dialogue] The adversarial review names this the best line in Ep 01. |
| 6 | "female socket… intermittent contact with the adjacent ground pin" / "male plug… shorting… against the grounded metal connector shell" | ARCHIVE | [tech] Pins bend on a male DB-9. A female connector has sockets. |
| 7 | baud paragraph (vendor docs on his phone) / FIGURE 1.1 pin-realignment panel | ARCHIVE | [dialogue] BRANCH hands him the answer over a phone signal that canon says is dead in the high bay. |
| 8 | flips DIP switches 3 and 4 / tightens screws, then 14,000 framing faults per second | ARCHIVE | [dialogue] The second failure is a real reversal (praised in the review). BRANCH's fix is an unearned leak of knowledge Ethan doesn't have yet. |
| 9 | "torrent… vanished instantly" / "Ken stepped up behind me" | ARCHIVE | [dialogue] Coheres with H8. |
| 10 | "## The Cost of the Shift" / "It's four-twenty, Ethan… what are you going to do about it?" | ARCHIVE | [dialogue] Pressure delivered as a question. |
| 11 | Ken whistles the line live / "the signal in the high-bay metal building was weak" | ARCHIVE | [dialogue] Keeps the dead phone (the review says to lock that in). |
| 12 | "Line four is live!" / "Guessing which switch to flip would lock the port" | ARCHIVE | [dialogue] Keeps the stakes open. |
| 13 | trailers leave on time at 5:04, "the morning route was saved" / `---` | ARCHIVE | [canon] The bible says Seattle leaves 51 minutes late. BRANCH's version is a free win. |
| 14 | epilogue; he applies for the Tier 1 opening himself / "Dispatch Crucible" handoff gate | ARCHIVE | [canon] A walk-in application breaks the Internal Transfer Law (Ken's referral, then the rotation). NOTE: ARCHIVE's "Your Turn at the Console" handoff violates the 2026-10-26 story/lab model, and its link `workbench/01-the-paper-cert.md` is broken in the archive folder. Neither side is clean; kept ARCHIVE under rule 1. |
| 15 | baud "directly proportional to bits per second" / "In binary baseband RS-232 serial, one baud equals exactly one bit per second" | ARCHIVE | [tech] More precise. It has a stray capital "In" after a comma. |
| 16 | title "Workbench" / "Lab" | ARCHIVE | [style] Matches the live label. |
| 17 | `target: workbench.md` / `workbench/01-the-paper-cert.md` | BRANCH | [style] Correct archived path. |
| 18 | badge | ARCHIVE | [style] Matches the live label. |
| 19 | "Gresham freight terminal" / "Harrowmere Gresham distribution warehouse" | ARCHIVE | [canon] Employer and site. |

## a-plus-os-helpdesk.narrative

| H | Hunk | Winner | Reason |
|---|---|---|---|
| 1 | resume, "eighteen months", "$19.50 an hour" / six-month rotation, Ken's referral, "fourteen months on the concrete docks" | ARCHIVE | [canon] Internal Transfer Law, the 14-month dock tenure, no walk-in interview. |
| 2 | "three weeks memorizing flashcards before this interview" / "My rotation lead had signed me off on Tuesday… Jules's ninety-minute practical" | ARCHIVE | [canon] Ep 02 is the practical that closes the rotation. |
| 3 | "paper does not answer the phone" / "Ken says you have steady hands… training bridge" | ARCHIVE | [canon] Dual-headset training bridge. It is also better Jules: she has read his file. |
| 4 | "municipal payroll ledger" / "regional", training lead | ARCHIVE | [canon] Never a city agency. |
| 5 | (none) / FIGURE 2.1 Event Viewer panel | ARCHIVE | [style] House panel syntax. |
| 6 | "My immediate instinct… replacement bin" / "you didn't troubleshoot it—you tossed it into the RMA bin" | ARCHIVE | [dialogue] The habit and the instinct arrive in one breath. |
| 7 | "complete operating system re-installation… would clear" / "re-image the box… clears out" | ARCHIVE | [dialogue] Spoken, not written. |
| 8 | Jules: "standardized… establishing a testable theory of cause" / "walk the CompTIA… forming a theory you can actually test" | ARCHIVE | [dialogue] Both sides are bad (the review flags exam-guide Jules). ARCHIVE is less stiff. |
| 9 | "draw a clean line straight down the middle of the problem space" / "If your payroll app opens there without freezing, we know…" | ARCHIVE | [dialogue] Talks to the user in user terms. |
| 10 | "UEFI firmware detected" / "Windows Boot Manager… against the TPM's measured boot state" | ARCHIVE | [tech] Boot Manager and the TPM measurements are what trigger recovery. |
| 11 | "completely expected when we modify startup parameters… I reassured her" / "Don't worry, Maya… That's just BitLocker" | ARCHIVE | [dialogue] Less stilted. Both still give Ethan the free win the review complains about. |
| 12 | "municipal database server" / "regional" | ARCHIVE | [canon] Not a city agency. |
| 13 | "## The clean boot and the graphics stack" / "## The eighteen-service wall" | ARCHIVE | [dialogue] Fits the scene that follows. |
| 14 | "non-standard drivers" / "a non-standard [[device_driver]]" | ARCHIVE | [dialogue] Coheres with the ARCHIVE ending, and the mark appears in the body. |
| 15 | "isolate the background conflict" line / eighteen services "stared back at me" | ARCHIVE | [dialogue] It shows the problem instead of announcing it. |
| 16 | narrated clean boot succeeds / "Disable the whole batch, reboot, and see if the crash stops." | ARCHIVE | [dialogue] Ethan proposes; Jules pushes back. |
| 17 | "How are you going to identify the specific culprit" / "eighteen reboots… It is eight-forty… twenty-eight departmental supervisors" | ARCHIVE | [dialogue] Concrete numbers and a clock. |
| 18 | Ethan opens Event Viewer himself / Jules "letting the silence sit" | ARCHIVE | [dialogue] Coheres with H17. |
| 19 | Event ID 1000, `amdkmdag.sys` as faulting module, 4101 "failed to recover" / Jules: "What does Event Viewer say before you touch a single service?" | ARCHIVE | [dialogue] BRANCH also has tech errors: a kernel driver is not an app-crash faulting module, and 4101 means the driver recovered. ARCHIVE's "a clean boot divides the world… the kernel writes down the truth" is a fortune-cookie line; it is the less bad side. |
| 20 | full resolution, Maya "You just saved our entire payroll", "$19.50 an hour" / short cliffhanger | ARCHIVE | [canon] The bible's Ep 02 beat says "the fix lands in the lab, not in the story" and that Maya's trust is dented. The desk pays about $24 an hour. |
| 21 | glossary table without marks / with marks, plus "## The Handoff Gate" | ARCHIVE | [style] Keeps the second mark for each term. |
| 22 | "Workbench:" / "Lab:" | ARCHIVE | [style] Matches the live label. |
| 23 | `target: workbench.md` / `workbench/02-the-live-board.md` | BRANCH | [style] Correct archived path. |
| 24 | "Domain 1.0 & 2.0" / "1.0 & 3.0" | ARCHIVE | [tech] 220-1102 Domain 3.0 is Software Troubleshooting. 2.0 is Security. |
| 25 | badge | ARCHIVE | [style] Matches the live label. |
| 26 | "Step onto Ethan's shift with… prediction gates" / "Take over Ethan's workstation… before Maya Lin's payroll cutoff" | ARCHIVE | [dialogue] Plainer, and it ties to the incident. Both match the lab. |

## netplus-addressing-helpdesk.narrative

| H | Hunk | Winner | Reason |
|---|---|---|---|
| 1 | "three months into my probationary tenure", Jules's bike entrance / bullpen awake, Jared on syslog | ARCHIVE | [canon] Ep 03 is 2 months on the desk. Both sides say "Jared Vance" (registry: Lindqvist), which is unfixable by choice. |
| 2 | Jules wheels in the Kona, sticky note / "had already hung her wet rain shell", queue turns amber | ARCHIVE | [canon] Coheres with H1/H3. BRANCH also reuses the same Jules bike entrance across Act II units (rule 7/11). |
| 3 | "municipal service facilities" / both lines light up | ARCHIVE | [canon] Not a city agency. |
| 4 | "isolated from the city network" / panel + "company network" | ARCHIVE | [canon] Not a city agency. |
| 5 | "I do not understand why…" + "The logger can ping the gateway" / "These two servers can't talk… Destination host unreachable" | ARCHIVE | [tech] BRANCH says the gateway answers, then three lines later says it is unreachable. |
| 6 | "…in binary arithmetic?" / "…octet?" | ARCHIVE | [dialogue] Tighter. |
| 7 | "performs a bitwise logical AND… I explained" / "Destination dot-sixty-two ANDed with dot-one-nine-two gives network zero…" | ARCHIVE | [tech] Shows the arithmetic instead of naming it. |
| 8 | "configured gateway belongs to the first block" / "its exit door was assigned in Subnet A… off-link" | ARCHIVE | [tech] Correct off-link reasoning, and it explains the error message. |
| 9 | `arp -a 10.100.4.55` from the fourth-floor admin station / Jules: "You can't see his Layer 2 ARP table from our fourth-floor desk across a routed WAN" | ARCHIVE | [tech] ARP is local to the broadcast domain. BRANCH's step would show nothing. |
| 10 | `admin.emercer>` prompt / `shipping04>` + findstr | ARCHIVE | [tech] Matches running it from WS-BLDGB-04. |
| 11 | "changed before my eyes" / "flipped:" | ARCHIVE | [dialogue] Less melodrama. |
| 12 | prompt | ARCHIVE | [tech] Same as H10. |
| 13 | Ethan narrates the MAC flip / Jared queries the distribution switch | ARCHIVE | [tech] Switch-side evidence. |
| 14 | Jules: "A classic duplicate IP… endless Layer 2 war" / `show ip arp` output | ARCHIVE | [tech] Real console evidence. |
| 15 | Jared on DHCP logs / Jared on the CAM table, Gi1/0/12 vs Gi1/0/28 | ARCHIVE | [tech] Localizes the device to a port. |
| 16 | "Did someone install new hardware?" / Jules: "Traffic flips back and forth depending on who spoke last." | ARCHIVE | [dialogue] Short and plain. |
| 17 | Ken confesses the LaserJet 4050 in the breakroom / Jared: hardcoded static inside the pool, "before the noon freight trucks" | ARCHIVE | [dialogue] BRANCH's confession is the better line, but it solves the mystery that ARCHIVE's H19 still asks about. It is already in live Ep 03 (see below). |
| 18 | Ken pulls the cable, Frank shouts / Jules taps her pen | ARCHIVE | [dialogue] Coherence. |
| 19 | "Now fix the underlying cause" / "Two physical machines fighting over one Layer 3 address… before Ken has to shut down the dock?" | ARCHIVE | [dialogue] Stakes stated as a question. |
| 20 | reservation fix + "The letter on the wire" lecture ("Let us review…", "Exactly,", "quiet satisfaction") / two-line cliffhanger | ARCHIVE | [dialogue] BRANCH's ending is an "As you know, Bob" lecture with a moral at the end. NOTE: ARCHIVE's cliffhanger plus handoff gate goes against the 2026-10-26 model. |
| 21 | (none) / "## The Handoff Gate" | ARCHIVE | [style] Coheres with H20. |
| 22 | "Workbench:" / "Lab:" | ARCHIVE | [style] Matches the live label. |
| 23 | `target: workbench.md` / `workbench/03-...` | BRANCH | [style] Correct archived path. |
| 24 | badge | ARCHIVE | [style] Matches the live label. |
| 25 | APIPA/CBYT list / "Isolate the Layer 2 MAC address flapping war…" | ARCHIVE | [dialogue] Both describe the lab. ARCHIVE stays with the incident. |

## netplus-dns-helpdesk.narrative

| H | Hunk | Winner | Reason |
|---|---|---|---|
| 1 | "five months into my tenure… My morning routine remained largely unchanged" / "Five months… had taught me the rhythms of the building" | ARCHIVE | [canon] NOTE: both sides say five months. The timeline puts Ep 04 at 7 months on the desk, so neither agrees; kept ARCHIVE. ARCHIVE's line is also better. |
| 2 | Jules's bike, helmet, sticky entrance + "Maya Chen" / short "Maya Chen" + "Jules… auditing overnight firewall changes" | ARCHIVE | [dialogue] Avoids reusing the Jules entrance device. NOTE: both sides say "Maya Chen", a Tier 2 sysadmin. The registry has Lena Chen (Tier 2) and Maya Lin (accounting). |
| 3 | Jared: "CenturyLink has a backhoe problem… dedicated synchronous fiber loop" / "Comcast probably pushed another broken routing update… Have them reboot" | ARCHIVE | [dialogue] Jared's real cadence, and no spec-sheet aside. |
| 4 | "walk the internet root servers… .local… does not exist in public root zone files" / "RFC 6762 reserves .local… drop an NXDOMAIN" | BRANCH | [dialogue] Both are correct. A Tier 1 citing RFC numbers off the top of his head is unearned, and "drop an NXDOMAIN" garbles it. BRANCH teaches how a recursive resolver works (helps the cover test). Still a lecture; less bad. |
| 5 | Jules: "multi-homed resolution… authoritative NXDOMAIN" / "Smart Multi-Homed Name Resolution… metric" | ARCHIVE | [tech] Uses the real feature name. A home router forwarding a query is not "authoritative". |

## netplus-flood-capstone.narrative

| H | Hunk | Winner | Reason |
|---|---|---|---|
| 1 | "water billing, logistics dispatch" / "regional order desk, field-service dispatch" | ARCHIVE | [canon] Not a city agency. |
| 2 | (none) / FIGURE 6.1 panel | ARCHIVE | [style] House panel syntax. |
| 3 | "water billing halts" / "Surge killed both lower switches… Rivergate goes blind" | ARCHIVE | [canon] Rivergate is a canon Harrowmere site, and the line reads better too. |
| 4 | "I knew from my hardware training… flea power" / Jared: "Hold the front power button thirty seconds…" | ARCHIVE | [dialogue] The knowledge comes from the mentor, not from Ethan. Jared's "over-voltage clamp" line is technobabble but less of a leak. |
| 5 | "breached the varistors and scorched the power distribution boards" / "blew right through the primary transformer coils" | BRANCH | [tech] Surge damage hits the MOVs and front-end boards first. Blown transformer coils are the less likely failure. Coheres with ARCHIVE H4. |
| 6 | "two-hundred-pair patch panel" / "48-port Cat6 modular patch panel" | ARCHIVE | [tech] "Pairs" describes a voice punch block. The paragraph talks about modular ports. |
| 7 | "VLAN 10 handles Corporate Water Billing… municipal security policy" / "Three VLANs down here… we're all out of a job" | ARCHIVE | [canon] No municipal setting, and it is the best Jules line in the file. |
| 8 | "municipal devices… water billing" / "company… order desk" | ARCHIVE | [canon] Not a city agency. |
| 9 | "water billing subnet" / "order desk" | ARCHIVE | [canon] Not a city agency. |
| 10 | same | ARCHIVE | [canon] Not a city agency. |
| 11 | "old leases still active… refused to reassign" / docks present new MACs and eat the last twenty | ARCHIVE | [tech] BRANCH contradicts itself: returning clients get their own active leases back. ARCHIVE's mechanism (dock NIC MACs) holds. |
| 12 | "lease duration is set to eight days… binary search method" / "transient MACs claimed the buffer" | ARCHIVE | [tech] Coheres with H11. |
| 13 | "What is your plan of action?" / "Jules set her flashlight down" | ARCHIVE | [canon] Coheres with the ARCHIVE ending (H15). |
| 14 | Ethan recites his four-step plan / Jules: "Eighty order clerks are locked out… Call your shot, Ethan." | ARCHIVE | [canon] Rivergate (not water billing), and stakes in Jules's mouth. |
| 15 | full resolution, "Pale winter morning light", "municipal elevator", Jules: "That is the difference between guessing in the dark and doing the work" / short cliffhanger | ARCHIVE | [canon] Ep 06 is late May, the bible cost (twelve label printers down until ten) is missing, and BRANCH also ends on a moral (banned). |
| 16 | (none) / "## The Handoff Gate" | ARCHIVE | [style] Coheres with H15. |
| 17 | `target: workbench.md` / `workbench/06-...` | BRANCH | [style] Correct archived path. |
| 18 | "Step into Ethan's rubber boots at 04:00…" / "Take over Ethan's console at 07:35…" | ARCHIVE | [dialogue] Both match the lab. ARCHIVE ties to the cliffhanger. |
| 19 | extra "Take the Ticket" link after the bridge card / none | ARCHIVE | [style] Repeats the bridge card. |

## netplus-transport-helpdesk.narrative

| H | Hunk | Winner | Reason |
|---|---|---|---|
| 1 | "Marquam Bridge… bullpen was normally quiet" / "riverfront bridges into gray silhouettes" | ARCHIVE | [dialogue] Tighter. NOTE: both sides say "October" and "four months". The timeline has Ep 05 in April at 8 months on the desk, so neither agrees. |
| 2 | "three hundred municipal switches" / no municipal | ARCHIVE | [canon] Not a city agency. |
| 3 | Jared: "note on the change board… wrecked my entire morning schedule" / "change ticket… blew up my whole morning" | ARCHIVE | [dialogue] Sounds like Jared. |
| 4 | Jules's full bike entrance + speech / "didn't look up from her coffee. 'The core firewall didn't drop a single packet overnight, Jared.'" | ARCHIVE | [dialogue] The best entrance in the batch: no staging, all subtext. BRANCH reuses the bike device again. |
| 5 | Ken thinks wind snapped a fiber drop / panel + "on port 8443" | ARCHIVE | [dialogue] Drops a repeat of Ken's Ep 03 fiber theory and plants the port. |
| 6 | "Listen carefully to your own words" / "Look at the timing, Ethan. If an edge firewall silently dropped that SYN…" | ARCHIVE | [dialogue] A question tied to evidence. |
| 7 | "A stealth security appliance… recalling the rule from my study guides" / "A timeout. Three retransmissions and twenty-one seconds of dead silence." | ARCHIVE | [dialogue] Shows he knows it instead of footnoting it. |
| 8 | three-paragraph quiz ("Exactly,") / "Right. A firewall drop is silence… nobody is listening on port 8443." | ARCHIVE | [dialogue] Says the same thing in a third of the words. |
| 9 | "four hundred municipal field devices" / "across the Portland sites… every five hundred milliseconds" | ARCHIVE | [canon] Not a city agency. It also sets up the retry storm. |
| 10 | "creates a new TCP client object… close… next device" / "retries immediately… without connection pooling" | ARCHIVE | [tech] BRANCH's loop (one connection per device, 400 devices) could not exhaust 16k ports. NOTE: Jared naming his own code by what it lacks ("without connection pooling") is a tell. |
| 11 | "TCP standard requires… In Windows, that timer defaults to" / "Under RFC 793… you burned through all sixteen thousand" | ARCHIVE | [dialogue] Lands the diagnosis with the number. Ethan citing RFC 793 is a flaw on this side. |
| 12 | "And what happens when you open fifteen thousand connections" / Jules wheels closer | ARCHIVE | [canon] Coheres with the cliffhanger. |
| 13 | Ethan names [[port_exhaustion]] / Jules: "Call your shot, Ethan." | ARCHIVE | [canon] Coheres. The `port_exhaustion` mark stays (it is in the glossary table). |
| 14 | pooling fixed on the spot, all 400 devices in under three minutes, "Capacity belongs to both ends of the wire", "quiet confidence" / cliffhanger | ARCHIVE | [canon] The bible says the Tuesday backups never ran, Jared stays until nine, and pooling becomes a change request. BRANCH's ending also says "autumn" and closes on a moral. Its phone-bucket line is already in live Ep 05. |
| 15 | (none) / "## The Handoff Gate" | ARCHIVE | [style] Coheres with H14. |
| 16 | `target: workbench.md` / `workbench/05-...` | BRANCH | [style] Correct archived path. |
| 17 | "Take the Ticket & Open the Lab -> Step onto…" / "Take over Ethan's triage console…" | ARCHIVE | [dialogue] Cleaner, with no stray "->". |

## secplus-auth-helpdesk.narrative

| H | Hunk | Winner | Reason |
|---|---|---|---|
| 1 | "Password is something you know. PIN is also something you know. Same bucket… single-factor with extra typing" / long "Real MFA needs… like the authenticator app" | BRANCH | [dialogue] ARCHIVE names "something you have" and then Ken asks "So what counts as the second thing?", which is now redundant. BRANCH leaves him room to ask. `something_you_have` is still marked in the next line. |
| 2 | "turned into a hallway class for two other people who 'just need the code thing'" / "two other sales reps stopped by" | BRANCH | [dialogue] It has a voice; ARCHIVE is a stage direction. |
| 3 | "Fine for device unlock… not the same as proving you to every SaaS tile" / Windows Hello for Business, TPM key, satisfies MFA | ARCHIVE | [tech] WHfB does count as MFA. The next line, "hoped for a shorter answer", only pays off after ARCHIVE's longer answer. |

## secplus-ir-helpdesk.narrative

| H | Hunk | Winner | Reason |
|---|---|---|---|
| 1 | "rain came in sideways… a USB drawer I trusted too much" / "Eleven months on the service desk… quietest tickets… sharpest edges" | BRANCH | [canon] IR maps to Ep 12 (22 months on the desk); "eleven months" contradicts that. ARCHIVE also ends on a maxim. NOTE: BRANCH has narrator foreshadowing ("trusted too much", rule 3) and a lowercase "*which decision?*". |
| 2 | "a different Maya" / "Elena from payroll audit" | ARCHIVE | [canon] A second Maya clashes with Maya Lin. NOTE: Elena is not in the registry either. |

## secplus-malware-helpdesk.narrative

| H | Hunk | Winner | Reason |
|---|---|---|---|
| 1 | "That cluster is PUPs… riding a free install… We do not tune it." / "You got bundled, Maya… It's essentially a trojan carrying a hidden payload." | BRANCH | [dialogue] It splits the teaching across the exchange, and "essentially a trojan" overstates what a PUP bundle is. Taken together with H2 so all marks stay. |
| 2 | "Useful-looking installer, extra payload in the luggage… trojan territory" / "Next time: company software portal only" | BRANCH | [dialogue] Answers Maya's "scammed by a checkbox" with a picture she will remember. |
| 3 | `net.exe view /all` / `/domain` | ARCHIVE | [tech] `/domain` is the usual discovery command in a worm process tree. |
| 4 | "Event ID 7045 services" / "System log Event ID 7045" | ARCHIVE | [tech] Names the right log. |

## secplus-phishing-helpdesk.narrative

| H | Hunk | Winner | Reason |
|---|---|---|---|
| 1 | "Typosquatting plus brand impersonation… because the page asked nicely" / "a zero instead of an 'o'… immediately prompts" | BRANCH | [dialogue] The narration just said "a zero where an o should live", so ARCHIVE repeats it. BRANCH's last clause has some bite. |
| 2 | "Aimed at money movers — that is whaling when the target is the whale" / "When an attacker targets the executive directly, that's whaling; when they impersonate the executive to trick AP…" | ARCHIVE | [tech] Gets the whaling / CEO fraud / BEC distinction right. NOTE: both sides call the CFO "Avery Chen"; the registry has Avery Holloway. |

## secplus-ports-helpdesk.narrative

| H | Hunk | Winner | Reason |
|---|---|---|---|
| 1 | Ethan: "So which port do we allow on the management path, and which protocol is carrying that password?" / "Port twenty-two, Jared. SSH. It sends everything encrypted…" | BRANCH | [dialogue] ARCHIVE has a Tier 1 explain SSH to a senior network engineer ("As you know, Bob"). BRANCH asks the question. Taken with H2–H3, and it keeps both `protocol` marks. |
| 2 | Jared: "You're going to say SSH. Same remote shell, encrypted, twenty-two. Fine." / "Yeah, yeah. Encrypted remote shell." | BRANCH | [dialogue] Jared gets ahead of the kid. That keeps his dignity and his grudge. |
| 3 | "Then let's put key auth on it now instead of passwords… You rewrite once." / "Configure key auth while you're in there" | BRANCH | [dialogue] Answers "don't make me do it twice" directly. |
| 4 | SFTP/FTPS: "implicit… 990… 989… If your appliance speaks FTPS then we'll do FTPS" / "the modern RFC standard is explicit FTPS on… twenty-one" | BRANCH | [dialogue] Both are technically right. BRANCH ends on a decision instead of an RFC lecture, and keeps the exam ports 989/990. |

## secplus-wireless-helpdesk.narrative

| H | Hunk | Winner | Reason |
|---|---|---|---|
| 1 | "`CORP-EMPLOYE` with the last letter missing" / identical `CORP-EMPLOYEE`, unknown BSSID | BRANCH | [dialogue] Maya has just said "two networks named almost the same". ARCHIVE contradicts her. |
| 2 | "old PSK world… do not join the loud almost-name" / "old guest method… don't touch the duplicate network" | BRANCH | [dialogue] Coheres with H1, and a user can't pick out an exact duplicate by name. |
| 3 | "war driving energy from a car with too many antennas… discovery is cheap" / "radio boundaries stop where walls end" | BRANCH | [dialogue] ARCHIVE's closing line says the opposite of the point (radio does not stop at walls). |
| 4 | "[[disassociation\|disassociation / deauthentication]] frames" / "[[disassociation\|deauthentication frames]]… 802.11w" | BRANCH | [tech] ARCHIVE labels the `disassociation` term as a different frame type. ARCHIVE's 802.11w context is right but not needed. |

## Workbenches

| File | Hunks | Winner | Reason |
|---|---|---|---|
| a-plus-foundations-prologue, a-plus-hardware-helpdesk, netplus-dns-helpdesk, netplus-flood-capstone, netplus-transport-helpdesk | 0 (identical) | ARCHIVE (copied) | No difference. |
| a-plus-os-helpdesk | 6 `<summary>🔍 …` | ARCHIVE | [style] No emoji in summaries. |
| secplus-auth / malware / phishing / ports / wireless | 7 each, `<summary>🔍 …` | ARCHIVE | [style] Same. |
| secplus-ir | 9 (summaries, plus 🎯 in a heading and the deliverables table) | ARCHIVE | [style] Same. |
| netplus-addressing-helpdesk | 4: H1–H3 `arp -a` "from local broadcast domain" + `show ip arp` on the switch; H4 extra `ping 192.168.10.1` output | ARCHIVE | [tech] ARP is only visible inside the broadcast domain. ARCHIVE says where to run it and adds the switch view. |

### Problems in text both sides share (choosing a side can't fix them)

- "Jared Vance" in the addressing, DNS, flood, transport, and ports units. The registry has Jared Lindqvist; Vance is Ken's surname.
- "Maya Chen" in DNS, and "Avery Chen" in phishing. The registry has Lena Chen (Tier 2), Maya Lin, and Avery Holloway.
- "Frank" as a Building B dispatcher (Frank Kowalski in the addressing workbench). The registry's only Frank is Ethan's father. Live Ep 03 has the same collision.
- Banned words survive in unchanged workbench text. The prologue workbench uses "Invariant" and "falsifiable" throughout, plus "Rubric"; the hardware, OS, and IR workbenches have "Rubric"; the addressing and prologue workbenches have "Heuristic". The flood workbench has the heading "Five Invariant Ground Truths".
- The flood workbench is set in December and in municipal offices, against a narrative set at Rivergate in May. The OS workbench has "twenty-eight city supervisors".
- Ticket IDs carry a year (`INC-2026-…`), against rule 13.
- Every ARCHIVE netplus and A+ narrative ends on a "Handoff Gate" cliffhanger, which the 2026-10-26 story/lab model forbids. The BRANCH endings that resolve the story break canon, so ARCHIVE stayed in each case.

---

## Lines worth carrying into the live Portland Desk episodes

I read each matching live episode in `docs/portland-desk/narrative/`. Two of BRANCH's best lines are already live in some form, so they are not repeated here: the phone-in-a-bucket line (live Ep 05, line 166) and Ken's LaserJet 4050 breakroom confession (live Ep 03, line 167). The four below are not live yet.

### 1. Ep 07, Jared and SSH (strongest)

Live `07-the-port-that-is-open.md`, lines 34–36:
> "Port twenty-two, Jared. [[ssh|SSH]]."
>
> He sighed, shaking his head. "Yeah, yeah. Encrypted remote shell. Script's mine, I'll update it. Just don't make me touch it twice."

BRANCH (`secplus-ports-helpdesk`):
> "So which [[port|port]] do we allow on the management path," I said, "and which [[protocol|protocol]] is carrying that password? Telnet sends it in [[cleartext|cleartext]]."
>
> He sighed at me. "You're going to say [[ssh|SSH]]. Same remote shell, encrypted, twenty-two. Fine. The script's mine, I can rewrite it. Just don't make me do it twice."

Why: in the live version, a Tier 1 tech tells a 42-year-old network engineer what SSH is. In BRANCH, Ethan asks and Jared gets there first, which keeps Jared senior and grudging, the way the bible describes him. Keep live's next line (the privilege-fifteen account); it already answers "don't make me do it twice". Check the `port` and `protocol` marks against Ep 07's glossary.

### 2. Ep 10, Maya's bundled installer

Live `10-something-on-the-box.md`, lines 48–52:
> "…Some of these bundles also drop [[spyware|spyware]] that tracks your browsing. It's essentially a [[trojan|trojan]] carrying a hidden [[payload|payload]]. We remove the bundle…"
>
> Maya winced. "So I got scammed by a checkbox."
>
> "Next time: company software portal only," I told her.

BRANCH (`secplus-malware-helpdesk`):
> Maya winced. "So I got scammed by a checkbox."
>
> "Useful-looking installer, extra [[payload|payload]] in the luggage," I said. "That is [[trojan|trojan]] territory even when the merger itself works. Next time: company software portal only."

Why: live answers Maya's wince with a policy line and packs the trojan point into the lecture before it. BRANCH answers her with a picture she will remember. It also hedges ("trojan territory") instead of calling a PUP bundle "essentially a trojan", which is a definition a Sec+ student could get wrong on the exam. Live's "it's not a utility we support" reads better than BRANCH's "merger".

### 3. Ep 08, Todd's password-plus-PIN

Live `08-prove-who-you-are.md`, lines 50–52:
> "…Real MFA needs two distinct factor types, like combining your password with [[something_you_have|something you have]], like the authenticator app on your phone."
>
> Todd was quiet for a second. "So what counts as the second thing?"

BRANCH (`secplus-auth-helpdesk`, with Ken in place of Todd):
> "…Password is [[something_you_know|something you know]]. PIN is also something you know. Same bucket. That is [[single_factor|single-factor]] with extra typing — not [[mfa|multifactor authentication]]."

Why: live has Ethan answer the question before Todd asks it, so Todd's line is dead air. BRANCH stops at "same bucket" and lets Todd ask. Live dropped the `single_factor` mark here; check Ep 08's glossary before adding it back.

### 4. Ep 09, the typosquatted login (smaller)

Live `09-dont-click-that.md`, line 28, comes right after the narration "with a zero where an o should live":
> "They're using [[typo_squatting|typosquatting]] with a zero instead of an 'o' to pull off [[brand_impersonation|brand impersonation]]."

BRANCH (`secplus-phishing-helpdesk`):
> "[[typo_squatting|Typosquatting]] plus [[brand_impersonation|brand impersonation]]. The destination is [[credential_harvesting|credential harvesting]] — a fake login that eats your password and maybe your MFA code if you type one in because the page asked nicely."

Why: live repeats the zero/o detail one line after the narrator gives it. BRANCH doesn't, and its last clause sounds like Ethan.

One continuity note, not a line to carry: live Ep 11 (line 24) still has Maya say "two networks named almost the same", but live now makes the evil twin an exact copy of `CORP-EMPLOYEE`. Her line should change to match.
