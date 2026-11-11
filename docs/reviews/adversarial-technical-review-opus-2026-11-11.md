# Adversarial technical review: Book 0 fixes, Book 1 patch, practice pilots

Date: 2026-11-11. Reviewer: Claude (Opus 5.5), read-only. I did not write any of the work reviewed here.

Scopes: **A** = Book 0 fixes, commit `e1c98f5` (diff against `1561475`). **B** = NADF Book 1 patch, branch `book1-handoff-fixes` (three commits on `31a4ae4`). **C** = Excel 3 practice pilot (kit `a1107fd`) and NADF later case (`b4a9e9a`).

Short names: **PD** = `docs/portland-desk/`, **NADF** = `/home/user/cwarloe/network-analyst-development-framework` (branch as patched), **NADF-up** = the upstream copy at `b4a9e9a`.

## 1. Bottom line

It is safe to build on most of this work. The renames, the Ep 07 password change, the ticket order, the weekdays and the Book 1 callbacks to Book 0 all check out, and every automated check passes. All the arithmetic in the practice files is correct. There are three problems to fix before more work goes on top:

1. **Book 1's address relabel is half done (B).** Book 0 puts the Gresham dock *and* its inventory server in `10.100.4.0/24`. Book 1 now calls `10.100.0.0/16` "the Portland offices" and `10.110.0.0/16` "Gresham", and its one bridging sentence contradicts Ep 05. The telemetry generator and three hunt chapters still treat `10.100` as headquarters.
2. **The Ep 07 capture is not consistent with itself (A).** The new date puts Jared's "previous run" one minute before his own ticket. The syslog text inside the same file still says `Oct 13`. Separately, the drill's answer key describes echoes that the capture does not contain.
3. **Book 1 turns "memory first, then isolate" into a rule (B).** Ch 09, 12 and 13 now teach it, and Dana says she "had it backwards". Book 0's lesson was different: a *local* capture survives isolation, and stopping the spread came first. The hunt lessons' answer keys still put isolation first.

## 2. Findings, most severe first

### F1. Gresham addresses: Book 1's bridge contradicts Book 0
- **Scope:** B. **Severity:** wrong. **Confidence:** probable. It is confirmed that the addresses clash. That the Ep 05 server sits in Gresham is my inference.
- **Evidence:** Book 0 Ep 03 puts the Gresham dock PCs in `10.100.4.x`, on Vlan4 (`PD/narrative/03-…md` l.61, 119, 146). Ep 05 has the Gresham intake terminals reach "the inventory database server at `10.100.4.20`" on the same /24 in under 2 ms, and Ethan remotes into it as `PDX-ARCHIVE01` (`PD/narrative/05-…md` l.30, 100, 119, 137). Book 1 ch 14 l.105 says: "On the help desk I had known its dock terminals by a different range, `10.100.4`-something, and I had never had a reason to ask what sat in the server room." In ch 14 Hypothesis 2 (l.94), the filter for "the Portland offices (10.100.0.0/16)" now catches Gresham's own dock subnet.
- **Why it matters:** A reader who did Ep 05 knows Ethan worked a Gresham server for a whole episode. The Hunt 05 site filter also mislabels traffic, which breaks the very thing the lesson teaches.
- **Fix:** Pick one of two. (a) Move Book 1's Gresham range to cover `10.100.4.0/24`, which means editing Hunt 05, `lab/generate-hunt-telemetry.py` and `lab/HUNT-DATA-GUIDE.md`. Or (b) keep `10.110` as a *new* server range for Gresham and rewrite the ch 14 sentence so it names the Ep 05 server ("I knew `10.100.4.20`; I had never seen anything in `10.110`"). In both cases, make Hypothesis 2 say which range holds the Gresham dock.

