# Portland Desk Courseware Audit: Technical SME & Protocol Pedant Review (V2)
**Repository:** `learning-narrative-kit`  
**Reviewer:** Adversarial Technical SME & Protocol Pedant (`technical_nitpicker`)  
**Target:** Live Courseware Narrative (Episodes 00–12) and Workbench Labs (Workbenches 00–12)  
**Governing Standards:** `TECHNICAL_NARRATIVE_AUTHORING_PRINCIPLES.md`, `PORTLAND_AUTHOR_BIBLE.md`, `PORTLAND_CURRICULUM_PLAN.md`, RFC 793/9293 (TCP), RFC 826 (ARP), RFC 2131/2132 (DHCP), RFC 1035/2308/6762 (DNS), RFC 5321/5322/7208/6376/7489 (Email/SPF/DKIM/DMARC), RFC 3227 (Evidence Collection), IEEE 802.1Q / 802.1w / 802.1X / 802.11, ATX12V 2.52, NIST SP 800-63B.

---

## Executive Verdict: Ground Truth vs. Operational Sloppiness

The Portland Desk curriculum possesses strong narrative pacing, compelling character dynamics, and an admirable commitment to demystifying IT certification trivia through the lens of machine shop precision. When it hits its stride (e.g., in TCP socket lifecycle, split-horizon DNS race conditions, and email MIME decomposition), it teaches enterprise operations with high fidelity.

However, an exhaustive adversarial audit of all 13 narrative episodes and 13 workbench labs reveals **systematic technical contradictions, layer conflations, copy-paste artifacts, and terminal command hallucinations**. While the course prides itself on teaching students to "stop guessing and look at the circuit path," the courseware itself repeatedly commits the very sins it warns against:
1. **Layer 2 / Layer 3 Conflation:** The curriculum repeatedly asserts that an IP address conflict causes "switch MAC table poisoning" and "MAC address flapping" across switch ports, failing to grasp that switches map MACs, not IPs. This mistake even appears in student grading rubrics.
2. **Lab Terminal & Narrative Disconnects:** In Workbench 02, while the entire narrative, drill, and ticket resolution note focus on Maya Lin's `PDX-Pay` (`PDXPayClient.exe`) crashing on AMD driver `amdkmdag.sys`, the interactive terminal widget suddenly presents `QuickBooks.exe` crashing on an audio overlay DLL (`NahimicOSD.dll`). In Workbench 01 and Narrative 01, the transmitter and receiver baud rates are inverted.
3. **Pervasive Character Lore Conflation:** Across four consecutive narrative episodes (08, 09, 10, 11) and workbenches (08, 10, 11), the author repeatedly conflates 50-year-old Gresham freight warehouse cross-dock supervisor **Ken Vance** with Inside Sales representative **Todd Miller**, creating nonsensical scenes such as "Ken from sales" wiping his phone or plugging malware-laden USBs into `TODD-SALES-14`.
4. **Structural Omissions:** Workbenches 00 and 01 completely lack the mandatory Section 5 Performance Deliverable Rubrics ("What Good Looks Like / Shift Quality Checklist"), jumping straight to Section 6 or ending abruptly.

If published without remediation, these errors will undermine the curriculum's credibility with senior engineers and misinform junior students entering enterprise operations.

---

## PART 1: Narrative Technical Scorecard (Episodes 00–12)

| Episode | Title | Severity | Primary Technical Issue / Defect | Prescribed Fix |
| :---: | :--- | :---: | :--- | :--- |
| **00** | The Four Rubber Bands | LOW | **VRM Capacitor Filtering Misnomer (L44):** Claims electrolytic capacitors adjacent to CPU socket "regulate clean DC voltage to the memory bus." | Relabel as CPU VCore voltage regulator module (VRM) filtering stages; memory VRM sits beside DIMM slots. |
| **00** | The Four Rubber Bands | LOW | **APIPA Intranet Phrasing (L89):** States workstation "retained network connectivity" while pulling APIPA address. | Clarify workstation maintained physical link carrier (L1/L2) but had zero L3 network connectivity. |
| **01** | The Paper Cert | HIGH | **DIP Switch Power Loss Paradox (L130–136):** Claims cutting standby power reset hardware DIP switches (`SW1`) to 9600 baud factory defaults. | Mechanical DIP switches cannot reset on power cut. State that power cut wiped volatile NVRAM/UART registers, reverting to hardware DIP fallback. |
| **01** | The Paper Cert | HIGH | **Baud Rate Inversion with Workbench 01 (L132):** Narrative claims scale is 19,200 baud and receiver is 9,600; Workbench 01 claims scale is 9,600 and receiver is 19,200. | Align Narrative 01 to match Workbench 01: Toledo scale is fixed at 9,600 baud (104.17 µs), terminal receiver was misclocked at 19,200 baud (52.08 µs). |
| **02** | The Live Board | HIGH | **BitLocker Recovery Key Grouping (L92):** Narrative claims console displayed BitLocker recovery key as "twelve groups of four digits." | BitLocker recovery keys are strictly **eight groups of six digits** (48 digits total). Correct the prose to match Microsoft BitLocker architecture. |
| **03** | The Default Gateway Doesn't Care | HIGH | **Switch MAC Table vs ARP Cache Conflation (L159, L184):** Claims duplicate IP conflict "poisons switch MAC table" and causes "Layer 2 MAC address flapping war." | Switches map MACs to ports, not IPs. CAM tables remain stable; what flaps/poisons is the Layer 3 **ARP cache** on routers and neighboring hosts. |
| **04** | The Name Is Not the Number | LOW | **`router.local` Resolution (L70):** Terminal shows `router.local` resolving `payroll.harrowmere.local`. | Technically sound demonstration of RFC 6762 mDNS `.local` leakage and Smart Multi-Homed Name Resolution race conditions. Pass with honors. |
| **05** | The Wire Has Two Ends | PASS | **TCP State Machine & TIME_WAIT:** Exceptional technical accuracy regarding 2MSL timers (120s), dynamic port range (49152–65535 = 16,384 ports), and active close RST vs drop. | No fix required. Model chapter. |
| **06** | The Portland Flood | MEDIUM | **Deprecated Cisco Trunk Encapsulation Syntax (L73):** Specifies `switchport trunk encapsulation dot1q` on Cisco Catalyst 2960-X interface range. | Catalyst 2960-X only supports dot1q; the command throws a syntax error. Remove encapsulation command; specify `switchport mode trunk` directly. |
| **07** | The Port That Is Open | MEDIUM | **Verbatim Paragraph Repetition (L116–119):** Two consecutive paragraphs repeat almost word-for-word descriptions of queue monitor requests (TFTP, LDAP, SNMP). | Delete duplicate paragraph (L118–119). |
| **08** | Prove Who You Are | HIGH | **Todd Miller vs Ken Vance Character Conflation (L40–74, L94):** Starts with "Todd in sales," abruptly switches to "Ken said" throughout the scene, and concludes "Ken is insisting Password plus PIN is multifactor." | Replace "Ken" with "Todd" throughout Episode 08. Ken is the warehouse cross-dock supervisor, not the inside sales rep. |
| **09** | Don't Click That | HIGH | **Todd vs Ken Character Conflation (L70–74):** "Todd in sales texted a screenshot... which Ken trusts more than HR-formal... Ken muttered, 'I almost clicked...'" | Fix character name to Todd Miller throughout lines 70–74. |
| **10** | Something on the Box | HIGH | **Todd vs Ken Character Conflation (L97–126):** "Todd from sales called... user: todd.miller... TODD-SALES-14... Ken unplugged. He still had a file mid-copy..." | Fix line 126: Todd unplugged his laptop, not Ken. |
| **11** | The Air Is Shared | HIGH | **Todd vs Ken Character Conflation (L36–48):** "Todd from sales called from a hotel... 'And WEP?' Ken asked... Ken muttered something about customer politics..." | Fix lines 44–48: Todd is at the hotel customer demo, not Ken. |
| **12** | When the Ticket Escalates | PASS | **Forensics & Order of Volatility:** Excellent technical alignment with RFC 3227, live memory capture vs persistent disk write-blocking, and Sysmon/EDR telemetry. | Minor copy-paste artifact in Ken/Todd backstory, otherwise pristine. |

