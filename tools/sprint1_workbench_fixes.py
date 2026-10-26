import os

os.chdir(r"C:\Users\charl\learning-narrative-kit")

def update_file(path, replacements):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
        elif old.replace("\n", "\r\n") in content:
            content = content.replace(old.replace("\n", "\r\n"), new.replace("\n", "\r\n"))
        elif old.replace("\r\n", "\n") in content:
            content = content.replace(old.replace("\r\n", "\n"), new.replace("\r\n", "\n"))
        else:
            print(f"WARNING: substring not found in {path}:\n  {old[:60]}...")
            
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"Successfully processed {path}")

# ==============================================================================
# WORKBENCH 00: ADD SECTION 5 AND SECTION 6
# ==============================================================================
wb00_old = """### Part C: Scoring & Passing Standards

Use this objective scoring guide to evaluate entry-level diagnostic performance across four core competencies:

| Competency Area | Points | Criteria for Full Credit (Pass) | Criteria for Partial Credit | Criteria for Zero Credit (Fail) |
| :--- | :---: | :--- | :--- | :--- |
| **1. Component Identification** | **25** | Correctly distinguishes between volatile memory (RAM) and non-volatile persistence (storage); explains why rebooting purges memory state but preserves disk persistence. | Identifies RAM as memory but cannot articulate volatility implications during an active infection or crash. | Confuses RAM with disk storage capacity (e.g., "I need more RAM to save my photos"). |
| **2. Layer Isolation & Identity** | **25** | Accurately explains why MAC addresses are stripped at the default gateway while IP addresses persist; calculates whether an IP is local or remote using the subnet mask. | Understands MAC vs IP roles but fails to explain what happens to Layer 2 frames at a router boundary. | Believes MAC addresses route across the internet; unable to define default gateway purpose. |
| **3. Command Telemetry Literacy** | **25** | Correctly interprets outputs from `whoami`, `hostname`, `ipconfig /all`, and `netstat`; identifies an APIPA address (`169.254.x.x`) as a DHCP failure. | Runs command-line tools but requires assistance interpreting subnet masks or process identifier (PID) outputs. | Relies solely on GUI menus; cannot interpret command-line network configuration outputs. |
| **4. Diagnostic Discipline (CBYT)** | **25** | Formulates a clear, testable prediction before altering any hardware or software setting; follows the structured 5-step ping ladder sequentially. | Troubleshoots methodically but occasionally reboots or alters configurations without stating a hypothesis. | Clicks random settings, reboots frantically, or replaces hardware components without testing. |
| **TOTAL** | **100** | **Passing Score: 85 Points or higher** | | |"""