### F2. The relabel leaves headquarters work inside "Portland offices" addresses
- **Scope:** B. **Severity:** misleading. **Confidence:** confirmed.
- **Evidence:** `lab/generate-hunt-telemetry.py` l.40 still has `"corp_hq": "10.100.0.0/16"`, and its comments (l.19, 382 to 385) say "Chicago -> Portland". `lab/HUNT-DATA-GUIDE.md` l.111 says "Portland repository 10.110.16.5". Ch 13 l.5 makes `10.100.40.0/24` "Harrowmere's financial operations and treasury subnet". Ch 11 l.29 puts "Dave Henderson in manufacturing fabrication" at `10.100.12.44`. Under the new labels, both now sit in the Portland offices. Patched ch 14 l.9 puts "the manufacturing engineering floor" in Chicago.
- **Why it matters:** Book 1's thesis is "a number and its label must agree", and these pages now break it. A learner who reads the generator alongside the chapters gets two maps.
- **Fix:** Rename the generator keys (`portland_offices`, `gresham_wh`, `chicago`) and fix the guide's label. Then either say treasury and fabrication have Portland seats, or move those hosts. Change log item 2 names only the key.

### F3. The Ep 07 capture: same-day date, old syslog text
- **Scope:** A. **Severity:** wrong. **Confidence:** confirmed.
- **Evidence:** `tools/generate_ep07_telnet_capture.py` l.25 now sets frame 101 to 2025-08-12 08:44:12 UTC. Jared's ticket `INC0063140` was created `2025-08-12T08:45:12Z` (`PD/artifacts/tickets.json`), one minute later. The drill calls the capture "Jared's previous run" (`PD/workbench/07-…md` l.108), and the ticket says port 23 is now *refused*. The old pair was a week apart (2026-10-13 against 2026-10-20) and made sense. Generator l.76 still hard-codes `strftime("Oct 13 %H:%M:%S")`, so the 30 syslog frames in the regenerated pcap read `<189>Oct 13 08:43:32 Switch-Closet-C: …` while their frame timestamps say Aug 12. The primer video (`PD/assets/video/wireshark-find-the-conversation.html` l.194) shows those `Oct 13` lines, and it is the conversation the primer tells learners to filter for. `check_ep07_capture.py` checks only the Telnet frames, so it passes.
- **Why it matters:** This is the episode that teaches learners to trust what the wire says. The file disagrees with itself in the frames the primer sends learners to look at.
- **Fix:** Set the start time about a week earlier (for example 2025-08-05) and build the syslog text from that date with `T0.strftime("%b %d …")`. Regenerate, then extend `check_ep07_capture.py` so it compares syslog dates with frame dates. Re-record or re-caption the primer only if its rows change.

### F4. The Drill 1 answer key describes a capture that is not in the file
- **Scope:** A. This was already there before the fix, but the fix touched this drill and regenerated the file. **Severity:** misleading. **Confidence:** confirmed.
- **Evidence:** Answer 3 (`PD/workbench/07-…md` l.177) says Telnet runs in "character-at-a-time mode (RFC 854), echoing every keystroke back from the server in separate TCP segments." The capture is different in four ways:
  - It has no server echo frames. A real switch also does not echo password characters.
  - The switch sends no ACKs for the 17 keystroke segments.
  - Frame 124 has the *switch* sending `Switch-Closet-C> enable`, with no client keystrokes for "enable".
  - The client (`192.168.10.45`) and the switch (`10.0.4.15`) are on different subnets, yet frames 101 to 137 carry each other's MAC addresses directly (`02:00:c0:a8:0a:2d` ↔ `02:00:0a:00:04:0f`) instead of the gateway's MAC address. Ep 03 teaches exactly that rule ("addressed the frame to the gateway's MAC").
  
  RFC 854's default is not character mode. Character mode is negotiated with the ECHO and SUPPRESS-GO-AHEAD options (RFC 857/858).
- **Why it matters:** A learner who opens the pcap, as the drill invites, will find the key wrong.
- **Fix:** Reword answer 3 as follows: each keystroke goes out in its own segment once the two sides negotiate character mode; the switch does not echo password characters, but it does echo ordinary commands. Then either add server ACK and echo frames and client "enable" keystrokes to the generator, or say in the drill that the table shows client data only. Use the gateway's MAC address for the cross-subnet frames.