---

## PART 2: Workbench / Lab Technical Scorecard (Workbenches 00–12)

| Workbench | Title | Severity | Primary Technical Issue / Defect | Prescribed Fix |
| :---: | :--- | :---: | :--- | :--- |
| **00** | The Beginner's Mental Model | HIGH | **Missing Section 5 Rubric & Epilogue:** Workbench terminates abruptly after Section 4 ticket notes; completely lacks Section 5 Performance Deliverable Rubric. | Author Section 5 ("What Good Looks Like / Shift Quality Checklist") and Section 6 Epilogue to align with workbench standards. |
| **01** | Hardware Fault Isolation | CRITICAL | **Missing Section 5 Rubric:** Jumps directly from Section 4 to Section 6; Section 5 rubric is completely omitted. | Author Section 5 Performance Checklist evaluating multimeter tolerances, POST triage, and UART timing calculations. |
| **01** | Hardware Fault Isolation | HIGH | **Baud Rate Inversion vs Narrative 01 (L218, L260):** Workbench establishes UART is locked to 19,200 and scale is 9,600. Narrative states the exact opposite. | Keep Workbench 01 math (it is mathematically rigorous) and rewrite Narrative 01 lines 130–136 to match. |
| **02** | OS Diagnostics & Boot Recovery | CRITICAL | **Complete Scenario Disconnect in Interactive Terminal (L316–336):** Terminal displays `QuickBooks.exe` crashing on `NahimicOSD.dll` (`NahimicService`), while lesson, figure, and narrative focus on `PDXPayClient.exe` on `amdkmdag.sys`. | Rewrite terminal objectives and mock output to inspect `PDXPayClient.exe`, `amdkmdag.sys`, and AMD driver rollback. |
| **02** | OS Diagnostics & Boot Recovery | MEDIUM | **Figure 2.1 Caption Discrepancy (L28):** Caption lists `PDXPay.exe` and `igdumdim64.dll` (Intel Graphics), conflicting with `amdkmdag.sys` in drill, resolution note, and epilogue. | Update Figure 2.1 caption to `PDXPayClient.exe` and `amdkmdag.sys` (AMD Radeon driver). |
| **03** | IPv4 Addressing & Boundaries | HIGH | **Grading Rubric Codifies Technical Error (L567):** Section 5 rubric awards Exemplary marks for explaining "switch CAM table poisoning" and "MAC address flapping" for an IP conflict. | Correct rubric: IP conflicts cause **ARP cache poisoning** and gateway IP-to-MAC oscillation. CAM tables do not flap for distinct MACs. |
| **04** | DNS Plumbing & Split-Horizon | MEDIUM | **Domain & IP Inconsistency in Terminal (L284–312):** Interactive terminal switches domain to `wiki.corp.local` and DC to `10.0.0.2`, diverging from `payroll.harrowmere.local` and `10.100.10.2`. | Align terminal commands and mock responses to use Harrowmere enterprise domain assets (`harrowmere.local`, `10.100.10.2`). |
| **05** | TCP Sockets & Port States | LOW | **Section Numbering Glitch (L195):** Heading reads `### 2.3 Interactive Diagnostic Console` immediately following Section 2.5. | Renumber heading to `### 3.1` or `### 2.6`. |
| **06** | Campus Flood Disaster Recovery | MEDIUM | **Terminal Command Mode Violation (L228):** Privilege EXEC prompt `Switch-BldgC# ` executes interface config command `switchport mode trunk` without entering configuration mode. | Add `configure terminal` and `interface range GigabitEthernet 0/49 - 50` steps to command sequence. |
| **06** | Campus Flood Disaster Recovery | LOW | **VLAN Name Inconsistency (L235):** Terminal outputs `VLAN 10 Corp_Workstations`; Section 2.1 and narrative define it as `CORP_WATER_BILLING`. | Synchronize terminal VLAN name to `CORP_WATER_BILLING`. |
| **07** | Protocol Triage & Hardening | PASS | **Cleartext Analysis & Security Matrix:** Flawlessly models packet capture credential extraction, STARTTLS transitions, and jump host rules. | Pass with distinction. |
| **08** | Identity & MFA Policy Triage | HIGH | **Terminal Flaw & Ground Truth Violation (L322–326):** Objective 3 uses `Get-ADUser` to "identify caller computer" (impossible; caller is in Event 4740). Objective 2 unlocks account before fixing caller, violating Rule 4. | Reverse order of objectives: isolate caller computer in Event 4740 first, remediate device, then unlock account. Replace `Get-ADUser` with Event 4740 XML parse. |
| **08** | Identity & MFA Policy Triage | MEDIUM | **Ken Vance in Sales Lore Defect (L42, L195):** Labels scenario as "Ken in Sales." | Rename character to Todd Miller (`TODD-SALES-14`). |
| **09** | Email Header Decomposition | LOW | **Maya Lin Title Inconsistency (L42):** Ticket subject refers to "Maya Lin (CEO)". | Change to "Maya Lin (Accounting Supervisor)" or use actual CEO Avery Chen. |
| **10** | Host Malware & Persistence | HIGH | **Terminal Label vs Command Contradiction (L367):** Objective claims to "remove persistence key" using trigger `Stop-Process -Id 4812 -Force`. | Killing a process does NOT remove persistence. Add command to delete Registry Run key (`Remove-ItemProperty`) or fix objective label. |
| **10** | Host Malware & Persistence | MEDIUM | **User Path Discrepancy (L373):** Terminal output shows path `C:\Users\Ken\AppData\Local\Temp\svch0st.exe` for host `TODD-SALES-14`. | Change path to `C:\Users\todd.miller\AppData\Local\Temp\svch0st.exe`. |
| **11** | Wireless Security & 802.1X | MEDIUM | **Terminal Diagnostic Trigger Misnomer (L197):** Objective claims to "identify rogue AP broadcasting on channel 6" using `netsh wlan show interfaces`. | `show interfaces` only shows connected adapter state. Change trigger to query BSSID list or review RSSI telemetry. |
| **11** | Wireless Security & 802.1X | LOW | **Ken in Sales Lore Defect (L43):** Refers to "Ken from Sales and the warehouse logistics team." | Disentangle Ken (Warehouse Supervisor) from Todd (Sales). |
| **12** | Incident Escalation & Handoff | MEDIUM | **PowerShell `Compare-Object` Output Hallucination (L385–389):** Mock terminal displays `Hash comparison: MATCH (0 differences)` for `Compare-Object`. | `Compare-Object` outputs nothing on identical strings. Use `$orig.Hash -eq $new.Hash` returning `True`. |