wb00_new = """## 5. What Good Looks Like (Shift Quality Checklist)

Before closing your intake checklist and logging your initial ticket notes, verify your performance against the Portland Desk Shift Quality Standard:

### Shift Quality Checklist
* [ ] **Physical Layer Verification:** Power rails, link carrier LEDs, and hardware integrity confirmed before software changes.
* [ ] **Identity Triad Isolated:** MAC address, IP address, and port number cleanly distinguished in diagnostic notes.
* [ ] **CBYT Hypothesis Formulated:** Testable failure theory committed to writing before issuing commands or touching hardware.
* [ ] **Sequential Ping Ladder:** Diagnostic pings executed in strict hierarchy (Loopback $\\rightarrow$ Local Host $\\rightarrow$ Default Gateway $\\rightarrow$ Remote IP $\\rightarrow$ DNS Hostname).
* [ ] **Actionable User Guidance:** Root cause communicated without jargon, and preventative advice documented in ticket closure notes.

---

### Shift Grading Rubric

Use this objective scoring guide to evaluate entry-level diagnostic performance across four core competencies:

| Competency Area | Points | Criteria for Full Credit (Pass) | Criteria for Partial Credit | Criteria for Zero Credit (Fail) |
| :--- | :---: | :--- | :--- | :--- |
| **1. Component Identification** | **25** | Correctly distinguishes between volatile memory (RAM) and non-volatile persistence (storage); explains why rebooting purges memory state but preserves disk persistence. | Identifies RAM as memory but cannot articulate volatility implications during an active infection or crash. | Confuses RAM with disk storage capacity (e.g., "I need more RAM to save my photos"). |
| **2. Layer Isolation & Identity** | **25** | Accurately explains why MAC addresses are stripped at the default gateway while IP addresses persist; calculates whether an IP is local or remote using the subnet mask. | Understands MAC vs IP roles but fails to explain what happens to Layer 2 frames at a router boundary. | Believes MAC addresses route across the internet; unable to define default gateway purpose. |
| **3. Command Telemetry Literacy** | **25** | Correctly interprets outputs from `whoami`, `hostname`, `ipconfig /all`, and `netstat`; identifies an APIPA address (`169.254.x.x`) as a DHCP failure. | Runs command-line tools but requires assistance interpreting subnet masks or process identifier (PID) outputs. | Relies solely on GUI menus; cannot interpret command-line network configuration outputs. |
| **4. Diagnostic Discipline (CBYT)** | **25** | Formulates a clear, testable prediction before altering any hardware or software setting; follows the structured 5-step ping ladder sequentially. | Troubleshoots methodically but occasionally reboots or alters configurations without stating a hypothesis. | Clicks random settings, reboots frantically, or replaces hardware components without testing. |
| **TOTAL** | **100** | **Passing Score: 85 Points or higher** | | |

---

## 6. The Shift Resolution & Epilogue: 02:15 AM

```callout-panel
title: "FIGURE 0.2: THE MIDNIGHT BENCH & FIRST WORKING VOUCHER"
badge: "Shift Epilogue"
caption: "Kitchen table bench: At 02:15 AM, Ethan categorizes his final index card into the Green Band stack while his father inspects the re-soldered power connector on the practice chassis."
prompt: "Grounded graphic novel illustration in Pacific Northwest silicon noir style, cool slate blue and rain-slicked dark grey palette (#0f172a, #1e293b). A quiet duplex kitchen at night under a low pendant lamp. A 19-year-old apprentice sits at a Formica table with four stacks of index cards held by colored rubber bands. Beside him, an older retired machinist in work socks inspects a dismantled PC power supply on a newspaper mat. Rain streaks the dark kitchen window. High contrast, atmospheric, no text, no words. 16:9 ratio."
```

*The following operational debrief records Ethan's transition from exam anxiety to diagnostic discipline:*

The kitchen clock clicked over to 2:15 AM. Outside the casement window, the East Portland rain tapped steadily against the glass.

On the Formica table, the mountain of loose flashcards had disappeared. In their place sat four neat, compact bundles, each bound by a thick colored rubber band: Red for syllabus trivia, Green for machine invariants, Yellow for addresses and ports, and Blue for the troubleshooting reflex.

My father stood by the sink, rinsing his water glass. He dried his hands on a dishtowel and walked over to the table, looking down at the four sorted stacks. He picked up the Green bundle, feeling the thickness of the cards.

"What holds tension?" he asked quietly.

"Volatile memory loses state when the circuit opens," I answered, looking up from the table. "Non-volatile storage holds the magnetic or charge state until you write over it. The bus bridges them, and the processor steps the clock."

My dad set the stack back down in line with the others. A faint, knowing smile touched the corner of his mouth.

"That's a machine," he said. "The rest is just part numbers in a catalog. Get some sleep, Ethan. The warehouse doesn't care how late you studied when the six o'clock bell rings."

Three weeks later, on a gray Thursday morning in Beaverton, I sat in front of the testing center monitor with my palms flat on the laminate desk. When the scoring engine finalized the results, the screen didn't show perfection—it showed a 685. A passing score by ten points. Scraped by on the retake, but the paper certificate was real, and it bought my ticket onto the graveyard maintenance rotation at the Gresham cross-dock."""

# ==============================================================================
# WORKBENCH 01: ADD SECTION 5 HEADER AND FIX MERCER NAME
# ==============================================================================
wb01_old_c = """### Part C: Scoring & Passing Standards

Use this objective scoring guide to assess technician performance across the five core competency areas:"""

wb01_new_c = """## 5. What Good Looks Like (Shift Quality Checklist)

Before handing the clipboard to Ken Vance and signing off on the Line 4 dispatch log, verify your diagnostic passdown against the Portland Desk Shift Quality Standard:

### Shift Quality Checklist
* [ ] **Flea Power Hygiene:** AC mains disconnected and residual capacitor charge drained for 20 seconds before touching internal bus components.
* [ ] **Quantitative Power Telemetry:** Multimeter measurements recorded with exact DC voltages (+12V, +5V, +3.3V) and tolerance calculations.
* [ ] **Physical Layer Continuity:** Ground fault isolated with audible continuity beeper; harness insulated with high-temp Kapton tape and strain-relief zip ties.
* [ ] **Serial Timing & Baud Alignment:** DB-9 Pin 2 straightened without fracturing; motherboard SW1 DIP switch clock dividers matched to Toledo scale baud rate (9600 8-N-1).
* [ ] **Operational Root Cause Reporting:** Formal passdown log drafted detailing failure mechanism, corrective action, and preventative maintenance action items for facilities.

---

### Shift Grading Rubric

Use this objective scoring guide to assess technician performance across the five core competency areas:"""