### F5. "Memory first, then isolate" becomes a rule, and Book 0 is misread
- **Scope:** B. **Severity:** misleading. **Confidence:** probable.
- **Evidence:** In Book 0 Ep 12 l.134, Nia rules "Stopping the spread came first", and the fix she asks for is "local capture, or a tested containment channel that keeps the collector reachable". The problem was the *remote stream*, not the order of steps. A local capture keeps running after a network cable is pulled. Book 1:
  - Ch 09 l.114, Cal: "Local capture first, then isolate. We wrote it down in July."
  - Ch 13 l.144 to 146: Ethan says "Memory first … then the switch port", and Dana answers "Yes. That order. I had it backwards." Her original line, isolate at the switch port to preserve memory, was not wrong. Ch 13's host is actively leaking data over a DNS tunnel, so waiting to isolate has a cost.
  - The answer keys in `lessons/hunt-04-…/README.md` l.142 ("Sever 10.100.40.12 at switch port; preserve volatile RAM") and `hunt-03` l.149 still put isolation first.
- **Why it matters:** The chapters now teach the opposite of Book 0's ruling, and they disagree with their own lessons. A practitioner would say the order is a judgment call. If the capture is local, or the isolation keeps the endpoint tool's channel open, you can isolate at once.
- **Fix:** Keep Ethan's question in ch 09 ("How does the memory come off?"); it is right. Change Cal's line to "Local capture, so isolation can't cut it. Start it, then isolate." In ch 13, have Ethan ask how the memory will be collected, and have Dana answer "local, so the port comes down now". Drop "I had it backwards", or move her admission to something she actually got wrong.

### F6. Book 1 says Ethan took Leah's gateway dark; Book 0 says he didn't
- **Scope:** B. **Severity:** misleading (unsupported canon). **Confidence:** confirmed.
- **Evidence:** Book 0 Ep 12 l.116 says "we had isolated the Willamette River gateway". At l.124 Jules says: "There was no plan. That's on us, not on Ethan." Book 1 states his blame as fact in its planning files: `author-bible/cast-and-relationships.md` l.214 ("he isolated her gateway in June") and `page-one-world-state.md` l.854 ("in June he isolated her gateway"). In dialogue (ch 01 l.120, world-state l.325) it is Leah's view.
- **Why it matters:** As Leah's unfair grievance in dialogue, the line works well. As a bible fact it is a new event Book 0 does not support, and later writers will build on it.
- **Fix:** In the two bible files, write it as her view: "she holds him responsible for the dark gateway, though Jules took the blame in the review". Leave her dialogue as it is.

### F7. Local times stamped as UTC ("Z") in the moved artifacts
- **Scope:** A. This was already there, and the fix carried it into the new dates. **Severity:** sloppy. **Confidence:** confirmed.
- **Evidence:**
  - Ep 07: `tickets.json` and `.csv` give `INC0063141` updated `2025-08-12T09:35:10Z`, while the lab note (`PD/workbench/07-…md` l.432) gives `2025-08-12 09:35:10 PDT`. Leah's ticket has the same mismatch (15:25:12Z against 15:25:12 PDT, l.472).
  - Ep 10: Todd calls "at 10:17 AM", and `powershell_event_4104.json` gives `2026-02-12T10:17:42Z`. That is 02:17 Pacific. `event_7045_dump.txt` uses `Z`, while `autoruns_dump.txt` uses `PST`.
  - Ep 08: `security_events.json` uses `Z`, while the lab uses PDT.
  - Ep 07: three `.eml` files use `+0000` for internal Portland mail.
- **Why it matters:** Log fidelity is one of the kit's six realism principles. A learner who converts correctly will place the events seven or eight hours early.
- **Fix:** Either use real UTC (08:45 PDT is 15:45Z) or write a Pacific offset (`-07:00`, or `-08:00` in February). Do this in one pass across `tickets.*`, `security_events.json`, the Ep 10 dumps and the `.eml` headers.