---

## Deep-Dive Technical Audits (CRITICAL & HIGH Severities)

---

### Audit 1: The Layer 2 Switch CAM Table vs. Layer 3 ARP Poisoning Conflation
* **Location:** Narrative 03 (L159, L184); Workbench 03 (L48, L57, L328, L567)
* **The Claim in Text:**  
  > *"Every time one of them talks, its gratuitous ARP announcement poisons the switch MAC table and the ARP cache on neighboring PCs."* (Narrative 03, L159)  
  > *"Isolate the Layer 2 MAC address flapping war between Frank's shipping PC and the rogue device"* (Narrative 03, L184)  
  > *"Rule 4: Two Devices Cannot Share a Cubicle. Duplicate IPs cause continuous ARP poisoning and MAC flapping"* (Workbench 03, L48)  
  > Section 5 Rubric awards Exemplary to students who explain *"MAC address flapping; isolates duplicate IP address conflicts; explains gratuitous ARP and switch CAM table poisoning."* (Workbench 03, L567)

* 👓 **"Well, Actually..." (The Technical Flaw):**  
  An unmanaged or Layer 2 Ethernet switch **has zero awareness of IPv4 addresses**. A switch's forwarding database—known as the Content-Addressable Memory (CAM) table or MAC address table—maps **Source Layer 2 MAC addresses to physical ingress switch ports**.
  
  In the scenario presented:
  - Frank's Dell desktop possesses MAC `0014.228a.41ef` on physical port `GigabitEthernet 1/0/12`.
  - The rogue HP printer possesses MAC `0025.b318.c290` on physical port `GigabitEthernet 1/0/28`.
  - Both devices are configured with the identical IP address: `10.100.4.55`.

  When Frank's PC transmits an Ethernet frame, the switch observes source MAC `0014.228a.41ef` entering port `Gi1/0/12` and updates its CAM table entry for that MAC. When the HP printer transmits an Ethernet frame, the switch observes source MAC `0025.b318.c290` entering port `Gi1/0/28` and updates its CAM table entry for that MAC. 
  
  **The switch CAM table is completely stable and never flaps!** Port 12 has MAC A; Port 28 has MAC B.
  
  What *is* poisoned and what *does* flap is the **Layer 3 ARP Cache** on the default gateway router and neighboring workstations! Under RFC 826, when Frank's PC sends a gratuitous ARP, neighboring hosts bind `10.100.4.55 -> 0014.228a.41ef`. When the printer speaks, they overwrite their cache with `10.100.4.55 -> 0025.b318.c290`. 
  
  **"MAC address flapping"** occurs *only* when the **exact same MAC address** is seen on multiple switch ports (e.g., during a Layer 2 loop, or an active MAC spoofing/cloning attack). Calling an IP conflict a "switch MAC table poisoning" and "MAC flapping war" is a grave layer conflation that directly undermines CompTIA Network+ Domain 1.4 and 5.2 objectives.

* 🔬 **RFC & Architectural Reality:**  
  - **RFC 826 (Address Resolution Protocol):** ARP is an encapsulation translation protocol mapping Layer 3 protocol addresses to Layer 2 hardware addresses on a local broadcast domain. ARP cache tables exist exclusively on Layer 3 host network stacks and router routing engines.
  - **IEEE 802.1D / 802.1Q (Bridging Architecture):** Layer 2 bridges filter and forward frames strictly by destination MAC address using the filtering database (FDB / CAM). Bridges do not parse payload bytes beyond the 802.3/Ethernet II header.

* 🛠️ **The SME Fix:**  
  1. In Narrative 03, line 159, replace:
     ```markdown
     "Every time one of them talks, its gratuitous ARP announcement poisons the switch MAC table and the ARP cache on neighboring PCs. Traffic flips back and forth depending on who spoke last."
     ```
     With:
     ```markdown
     "Every time one of them talks, its gratuitous ARP announcement poisons the Layer 3 ARP table on the router and neighboring PCs. The switch MAC table is completely steady—it knows exactly which port owns each physical card—but the IP-to-MAC mapping flaps wildly across the subnet depending on who spoke last."
     ```
  2. In Narrative 03 line 184 and Workbench 03 line 48, replace `"MAC address flapping war"` and `"MAC flapping"` with `"IP-to-MAC ARP oscillation"` or `"ARP cache poisoning war"`.
  3. In Workbench 03 Section 5 rubric (line 567), rewrite the criterion:
     ```markdown
     | **ARP Dynamics & Layer 2/3 Troubleshooting** | Flawlessly inspects and interprets `arp -a` output; detects IP-to-MAC ARP cache poisoning; isolates duplicate IP address conflicts; explains gratuitous ARP and distinguishes Layer 3 ARP cache corruption from Layer 2 switch CAM table forwarding. |
     ```