wb01_replacements = [
    (wb01_old_c, wb01_new_c),
    ('"You cost us twenty minutes with that power switch, Brooks," Ken said', '"You cost us twenty minutes with that power switch, Mercer," Ken said')
]

# ==============================================================================
# WORKBENCH 08: TODD MILLER VS KEN
# ==============================================================================
wb08_replacements = [
    ("* **Ken in Sales** wiped his phone over the weekend", "* **Todd Miller in Sales** wiped his phone over the weekend"),
    ("| **Case 2** | Ken enters his domain password,", "| **Case 2** | Todd enters his domain password,"),
    ("* **Rationale:** Ken’s proposal of Password + PIN represents two knowledge factors", "* **Rationale:** Todd’s proposal of Password + PIN represents two knowledge factors"),
    ("Ken must install the approved authenticator app", "Todd must install the approved authenticator app"),
    ("#### Part B: Phishing-Resistant MFA Enrollment & Security Escalation Note (Example: Ken Vance / INC0066915)", "#### Part B: Phishing-Resistant MFA Enrollment & Security Escalation Note (Example: Todd Miller / INC0066915)"),
    ('Across the aisle, Ken was back at his desk, staring at his phone. "Sign in with company worked," he called over.', 'Across the aisle, Todd was back at his desk, staring at his phone. "Sign in with company worked," he called over.')
]

# ==============================================================================
# WORKBENCH 10: TODD MILLER VS KEN & USERS PATH
# ==============================================================================
wb10_replacements = [
    ("* **Ken from the warehouse** walked into the dispatch bullpen holding an unbranded 32GB USB flash drive with the words *\"CLIENT DECK\"* scribbled in blue sharpie. Within four minutes of plugging it into his laptop (`TODD-SALES-14`) to check a purchase order", "* **Todd Miller from Inside Sales** walked into the dispatch bullpen holding an unbranded 32GB USB flash drive with the words *\"CLIENT DECK\"* scribbled in blue sharpie. Within four minutes of plugging it into his laptop (`TODD-SALES-14`) to check a proposal"),
    ("At 10:17 AM, Ken Vance from Sales called the help desk in a panic:", "At 10:17 AM, Todd Miller from Sales called the help desk in a panic:"),
    (r"C:\Users\Ken\AppData\Local\Temp\svch0st.exe", r"C:\Users\todd.miller\AppData\Local\Temp\svch0st.exe"),
    ("Even though the local AV quarantined the initial dropper file (`SOW_final.pdf.exe`), Ken's roaring fans indicate secondary payload execution.", "Even though the local AV quarantined the initial dropper file (`SOW_final.pdf.exe`), Todd's roaring fans indicate secondary payload execution."),
    ("*(Reference Case: Ken Vance / Workstation `TODD-SALES-14` / Incident `INC0070418`)*", "*(Reference Case: Todd Miller / Workstation `TODD-SALES-14` / Incident `INC0070418`)*"),
    ("Ken had unplugged a worm commute and was still owed a file copy.", "Todd had unplugged a worm commute and was still owed a file copy.")
]

# ==============================================================================
# WORKBENCH 11: KEN VANCE AT WAREHOUSE VS TODD AT HOTEL
# ==============================================================================
wb11_replacements = [
    ("1. **The Warehouse Annex Barcode Outage:** At 08:15, Ken from Sales and the warehouse logistics team reported that six mobile Zebra barcode scanners", "1. **The Warehouse Annex Barcode Outage:** At 08:15, Ken Vance from Warehouse Operations and his logistics team reported that six mobile Zebra barcode scanners"),
    ("Ken was on VPN and not on WEP.", "Todd was on VPN and not on WEP.")
]

# ==============================================================================
# ARTIFACT: POWERSHELL EVENT 4104 HOSTNAME
# ==============================================================================
art_replacements = [
    ('"Computer": "KEN-SALES-14.harrowmere.local"', '"Computer": "TODD-SALES-14.harrowmere.local"')
]

for prefix in ["docs/portland-desk/", "docs/portland-desk/"]:
    update_file(prefix + "workbench/00-the-four-rubber-bands.md", [(wb00_old, wb00_new)])
    update_file(prefix + "workbench/01-the-paper-cert.md", wb01_replacements)
    update_file(prefix + "workbench/08-prove-who-you-are.md", wb08_replacements)
    update_file(prefix + "workbench/10-something-on-the-box.md", wb10_replacements)
    update_file(prefix + "workbench/11-the-air-is-shared.md", wb11_replacements)
    update_file(prefix + "artifacts/powershell_event_4104.json", art_replacements)

print("All workbench structural and character updates complete.")