### F8. Artifact leftovers inside files the fix edited
- **Scope:** A. **Severity:** sloppy. **Confidence:** confirmed.
- **Evidence:**
  - `PD/artifacts/sample_legit_payroll.eml` (and the copy in `eml_samples/`) is now dated 12 Aug 2025 but is "Open Enrollment 2027" (l.15, 24). It should be the 2026 plan year.
  - `sample_spoofed_exec.eml` (both copies) is signed "Walt Brandvold". He is the Tamarack track's owner and has no row in the Portland registry (rule 14).
  - Tickets use `@harrowmere.local` addresses, while the Timeline (§3 rule 1) says the subsidiary uses the parent's `harrowmere.com` email.
  - No lab links any of the moved `.eml` files, `phishing_iocs.json` or `gpresult.txt`. Three phishing samples are dated to Ep 07's day rather than Ep 09's.
- **Fix:** Change 2027 to 2026. Rename Walt to a registry name, such as Avery Holloway (CFO), or add a registry row. Decide on `.com` or `.local` and record the choice. Date the phishing samples into Ep 09 or note that they have no episode.

### F9. Excel practice: the four clips named cannot produce the numbers they promise
- **Scope:** C. **Severity:** misleading. **Confidence:** confirmed.
- **Evidence:** `examples/excel-03-formulas-functions/practice.md` l.7 says "Follow clips 5, 6, 9, and 10 … The other clips are available if you need them". The bullet at l.12 promises the total moving from $9,840 to $10,255. But `workbook/crew-bonus-start.xlsx` has no formulas at all: the Bonus sheet holds only IDs, and L40 is an empty styled cell. The eligibility columns F, G and I come from clip 2. Column M, the fill-down to row 38, and the L40 total `=SUM(L2:L38*M2:M38)` come from clip 8 (`RECORDING.md`). Clip 9 says "L40 shows $9,840", which needs clip 8 done first.
- **Why it matters:** A learner who does exactly what the practice says sees a blank total, and the worked example fails on its first visible check.
- **Fix:** Change l.7 to "clips 2, 5, 6, 8, 9 and 10 (clip 2 sets eligibility; clip 8 builds the total)", or supply a start file that already has clips 1 to 8 done.

### F10. The later Excel problem's rule wording, and Excel's blank-is-zero behavior
- **Scope:** C. **Severity:** misleading wording. **Confidence:** confirmed for the term; the Excel behavior is standard.
- **Evidence:** `later-practice.md` l.5 says "order enough to reach the target stock, **with a minimum order quantity of zero**". In ordering, "minimum order quantity" (MOQ) means a supplier's smallest batch. The intended rule is "never order a negative amount", which is what the feedback means by "maximum of zero and target minus counted stock". The feedback also never names the Excel mechanism behind the F40 trap: a blank count cell is read as 0, so `=MAX(0,5-blank)*2` quietly gives the $10 the feedback warns about. The supplier feedback (`practice-feedback.md`) likewise never says that `IFERROR(…,0)` hides *every* error (`#VALUE!`, `#REF!`, `#DIV/0!`), not just a failed lookup, and that `IFNA` is the narrower trap.
- **Fix:** Reword the rule as "order up to the target; if stock already meets it, order 0". Add one feedback sentence: "Excel treats an empty cell as 0 in arithmetic, so test for a missing count (`ISBLANK`/`COUNT`) before computing; prefer `IFNA` with a visible label over `IFERROR(…,0)`."

### F11. NADF's comparison table keeps the old "novice → transformed" answers in two rows
- **Scope:** C. **Severity:** sloppy, and in tension with NADF's no-scoring rule. **Confidence:** confirmed.
- **Evidence:** `NADF-up/lessons/run-records.md` l.176 to 182. Rows 1, 2 and 4 were rewritten as neutral questions. Rows 3 and 5 still prescribe outcomes: A "Collapses layers" against B "Decouples layers", and A "Nuclear or passive" against B "Calibrated". The column header is still "Transformation Signal". The prose just above says these are "prompts for review, not a score or a required progression". `lessons/00-baseline-alert.md` l.11 to 12 still opens with the R005 quote ("Detecting real capability change … requires the same task twice") directly above the new line saying it does not.
- **Fix:** Rewrite rows 3 and 5 as questions ("Does the note keep transport success separate from what TLS hides?" and "Is the proposed action sized to the evidence, with a stated breaker?"). Rename the column "Feature". Qualify the quote or move it below the caveat.