---

### Audit 2: Workbench 02 Scenario Disconnect & Application/Driver Chaos
* **Location:** Workbench 02 (L28, L251, L287, L316–336, L522)
* **The Claim in Text:**  
  - Chapter Title: "OS Diagnostics, Event Log Triage, & Boot Recovery (Maya Lin / PDX-Pay)"
  - Figure 2.1 Caption (L28): `Faulting application name PDXPay.exe, faulting module name igdumdim64.dll (Intel Graphics User Mode Driver)`
  - Drill 1 Solution (L251): `FaultModuleName: amdkmdag.sys during hardware acceleration rendering... PDXPayClient.exe`
  - Clean Boot Matrix (L287): Culprit is `Service 3 (OEM-GpuAssist.exe)`
  - Interactive Terminal (`lnk-terminal`, L316–336):
    ```powershell
    Application Error 1000: Faulting application name: QuickBooks.exe, version: 23.0.4
                            Faulting module name: NahimicOSD.dll, version: 2.1.8
    Stop-Service -Name NahimicService
    ```
  - Ticket Resolution Note (L522): `Faulting Application: PDXPayClient.exe | Faulting Module: amdkmdag.sys`

* 👓 **"Well, Actually..." (The Technical Flaw):**  
  This is a blatant copy-paste defect that shatters pedagogical agency. A student reading about Maya Lin's mission-critical payroll application (`PDX-Pay` / `PDXPayClient.exe`) freezing under an AMD Radeon kernel driver deadlock (`amdkmdag.sys`) steps up to the interactive terminal and is asked to run:
  `Get-EventLog -LogName Application -InstanceId 1000`
  Which suddenly outputs a crash for **QuickBooks.exe** crashing on **NahimicOSD.dll** (an MSI audio on-screen display overlay helper)! The terminal objective then requires them to run `Stop-Service -Name NahimicService`.
  
  Worse still, Figure 2.1 caption refers to **igdumdim64.dll** (an Intel Integrated Graphics user-mode driver). There are FOUR completely conflicting failure scenarios running simultaneously in the same lab:
  1. `PDXPayClient.exe` on `amdkmdag.sys` (Narrative, Drill 1, Ticket Note, Epilogue)
  2. `PDXPay.exe` on `igdumdim64.dll` (Figure 2.1 Caption)
  3. `OEM-GpuAssist.exe` (Clean Boot Table)
  4. `QuickBooks.exe` on `NahimicOSD.dll` (Interactive Terminal)

* 🔬 **Architectural Reality:**  
  Enterprise accounting clients invoking Direct3D hardware acceleration frequently conflict with buggy OEM kernel display drivers (`amdkmdag.sys`), tripping Windows Display Driver Timeout Detection and Recovery (TDR Event ID 4101). The entire lab was designed around this scenario. The QuickBooks/Nahimic block is an unedited snippet copied from a consumer gaming PC troubleshooting forum.

