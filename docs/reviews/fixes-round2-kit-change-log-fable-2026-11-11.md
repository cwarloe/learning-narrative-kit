# Round 2 fixes, kit repo: change log

Date: 2026-11-11. Writer: Claude (Fable 5.2). Work order: `docs/reviews/adversarial-technical-review-opus-2026-11-11.md`, scope A (Book 0) and the Excel findings in scope C. Scope B and the NADF later case (F1, F2, F5, F6, F11, F12, F13 and the B items in F14) were not touched. Nothing is committed.

`PD` = `docs/portland-desk/`.

## What changed, by finding

### F3. Ep 07 capture: date and syslog text
- `tools/generate_ep07_telnet_capture.py` (l.5 to 15, 32 to 34, 90 to 91). Frame 101 is now 2025-08-05 08:44:12 PDT, a Tuesday one week before Jared's ticket `INC0063140` (2025-08-12). The Timeline puts Ep 07 in "Year 3 August", so the date fits. The 30 syslog lines are built from the same start time (`Aug  5 08:43:32 …`), so they cannot drift from the frame dates again.
- The start time is now written as Portland time (UTC-7). Before, 08:44:12 was stored as UTC, which is 01:44 in Portland. This is the same defect as F7, so I fixed it here too.
- `tools/check_ep07_capture.py` (l.11 to 18, 34 to 38, 77 to 98, 151 to 185). Three new checks: syslog text date and time against the frame's own time; the capture ends before the day the ticket was filed; frames to or from another subnet carry the gateway's MAC address. I ran the new check against the old capture and it failed on all three, as it should.
- `PD/artifacts/jared-telnet-capture.pcap` regenerated with scapy from the throwaway venv. Still 137 frames, in the same order. The password is unchanged (`C1sco_Sw!tch_2025`); the year still fits.
- `PD/workbench/07-the-port-that-is-open.md` l.109: the drill now says the capture is from a week before the ticket (Tuesday, August 5, 2025).
- `PD/assets/video/wireshark-find-the-conversation.html` l.194: 63 `Oct 13` strings became `Aug  5`. No other row changed (the time column is relative seconds, and the ARP rows are local).
- `tools/README.md` l.20: the tool index line describes the new checks.

### F4. Drill 1 answer 3 and the capture
I chose the smaller fix: reword, and say plainly what the file leaves out. I did not add frames.
- `PD/workbench/07-…md` l.179: answer 3 no longer cites RFC 854 or claims echoes. It says the two sides agree to work one character at a time, each keystroke then travels in its own segment, and the switch sends ordinary commands back but not password characters.
- `PD/workbench/07-…md` l.111 (new note, "About this file"): the times are Portland time and Wireshark shows the viewer's own zone; the file was built for the practice rep; it leaves out the switch's bare acknowledgment frames; frame 124 shows `enable` as one line where a live session would show six typed and echoed characters; frames between the two subnets use the gateway's MAC address, as Ep 03 teaches.
- Generator `hop()` (l.42 to 48): every frame to or from `10.0.4.15` now carries the MAC address of `192.168.10.1` on the captured segment. This covers the Telnet frames and also the ping and syslog frames, which had the same fault.
- Why not add frames: realistic acknowledgments plus typed and echoed `enable` would grow the table from 37 rows to about 65, renumber the two password ranges in the questions, and change the primer's row count. See author item 2.

### F7. Local times marked as UTC
Wall-clock times are unchanged; only the zone mark changed.
- `PD/artifacts/tickets.json`, `tickets.csv`: 39 stamps each, `Z` to `-07:00` (August 12, 2025 is PDT). They now agree with the Ep 07 lab notes.
- `PD/artifacts/security_events.json`: 6 stamps, `Z` to `-07:00` (October 20, 2025 is still PDT).
- `PD/artifacts/powershell_event_4104.json` l.15 and the copy shown in `PD/workbench/10-…md` l.229: `Z` to `-08:00` (February is PST). Todd's 10:17 AM call and the event now agree.
- `PD/artifacts/event_7045_dump.txt` l.7: `Z` to `-08:00`, matching `autoruns_dump.txt` (PST).
- The three older `.eml` samples (both copies of each): `+0000` to `-0700`.
- Not in the report, same defect: `PD/workbench/02-the-live-board.md` l.225 and l.246 (`Z` to `-07:00`; the lab says 08:15 and 08:22 PDT), and `PD/workbench/12-…md` l.196 ("PDT/PDT" to "PST/PDT").