### F12. The NADF later-case review misses the cheapest checks and the strongest point
- **Scope:** C. **Severity:** misleading by omission. **Confidence:** probable (this is analyst judgment).
- **Evidence:** In `later-case.md`, L-06 says the workstation "exchange[d] 28 MB" with no direction. The capstone gives direction (E-03: "18.4 MB outbound and 1.8 MB inbound"). The review (`later-case-review.md`) never asks which way the bytes went, although that is the network analyst's own data and the cheapest discriminating check. It also misses two timing facts that weaken the ticket's "uploading stolen data" story: L-06 began at 13:50, before the 14:00 export request, and the job failed at 14:01 (L-03), so the export file never existed to upload. Elsewhere the review is accurate. Its claims about HTTP 202, TLS, byte volume and retention are stated carefully; none is overstated.
- **Fix:** Add one sentence on direction (request it from the sensor before the endpoint record) and one on timing.

### F13. Ch 09's new line extends a doubtful premise about lost work
- **Scope:** B. **Severity:** misleading. **Confidence:** probable.
- **Evidence:** Ch 09 l.124 adds: "Two days of his work sat in the memory of a machine nobody was allowed to touch." This builds on the earlier claim that cutting the network "mid-compile" wipes "two days of uncommitted engineering builds". Uncommitted source and build output live on disk. Network isolation does not erase them; at worst a build that needs the network fails.
- **Fix:** Make the cost something isolation really causes: a long build that has to restart, a deadline missed, or a machine held as evidence for days so Marcus cannot use it.