* 🛠️ **The SME Fix:**  
  1. Update Figure 2.1 caption in Workbench 02 (line 28) and Narrative 02:
     ```markdown
     caption: "Macro console view: Windows Event Viewer Application log. Event ID 1000: Faulting application name PDXPayClient.exe, faulting module name amdkmdag.sys (AMD Radeon Kernel Mode Driver), exception code 0xc0000005."
     ```
  2. Overhaul the `lnk-terminal` block in Workbench 02 (lines 297–338) to simulate the actual Maya Lin incident:
     ```yaml
     ```lnk-terminal
     title: "POWERSHELL: EVENT VIEWER & DISPLAY DRIVER TRIAGE"
     shell: "powershell"
     prompt: "PS C:\Support> "
     replay: true
     objectives:
       - id: "obj-crash"
         label: "Query Application crash logs for PDXPayClient (Event ID 1000)"
         trigger: "Get-WinEvent -FilterHashtable @{LogName='Application'; Id=1000} | Select -First 1"
       - id: "obj-tdr"
         label: "Query System log for Display Driver TDR timeouts (Event ID 4101)"
         trigger: "Get-WinEvent -FilterHashtable @{LogName='System'; Id=4101} | Select -First 1"
       - id: "obj-accel"
         label: "Disable client GPU hardware acceleration in config"
         trigger: "Set-Content -Path 'C:\Program Files\PDX-Pay\config.ini' -Value 'HardwareAcceleration=0'"
     ---
     Get-WinEvent -FilterHashtable @{LogName='Application'; Id=1000} | Select -First 1: |
       TimeCreated          Id Message
       -----------          -- -------
       10/18 08:15:22 AM  1000 Faulting application name: PDXPayClient.exe, version: 4.2.1
                               Faulting module name: amdkmdag.sys, version: 31.0.12024.2005
                               Exception code: 0xc0000005 (Access Violation)
                               Fault offset: 0x00084a10
                               Faulting process id: 0x1420

     Get-WinEvent -FilterHashtable @{LogName='System'; Id=4101} | Select -First 1: |
       TimeCreated          Id Message
       -----------          -- -------
       10/18 08:15:24 AM  4101 Display driver amdkmdag stopped responding and has successfully recovered.

     Set-Content -Path 'C:\Program Files\PDX-Pay\config.ini' -Value 'HardwareAcceleration=0': |
       Updating PDX-Pay configuration...
       Setting: HardwareAcceleration=0 (Fallback to stable CPU GDI+ rasterization)
       [OK] Direct3D acceleration disabled. Payroll client initializes cleanly without GPU deadlock.
     ```

---

### Audit 3: Narrative 01 vs. Workbench 01 Baud Rate Timing Inversion & DIP Switch Physics
* **Location:** Narrative 01 (L130–136); Workbench 01 (L218, L260, L270–283)
* **The Claim in Text:**  
  - Narrative 01:
    > *"the abrupt loss of standby voltage had reset the industrial serial controller back to its unconfigured factory defaults—reverting the communication baud rate from 19,200 baud back to 9,600 baud. The Toledo scale head was streaming data twice as fast as the receiver clock could sample it, slicing every byte in half. On the lower edge of the motherboard sat a small blue block of eight miniature switches labeled SW1."*
  - Workbench 01:
    > *"When the Toledo scale transmits at 9600 baud ($T_{\text{bit}} = 104.17\,\mu\text{s}$) but the terminal UART is configured for 19200 baud ($T_{\text{bit}} = 52.08\,\mu\text{s}$)..."* (L218)  
    > `Baud Rate: 19200... Diagnostics: Switch 3 is ON, locking the UART receiver to 19200 baud. Scale transmitter hardware is calibrated for 9600 baud. Action Required: Set Switch 3 OFF, Switch 4 ON.` (L260–277)

* 👓 **"Well, Actually..." (The Technical Flaw):**  
  1. **Physical Impossibility of DIP Switch Power Reset:** A Dual In-line Package (DIP) switch is a set of manual, mechanical slide or rocker switches soldered directly to a PCB. It contains mechanical copper wiper contacts. **Cutting power to a motherboard cannot physically toggle a mechanical DIP switch!** If the UART clock prescaler is hardwired to DIP switch bank `SW1`, toggling the AC power breaker will leave the DIP switches in the exact physical position they were in before the power cut.
  2. **Mathematical Inversion between Narrative and Lab:**  
     - In Narrative 01: The terminal reset to **9,600 baud**, while the scale is sending at **19,200 baud** ("scale was streaming twice as fast as the receiver clock could sample it").
     - In Workbench 01: The terminal is locked at **19,200 baud**, while the scale transmits at **9,600 baud** ("receiver clock samples at $26\,\mu\text{s}$ and $78\,\mu\text{s}$ while scale is still in Start bit").
     These two documents present the exact opposite mathematical scenarios!

* 🔬 **Hardware & Serial Timing Reality:**  
  Standard PC 16550 UARTs derive their baud rates from a master crystal oscillator (typically $1.8432\text{ MHz}$). The clock divider is:
  $$\text{Divisor} = \frac{1,843,200}{16 \times \text{Baud Rate}}$$
  - For $9,600\text{ Baud}$: $\text{Divisor} = 12$ ($0x000C$). Bit duration $T_{\text{bit}} = \frac{1}{9600} \approx 104.17\,\mu\text{s}$.
  - For $19,200\text{ Baud}$: $\text{Divisor} = 6$ ($0x0006$). Bit duration $T_{\text{bit}} = \frac{1}{19200} \approx 52.08\,\mu\text{s}$.
  Workbench 01's mathematical explanation of a 9,600 baud transmission sampled by a 19,200 baud receiver (sampling twice per bit and framing out by Bit 4) is brilliant and accurate. Narrative 01 must be corrected to match Workbench 01.

* 🛠️ **The SME Fix:**  
  Rewrite Narrative 01 lines 130–136:
  ```markdown
  Then the mistake hit me like cold water: the serial baud rate.
  
  When Sorting Line 4 had glitched earlier in the week, an external contractor had strapped the motherboard's hardware DIP switch bank SW1 to 19,200 baud to test a high-speed scanner, leaving the UART clock divider prescaler locked at twice its normal frequency. The Toledo scale head was streaming weight data at its factory-calibrated 9,600 baud—half as fast as the receiver UART was sampling it. By the time the receiver clock counted down ten bit-times, the scale had only transmitted five bits, triggering persistent framing errors.
  
  On the lower edge of the motherboard sat the small blue block of eight miniature switches labeled SW1. Switch 3 was toggled ON for 19,200 baud. I had to slide Switch 3 OFF and Switch 4 ON to set the divider back to 9,600 baud before the five o'clock whistle blew.
  ```

---

### Audit 4: The Todd Miller vs. Ken Vance Character Identity Crisis
* **Location:** Narrative 08 (L40–74, L94), Narrative 09 (L70–74), Narrative 10 (L97–126), Narrative 11 (L36–48); Workbench 08 (L42, L195), Workbench 10 (L41, L373), Workbench 11 (L43)
* **The Textual Errors:**  
  - Narrative 08:
    > *"Todd in sales was locked out of the CRM after a phone wipe. He wanted a quick fix.  
    > 'I already have multifactor,' Ken said. 'Password plus a PIN on the laptop...'"* (L40–42)  
    > *"Ken was quiet for a second... 'Password plus PIN was a house rule, then,' he muttered... While Ken got his phone out..."* (L50–60)  
    > *"Ken is insisting Password plus PIN is multifactor..."* (L94)
  - Narrative 09:
    > *"Todd in sales texted a screenshot... The tone was HR-casual, which Ken trusts more than HR-formal... Ken muttered, 'I almost clicked because it said my teammates already finished.'"* (L70–74)
  - Narrative 10:
    > *"Todd from sales called... user: todd.miller... TODD-SALES-14... Pull the cable — isolate the host. Ken unplugged. He still had a file mid-copy..."* (L97–126)
  - Narrative 11:
    > *"Todd from sales called from a hotel before a customer demo... 'And WEP?' Ken asked... Ken muttered something about customer politics..."* (L36–48)
  - Workbench 10 Terminal:
    > `C:\Users\Ken\AppData\Local\Temp\svch0st.exe` (L373)

* 👓 **"Well, Actually..." (The Technical Flaw):**  
  Under the `PORTLAND_AUTHOR_BIBLE.md` (lines 88, 144, 431):
  - **Ken Vance** is a 50-year-old shipping veteran, supervisor of the Gresham freight staging distribution warehouse. He moves freight pallets, wears a canvas jacket, hates when forklifts lose barcode connectivity, and helped Ethan land his help desk rotation.
  - **Todd Miller** is the young Inside Sales representative on the 4th floor (`TODD-SALES-14`), who works in an office cubicle, travels to hotels with a corporate laptop, and manages customer CRM accounts.
  
  The author introduced Todd in sales at the beginning of each of these scenes, but then suffered a catastrophic character alias bug, referring to him as "Ken" throughout the remainder of each episode! This creates absurdities: Ken Vance is suddenly traveling to hotels for sales demos, Ken is locked out of Salesforce CRM, Ken's laptop username is `C:\Users\Ken` while hostname is `TODD-SALES-14`, and Ken is pulling the cable on Todd's laptop.

* 🛠️ **The SME Fix:**  
  Systematically replace "Ken" with "Todd" across Episodes 08, 09, 10, and 11, and in Workbenches 08, 10, and 11, wherever the Inside Sales representative is being depicted. Preserve Ken Vance strictly for the Gresham loading dock and warehouse logistics contexts.

---

### Audit 5: BitLocker Recovery Key Formatting Hallucination
* **Location:** Narrative 02 (L92)
* **The Claim in Text:**  
  > *"my console refreshed to display the twelve groups of four digits. I read the 48 digits clearly over the phone. Once Maya keyed in the final number, the machine unlocked..."* (Narrative 02, L92–93)

* 👓 **"Well, Actually..." (The Technical Flaw):**  
  Microsoft BitLocker full-disk encryption utilizes a 48-digit numerical recovery password. However, Windows Boot Manager, Active Directory Users & Computers (ADUC), Microsoft Entra ID (Azure AD), and the BitLocker Recovery Console format this 48-digit number as **eight groups of six digits**, separated by hyphens:
  $$\boxed{\text{XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX-XXXXXX}}$$
  
  Each 6-digit block represents 16 bits of key data encoded with a built-in checksum: the 6-digit number is mathematically verified by the BitLocker bootloader using a modulo-11 check ($N \pmod{11} == 0$). If a single digit in a 6-digit block is mis-typed, Windows immediately flags that specific 6-digit box in red before the user enters the remaining digits!
  
  "Twelve groups of four digits" is a hallucination that conflates 16-character credit card numbers or software license product keys. No BitLocker system in Microsoft's history has ever formatted a recovery key in 12 groups of 4 digits.

* 🔬 **Architectural Citation:**  
  Microsoft Learn: *BitLocker Recovery Guide* & *BitLocker Key Protector Architecture*:  
  > *"The BitLocker recovery password is a 48-digit numerical password divided into eight 6-digit segments. The boot environment validates each 6-digit segment using an arithmetic checksum before processing the full AES volume master key (VMK)."*

* 🛠️ **The SME Fix:**  
  In Narrative 02, line 92, replace:
  ```markdown
  Jules reviewed the log, approved the request with her smartcard badge, and my console refreshed to display the twelve groups of four digits. I read the 48 digits clearly over the phone.
  ```
  With:
  ```markdown
  Jules reviewed the log, approved the request with her smartcard badge, and my console refreshed to display the eight groups of six digits. I read the 48 numbers clearly over the phone, six digits at a time.
  ```

---

### Audit 6: Complete Absence of Section 5 Performance Rubrics in Workbenches 00 and 01
* **Location:** `workbench/00-the-four-rubber-bands.md` and `workbench/01-the-paper-cert.md`
* **The Defect:**  
  - Workbench 00 ends abruptly after Section 4 (line 609), lacking Section 5 (What Good Looks Like / Shift Quality Checklist) and Section 6 (Epilogue).
  - Workbench 01 contains Sections 1, 2, 3, 4, and 6, but completely skips Section 5.
* **Governing Standard Violation:**  
  `TECHNICAL_NARRATIVE_AUTHORING_PRINCIPLES.md` mandates that every single workbench module must conclude with an objective, four-tier Performance Deliverable Rubric ("What Good Looks Like / Shift Quality Checklist") grading learners on Diagnostic Methodology, Technical Analysis, Operating System / Security Execution, and Documentation Quality. Omitting Section 5 deprives students and instructors of passing criteria for their first two labs.
* 🛠️ **The SME Fix:**  
  Draft and insert standard Section 5 rubric tables into `workbench/00-the-four-rubber-bands.md` and `workbench/01-the-paper-cert.md` (see Section 6 of this review for exact markdown).

---

### Audit 7: Workbench 08 Terminal Logic and Tool Mismatch
* **Location:** Workbench 08 (L321–326)
* **The Defect in Terminal Objectives:**  
  ```yaml
  objectives:
    - id: "obj-lockout"
      label: "Find account lockout events (Event ID 4740)"
      trigger: "Get-WinEvent -FilterHashtable @{LogName='Security';Id=4740}"
    - id: "obj-unlock"
      label: "Unlock Nora's domain account"
      trigger: "Unlock-ADAccount -Identity nora.finance"
    - id: "obj-caller"
      label: "Identify caller computer causing stale password lockouts"
      trigger: "Get-ADUser -Identity nora.finance -Properties *"
  ```
* 👓 **"Well, Actually..." (The Technical Flaw):**  
  1. **Ground Truth Violation:** Workbench 08 Ground Truth Rule 4 explicitly warns:
     > *"Never Clear a Lockout Without Identifying the Caller: Clicking 'Unlock Account' treats the symptom, not the cause. If a user's phone is still hammering the domain controller, the account will re-lock within minutes. You must inspect Event ID 4740 in the Security Event Log, extract the Caller Computer Name, and terminate the offending session before unlocking."*  
     Yet the terminal widget requires the student to run `Unlock-ADAccount` in Objective 2 *before* identifying the caller computer in Objective 3!
  2. **Invalid Cmdlet Capability:** Objective 3 uses `Get-ADUser -Identity nora.finance -Properties *` to "Identify caller computer causing stale password lockouts."  
     **`Get-ADUser` does not return the Caller Computer Name!** Active Directory user objects have attributes like `BadLogonCount`, `badPasswordTime`, `lastLogonTimestamp`, and `LockedOut`. The name of the client machine that transmitted the bad password exists **strictly inside the Security Event Log under Event ID 4740 XML event data (`CallerComputerName`)**!
* 🛠️ **The SME Fix:**  
  Restructure the objectives:
  1. Objective 1: Query Event ID 4740 to locate lockout event.
  2. Objective 2: Parse Event ID 4740 XML message to extract `CallerComputerName` (`WKS-NORA-PHONE`).
  3. Objective 3: Unlock account with `Unlock-ADAccount -Identity nora.finance` after the caller is identified.

---

### Audit 8: Workbench 10 Process Termination vs. Persistence Removal
* **Location:** Workbench 10 (L366–368)
* **The Defect in Terminal Objectives:**  
  ```yaml
  - id: "obj-kill"
    label: "Terminate malicious process and remove persistence key"
    trigger: "Stop-Process -Id 4812 -Force"
  ```
* 👓 **"Well, Actually..." (The Technical Flaw):**  
  `Stop-Process -Id 4812 -Force` executes the `TerminateProcess()` Windows Win32 API. It forcibly terminates threads executing inside the RAM address space of process 4812. **It touches zero registry keys, deletes zero scheduled tasks, and removes zero services!**  
  Labelling this command as "Terminate malicious process and remove persistence key" directly reinforces the lethal junior technician mistake that Ground Truth Rule 3 explicitly condemns: *"Killing the Process Does Not Kill the Persistence."*
* 🛠️ **The SME Fix:**  
  Split into two distinct commands:
  ```yaml
  - id: "obj-kill"
    label: "Terminate in-memory malicious process"
    trigger: "Stop-Process -Id 4812 -Force"
  - id: "obj-persist"
    label: "Delete malicious Registry Run persistence key"
    trigger: "Remove-ItemProperty -Path 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' -Name 'svch0st'"
  ```

---

## 👓 "Well, Actually..." Callouts & Engineering Reality

1. **"The capacitors regulate clean DC voltage to the memory bus."**  
   *Narrative 00, Line 44*  
   *Reality:* Motherboard capacitors ringing the CPU socket are multi-phase VRM buck converters filtering CPU VCore (typically $0.8\text{V} - 1.4\text{V}$). Memory bus DDR voltage regulation ($1.2\text{V} - 1.35\text{V}$) is physically located adjacent to the DIMM slots on modern PCBs.
2. **"The abrupt loss of standby voltage had reset the industrial serial controller... On the lower edge of the motherboard sat a small blue block of eight miniature switches labeled SW1."**  
   *Narrative 01, Line 132*  
   *Reality:* Mechanical DIP switches cannot change physical position during an electrical brownout. If baud rates are strapped by DIP switches, the setting is physically non-volatile.
3. **"Every time one of them talks, its gratuitous ARP announcement poisons the switch MAC table..."**  
   *Narrative 03, Line 159*  
   *Reality:* A switch MAC table records which physical port sent which MAC address. It does not map IP addresses. Two distinct MAC addresses on two distinct ports produce two steady CAM entries. It is the host and router **ARP cache** that flaps.
4. **"display the twelve groups of four digits"**  
   *Narrative 02, Line 92*  
   *Reality:* BitLocker recovery keys have never been 12 groups of 4 digits. They are 8 groups of 6 digits with modulo-11 arithmetic checksums.
5. **"switchport trunk encapsulation dot1q"**  
   *Narrative 06, Line 73; Workbench 06, Line 190*  
   *Reality:* On Cisco Catalyst 2960-X and all modern Catalyst switches, ISL is completely unsupported. Entering `switchport trunk encapsulation dot1q` returns `% Invalid input detected at '^' marker`. Only `switchport mode trunk` is valid.
6. **"Get-ADUser -Identity nora.finance -Properties * to identify caller computer"**  
   *Workbench 08, Line 325*  
   *Reality:* `ADUser` directory objects do not track client hostnames of failed logons. That data lives exclusively in Domain Controller Security Event ID 4740 (`CallerComputerName`).
7. **"Stop-Process -Id 4812 -Force to terminate malicious process and remove persistence key"**  
   *Workbench 10, Line 367*  
   *Reality:* `Stop-Process` kills threads in volatile RAM. It does not touch the registry or scheduled tasks.
8. **"netsh wlan show interfaces to identify rogue access point broadcasting on channel 6"**  
   *Workbench 11, Line 197*  
   *Reality:* `show interfaces` only outputs telemetry for the adapter's currently connected BSSID. It cannot detect or display unassociated rogue APs broadcasting in the surrounding RF spectrum.
9. **"Compare-Object -ReferenceObject $orig -DifferenceObject $new -> Hash comparison: MATCH (0 differences)"**  
   *Workbench 12, Line 385*  
   *Reality:* In PowerShell, `Compare-Object` on two equal objects produces `$null` (zero output). It does not print "MATCH (0 differences)".

---

## 🔬 RFC & Architectural Citations

- **RFC 826:** *An Ethernet Address Resolution Protocol*. Delineates the boundary between Layer 2 MAC delivery and Layer 3 IP mapping. ARP caches live in host/router IP stacks, not Layer 2 bridge CAM tables.
- **RFC 2131 & 2132:** *Dynamic Host Configuration Protocol*. Specifies UDP ports 67/68, the DORA state machine, and DHCP Relay Agent `giaddr` behavior.
- **RFC 3927:** *Dynamic Configuration of IPv4 Link-Local Addresses*. Specifies `169.254.0.0/16` (APIPA), mandating that link-local addresses must never route across a router.
- **RFC 1035 & 2308:** *Domain Names - Implementation and Specification* & *Negative Caching of DNS Queries (DNS NCACHE)*. Dictates that NXDOMAIN responses must be cached by client resolvers for the duration of the SOA Minimum TTL.
- **RFC 793 & RFC 9293:** *Transmission Control Protocol*. Specifies the 11-state TCP state machine, 3-way handshake, active closure, and the $2 \times \text{MSL}$ `TIME_WAIT` duration.
- **RFC 5321 & 5322:** *Simple Mail Transfer Protocol* & *Internet Message Format*. Formally distinguishes between the SMTP transport envelope (`MAIL FROM`) and the message presentation header (`From:`).
- **RFC 7208, 6376, 7489:** *SPF, DKIM, and DMARC Specifications*. Defines identifier alignment: DMARC requires that the domain in RFC 5322 `From:` align with either an authorized SPF envelope domain or a cryptographically valid DKIM `d=` domain.
- **RFC 3227:** *Guidelines for Evidence Collection and Archiving*. Establishes the authoritative Order of Volatility: CPU registers/cache $\rightarrow$ RAM $\rightarrow$ Temporary file systems $\rightarrow$ Persistent disk $\rightarrow$ Network topology $\rightarrow$ Archival media.
- **NIST SP 800-63B:** *Digital Identity Guidelines: Authentication and Lifecycle Management*. Deprecates arbitrary composition rules, mandatory 90-day rotations, and SMS OTP; mandates length and entropy (passphrases) and breach checking.

---

## 🛠️ Complete SME Fixes & Content Rewrites

### Fix 1: Section 5 Rubrics for Workbenches 00 and 01

#### For `workbench/00-the-four-rubber-bands.md` (Insert between Section 4 and end of file):
```markdown
---

