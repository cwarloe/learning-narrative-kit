# Book 0 to Book 1 canon and handoff review

Date: 2026-11-10. Reviewer: Claude (Fable 5.2), read-only pass. Scope: Portland Desk (Book 0) against the NADF narrative and author bible (Book 1, plus the hunt chapters 10 to 14).

Short names used below: **PD** = `learning-narrative-kit/docs/portland-desk/narrative/`, **NADF** = `network-analyst-development-framework/narrative/`, **Timeline** and **Bible** = the two Portland canon files, **Framework** = `docs/craft/learning-narrative-framework.md`.

## Summary

- The planning layer agrees. The Timeline, the Portland Bible, NADF's `BOOK-1.md`, and NADF's `cast-and-relationships.md` tell the same story of who Ethan is and how he gets upstairs.
- The prose does not agree. The NADF chapters, and two NADF bible files (`harrowmere-history.md`, `page-one-world-state.md`), still describe an Ethan with no Book 0 behind him.
- Book 1's Ethan cannot do things Book 0 shows him doing well: reading a capture, telling a refusal from a silent drop, DNS caching, spotting a beacon.
- Leah is the sharpest break. She and Ethan work two incidents together in Book 0 and meet as strangers in Book 1.
- Book 1 collects none of the debts Book 0 hands it. That includes the one it was built to hand over: the interrupted memory capture.
- Book 1's later chapters read as if Ethan sits at headquarters, with Portland as a remote branch. Settled canon says he is in Portland, one floor above the desk.
- Book 0 never shows the upstairs security team. It first exists in the last scene of Ep 12.
- **Verdict: not yet one series.** Most fixes are small text changes in Book 1. Four need Charles to choose a direction first.

## Findings (most severe first)

### 1. Book 1's Ethan has forgotten what Book 0 taught him
**Severity:** blocks the handoff. **Confidence:** confirmed.

| Book 1 says | Book 0 already showed |
|---|---|
| `00-prologue.md` l.18: two years "resetting passwords and unsticking printers" | `06-the-portland-flood.md` l.69-87: he builds trunks, link bundles, and checks spanning tree on a switch console. `12` l.66-70: he reads endpoint data and names "Host C2 beaconing" |
| `00-prologue.md` l.48: "could not pick them out of a row" (port numbers) | `05-the-wire-has-two-ends.md` l.144: he reads the port columns to Jared and names the ephemeral range |
| `01-who-is-talking-to-whom.md` l.80-84: a capture and the handshake are new ground | `03` l.175: Jules "opened a capture ... and made me walk the packet". `05` l.100: he watches the handshake complete |
| `03-names-have-behavior.md` l.82-84: the local DNS cache is "a half-remembered paragraph" | `04` l.38, l.54-56: he dumps the resolver cache, cleans the hosts file, flushes it |
| `06-conversations-have-structure.md` l.42, l.79-81: all four failures look the same to him; Owen explains "nothing was listening" | `05` l.46-50: Ethan himself says a drop is a timeout; Jules says "A firewall drop is silence" and an instant reset means nobody is listening |
| `12-the-heartbeat-with-a-stutter.md` l.9: "my initial security training before coming to Harrowmere ... Instructors had drawn diagrams" | He came to Harrowmere at about 20 as a dock worker and studied alone (Timeline §4). He met a five-minute beacon on the job (`10` l.175, `12` l.68) |

**Rule or source:** Framework principle 1 (skill shown once stays shown). NADF's own `docs/assumed-knowledge.md`, "Consequences for delivery": "A prequel must not pre-teach Book 1's scheduled content", naming "refusal versus silence". Book 0 Ep 05 teaches exactly that. Neither rule is in the Portland precedence list, so nothing "wins" here.

**Suggested fix:** needs the author's decision on direction. The cheap direction is Book 1: let Ethan know the fact from the desk and still fail to use it on log evidence or at the level of a claim. One or two sentences per chapter does it ("I had told Jared the same thing about his own script. I did not see it in four rows of a log."). Rewrite the prologue's second paragraph so his false belief is not "experts memorized more" (Ep 00 and Ep 02 already broke that) but the desk reflex Book 0 leaves alone: the ticket title is usually right, and speed is what gets rewarded. `12` l.70 already shows him building a whole attack story in one breath, unchallenged. Delete or rewrite NADF `12` l.9. The costly direction is trimming Book 0, which is shipped.

### 2. Leah and Ethan are strangers in Book 1
**Severity:** blocks the handoff. **Confidence:** confirmed.