### F8. Email leftovers
- "Open Enrollment 2027" is now the 2026 plan year (`sample_legit_payroll.eml`, both copies, and `phishing_samples.json`). The closing day read "Friday, November 13", which is a Friday in 2026 but a Thursday in 2025, so it is now "Friday, November 14".
- Walt Brandvold (the Tamarack owner) is gone from `sample_spoofed_exec.eml` (both copies) and `phishing_samples.json`. The sender is Avery Holloway, Chief Financial Officer, who is in the cast registry. The fake Gmail addresses changed to match (`avery.executive.desk77@`, `cfo-desk-office@`).
- Email domain: the Timeline (rank 2, section 3 rule 1) says the subsidiary uses `harrowmere.com` email, and the Ep 09, 11 and 12 labs already do. So I changed `@harrowmere.local` to `@harrowmere.com` in `tickets.json`, `tickets.csv` (13 each), the three older `.eml` samples and `phishing_samples.json`. Computer names such as `MAYA-W11.harrowmere.local` are directory names, not email, and stay.
- Search for others like these: no other Tamarack name, no other 2027, and no other wrong-year date in `PD/`.

### F14, scope A items
- Ep 03 geography: `PD/narrative/03-…md` l.7, dropped "two miles south".
- Stale active doc: `docs/research/STORYLINE_WORKBENCH_SYNC_SPECIFICATION.md` l.350, 409, 410, "Frank" the shipping clerk is now Carlos (registry: Carlos Gomez). Frank Mercer, the father, at l.112 is correct and stays.
- Ep 10 and 11 lab headers: `PD/workbench/10-…md` l.3 and `11-…md` l.3, "Level 1 Service Desk Terminal" is now "Service Desk Terminal".
- "They answer to Nia": `PD/narrative/12-…md` l.108 now reads "They take their calls from Nia on the bridge, not from me".
- DNP3 wording: `PD/workbench/07-…md` l.398 and l.484 to 489. Modbus has no authentication; DNP3 authentication is optional and often left off; neither encrypts. The risk now separates reaching the port (sending commands) from sitting on the path (reading or faking telemetry). Ports unchanged.

### F9. Excel clip list
- `examples/excel-03-formulas-functions/practice.md` l.7. I traced every cell that feeds L40 through `RECORDING.md` and `steps.yaml`, and confirmed with the two workbooks (the start file's Bonus sheet holds only IDs; the key file's row 2 has the formulas below).
  - Needed, in order: **2** (F, G, I: eligibility), **5** (B, C, H, D, J, E: lookups), **6** (K, L, N: bonus and rounding), **8** (M, fill down, L40), **9** ($9,840), **10** ($10,255).
  - Not needed: 1, 3, 4, 7. Clip 2's day count reads only the Timeclock ID column, which is already in the start file.
- l.12: "A conspicuous missing-ID message and an unresolved numeric error" is now plain wording.

### F10. Later problem and blank-is-zero
- `later-practice.md` l.5: the rule now reads "order enough filters to bring stock up to the target; if stock already meets or passes the target, order none".
- `later-practice.md` l.27 and `practice-feedback.md` l.26: one sentence each that Excel treats an empty cell as 0 in arithmetic, tied to the F40 count and to C02's zero.
- I did not add `IFNA`, `ISBLANK` or `COUNT`. The unit does not teach them; the chapter's own fix is `IFERROR` with a visible "ID NOT FOUND" label and an unwrapped amount lookup. See author item 6.

### Handout (new)
- `examples/excel-03-formulas-functions/handout.md`, about 550 words, five short parts: zero or unknown; exact match or cutoffs; what `IFERROR(...,0)` can hide; three checks before sending a total; what to ask for when a record is missing. Everything in it comes from the chapter, the walkthrough or the practice files. It makes no claim about what the learner can do.
- Linked by one sentence at `practice.md` l.17.
- The practice files and the handout are source files only; nothing under `docs/excel-03-formulas-functions/` changes, so I did not re-render.