## 5. What Good Looks Like (Shift Quality Checklist)

| Performance Criterion | Exemplary (Full Mastery) | Satisfactory (Competent) | Needs Revision (Deficient) |
| :--- | :--- | :--- | :--- |
| **Anatomy & Volatility Triage** | Flawlessly distinguishes volatile execution state (RAM) from non-volatile persistent storage (NVMe/SSD). Articulates why cutting power destroys in-memory C2 and decryption keys without eradicating persistence. | Understands RAM loses data on power loss, but hesitates when explaining why malware resurrects after reboot. | Asserts that powering down a machine eradicates a malware infection; confuses system memory with hard disk storage. |
| **Network Identity Triad (L2/L3/L4)** | Explains with precision how MAC addresses are rewritten hop-by-hop while IP addresses remain constant end-to-end. Correctly explains how Layer 4 ports map packets to OS socket buffers. | Explains that MAC addresses are local and IPs route globally, but displays minor confusion on router frame encapsulation. | Believes routers forward Layer 2 MAC addresses across the internet; confuses port numbers with physical hardware jacks. |
| **CLI Diagnostic Methodology** | Executes the systematic Ping Ladder (Loopback $\rightarrow$ Local IP $\rightarrow$ Gateway $\rightarrow$ Remote IP $\rightarrow$ FQDN). Accurately interprets `whoami /priv`, `hostname`, and `ipconfig /all`. | Runs CLI commands accurately but occasionally skips intermediate ping steps (e.g., pings Google before testing gateway). | Relies exclusively on graphical network status indicators; cannot interpret `ipconfig` or ping timeouts. |
| **Commit Before You Touch (CBYT)** | Consistently forms testable, falsifiable predictions before executing commands or opening chassis. Documents predicted layer, tool, and outcome. | Forms general theories before acting, but occasionally checks settings out of curiosity. | Reboots or alters settings randomly without forming a diagnostic hypothesis; destroys evidence. |
```

#### For `workbench/01-the-paper-cert.md` (Insert between Section 4 and Section 6):
```markdown
---