- PD `07` l.82-94: Leah calls the desk, says "Ethan," and they agree the VPN tunnel. PD `12` l.110, l.114-120: he isolates her gateway, she calls him at six, and they sit in the same review.
- NADF `01-who-is-talking-to-whom.md` l.118: "this was the first time we had spoken directly." `page-one-world-state.md` Day 5 (l.852-854) plans the same.
- NADF `cast-and-relationships.md` l.208 already says the opposite: she is "the one familiar face".
- Her history also breaks. `harrowmere-history.md` H-03 (Year -5), H-04, H-17, H-19, H-25 give her five years owning finance and inventory integrations. Bible §3.1 has her a plant controls tech through Ep 12.
- "A few months ahead of Ethan" (Bible l.20, NADF cast l.208) cannot be true. She speaks for the plant in the review in early July (`12` l.116). Ethan's day 11 is 20 August (prologue ticket l.34). That is about five weeks.

**Which source wins:** for Book 0 facts, the Bible and the shipped episodes. NADF's history file is outside the Portland list, so its rewrite is the author's call.

**Suggested fix:** Book 1: rewrite `01` l.118 and the Day 5 note so they know each other, and open on what changed since the gateway (Framework rule 7). Change "a few months" to "a few weeks" in both bibles, or move her transfer earlier and take her out of the Ep 12 plant scenes. Author decides whether Leah's five-year history in NADF moves to someone else or is recast as plant-side work. Book 0: one line in Ep 12 that she is leaving the plant.

### 3. Book 1 drops every debt Book 0 hands it
**Severity:** blocks the handoff. **Confidence:** confirmed.

- The planned handoff is the interrupted second memory capture. PD `12` l.124-126 charges it; l.132 has Nia say "she wants the second capture in it"; Bible l.136 says her staffing request "does not erase it".
- Book 1 never mentions it. Three scenes touch the same ground with no memory: NADF `09` l.106-110 (Ethan orders isolation, then Cal pulls memory), `12` l.136 (Cal: "pull the volatile memory before we sever the socket"), `13` l.144.
- Also dropped: Jules (zero mentions in NADF chapters; she is one floor down and paid for the referral per Bible l.102), Ken's lost notes ("That's twice, Mercer", `10` l.181), Leah's "I found out my gateway was going dark from a phone call" (`12` l.116), the tone complaint in his file (`08` l.114-118).
- Jules's cost for the referral is in the Bible but not in the chapter (`12` l.132). Framework rule 9 says a cost counts only if it is in the narrative file.