### F14. Smaller items
- **Ch 12 jitter (B, misleading, probable).** Ch 12 l.80 says the implant draws "between minus twenty percent and plus twenty percent" in "Cobalt Strike, Sliver, or Brute Ratel". As I understand Cobalt Strike, jitter only *shortens* the sleep, and other tools add to it. Say "varies the interval by up to 20 percent; tools differ on how". The new "none shorter than forty-eight seconds" line still holds either way.
- **Ch 08 sticky note (B, nit, confirmed).** Ch 08 l.88 says "For two years I had read that question off a yellow sticky note". Book 0 Ep 12 l.5 says the note "had gone into her drawer months ago". Write "for most of two years".
- **Ep 03 geography (A, sloppy, probable).** `PD/narrative/03-…md` l.7 puts "Building B at the logistics annex two miles south". The lab now names it the Gresham Logistics Annex (`PD/workbench/03-…md` l.3). Gresham is east of Portland and well over two miles from the Willamette. Drop "two miles south".
- **Stale active doc (A, nit, confirmed).** `docs/research/STORYLINE_WORKBENCH_SYNC_SPECIFICATION.md` l.350 and l.409 to 410 (an active standard, rank 5) still say "Frank in Shipping". The change log did not flag it, though AGENTS.md says to fix or flag the lower document. `tools/refactor_episode_03.py` and `_05.py` still carry Frank and `jvance` and write into `PD/`; `tools/README.md` already warns not to rerun them.
- **Ep 10 and 11 lab headers (A, nit, confirmed).** Both still say "Level 1 Service Desk Terminal" on l.3, directly above "Your Role: Tier 2" on l.4 (the change log's open item 10).
- **"They answer to Nia" (A, nit, probable).** Jules says this in the new Ep 12 l.108, before Nia's promotion. It reads fine as incident command; consider "They take Nia's calls on a bridge".
- **Ch 14 site list (B, nit, confirmed).** Ch 14 l.9 calls three sites "every production boundary in the company". Ch 10 says the plant and Rivergate also feed the data lake.
- **DNP3 wording (A, nit, confirmed).** The `wb/07` rationale says DNP3 has "no built-in … authentication". DNP3 has an optional Secure Authentication; write "no encryption, and authentication is optional and rarely deployed". The ports (Modbus 502, DNP3 20000) are correct. "Intercept … could send a command" mixes up reading the traffic with reaching the port. The bigger risk of opening 502 is that anyone who can reach it can write to the controller.
- **Two transfer problems (C, nit).** The kit's lab rule says "ends with one transfer problem". The pilot has two (section 3 and the later file). The author meant this, but AGENTS.md should say whether a delayed second problem is allowed.
- **Wording (C, nit).** `practice.md` l.68 uses "meta-analysis", "causal" and "measurement quality", which are hard words for the plain-English standard. "A conspicuous missing-ID message" could be "a missing-ID message you can't miss".

## 3. What I checked and found sound

**Scope A (Book 0 fixes)**
- **Renames.** No `CORP_WATER`, `PDX-PUMP`, `jvance` or Frank-as-clerk remains anywhere in `PD/`. Water, pump and treatment wording is gone from `PD/`; the remaining matches are a sump pump, river water and a water glass. Ethan is not called Tier 1 in any Ep 10 to 12 chapter, or in the "Your Role" line or note signatures of any Ep 10 to 12 lab.
- **Ep 07 password.** The drill table (frames 106 to 122), the answer key, generator l.112 and the pcap bytes (`C1sco_Sw!tch_2025\r\n`) agree. `check_ep07_capture.py` passes: 137 frames. No file outside `archive/` or `docs/reviews/` contains `Sw!tch_2026`.
- **Ep 07 calendar.** 2025-08-12 is a Tuesday, about a year after the late-August 2024 desk start, which matches the Timeline's "Year 3 August".
- **Checks.** `check_dates.py` found 0 problems. `check_decks.py` found 0 problems (57 files). `check-links.py` on `PD/` passed (29 files). All `PD/artifacts/*.json` files parse.
- **Weekdays.** These all match their stated days: 2024-08-22 (Thu), 2025-03-11 (Tue), 2025-08-12 (Tue), 2025-10-20 (Mon), 2025-12-10 (Wed), 2026-02-12 (Thu), 2026-04-17 (Fri), 2026-06-24 (Wed), 2026-06-30 (Tue, the review), 2026-07-06 (Mon, the posting). The Ep 09 email date (Wed 10 Dec 2025 -0800) and the IOC file date agree.
- **Tickets.** For all 14 Ep 07 tickets, created ≤ updated ≤ closed. INC, ESC and EVD counters rise in episode order. The new Ep 12 hash is 64 hex characters, appears only in Ep 12, and no longer reuses Ep 10's.
- **Ep 08.** Nora's `Spring2025!`/`Summer2025!` fits an October 2025 episode and a 91-day password age.
- **New canon facts.** These all agree with the updated Timeline (l.120 to 121, 152 to 154) and Bible (l.19 to 22, 102, 145, 165 to 172): Leah's departure line and its date arithmetic (about 21 July, a few weeks before Ethan), Nia's move, the "Tier 2 seat" backfill, "Security+ … scheduled", D. Shah as a signature only, and the unnamed pod voice. Jules's rollout habit has a source in Bible l.102. The fix adds no new promotion, raise or forgiveness that refunds one of Ethan's costs (rule 1). Nia's added line keeps the lost capture charged, and no narrator foreshadowing was added.
- **Ep 12 callbacks.** Ep 10 has Sam walking his February stick to the counter and asking for a sticker (l.68 to 70), and Maya calling and narrating (l.33).

**Scope B (Book 1 patch)**
- **The patch.** It applies cleanly to upstream `b4a9e9a` (`git apply --check`), and NADF `check-links.py` passes on both the branch (676 links) and upstream (684).
- **Book 0 callbacks.** Every one I checked is supported by Book 0's text:
  - the Saturday pack station dark for 35 minutes (Ep 07 l.130);
  - Ken's "two years of carrier contact notes" (Ep 10 l.177);
  - the tone complaint, the panel, and "be right and give her a date" (Ep 08 l.114 to 118);
  - flushing the DNS cache on Greg's remote laptop (Ep 04 l.56);
  - drop versus reset (Ep 05 l.48 to 50);
  - the two five-minute beacons (Ep 10 l.175, Ep 12 l.68);
  - Leah's "phone call" and "nine days" (Ep 12 l.116, 122);
  - Jules's bike (Timeline);
  - D. Shah as a December signature.
- **Calendar.** "Eleven days", "more than five months upstairs", Security+ at about 29 months, and Tier 2 from January all agree with the Timeline.
- **Arithmetic.** In ch 12, 60 s ± 20% gives a 48 s floor. In Hunt 05, CV = 24.1 / 300.2 ≈ 0.080.
- **NADF rules.** No new process document, score, level or validity claim was added. "Falsifiable hypothesis" stays only where it already was.

**Scope C (practice pilots)**
- **Excel arithmetic.** All of it is right:
  - P01 $100, P02 $110 (40 enters the second tier), P03 $125 but held; the $5 rounding changes none of them.
  - C01 $40, C02 $0, C03 $40 held, C04 $60. Releasable $100, unresolved $40, full $140. The IFERROR sheet would also show $100.
  - F10 8 filters for $24, F20 0, F30 and F40 held. "$10 for F40 assumes zero stock" is right.
  - $9,840 + $415 = $10,255, which matches the chapter and clip 10.
- **Excel logic.** Exact match for IDs and approximate match for tiers is correct. For an approximate VLOOKUP, the cutoffs must be sorted ascending and must start at 0, or values below the first cutoff return `#N/A`. A reasonable alternative formula (XLOOKUP, IFS, SUMPRODUCT) gives the same answers.
- **The zero-versus-missing argument** is sound and is the right lesson.
- **NADF later case.** It describes HTTP 202 correctly (RFC 9110: accepted for processing, not completed), and it states TLS and capture limits, retention urgency, and who has authority to isolate without overclaiming. Both repos' new text avoids mastery or validity claims, and the README and capstone wording is careful. The later case changes the surface (a failed export against an exfiltration claim) while keeping the same decision as the capstone, which is what was intended.
- **Design intent.** Both pilots deliver the intended shape: a worked example, a try with heavy help and feedback, then a later try with less help. Each asks learners to save the first answer and record help used. That shows how much help was needed, not mastery.

## 4. Handout ideas (suggestions only)

- **Excel: "Zero or unknown?" card.**
  - Exact match for identities (`FALSE`/`0`); approximate match for bands, with ascending cutoffs that start at 0 (or `XLOOKUP` match mode -1).
  - `IFNA` with a visible label instead of `IFERROR(…,0)`.
  - "An empty cell counts as 0", with an `ISBLANK`/`COUNT` test.
  - Keep amount and status in separate columns.
  - Report three totals (releasable, held, full).
  - `MROUND` versus `ROUNDDOWN` versus `INT`.
  - `MAX(0, target - count)`.
  - A box for "who owns the missing fact".
- **NADF: one-page handoff check.**
  - Split the ticket into separate claims.
  - For each source, note what it can and cannot show, layer by layer (TCP, TLS, HTTP status, application or job log).
  - Ask "which way did the bytes go, and when, relative to the event?"
  - Pull short-lived evidence first.
  - Name an owner for each check.
  - Say what would change the action and who authorizes disruption.
  - Give one plain sentence of confidence, with its reason.

## 5. What I could not check

- **The three DOIs** in `practice.md` l.68 are unverified. I was told not to contact outside services.
  - `10.1007/s10648-026-10225-5`: Educational Psychology Review, going by the prefix. It is attached only to a limiting claim ("do not establish workplace transfer"). Cautious.
  - `10.1108/EBHRM-03-2025-0117`: Evidence-based HRM, going by the prefix. The text admits only the abstract was read and that causal effects were not verified. Cautious.
  - `10.1186/s13063-026-10057-2`: the journal *Trials*, going by the prefix. It is described as "small and inconclusive". Cautious, but *Trials* also publishes study protocols. If this is a protocol, "inconclusive" is the wrong word; check the article type.
- **Tooling I could not run.** The headless-browser render (no Playwright), and NADF `validate-captures.py` and `check-lesson-commands.py` (no tshark or zeek).
- **Field names and formats I could not confirm here.** Security Onion field names in the hunt chapters (`connection.state`, `source.bytes`, `user_agent.original`), against a specific Security Onion version; these lines were not touched by the patch. The exact `gpresult` copyright line. Whether Cloudflare still allows domain fronting (ch 13, untouched).
- **The primer video.** Only its HTML scene file was inspected, not the MP4 frames.