## Items for the author

1. **Primer video MP4.** `wireshark-find-the-conversation.mp4` still shows `Oct 13` in the syslog rows. Its scene file is fixed, but the renderer (`render.py`) lives in the knowledge-harvest repo and there is no Playwright here. Re-render from the fixed HTML, or accept the mismatch until the next recording.
2. **Drill 1 capture, fuller fix.** If you would rather have a capture with real acknowledgments and a typed, echoed `enable`, the table grows to about 65 rows and the question ranges renumber. Say so and it is a generator change plus the table.
3. **Windows event times.** A real Windows event record always stores `SystemTime` in UTC with a `Z`. I followed the work order and wrote Pacific offsets, which is unambiguous but not what Windows prints. The other honest choice is true UTC (`18:17:42Z` for Todd's 10:17 AM) with a line in the lab telling learners to convert.
4. **Three older email samples have no episode.** `sample_legit_payroll.eml`, `sample_phish_invoice.eml`, `sample_spoofed_exec.eml` and `phishing_samples.json` are dated to Ep 07's day and no lab links them. Nor does any lab link `phishing_iocs.json` or `gpresult.txt`. I left the dates alone: moving them to Ep 09 (December) would break the enrollment deadline and the `INV_Aug2025` attachment name. Choose: link them, re-date them, or archive them.
5. **Email address style.** The domain is now one thing, but the name part is not: tickets use `jlindqvist@`, the Ep 09 samples use `jules.brooks@`, and one older sample uses `ethan@`. Pick one style if it matters.
6. **`IFNA` in the Excel unit.** The reviewer prefers `IFNA` with a label over `IFERROR`, because `IFERROR` hides every kind of error. That is true, but it is new content for this unit. Add it to the chapter first if you want it in the practice and the handout.
7. **Two transfer problems.** The lab rule says a lab "ends with one transfer problem"; this pilot has one in section 3 and a later one. If the later problem is meant, AGENTS.md should say a delayed second problem is allowed.
8. **Hard words beside the citations.** `practice.md` l.70 still has "meta-analysis", "causal" and "measurement quality". I was told not to touch that paragraph or the three DOIs.
9. **"Tier 1" in Ep 10 and 11 lab note titles.** Only the two l.3 headers changed. Titles such as "Tier 1 Host Infection Isolation & Containment Ticket Note" (Ep 10 l.528 to 532, Ep 11 l.320, 466, 470) name a kind of note, and renaming them is your call.
10. **`tools/generate_helpdesk_artifacts.py` is stale.** It still holds 2026 dates, `Z` stamps, `portland-ops.local`, Walt Brandvold and "2027", and writes to `archive/` by default. I did not edit it. Do not run it against `PD/artifacts/`, or retire it.
11. **Routed frames keep TTL 64.** Frames from the switch crossed a router, so a live capture would show a lower TTL. Not in the report; left alone.

## Check results

| Check | Result |
|---|---|
| `python3 tools/check_dates.py` | 0 date findings |
| `python3 tools/check_decks.py` | 57 files, 14 decks, 0 problems |
| `python3 template/tools/check-links.py docs/portland-desk` | PASS, 29 files |
| `python3 template/tools/check-links.py examples/excel-03-formulas-functions` | PASS, 7 files |
| `python3 tools/check_ep07_capture.py` | OK: 137 frames, Telnet frames 101 to 137 match 37 rows, passwords match, 30 syslog dates match, gateway MAC rule holds |
| Same check against the old capture | FAILED, as intended (syslog dates, same-day capture, MAC addresses) |
| `python3 tools/check_cleanliness.py` | PASSED, 323 files |
| `python3 tools/check_hub_links.py` | PASS |
| `validate_unit.py examples/excel-03-formulas-functions` | PASS (46 marks, 46 glossary ids) |
| All `PD/artifacts/*.json` parse | yes |
| `render_unit.py` | not run; no shipped output for the unit changes |
| Headless browser pass on the Ep 07 lab page | not run; no Playwright in this sandbox |