## 5. What Good Looks Like (Shift Quality Checklist)

| Performance Criterion | Exemplary (Full Mastery) | Satisfactory (Competent) | Needs Revision (Deficient) |
| :--- | :--- | :--- | :--- |
| **Physical & Electrical Safety** | Measures DC voltage rails (+12V, +5V, +3.3V) against strict ATX $\pm 5\%$ tolerance limits. Discharges flea power before probing; verifies zero ground-fault potential. | Uses multimeter correctly and identifies failing rails, but forgets to bleed flea power before extracting circuit boards. | Probes energized circuits recklessly; unaware of ATX voltage tolerance thresholds; fails to check ground continuity. |
| **POST Code Diagnostic Triage** | Accurately correlates hexadecimal POST codes (`00`/`FF`, `C1`, `E0`) with specific hardware initialization stages (CPU, Memory, Bus). Never reseats components blindly. | Looks up POST codes in matrix correctly, but occasionally jumps to swapping hardware before checking cable continuity. | Ignores diagnostic LED readouts; assumes all boot halts are caused by unseated RAM modules. |
| **Serial Communications & Timing Math** | Flawlessly calculates bit duration ($T_{\text{bit}} = \frac{1}{\text{Baud}}$) and frame timing. Explains how receiver clock desynchronization triggers UART framing errors (`FE`). | Recognizes framing errors stem from baud rate mismatches, but relies on trial-and-error rather than calculating symbol periods. | Confuses baud rate with bandwidth; unable to explain why mismatched baud rates produce garbled ASCII text. |
| **Physical Component Handling** | Employs precision mechanical techniques for pin alignment without snapping contacts; respects dielectric boundaries; inspects wire harnesses for chassis pinch points. | Handles hardware safely but applies excessive force when seating memory or expansion cards. | Forces misaligned RAM modules, breaking retention latches; bends connector pins beyond yield strength. |
```

---

## Actionable Summary: Top 15 Recommendations

1. **[CRITICAL - Workbench 02]:** Replace the entire QuickBooks/NahimicOSD terminal block with the authentic `PDXPayClient.exe` / `amdkmdag.sys` display driver triage console.
2. **[CRITICAL - Workbench 01]:** Author and insert Section 5 Performance Checklist into `workbench/01-the-paper-cert.md`.
3. **[HIGH - Workbench 00]:** Author and insert Section 5 Performance Checklist and Section 6 Epilogue into `workbench/00-the-four-rubber-bands.md`.
4. **[HIGH - Narrative 08, 09, 10, 11 & Workbench 08, 10, 11]:** Disentangle Ken Vance (Warehouse Supervisor) and Todd Miller (Inside Sales). Replace "Ken" with "Todd" across all sales, hotel, and workstation-14 scenes.
5. **[HIGH - Narrative 03 & Workbench 03]:** Eliminate the Layer 2/3 conflation. Clarify that duplicate IP conflicts cause Layer 3 **ARP cache poisoning**, NOT "switch CAM table poisoning" or "MAC address flapping." Correct the Section 5 rubric.
6. **[HIGH - Narrative 01 & Workbench 01]:** Harmonize serial baud rate settings. Update Narrative 01 to match Workbench 01 (scale at 9,600 baud, terminal misconfigured to 19,200 baud). Remove the claim that cutting power resets mechanical DIP switches.
7. **[HIGH - Narrative 02]:** Correct BitLocker recovery key grouping from "twelve groups of four digits" to "eight groups of six digits."
8. **[HIGH - Workbench 08]:** Fix terminal objectives: parse Event ID 4740 XML for `CallerComputerName` instead of `Get-ADUser`, and enforce identifying the caller *before* running `Unlock-ADAccount`.
9. **[HIGH - Workbench 10]:** Fix terminal objective: `Stop-Process` does not remove persistence. Add a registry deletion command (`Remove-ItemProperty`) or correct the objective label.
10. **[MEDIUM - Narrative 06 & Workbench 06]:** Remove deprecated `switchport trunk encapsulation dot1q` command from Cisco Catalyst 2960-X configuration blocks.
11. **[MEDIUM - Narrative 07]:** Remove duplicate paragraph describing the queue monitor tickets (lines 116–119).
12. **[MEDIUM - Workbench 06]:** Add `configure terminal` and interface selection commands to Cisco IOS terminal trigger `switchport mode trunk`.
13. **[MEDIUM - Workbench 11]:** Replace `netsh wlan show interfaces` with a scan/telemetry command that actually identifies surrounding rogue BSSIDs.
14. **[MEDIUM - Workbench 12]:** Correct mock PowerShell output for `Compare-Object` to reflect authentic PowerShell syntax (`$orig.Hash -eq $new.Hash`).
15. **[LOW - Workbench 04]:** Synchronize terminal domain names to `harrowmere.local` and DC IP to `10.100.10.2`.
