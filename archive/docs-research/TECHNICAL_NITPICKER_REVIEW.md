# Portland Desk Visual Production Audit: Technical SME & Adversarial Nitpicker Review
**Repository:** `learning-narrative-kit`  
**Reviewer:** Adversarial Technical SME & Hardware/Network Nitpicker (`technical_nitpicker`)  
**Target Document:** `docs/research/PROPOSED_VISUALS_AUDIT.md` (Digital Art Director)  
**Governing Standards:** `docs/research/TECHNICAL_NARRATIVE_AUTHORING_PRINCIPLES.md`, `docs/research/VISUAL_ART_DIRECTION.md`, RFC 793/9293 (TCP), RFC 826 (ARP), RFC 3227 (Evidence Collection), RFC 5321/5322/7489 (Email/DMARC), EIA/TIA-574 (DE-9), NIST SP 800-63B, TCG TPM 2.0 Library Specification.

---

## 1. Executive Verdict: Ruthless Ground Truth vs. Engineering Hallucinations

The Digital Art Director's visual catalog (`docs/research/PROPOSED_VISUALS_AUDIT.md`) establishes a commendable structural foundation, particularly in enforcing **The Absolute Zero-Text Rule** and isolating semantic badges to Docsify `callout-panel` overlays.

However, an engineering audit of the physical geometry, circuit properties, protocol state machines, and forensic mechanics reveals **critical technical errors and physical hallucinations**. If published as drafted, these plates would fail real-world operational peer review and teach dangerous technical falsehoods to students preparing for CompTIA A+, Network+, Security+, and live enterprise operations.

### High-Severity Failure Summary
1. **The Write-Blocker Live RAM Hallucination (Figure 12.1 — CRITICAL):**  
   The catalog depicts and captions an *"external hardware write-blocking acquisition bridge copying live memory from an energized laptop to an external solid-state drive."*  
   **Reality:** A hardware write-blocker is a storage bus controller bridge (SATA/NVMe/USB) engineered strictly for **dead-disk forensic acquisition** to block ATA/SCSI write commands. A write-blocker cannot extract volatile DRAM from a laptop USB port. Furthermore, placing a write-blocker in-line with an external evidence drive would *block writes to the evidence drive*. Live memory capture under RFC 3227 requires trusted software utilities executing on the host.
2. **The 0.5mm Mechanical Pencil vs. 1.0mm D-Sub Pin Paradox & "Ground Fault" Error (Figure 1.1 — SEVERE):**  
   - **Mechanical Sizing Paradox:** Standard RS-232 DE-9 Size 20 contact pins have an outer diameter of **1.016 mm (0.040 in)**. The hollow guide tube of a 0.5 mm drafting pencil has an internal bore of **~0.55 mm**. A 1.0 mm solid copper-alloy pin physically cannot fit inside a 0.55 mm sleeve.
   - **Circuit Misnomer:** Overlay Pin 1 labels a pin bent backward against the blue plastic insulator as a *"Ground Fault."* The plastic housing is a non-conductive dielectric. Bending against plastic creates an **open circuit (signal discontinuity / floating line)**, not a short to ground. Signal ground (Pin 5) is on the opposite corner.
3. **Layer 2 Switch Backplane Conflation (Figure 3.1 — HIGH):**  
   The prompt depicts a *"sharp vertical threshold barrier"* on a Layer 2 switch halting packets between two `/26` subnets. Unmanaged Layer 2 switches have zero awareness of IP subnets or CIDR masks. The boundary is an internal Layer 3 host network stack route evaluation (`Destination host unreachable`).
4. **Directional Socket Inversion in Port Exhaustion (Figure 5.1 — HIGH):**  
   The prompt describes *"incoming new connection requests bouncing off"* a congested ring buffer. Jared's desktop is the **client** executing rapid-fire *outbound* connections. Ephemeral port exhaustion starves *outbound source port allocation*, causing local `connect()` / `bind()` calls to fail with `WSAEADDRINUSE`.
5. **Industrial PLC Direct VPN Termination Hallucination (Figure 7.1 — MEDIUM):**  
   The prompt depicts an encrypted IPsec VPN pipe *"safely terminating into an industrial programmable logic controller (PLC)."* Field PLCs run bare-bones microcontrollers incapable of terminating IPsec tunnels; enterprise OT architecture terminates VPNs at an industrial edge security gateway/firewall.
6. **Multi-Homed Wi-Fi Failover Blindspot during Host Isolation (Figure 10.1 — MEDIUM):**  
   Yanking an Ethernet cable from a modern enterprise laptop without toggling hardware Wi-Fi triggers instantaneous failover to the active corporate 802.11 SSID, allowing lateral worm propagation to continue over the air.