**Rule:** Framework rule 1 (a promotion may not offset the previous chapter's cost), rule 4 (a carry-forward must change action), principle 5 ("the next chapter must collect it"). The job offer sits right after the Ep 12 cost. If Book 1 stays silent, the offer reads as the refund.

**Suggested fix:** Book 1. In `09`, have Ethan ask how the memory will be collected before the host is cut off, because of June. Give that line to him, not Cal, in `12`. One short Jules beat early (stairs, lobby, a forwarded ticket) that opens on what changed. Book 0: put one visible cost of the referral on Jules in Ep 12.

### 4. Book 1 reads like headquarters; canon says a Portland pod
**Severity:** blocks the handoff (setting is settled). **Confidence:** confirmed for the text; the org layout behind it is not stated.

- Timeline §3 rule 1 (l.120-121): SOC leadership sits in Chicago; Ethan's job is "in the parent's security pod, one floor above PROC". PD `12` l.100, l.114: Nia is "on the bridge from Chicago"; l.132: "the Portland seat".
- NADF puts Nia in the room: `08` l.24 (conference room, CIO calling), `09` l.108 (she hits isolation "on her console"), `10` l.9, `14` l.13.
- NADF treats Portland as somewhere else: `10` l.23 "every branch office in Portland, the manufacturing floor in Chicago"; `14` l.9 and l.94 list Portland, Chicago, and "Corporate HQ" as three sites; `14` l.111 "pivoted silently into Portland". Ethan worked that warehouse for fourteen months and does not react.
- NADF's floor has a Tier-1 triage room, a hunting pod with server racks, and an executive committee down the hall (`14` l.3, l.229). Book 0's upstairs is one "seat".
- Book 0 never shows the pod. No named person from upstairs appears in Ep 09 to 12 ("SOC" and "Security" act offstage), even when Chicago bridges in for a Portland intrusion. "Harrowmere Northwest" first appears in PD at `12` l.130.
- Addresses disagree too: Book 0 puts Gresham and the Portland datacenter in `10.100.x` (`03` l.51-63, `12` l.80); NADF `14` l.94 makes `10.100.0.0/16` headquarters and Portland `10.110.0.0/16`.

**Which source wins:** the Timeline for Book 0 facts, and the employer and setting statement is settled.

**Suggested fix:** needs the author's decision on one fact: does Nia move to Portland, or does she stay in Chicago and appear by bridge? Then Book 1: fix the "Portland as remote" lines in `10` and `14` and give Ethan one beat of recognition when the trail reaches his old warehouse. Book 0: show the upstairs team at least once before the last page of Ep 12 (a name on a reply, a badge in the elevator), or say why they were not in the room.

### 5. Nia's history and her view of Ethan
**Severity:** needs a decision. **Confidence:** confirmed.

- Timeline l.153 and Bible l.22: promoted to Security Operations Manager "right after Ep 12".
- NADF `harrowmere-history.md` H-01 (l.7-8): she moved "into security-operations management" in Year -5. H-23 has her changing how she assigns work as a manager months before Ethan arrives. NADF cast l.100 already has the Portland version, so the NADF bible disagrees with itself.
- `page-one-world-state.md` l.272-276: Nia sees Ethan as "Unknown judgment". In PD `12` l.104 and l.124-132 she tests his evidence, rules on his containment call, and asks for his name.

**Suggested fix:** Book 1 bible. Reword H-01 and H-23 so the old events happen while she leads incident response, and change "Unknown judgment" to what she saw in June.

### 6. The first sentence of Book 1 is false for a Book 0 reader
**Severity:** minor to fix, large in effect. **Confidence:** confirmed.

NADF `00-prologue.md` l.16: "I had been at Harrowmere eleven days". `10` l.5: "For four months, my working life at Harrowmere". He has been at Harrowmere since the dock (PD `00` l.7). Later chapters say "Harrowmere Equipment Group", which works. **Fix in Book 1:** "eleven days upstairs" or the parent's full name.

### 7. Ethan's flaws do not match across the books
**Severity:** needs a decision. **Confidence:** probable.

Bible l.92-93 names two standing struggles. The second: "He works alone when he should ask, and he gets curt when he is sure." NADF cast l.39 and l.324 build Book 1 on the reverse: "respect for expertise → deference" and "Owen knows; I'll ask Owen." The first struggle (acting before he has the picture) carries over well. **Fix:** author decides whether asking too much upstairs is an overcorrection from the Saturday in Ep 07. If so, one sentence in Book 1 says it. Framework rule 6 says not to invent a new flaw.

### 8. Three mentors, one voice
**Severity:** minor. **Confidence:** confirmed.

Jules has "nine years" (Timeline l.104); Dana has "nine years" (NADF prologue l.80). Jules's note is "Which decision?"; Nia's line is "What decision does that change?" (NADF cast l.135). Jules and Dana both pause, both ask questions, both say "walk me through". Ethan never compares them. **Fix in Book 1:** change one number, and let Ethan hear Jules once when Nia asks her question.

### 9. Craft drift a reader will feel
**Severity:** minor for canon, real for "one series". **Confidence:** confirmed.

- Book 0 ends chapters flat and charges Ethan each time (Bible §5.1 item 4; Framework rule 5). NADF chapters 03 to 14 end on a moral and often on praise: `09` l.132 "I had learned to see", `14` l.225 "You own this desk now."
- Book 0 uses first names after the introduction (Framework rule 10). NADF repeats "Dana Shah", "Leah Moreno", "Cal Rowan" in most chapters; Owen calls him "Mercer" only in `11`.
- Book 1's plan ends with Ethan "not expert" (NADF cast l.60). The chapters end with him presenting to the executive committee about seven months in.
- NADF prologue to `02` read like Book 0. `03` onward do not.

**Fix in Book 1:** cut the last paragraph of each chapter from `03` on and see what is lost. This is the author's call; Portland's rules do not bind NADF.

### 10. Certificates and tier
**Severity:** minor. **Confidence:** confirmed.

- Security+: Timeline l.152 says about 29 months into IT, "just after Ep 12". Bible l.89 and NADF cast l.24 say about 26 months. Twenty-six months is April of Year 4, before Ep 12. **Timeline wins.** Fix the Bible and the NADF cast file.
- Neither Network+ nor Security+ is ever earned on the page in Book 0. Book 1 assumes both.
- Tier: canon has him Tier 2 from January. PD `12` l.149 and the Ep 12 lab (l.4, l.320, l.544) call him Tier 1. NADF then calls his first months upstairs "Tier-1" (`11` l.11, `14` l.221) with no remark that he just earned Tier 2. His pay upstairs is not stated in any source; the Timeline §4 table would be the place.

### 11. Calendar
**Severity:** minor. **Confidence:** confirmed.

- Year 4 is 2026 on both sides (Ep 12 lab 2026-06-24; NADF ticket 2026-08-20). Good.
- The posting goes up about 6 July; the Timeline puts the offer in August; day 1 is about 10 August. That leaves ten days at most from offer to start.
- Book 0 artifacts carry dates inside Book 1's calendar: `artifacts/tickets.csv` and `tickets.json` are stamped 2026-10-20 with Ethan as "Tier 1 Service Desk"; `workbench/02` l.225 has 2026-08-14 for an August 2024 incident; `workbench/10` l.229 has 2026-10-22. Framework rule 13. `tools/check_dates.py` reports 0 findings, so these sit outside what it checks.
- PD `08` l.24: "Spring2024!, Summer2024!" in what is October 2025.
- NADF months run out of order: `05` is month three, `06` is month two, `09` is month five, `10` says "four months".

### 12. What the Portland plant is
**Severity:** needs a decision. **Confidence:** confirmed for the text.

Harrowmere makes and distributes industrial equipment. Book 0 still reads like a water utility in places: `06` l.59 `CORP_WATER_BILLING`; `03` l.7 "water pump station"; `07` l.82 "treatment facility"; `12` l.110 "treatment line"; `workbench/02` l.414 "Water Bureau service counter". Timeline §3 rule 1 says never a city agency. NADF moves manufacturing to Chicago and makes Portland "the warehouse" (`14` l.9). What the Willamette River plant makes is not stated in the Timeline. Leah's Book 1 job depends on the answer.

### 13. Small items found in passing (Book 0)
**Severity:** minor. **Confidence:** confirmed unless noted.

- Rule 7: Maya enters twice in Act III with adware and a standup "in twelve minutes" (`10` l.35, `12` l.24). Todd's USB and the file `SOW_final.pdf.exe` also repeat (`10` l.85, `12` l.76-80).
- Rule 11 (probable): two carried "like a" entrances in Act III (`10` l.68, `12` l.22).
- Rules 13 and 14: `PS C:\Users\jvance>` on Jared Lindqvist's workstation (`05` l.126). "Frank" the dock clerk (`03` l.117) shares a first name with Ethan's father and has no registry row; nor does Lila (`08` l.88).
- Bible l.9 still says "Tier 2 Help Desk Lead at Harrowmere Equipment Group's" operations center. Timeline wins: subsidiary, and he is not a lead.
- Bible l.109 calls Leah his "staunchest operational ally". The shipped chapters show a wary, tired colleague. The Bible says shipped episodes are canon.
- Leah has three Book 0 titles: controls tech (Bible l.105), "plant operations lead" (registry l.155), "ran plant ops" (`07` l.82).
- Bible l.191 says the Ep 09 phish is "a scout" for Ep 12; `12` l.122 says none of the saved indicators matched.

## The handoff checklist

**Book 0 must establish (on the page, not only in the Bible):**
- The upstairs security team exists and belongs to the parent, before the last scene of Ep 12.
- Leah is leaving the plant, and where she and Ethan stand after the gateway.
- What the referral costs Jules.
- Ethan's cert status at the end (Security+ pending, per the Timeline).
- Ethan leaves still trusting speed and the ticket's framing. Ep 12 l.70 already does this; keep it.

**Book 0 must avoid:**
- Any scene where someone teaches him to separate what he saw from what he thinks. That is Book 1's first lesson.
- Any more capture reading, session-state reading, or cache reasoning than is already shipped.
- An offer, raise, or thank-you speech inside Ep 12 (Framework rule 1).
- Putting Dana on the page. A name on a ticket reply is the most it can carry.
- New calendar dates that land after June 2026.

**Book 1 must do for the handoff to hold:**
- Stop calling him new to Harrowmere; stop treating Leah as a stranger.
- Collect the interrupted capture and one Jules beat.
- Keep Ethan in Portland in every chapter.

## Open questions for the author

1. Skills: does Book 1 admit Ethan's desk knowledge and show it failing to carry over, or does Book 0 get trimmed?
2. Nia: Portland or Chicago during Book 1? And how big is the Portland team: a pod, or the main operations floor the chapters describe?
3. Leah: who owns her five years of integration history in NADF's bible, and when exactly does she move?
4. The plant: what does it make, and does any "treatment" language stay?
5. Did Ethan ever meet Dana, Owen, Cal, or Priya during 22 months one floor below them? Not stated in either repo.

## What I did not check, and why

- `archive/` in both repos, `docs/reviews/` and `workshop/` in Portland, and NADF `docs/research/R005` to `R009`: excluded by instruction.
- NADF lessons and Portland labs and artifacts: searched for names, places, dates, and domains, not read in full.
- NADF `book-1-story-snowflake.md`, `book-1-causal-beat-matrix.md`, `book-1-episode-cards.md`, the scene cards, and `harrowsync-system-bible.md`: read where searches pointed (openings, and every Leah, Nia, Portland, and site mention), not line by line. `COURSE.md` and `ROADMAP.md`: searched only.
- Technical accuracy of either book (ports, protocol behavior, exam facts): out of scope.
- "Backstory Bible v3" on Charles's Drive, cited by the Timeline: not in either repo.
- NADF's own internal mismatches (the same host at different addresses, a 14-episode plan against 10 Book 1 chapters): noted only where they touch the handoff.
- Tools: I ran `tools/check_dates.py` only (0 findings). No validators or renders.