7. **Public Key "Decryption" Misnomer (Figure 9.1 — MEDIUM):**  
   Prompt specifies Gate 2 *"decrypts a cryptographic wax-seal stamp using a public key."* Asymmetric digital signatures are *verified*, not decrypted.

---

## 2. Technical Scorecard across All 13 Figures

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                               TECHNICAL NITPICKER AUDIT SCORECARD                                      │
├─────────┬──────────────────────┬─────────────┬─────────────┬───────────────────────────────────────────┤
│ Figure  │ Candidate Plate      │ Layer / Sys │ Status      │ Primary Technical Defect / Nitpick        │
├─────────┼──────────────────────┼─────────────┼─────────────┼───────────────────────────────────────────┤
│ Fig 0.1 │ Motherboard Anatomy  │ Physical/L1 │ Pass w/ Fix │ Pin 2 vent labeled "Normal Voltage"       │
│ Fig 1.1 │ DB-9 Pin Realignment │ Physical/L1 │ FAIL        │ Sizing paradox (0.5mm vs 1.0mm); open!=gnd│
│ Fig 2.1 │ Workstation 14 Pod   │ OS / L1-L7  │ PASS        │ Mechanically sound (Y-bridge & Safe Mode) │
│ Fig 3.1 │ /26 Subnet Boundary  │ Layer 2 / 3 │ Pass w/ Fix │ Switch backplane conflated with L3 route  │
│ Fig 4.1 │ Split-Horizon DNS    │ Layer 3 / 7 │ PASS        │ RFC 2308 negative cache race is accurate  │
│ Fig 5.1 │ TCP Port Exhaustion  │ Layer 4     │ Pass w/ Fix │ Inversion: outbound connect vs incoming   │
│ Fig 6.1 │ Sub-Basement Flood   │ Layer 1 / 2 │ PASS        │ 4U elevation, LACP, 802.1Q trunk verified │
│ Fig 7.1 │ Perimeter Hardening  │ Layer 3-4/OT│ Pass w/ Fix │ PLC cannot terminate IPsec tunnel         │
│ Fig 8.1 │ Auth Triad & TPM 2.0 │ Hardware/Crypto Pass w/ Fix│ Optical scanner trope; PCR sealing detail │
│ Fig 9.1 │ Email MIME Envelope  │ Layer 7 App │ Pass w/ Fix │ Signature verification vs "decryption"    │
│ Fig 10.1│ Host Isolation Pull  │ Layer 1 / 2 │ Pass w/ Fix │ Wi-Fi automatic failover bypasses pull    │
│ Fig 11.1│ RF Spectrum Chaos    │ Layer 1 RF  │ PASS        │ 20MHz masks, 1/6/11 spacing, 2450MHz oven │
│ Fig 12.1│ Forensic Bench       │ Forensics   │ CRITICAL FAIL Live RAM capture with write-blocker       │
└─────────┴──────────────────────┴─────────────┴─────────────┴───────────────────────────────────────────┘
```

---

## 3. Deep-Dive Technical Audits & Forensic Engineering Breakdowns

### 3.1 Figure 12.1: The Hardware Write-Blocker Hallucination (CRITICAL AUDIT)
* **The Error in Draft:**  
  Prompt text: *"Connected to the laptop's side port via a short shielded cable is an external hardware write-blocking acquisition bridge with glowing green status LEDs, copying live memory to a dedicated rugged external solid-state drive."*  
  Caption text: *"Ethan Mercer preserves live volatile memory using a hardware write-blocker before disk acquisition or power-down."*
* **The Engineering Reality:**  
  1. **Storage Bus vs. Memory Architecture:** System RAM lives in DDR4/DDR5 DRAM modules connected directly to the CPU memory controller via high-speed parallel bus channels (64-bit per channel). RAM cannot be read or polled over external SATA, SAS, or NVMe storage protocols.
  2. **The Function of a Hardware Write-Blocker:** A hardware write-blocker (e.g., Tableau T8u, Forensic UltraDock) is an inline storage bridge that intercepts ATA, SCSI, or NVMe commands traveling to a *suspect disk drive*. It physically or logically blocks write commands (`WRITE SECTOR`, `WRITE DMA`, `FORMAT`) while passing read commands through to an examiner's forensic workstation.
  3. **The In-Line Writing Paradox:** If Ethan placed a hardware write-blocker between the laptop and the external destination SSD, the write-blocker would **prevent writing the image to the destination SSD**!
  4. **RFC 3227 Order of Volatility Compliance:**  
     Under RFC 3227, the collection sequence is:
     $$\text{Registers, Cache} \rightarrow \text{RAM / Routing / ARP / Kernel State} \rightarrow \text{Temporary Files} \rightarrow \text{Persistent Disk} \rightarrow \text{Network Topology / Media}$$
     Live memory acquisition is executed by inserting a forensically prepared external USB drive containing static, pre-compiled software capture tools (e.g., `winpmem.exe`, `DumpIt.exe`, or FTK CLI) and streaming the raw RAM buffer (`memdump.raw`) directly out to that external drive.  
     **The hardware write-blocker is only used AFTER live triage**, when the target machine is powered down, its internal NVMe/SATA SSD is physically extracted (or booted into target disk mode), and connected to the write-blocker to image persistent storage without altering access timestamps.
* **Mandatory Technical Correction:**  
  Depict the live enterprise laptop with a high-speed external forensic capture SSD plugged into the USB-C / Thunderbolt port, actively streaming volatile memory via a lightweight console command line. On the bench *beside* the laptop, staged on an ESD mat ready for Step 2 (persistent disk acquisition), sits the standalone hardware write-blocker, SATA/NVMe adapter sleds, and tamper-evident drive bags.

---

### 3.2 Figure 1.1: DB-9 Pinout, Ground Faults & Tool Geometry (SEVERE AUDIT)
* **The Errors in Draft:**  
  1. Pin 1 Overlay: `Pin 2: Receive Data (RXD) — Ground Fault`
  2. Prompt & Narrative: Ethan slips the hollow 0.5mm guide sleeve of a drafting pencil over Pin 2 to lever it upright.
* **The Electrical & Circuit Reality:**  
  - **Dielectric vs. Conductor:** In a standard DE-9 male connector, the pins are embedded in a blue or black molded PBT/diallyl phthalate insulator block. If Pin 2 bends backward against this plastic block, it is isolated by a dielectric material. It does **not** short to ground; it creates an **Open Circuit (Signal Discontinuity / Floating Input)**.  
  - **Ground Pin Location:** On an EIA/TIA-574 DE-9 connector (DTE face):
    - Top row (left to right): Pin 1 (DCD), Pin 2 (RXD), Pin 3 (TXD), Pin 4 (DTR), Pin 5 (GND).
    - Bottom row (left to right): Pin 6 (DSR), Pin 7 (RTS), Pin 8 (CTS), Pin 9 (RI).
    Pin 5 (Signal Ground) is on the far opposite corner of the upper row. Pin 2 cannot short to Pin 5 via a single bend. The outer metal trapezoidal shell is Chassis Ground, but Pin 2 is internal to the row. The electrical symptom is loss of serial continuity, resulting in framing errors and zero incoming ASCII bytes.
* **The Mechanical Sizing Reality:**  
  - **Size 20 D-Sub Contact Dimensions:** Under MIL-DTL-24308 and EIA-232 standards, standard D-sub male pins are Size 20 contacts with an outer pin diameter of **$0.040\text{ inches} \pm 0.001\text{ in} = 1.016\text{ mm}$**.
  - **0.5mm Drafting Pencil Guide Sleeve:** A 0.5 mm mechanical drafting pencil is dimensioned for 0.50 mm graphite lead. The inner bore of its brass guide tube is **$\approx 0.53\text{ to }0.58\text{ mm}$**. The outer diameter of the sleeve is $\approx 0.85\text{ to }0.90\text{ mm}$.  
  - **The Sizing Paradox:** A 1.016 mm solid brass pin **physically cannot enter** a 0.55 mm hole. ($1.016\text{ mm} > 0.55\text{ mm}$).
* **Field Engineering Lore vs. Physics:**  
  Real field technicians do not insert 1.0mm pins into 0.5mm lead sleeves. They use:
  1. A **2.0 mm drafting lead holder** (clutch pencil sleeve / chuck), which has a 2.1 mm internal diameter, or
  2. The hollow brass ferrule of a ballpoint pen barrel (like a modified Bic round stic), or
  3. A standard military-spec pin insertion/extraction tool (M81969/1-02), or
  4. They use the **flat exterior side** of the rigid drafting pencil barrel as a fulcrum/lever to coax the pin upright without sleeving it.
* **Mandatory Technical Correction:**  
  - Change Pin 1 Overlay to: `Pin 2: Receive Data (RXD) — Open Circuit (Signal Discontinuity)`.
  - In prompt and overlay, clarify that Ethan uses the rigid cylindrical exterior guide sleeve of the pencil as a micro-fulcrum to press against the pin stem, OR specify a 2.0mm drafting lead holder.

---

### 3.3 Figure 3.1: Layer Boundary Invariance & Routing Table Logic (HIGH AUDIT)
* **The Error in Draft:**  
  Prompt text: *"An outgoing packet envelope emerging from the lower server travels toward the switch but encounters a sharp vertical threshold barrier, unable to cross into the upper zone without routing through an external gateway appliance depicted on the periphery."*  
  Caption text: *"stranding frames at the local broadcast boundary."*
* **The Layer 2 / Layer 3 Protocol Reality:**  
  - **The Switch Backplane:** In the narrative, both servers (`192.168.10.65` and `192.168.10.62`) are plugged into the same unmanaged or single-VLAN Layer 2 switch. A Layer 2 switch operates strictly on Ethernet frames (source and destination MAC addresses). It has no knowledge of IPv4 headers, network octets, or `/26` subnet masks. A Layer 2 switch **never** blocks a packet because two IP addresses belong to different subnets!
  - **Where the Barrier Actually Lives:** The barrier exists entirely inside the **host operating system's Layer 3 network stack**:
    1. Host `.65` wants to send to `.62`.
    2. Host `.65` evaluates: `192.168.10.62 AND 255.255.255.192 = 192.168.10.0`.
    3. Host `.65` compares this with its own subnet: `192.168.10.65 AND 255.255.255.192 = 192.168.10.64`.
    4. Because `192.168.10.0 != 192.168.10.64`, the OS stack determines the destination is **off-link**.
    5. The OS looks for a route to its configured default gateway: `192.168.10.1`.
    6. But the default gateway (`192.168.10.1`) is *also* in `192.168.10.0` (off-link!).
    7. Because the host has no local on-link route to its own gateway, the Windows IP stack aborts transmission immediately, returning `Destination host unreachable`. The packet is **dropped inside the host kernel before an Ethernet frame is ever queued on the wire**!
* **Mandatory Technical Correction:**  
  The visual must show that the packet is halted **at the host's internal network stack / NIC egress queue**, not blocked by a magical invisible wall on the switch backplane. Alternatively, if the switch is managed, it must depict two isolated 802.1Q access VLANs (e.g. VLAN 10 and VLAN 20) with the switch dropping the frame at the ingress port boundary.

---

### 3.4 Figure 5.1: TCP State Machine & Outbound Port Depletion (HIGH AUDIT)
* **The Error in Draft:**  
  Prompt text: *"Incoming new connection requests bounce harmlessly off the congested ring buffer perimeter, depicting port exhaustion."*
* **The RFC 793 / RFC 9293 Transport Layer Reality:**  
  - **Client vs. Server Roles:** In Episode 05, Jared's administrative desktop (`10.100.1.50`) is the **client**. It is running an aggressive multi-threaded PowerShell/C# loop initiating connections to the backup archive server (`10.100.4.20:8443`).
  - **Ephemeral Port Mechanics:** Under RFC 6335 / IANA standards, dynamic/ephemeral client ports span **49,152 to 65,535** (a pool of exactly 16,384 sockets). When an application calls `connect()` without an explicit `bind()`, the OS kernel allocates a free ephemeral port from this pool.
  - **Active Close & TIME_WAIT:** Under RFC 793/9293, the endpoint that initiates the **Active Close** (sends the first `FIN`) enters `TIME_WAIT` for $2\text{MSL}$ ($2 \times \text{Maximum Segment Lifetime} = 120\text{ seconds}$ in Windows). Because Jared's script rapidly created and closed connections without connection pooling, it parked $>15,000$ client sockets in `TIME_WAIT`.
  - **The Inversion:** The failure is **outbound**, not inbound. When the script attempts to launch the next connection, the local Windows socket manager attempts to allocate an outbound ephemeral port, finds zero available sockets in the pool, and throws:
    `System.Net.Sockets.SocketException: Only one usage of each socket address is normally permitted (WSAEADDRINUSE 10048)`.
    No "incoming connection requests" are bouncing off anything; the client machine is suffocating its own ability to reach outward!
* **Mandatory Technical Correction:**  
  Modify the ring-buffer prompt to show **outbound application connection requests from the local process pool** attempting to bind to the exhausted ephemeral ring buffer and failing to launch into the network stack. Clarify in Pin 1 that `TIME_WAIT` is maintained exclusively by the active-closing client endpoint.

---

### 3.5 Figure 7.1: OT Architecture & Industrial PLC VPN Termination
* **The Error in Draft:**  
  Prompt text: *"an armored site-to-site VPN pipe safely terminating into an industrial programmable logic controller (PLC) and an enterprise server rack."*
* **The Industrial Control System (ICS/SCADA) Reality:**  
  - In industrial facilities (Purdue Enterprise Reference Architecture / ISA-95 / IEC 62443), field PLCs (e.g., Allen-Bradley ControlLogix, Modicon M340, Siemens S7) sit at **Level 1 (Basic Control)** or **Level 2 (Area Supervisory Control)**.
  - PLCs are low-power real-time controllers running embedded RTOS kernels with minimal IP stacks. They do **not** run IPsec daemons (IKEv2/ISAKMP), negotiate Diffie-Hellman key exchanges, or decrypt AES-GCM payloads.
  - A site-to-site IPsec VPN terminates at an **Industrial Edge Gateway / Security Appliance** (e.g., Fortinet Rugged, Moxa Industrial Router, Phoenix Contact mGuard) located at the **Level 3 / IT-OT DMZ perimeter**. The gateway authenticates and decrypts the traffic, strips the IPsec encapsulation, and forwards native, unencrypted Modbus/TCP (Port 502) or DNP3 (Port 20000) frames across the isolated local plant floor subnet to the PLC.
* **Mandatory Technical Correction:**  
  Depict the encrypted IPsec VPN pipe terminating into an industrial DIN-rail or rackmount **OT Perimeter Security Gateway**, which in turn connects via an isolated, shielded industrial Ethernet patch cable to the plant PLC.

---

### 3.6 Figure 8.1: Biometric Sensors & TPM 2.0 Silicon Ground Truth
* **The Flaws in Draft:**  
  1. Biometric representation: *"On the right, a biometric optical scanner emits an emerald inspection grid."*
  2. TPM representation: *"miniature square TPM 2.0 cryptographic microcontroller securely anchoring an asymmetric key icon."*
* **The Hardware & Cryptographic Reality:**  
  - **Biometric Sensor Engineering:** Optical scanners with glowing green platen lights are a 1990s visual cliché. Modern enterprise laptops (ThinkPad, Latitude, EliteBook) utilize **capacitive silicon area touch sensors** or **ultrasonic fingerprint readers**. They emit zero visible light; they measure micro-capacitance differences between the conductive ridges and air valleys of the user's epidermal layer.
  - **TPM 2.0 Silicon Architecture:** A discrete TPM 2.0 (e.g., Infineon SLB9670/9672, Nuvoton NPCT750) is typically a 28-pin or 32-pin surface-mount QFN/TSSOP package communicating over the SPI or LPC bus.
  - **PCR Hardware Sealing Mechanics:** Under TCG specifications, the TPM provides **Platform Configuration Registers (PCR 0–23)**. Integrity measurements (hashes of UEFI firmware, Option ROMs, bootloader, kernel) are chained into PCRs using `TPM2_PCR_Extend(pcrIndex, hash)`. The TPM **seals** private authentication keys to specific PCR states. Biometric authentication (Inherence) verified by the local OS Match-on-Chip/Host subsystem instructs the TPM to release or sign with the hardware-bound private key. The biometric image is never stored or transmitted; it acts as a local authorization trigger.
* **Mandatory Technical Correction:**  
  Replace the glowing green optical scanner with a modern flush capacitive biometric sensor with a subtle metallic bezel ring. Ensure Pin 3 explicitly highlights PCR platform integrity measurement and key sealing.

---

### 3.7 Figure 9.1: Email Triple-Gate & Digital Signature Verification
* **The Flaw in Draft:**  
  Prompt text: *"Gate 2 decrypts a cryptographic wax-seal stamp using a public key to verify content integrity (DKIM)."*
* **The Asymmetric Cryptography Reality:**  
  - Public-key cryptography does **not** "decrypt" a digital signature. In asymmetric signing (RSA / Ed25519), the sender hashes the canonicalized message headers and body, then signs (encrypts) the hash with their **private key** to produce the signature (`b=` tag in RFC 6376).
  - The receiving mail gateway fetches the sender's public key from DNS (`selector._domainkey.domain.com`), independently computes the cryptographic hash of the received message headers and body, and applies the public key to **mathematically verify** that the signature corresponds to the calculated hash.
  - **DMARC Alignment Ground Truth:** DMARC (RFC 7489) does not merely check if SPF and DKIM pass; it checks **Identifier Alignment**. An attacker can send an email from `evil.com` with valid SPF for `evil.com` and a valid DKIM signature for `evil.com`. But if the RFC 5322 visual presentation header displays `From: ceo@harrowmere.com`, DMARC flags the domain mismatch (unaligned) and enforces the `p=reject` or `p=quarantine` policy.
* **Mandatory Technical Correction:**  
  Change prompt from "decrypts a cryptographic wax-seal stamp" to *"Gate 2 mathematically verifies the cryptographic signature against the DNS public key to validate payload integrity (DKIM); Gate 3 evaluates strict domain alignment between the visible From header and the verified signing domain (DMARC)."*

---

### 3.8 Figure 10.1: Multi-Homed Wi-Fi Automatic Failover
* **The Operational Flaw:**  
  Yanking the RJ-45 Ethernet cable while Ken's warehouse laptop is running halts lateral SMB propagation across the wired segment. However, on any enterprise laptop with active 802.11 Wi-Fi, the moment link-carrier drops on the wired NIC (`ncpa.cpl`), the Windows Network Location Awareness (NLA) service immediately switches default routing to the active wireless adapter! If the laptop is associated with the corporate Wi-Fi or guest network, the worm's C2 beaconing and subnet scanning continue unabated over the air.
* **Mandatory Technical Correction:**  
  Ethan must execute **Dual Layer 1 Isolation**: his left hand disconnects the RJ-45 Ethernet patch cable, while his right thumb flips the laptop's physical Wi-Fi hardware kill switch (or engages Fn+Airplane Mode on the keyboard).

---

### 3.9 Figure 0.1: Capacitor Degradation Physics vs. Operating Voltage
* **The Defect in Draft:**  
  Pin 2 Overlay: `Intact Factory Vent (Normal Voltage)`
* **The Physical Reality:**  
  The stamped score lines (X, K, or Y pattern) on an aluminum electrolytic capacitor are **mechanical pressure-relief vents**. During thermal stress or electrolyte boiling caused by high Equivalent Series Resistance (ESR) or AC ripple current, hydrogen gas builds up. The vent score is engineered to dome and rupture safely rather than violently detonating the aluminum can.  
  A flat, intact vent indicates **normal internal pressure and hermetic seal integrity**, NOT "normal voltage." A capacitor can be subjected to damaging overvoltage for minutes before venting, or a completely unpowered board on an ESD mat has intact vents with exactly 0.00 V across its terminals.
* **Mandatory Technical Correction:**  
  Change Pin 2 Overlay to: `Intact Factory Vent Seal (Nominal Internal Pressure & Normal ESR)`. Change Pin 1 to: `Domed & Ruptured Vent Score (Electrolyte Boil-off & Dielectric Breakdown)`.

---

## 4. Zero-Text Compliance & Telemetry Overlay Audit

An audit of all 13 figure prompts confirms that the authoring team adhered closely to the negative prompting mandate (`no text, no letters, no words, no numbers, no watermarks`). However, two subtle prompt instructions present significant risks of generative text hallucination:

1. **Figure 12.1 Stopwatch Digit Hazard:**  
   Prompt specifies: *"a calibrated digital stopwatch displaying elapsed time"*.  
   **The Risk:** Generative image engines prompted with "digital stopwatch displaying elapsed time" invariably attempt to render 7-segment digital LED/LCD numerical readouts (e.g. `00:14:22`), resulting in garbled alien glyphs.  
   **Correction:** Change prompt to: *"an analog mechanical stainless-steel stopwatch with a blank, unprinted dial face and sweeping mechanical second hand"*.
2. **Figure 4.1 Latency Millisecond Hazard:**  
   Prompt specifies: *"representing an NXDOMAIN negative response in 4 milliseconds; arriving at 20 milliseconds"*.  
   **The Risk:** Generative models can take "4 milliseconds" as a text directive and attempt to paint `"4ms"` on the conduit.  
   **Correction:** Keep the timing concept strictly semantic: *"a straight, short high-speed conduit hitting an immediate red negative barrier block; a longer, coiled blue encrypted tunnel arriving at a remote server block"*. Render the metrics (`4ms`, `20ms`, `NXDOMAIN`) exclusively via Docsify SVG pin overlays.

---

## 5. Mandatory Actionable Corrections & Technical Text Replacements

Before the Digital Art Director begins generating visual plates for production, the following exact text replacements must be incorporated into `docs/research/PROPOSED_VISUALS_AUDIT.md`:

### 5.1 Exact Prompt Replacements

#### Figure 1.1 (DB-9 Serial Realignment) — Physical Correction
```text
Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, clean neutral ESD mat background, no heavy dark shadows, anatomically and electronically accurate hardware, true component colors. High-detail extreme macro technical illustration of a male DE-9 serial connector held up toward an inspection lamp. Maintain the exact trapezoidal 9-pin arrangement with five pins on the upper row and four pins on the lower row. Pin 2 on the upper row is bent backward at a 45-degree angle away from the contact plane. Positioned adjacent to the bent pin is the rigid cylindrical stainless-steel guide sleeve of a precision technical drafting pencil, using the flat side of the sleeve as an exact micro-lever to gently coax the copper pin upright. Crisp mechanical accuracy, clean lines, no text, no letters, no words, no numbers, no watermarks. 1:1 ratio.
```

#### Figure 3.1 (/26 Subnet Boundary) — Layer 3 Route Correction
```text
Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, clean neutral background, no heavy dark shadows. Architectural cutaway of a 19-inch steel equipment rack inside an industrial pump house. Two rackmount server chassis sit on adjacent metal shelf rails, connected via blue patch cords to a central 24-port switch. A stylized, semi-transparent glowing boundary plane horizontally bifurcates the rack into two distinct logical subnet zones: upper zone highlighted in cool slate blue, lower zone highlighted in warm amber. An outgoing packet envelope emerging from the lower server's network stack halts directly at its internal network interface buffer, flagged by an off-link routing barrier because its default gateway sits across the logical subnet boundary. Crisp mechanical and electronic accuracy, Ligne Claire linework, clean unlabeled panels, no text, no letters, no words, no numbers, no watermarks. 16:9 ratio.
```

#### Figure 5.1 (TCP Port Exhaustion) — Outbound Socket Correction
```text
Clean technical cutaway diagram of a network protocol transport layer architecture under bright, even inspection lighting. On the left side, a vertical state-machine sequence traces an active connection teardown cycle through distinct geometric nodes, terminating in a prominent 2MSL timer block. On the right side, a circular ring-buffer schematic represents a client computer host's dynamic ephemeral socket pool: the entire ring buffer is completely packed with glowing red occupied blocks, showing zero available open ports. Outbound connection requests generated by client application worker threads stall against the congested ring buffer boundary, unable to obtain a free dynamic source port. Crisp technical drawing style, Ligne Claire, clean uniform linework, no heavy shadows, no text, no letters, no words, no numbers, no watermarks. 16:9 ratio.
```

#### Figure 7.1 (Perimeter Hardening) — OT Gateway Correction
```text
Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, clean neutral background, no heavy dark shadows. A technical architecture schematic illustrating an enterprise network perimeter boundary. On the left, untrusted external networks are shown with incoming transmission conduits in alarming red: unencrypted terminal sessions, cleartext file transfers, unencrypted mail submission, and cleartext industrial control protocols. In the center, a heavy stylized firewall gateway appliance acts as a defensive threshold, blocking the red conduits. Emerging from the firewall on the right are fortified, glowing blue encrypted conduits: encrypted cryptographic shells, secure file tunnels, and an armored site-to-site IPsec VPN pipe safely terminating into a rugged DIN-rail industrial security gateway, which routes isolated control commands to an adjacent industrial programmable logic controller (PLC). Crisp Ligne Claire line art, clean geometry, true component colors, no text, no letters, no words, no numbers, no watermarks. 16:9 ratio.
```

#### Figure 10.1 (Physical Host Isolation) — Dual Layer 1 Correction
```text
Dramatic graphic novel scene in Pacific Northwest silicon noir style, crisp uniform ink linework, high contrast clean lines, authentic industrial warehouse office atmosphere. Inside a cramped shipping dispatch office, Ken, an exhausted 51-year-old supervisor in a hi-vis vest, leans over his cluttered laminate desk in frustration, one hand aggressively reaching toward the laptop power button. In sharp foreground focus, 22-year-old technician Ethan Mercer steps in decisively to isolate the host: his left thumb firmly depresses the clear plastic release tab of a blue RJ-45 patch cable, cleanly sliding it out of the side Ethernet port, while his right hand engages the laptop's physical Wi-Fi airplane mode switch to sever all wireless connectivity. On the laptop display, standard Windows diagnostic consoles display dense static log entries. On the desk sits a spiral incident notebook and a company badge. Outside the window behind them, grey Pacific Northwest rain streaks the industrial loading bay. Crisp mechanical accuracy, grounded procedural drama, no text, no letters, no words, no numbers, no speech bubbles, no watermarks. 16:9 ratio.
```

#### Figure 12.1 (Forensic Bench) — RFC 3227 Memory Acquisition Correction
```text
Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, clean neutral ESD mat background, no heavy dark shadows. A live computer forensic examination bench in an operations center. In the center, an energized, operating enterprise laptop sits on a grounded blue anti-static ESD mat with its wireless toggle switched off and Ethernet disconnected. Connected to the laptop's high-speed side data port via a short shielded cable is a rugged, forensically prepared external solid-state drive actively receiving a live stream of volatile system memory from a lightweight command line. Staged on an ESD mat beside the laptop, awaiting post-power-down persistent disk imaging, sits a standalone hardware write-blocking bridge, SATA and NVMe drive sleds, and tamper-evident evidence pouches. Next to the laptop lies an open red spiral-bound incident logbook, a stainless-steel mechanical drafting pencil, an analog mechanical stopwatch with a blank unprinted dial face, and evidence barcode labels. Sharp technical precision, Ligne Claire linework, authentic forensic equipment, clean unlabeled surfaces, no text, no letters, no words, no numbers, no watermarks. 16:9 ratio.
```

---

### 5.2 Exact Overlay & Caption Replacements

| Figure | Component | Draft Wording | Technical Nitpicker Mandated Replacement | Technical Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Fig 0.1** | Pin 1 | `Domed Vent Seal (Ruptured Electrolyte)` | `Ruptured Vent Score: Hydrogen Gas Outgassing & Dielectric Breakdown` | Specifies the chemical failure mode (outgassing from boiled electrolyte). |
| **Fig 0.1** | Pin 2 | `Intact Factory Vent (Normal Voltage)` | `Intact Factory Vent Seal: Nominal Internal Pressure & Healthy ESR` | Intact vent reflects physical pressure/ESR integrity, not active electrical voltage. |
| **Fig 1.1** | Pin 1 | `Pin 2: Receive Data (RXD) — Ground Fault` | `Pin 2: Receive Data (RXD) — Open Circuit (Signal Discontinuity)` | Plastic insulator is non-conductive dielectric; pin bend creates an open line, not a ground fault. |
| **Fig 3.1** | Caption | `...stranding frames at the local broadcast boundary.` | `...internal route lookup fails because gateway 192.168.10.1 is off-link, aborting transmission inside the host IP stack.` | Layer 2 switch does not stop packets; host Layer 3 routing table aborts before frame encapsulation. |
| **Fig 5.1** | Pin 1 | `Four-Way Teardown: FIN -> ACK -> FIN -> ACK` | `Active Close Teardown: Initiator enters TIME_WAIT (2MSL Hold)` | Distinguishes active closer (holds TIME_WAIT) from passive closer (CLOSE_WAIT). |
| **Fig 5.1** | Pin 3 | `Ephemeral Dynamic Range: 16,384 Sockets Blocked` | `Ephemeral Port Pool (49152–65535): Outbound Sockets Starved` | Clarifies failure is outbound source port allocation, not inbound. |
| **Fig 7.1** | Pin 3 | `Encrypted Cryptographic Enclave: SSH (22) & IPsec VPN` | `OT Perimeter Security Gateway: Terminating IPsec VPN & Shielding Modbus (502)` | Reflects true Purdue Model architecture (VPN terminates at gateway, not inside PLC). |
| **Fig 8.1** | Pin 3 | `Hardware Root of Trust: Asymmetric Private Key Storage` | `Hardware Security Anchor (TPM 2.0): Key Sealing & PCR Platform Measurements` | Incorporates Platform Configuration Register (PCR) hash measurement and sealing. |
| **Fig 9.1** | Caption | `...DKIM cryptographically authenticates payload hashes...` | `...DKIM cryptographically verifies header/body signature against DNS public key, and DMARC enforces strict header alignment.` | Eliminates loose "decryption" phrasing; emphasizes DMARC domain alignment. |
| **Fig 10.1** | Pin 1 | `Physical Layer 1 Isolation (Pull the Cable)` | `Dual Layer 1 Isolation: RJ-45 Disconnect & Hardware Wi-Fi Radio Kill` | Prevents automatic multi-homed failover to active 802.11 wireless network. |
| **Fig 12.1** | Caption | `...preserves live volatile memory using a hardware write-blocker before disk acquisition...` | `...preserves live volatile memory to an external evidence SSD via trusted software before powering down for write-blocked disk acquisition.` | Eliminates catastrophic technical blunder regarding write-blocker capabilities. |
| **Fig 12.1** | Pin 2 | `Hardware Write-Block Bridge & Evidence SSD` | `Staged Hardware Write-Blocker: Reserved for Secondary Persistent Drive Imaging` | Correctly positions write-blocker in RFC 3227 Order of Volatility. |

---

## 6. Sign-Off & Verification Gate

The catalog proposed in `docs/research/PROPOSED_VISUALS_AUDIT.md` is **CONDITIONALLY APPROVED** subject to the mandatory technical prompt and overlay text replacements defined in Section 5.

Upon updating `PROPOSED_VISUALS_AUDIT.md` with these engineering corrections, the visual asset specifications will be fully compliant with:
1. `docs/research/TECHNICAL_NARRATIVE_AUTHORING_PRINCIPLES.md` (Principles 6, 7, 8, 9, 10, 11)
2. RFC 793/9293, RFC 826, RFC 2308, RFC 3227, RFC 5321/5322, RFC 7489
3. EIA/TIA-574 and MIL-DTL-24308 physical connector specifications
4. TCG TPM 2.0 Library Specification
5. The Absolute Zero-Text Production Rule

*Audit completed by Technical SME & Hardware/Network Nitpicker. Forwarding to Digital Art Director and Lead Curriculum Architect.*
