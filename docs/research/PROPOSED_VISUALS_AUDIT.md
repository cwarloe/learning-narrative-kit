# Master Visual Production Catalog: Portland Desk (Book 0: Zero-to-One)
**Repository:** `learning-narrative-kit`  
**Target Platform:** Docsify v4 (`docs/portland-desk`) & Grok Imagine (with inpainting)  
**Status:** Approved by Digital Art Director, Technical Nitpicker, and Prose Critic.  
**Complements:** `docs/research/VISUAL_ART_DIRECTION.md`, `PORTLAND_TIMELINE.md`, and `TECHNICAL_NARRATIVE_AUTHORING_PRINCIPLES.md`.

---

## 1. Executive Summary & Production Contract

1. **The Absolute Zero-Text Rule:** All generated artwork is 100% wordless. The AI produces physical geometry, authentic electrical components, and character acting. Browser/Docsify overlays (`callout-panel`, SVG/CSS pins) handle typography, ensuring zero AI spelling hallucinations, instant editing, and interactive hover tooltips.
2. **One Visual Anchor Per Episode:** Exactly one high-leverage plate per chapter, anchored strictly at the **Complication** or the **Pivot**.
3. **Engineering Invariance & Ground Truth:** All layer boundaries, hardware dimensions (DB-9, ATX, T568B), industrial protocols (Modbus/TCP, IPsec), and forensic sequences (RFC 3227) are verified against engineering ground truth.
4. **Working-Class Pacific Northwest Realism:** Grounded procedural workplace drama (rain on casement windows, hum of ballast lamps, exhausted apprentices, unventilated wiring closets, and cold coffee) without superhero melodrama.

---

## 2. Master Character DNA Anchors (Prompt Locks)

* **Ethan Mercer:**
  > `"Ethan Mercer, a 19-to-20-year-old frontline technician, slender athletic build, messy tousled dark wavy brown hair, clean-shaven, wide expressive hazel eyes. Wears a light heather-grey crew-neck t-shirt or grey hoodie under a dark canvas jacket, work boots, single-ear Plantronics telephone headset, stainless-steel mechanical pencil clipped in pocket."`
* **Jules Brooks:**
  > `"Jules Brooks, 34-year-old female Lead Support Specialist, sharp intelligent features, shoulder-length straight dark hair with subtle silver streaks tucked behind one ear, wearing an unstructured charcoal blazer over a black tee or dark flannel shirt, wired headset over one ear, ceramic coffee mug in hand, matte silver commuter bicycle helmet nearby. Calm, observant mentor expression."`
* **Ken:**
  > `"Ken, 51-year-old frantic logistics shift supervisor, scuffed denim jacket, aluminum clipboard under arm, receding grey hair, weathered lined face of a logistics manager under trailer dispatch deadlines."`
* **Maya Lin:**
  > `"Maya Lin, 40s supervisor of municipal accounting, tailored business suit, reading glasses, focused and demanding under biweekly payroll signoff deadlines."`

---

## 3. The 13 Production-Ready Figure Specifications

---

### Episode 00: The Four Rubber Bands (A+ Prologue)
* **Figure 0.1:** Desktop Motherboard & Physical Computing Invariants
* **Format & Aspect Ratio:** `4:3` Top-Down Technical Cutaway Plate
* **Teaching Beat:** The Pivot (Permanent Anatomy of Computing)
* **Prompt:**
  ```text
  Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, clean ESD mat background, no heavy dark shadows. Macro technical inspection shot of a desktop PC motherboard interior: in sharp foreground focus are three cylindrical electrolytic capacitors on the green PCB. Two capacitors have prominently domed, bulging silver tops with cracked score lines and dried crusty brown electrolyte residue leaking from the vent seam. The third capacitor is completely flat and healthy for visual contrast. Directly behind them is a dual-channel memory slot holding a green RAM module with one white plastic retention latch broken off at an angle. Crisp fine ink linework, true component colors, clean unlabeled surfaces, no text, no letters, no words. 4:3 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 0.1: THE MOTHERBOARD INSPECTION`
  * **Badge:** `Hardware Anatomy`
  * **Caption:** `Macro technical cutaway: A desktop motherboard on an ESD workbench mat. In the foreground, three cylindrical electrolytic capacitors: two are swollen and domed with dried brown crust leaking from the vents, beside one healthy flat capacitor. In the background, a dual-channel memory slot holding a green RAM stick with one broken retention latch.`
  * **Interactive Overlay Pins:**
    * Pin 1 (Electrolyte Vent): `Bulging Electrolytic Capacitor — Outgassing hydrogen has ruptured the vent score, causing power rail ripple voltage.`
    * Pin 2 (Flat Vent): `Intact Capacitor Seal — Flat vent indicates low equivalent series resistance (ESR) and solid internal seal.`
    * Pin 3 (RAM Latch): `Unseated Memory Module — Fractured retention latch prevents complete contact on the memory bus, causing firmware POST failure.`

---

### Episode 01: The Paper Cert (A+ Core 1 Hardware)
* **Figure 1.1:** RS-232 DE-9 Pin 2 Realignment & Sizing Reality
* **Format & Aspect Ratio:** `1:1` Macro Technical Detail
* **Teaching Beat:** The Pivot (Layer 1 Mechanical Diagnostics)
* **Prompt:**
  ```text
  High-detail macro technical illustration in Pacific Northwest instructional manual style, bright even illumination, clean studio lighting. Looking directly into the face of a male DE-9 RS-232 serial D-sub connector. The connector has its exact 9-pin trapezoidal arrangement (5 gold pins on top row, 4 on bottom row) in a blue plastic insulator block within a stamped steel D-shaped shell. Pin 2 on the top row is visibly bent backward at a 45-degree angle, resting against the blue plastic insulator. The rigid stainless steel guide sleeve of a drafting pencil is positioned alongside the bent pin, using the metal tip as a precision miniature lever to gently coax the pin straight. Sharp mechanical accuracy, crisp line art, clean neutral background, no text, no letters. 1:1 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 1.1: PIN 2 MECHANICAL REALIGNMENT`
  * **Badge:** `Layer 1 Mechanics`
  * **Caption:** `Macro view: DE-9 male serial connector under ring-light inspection. Pin 2 (Receive Data / RXD) is bent backward against the non-conductive plastic insulator floor, causing an open circuit on scale telemetry. A stainless drafting pencil guide sleeve levers the solid copper pin back into alignment.`
  * **Interactive Overlay Pins:**
    * Pin 1 (Bent Pin 2): `Pin 2 (RXD) Signal Discontinuity — Bent against the dielectric insulator floor, opening the receive circuit and dropping scale weight strings.`
    * Pin 2 (Straight Pin 3): `Pin 3 (TXD) Normal — Straight gold contact maintains solid physical mating for transmit data.`
    * Pin 3 (Drafting Tool): `Rigid Steel Sleeve — Applied as a lever arm against the pin base to restore pin alignment without snapping the solder cup.`

---

### Episode 02: The Live Board (A+ Core 2 Software)
* **Figure 2.1:** Workstation 14 Dual-Headset Diagnostic Triage
* **Format & Aspect Ratio:** `16:9` Cinematic Procedural Spread
* **Teaching Beat:** The Complication (Live Audition Under Fire)
* **Prompt:**
  ```text
  Cinematic graphic novel illustration in modern DC Comics style (Jorge Jimenez). Crisp ink linework, moody Pacific Northwest interior office lighting. Inside the fourth-floor municipal operations center bullpen in Portland. Outside the panoramic windows, steady rain coats the glass overlooking the steel trusses of the Hawthorne Bridge. 

  At Workstation 14, 19-year-old rookie technician Ethan Mercer sits upright and tense, wearing a single-ear call-center headset connected to a dual-plug training splitter. Beside him, 34-year-old lead support specialist Jules Brooks leans in with acute focus, sharing the training bridge with her headset clamped over one ear. Jules's hand is frozen inches above the console mute button, eyes locked on the dual monitor displays with intense mentor concentration. 

  The left monitor displays a high-contrast ticket window with a blank red alert header block. The right monitor displays an open administrative management console window with a blank multi-tab dialog. On the partition wall behind Ethan, Jules's matte silver commuter bicycle helmet hangs from a bracket, with a yellow sticky note on her monitor bezel. Clean panel composition, no text, no letters, no words anywhere on screens or papers. 16:9 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 2.1: THE LIVE TRIAL ON WORKSTATION 14`
  * **Badge:** `Process of Elimination`
  * **Caption:** `Workstation 14 during Ethan's second-round working trial. Jules Brooks monitors the call on a dual-headset training splitter as Maya Lin's payroll application crashes. Jules coaches Ethan to isolate the failure domain using Safe Mode and Event Viewer rather than wiping the operating system.`
  * **Interactive Overlay Pins:**
    * Pin 1 (Left Monitor): `Ticket #4200 — High-priority payroll ledger freeze flagged 4 hours before biweekly direct deposit cutoff.`
    * Pin 2 (Mute Switch): `The Diagnostic Intervention — Jules intercepts Ethan's impulse to run an OS re-image, enforcing systematic elimination of variables.`
    * Pin 3 (Dual Splitter): `The Training Bridge — Dual-headset audio splitter allowing supervised triage without compromising municipal security clearance.`

---

### Episode 03: The Default Gateway Doesn't Care (Net+ Addressing)
* **Figure 3.1:** Local Subnet Boundary & Layer 3 Host-Stack Routing
* **Format & Aspect Ratio:** `16:9` Ligne Claire Schematic Cutaway
* **Teaching Beat:** The Complication (Off-Link Packet Abort)
* **Prompt:**
  ```text
  Clean technical schematic illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even lighting, neutral background, no heavy dark shadows. 

  Split-domain network topology diagram:
  On the left, an industrial logistics terminal connects through a blue patch cable to an unmanaged 8-port desktop switch. The switch blindly forwards Ethernet frames based on Layer 2 MAC addresses. Above the terminal, an architectural cutaway reveals the host's internal Layer 3 network stack: a mathematical bitwise AND operation compares the destination IP against the local /26 subnet mask. 

  Because the destination sits outside the local boundary, the host stack checks its internal routing table for a default gateway, finds the gateway IP is also off-link, and aborts transmission locally. A red obstruction icon appears inside the host stack, not on the physical switch. Crisp technical lines, true component colors, clean unlabeled surfaces, no text, no letters, no numbers. 16:9 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 3.1: THE HOST-STACK ROUTING ABORT`
  * **Badge:** `Subnet Boundaries`
  * **Caption:** `Architectural cutaway: Why packets fail to leave the local machine. The unmanaged Layer 2 switch forwards frames faithfully, but the host's Layer 3 network stack determines the destination is off-link and aborts locally because its configured gateway sits across a /26 subnet boundary.`
  * **Interactive Overlay Pins:**
    * Pin 1 (Host Stack): `Bitwise Subnet Evaluation — Host applies 255.255.255.192 mask, identifies target as off-link, and checks local routing table.`
    * Pin 2 (Off-Link Gateway): `Gateway Mismatch — Configured default gateway sits outside the host's local broadcast segment, causing immediate local packet drop.`
    * Pin 3 (Unmanaged Switch): `Layer 2 Transparency — Unmanaged switch forwards broadcast frames faithfully; failure occurs entirely in host IP logic.`

---

### Episode 04: The Name Is Not the Number (Net+ DNS)
* **Figure 4.1:** Split-Horizon DNS Resolution Race & Negative Cache
* **Format & Aspect Ratio:** `16:9` Dual-Conduit Technical Schematic
* **Teaching Beat:** The Complication (Resolver Cache Contamination)
* **Prompt:**
  ```text
  Clean technical schematic diagram in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even lighting, clean neutral background. 

  Dual-path DNS resolution schematic:
  A workstation network interface branches into two separate conduits. 
  Path A (Corporate Path): Routes upward through an internal firewall to an enterprise domain controller DNS server, showing an authoritative resource record returning a clean forward lookup address.
  Path B (Public ISP Path): Routes horizontally through an external ISP router to an authoritative external DNS server, which returns a negative response (NXDOMAIN). 

  A central cutaway inside the workstation operating system illustrates the local DNS resolver cache memory buffer. The faster negative response from Path B arrives first, locking the negative entry into local cache with a live countdown timer. Crisp lines, directional flow arrows, clean unlabeled surfaces, no text, no letters, no words. 16:9 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 4.1: SPLIT-HORIZON RESOLUTION RACE`
  * **Badge:** `DNS Architecture`
  * **Caption:** `Dual-conduit schematic: Multi-homed DNS resolver race. Workstation queries both corporate DNS and external ISP resolvers simultaneously. The faster negative response (NXDOMAIN) populates the local resolver cache, blocking access to the internal intranet.`
  * **Interactive Overlay Pins:**
    * Pin 1 (Local Cache): `Resolver Cache Contamination — Negative answer cached locally under RFC 2308, poisoning resolution until cache is flushed.`
    * Pin 2 (Corporate Path): `Authoritative Internal Zone — Corporate DC holds valid private record, but response arrives milliseconds after the public negative.`
    * Pin 3 (Hosts File): `Static Name Override — Local text file overrides DNS resolution hierarchy entirely, bypassing poisoned cache.`

---

### Episode 05: The Wire Has Two Ends (Net+ Transport)
* **Figure 5.1:** Client Outbound Ephemeral Port Exhaustion & TIME_WAIT
* **Format & Aspect Ratio:** `16:9` State Machine & Buffer Cutaway
* **Teaching Beat:** The Pivot (Outbound Source Port Starvation)
* **Prompt:**
  ```text
  Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, neutral background. 

  Operating system socket architecture diagram:
  At the top, a circular state-machine dial illustrates the TCP connection lifecycle: ESTABLISHED progressing through FIN_WAIT_1 and FIN_WAIT_2 to TIME_WAIT. 

  Below, a client socket allocation table is depicted as a circular ring buffer divided into numbered sectors representing the ephemeral port range (49152 to 65535). Nearly every slot in the ring buffer is choked with amber blocks representing active closer sockets held in a mandatory two-minute TIME_WAIT state. A client application thread attempting to execute an outbound connection encounters a depleted pool of available source ports, triggering an allocation failure icon. Crisp technical linework, clean unlabeled surfaces, no text, no letters, no words. 16:9 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 5.1: EPHEMERAL PORT STARVATION IN TIME_WAIT`
  * **Badge:** `Transport Protocols`
  * **Caption:** `Cutaway of client TCP socket architecture. Rapid-fire automated polling scripts close sessions actively, locking thousands of client outbound sockets into the 120-second TIME_WAIT state and starving new connection requests.`
  * **Interactive Overlay Pins:**
    * Pin 1 (Socket Ring Buffer): `Ephemeral Port Range (49152–65535) — Dynamic pool of source ports exhausted by rapid-fire outbound socket allocation.`
    * Pin 2 (TIME_WAIT State): `2MSL Timer Delay — TCP kernel locks active closer sockets for 120 seconds to prevent late duplicate segments from corrupting new sessions.`
    * Pin 3 (Connection Abort): `WSAEADDRINUSE Failure — Client cannot allocate an unused source port to complete the 4-tuple socket handshake.`

---

### Episode 06: The Portland Flood (Net+ Capstone)
* **Figure 6.1:** Sub-Basement Datacenter Water Elevation & Cable Dressing
* **Format & Aspect Ratio:** `21:9` Cinematic Ultrawide Silicon Noir Spread
* **Teaching Beat:** The Disaster / The Pivot (Physical Infrastructure Rescue)
* **Prompt:**
  ```text
  Cinematic ultrawide graphic novel spread in modern DC Comics style (Jorge Jimenez). High dramatic atmospheric lighting, gritty realism. Sub-basement telecommunications vault of the Portland operations center during a catastrophic storm water main break. Murky storm water sits eight inches deep across the concrete floor, reflecting emergency battery backup lights. 

  In the foreground, Ethan Mercer and Jules Brooks, soaked to their waists, work in synchronized partnership. Jules stands on an overturned heavy plastic milk crate, holding a tactical waterproof work light illuminating the open 42U equipment rack. Ethan uses ratcheting cable cutters to free tensioned bundles of blue Cat6 network cables from low-mounted wire trays. 

  Inside the rack, they are remounting core 48-port switches four rack units (4U) higher above the rising waterline. Heavy service loops of slack cable are neatly re-dressed overhead. Glowing green switch LED indicators reflect off the dark rippling water. Gritty working-class technical atmosphere, crisp line art, no speech bubbles, no text, no words. 21:9 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 6.1: SUB-BASEMENT FLOOD & EMERGENCY RACK RECOVERY`
  * **Badge:** `Physical Disaster Recovery`
  * **Caption:** `Sub-basement datacenter during water main break. Ethan Mercer and Jules Brooks hoist core network hardware above the rising flood line, preserving trunk uplinks and maintaining municipal communications.`
  * **Interactive Overlay Pins:**
    * Pin 1 (4U Elevation): `Vertical Hardware Relocation — Critical switches elevated 4 rack units (7 inches) above projected water table.`
    * Pin 2 (Overhead Service Loops): `Cable Slack Reserves — Factory service loops in overhead trays permit emergency vertical equipment relocation without re-terminating patch panels.`
    * Pin 3 (Spanning Tree Trunk): `Trunk Uplink Redundancy — Dual Cat6 links bonded in LACP aggregate port channel maintain network spine integrity under mechanical vibration.`

---

### Episode 07: The Port That Is Open (Sec+ Ports)
* **Figure 7.1:** Industrial OT Perimeter Gateway & Encrypted Tunneling
* **Format & Aspect Ratio:** `16:9` Ligne Claire Cutaway Schematic
* **Teaching Beat:** The Pivot (Cleartext Telnet Hardened to IPsec VPN)
* **Prompt:**
  ```text
  Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, clean neutral background. 

  Industrial network architecture cutaway:
  On the left, an office workstation communicates across an unencrypted corporate network. A red dashed conduit indicates vulnerable cleartext Telnet traffic exposed to internal network taps. 

  The connection terminates at an industrial DIN-rail security gateway mounted inside a NEMA electrical enclosure. The gateway establishes a secure IPsec VPN tunnel (green glowing shielded conduit) through an enterprise firewall. On the isolated right side (the plant floor), the gateway drops unencrypted control traffic onto a hardened industrial switch connected to a programmable logic controller (PLC) controlling municipal water valves. Clear structural division between enterprise office and operational technology (OT) zones. Crisp technical line art, clean unlabeled surfaces, no text, no letters, no words. 16:9 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 7.1: INDUSTRIAL OT GATEWAY & ENCRYPTED TUNNEL`
  * **Badge:** `Perimeter Hardening`
  * **Caption:** `Network perimeter hardening at Leah Moreno's municipal pump station. Jared's legacy cleartext script is replaced with SSH key authentication over an encrypted IPsec VPN tunnel terminating at an industrial security gateway.`
  * **Interactive Overlay Pins:**
    * Pin 1 (Legacy Red Conduit): `Cleartext Telnet (Port 23) — Unencrypted management session exposing administrative passwords to packet capture on the LAN.`
    * Pin 2 (Shielded Green Tunnel): `SSH (Port 22) over IPsec VPN — Encrypted tunnel protecting management traffic across public and corporate networks.`
    * Pin 3 (OT Security Gateway): `Purdue Model Boundary — Dedicated industrial gateway terminates VPN tunnel and isolates sensitive SCADA field hardware from corporate network hops.`

---

### Episode 08: Prove Who You Are (Sec+ Authentication)
* **Figure 8.1:** Hardware-Backed Authentication & TPM 2.0 PCR Sealing
* **Format & Aspect Ratio:** `4:3` Top-Down Technical Workbench Cutaway
* **Teaching Beat:** The Pivot (MFA Factor Classification & Hardware Trust)
* **Prompt:**
  ```text
  Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, clean ESD mat background, neutral shadows. 

  Top-down cutaway view of an enterprise authentication workbench:
  On the left, a modern smartphone displays an unprinted modal authorization prompt with a prominent thumbs-up icon. Directly beside it, a USB FIDO2 hardware security key is plugged into a laptop port, its gold capacitive touch ring glowing softly. 

  In the center, an architectural cutaway into the laptop's motherboard exposes the square surface-mount Trusted Platform Module (TPM 2.0) chip. Fine golden circuit traces illustrate cryptographic hash chaining into Platform Configuration Registers (PCRs), sealing private encryption keys until firmware state is verified. Beside the laptop rests an enterprise capacitive silicon fingerprint reader. Crisp fine lines, true component colors, clean unlabeled surfaces, no text, no letters, no words. 4:3 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 8.1: HARDWARE-BACKED AUTHENTICATION BENCH`
  * **Badge:** `Authentication Architecture`
  * **Caption:** `Hardware-anchored authentication triad. Workstation cryptographic secrets are sealed inside a TPM 2.0 chip, unlocked only through a combination of biometric presence and out-of-band FIDO2 token authorization.`
  * **Interactive Overlay Pins:**
    * Pin 1 (FIDO2 Hardware Key): `Something You Have — Hardware token with capacitive touch sensor; cryptographic private key never leaves physical silicon.`
    * Pin 2 (TPM 2.0 Cryptographic Chip): `Hardware Root of Trust — Platform Configuration Registers (PCRs) verify firmware integrity before releasing BitLocker master keys.`
    * Pin 3 (Capacitive Biometric Sensor): `Something You Are — Sub-dermal capacitive fingerprint reader verifying physical human presence against replay attacks.`

---

### Episode 09: Don't Click That (Sec+ Phishing)
* **Figure 9.1:** MIME Header Envelope Structure & DMARC Alignment
* **Format & Aspect Ratio:** `4:3` Layered Envelope & Protocol Cutaway
* **Teaching Beat:** The Complication / The Pivot (Triple-Gate BEC Detection)
* **Prompt:**
  ```text
  Clean technical schematic illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even lighting, clean neutral background. 

  Multi-layered email structure cutaway:
  An email message is rendered as three stacked semi-transparent technical parchment layers. 
  Layer 1 (The Envelope): The SMTP RFC 5321 Return-Path envelope layer showing originating IP address pointing to a verified SPF TXT record with a green checkmark.
  Layer 2 (The Cryptographic Seal): The DKIM signature block showing an asymmetric cryptographic hash validated against the sender's public DNS key.
  Layer 3 (The User-Facing Header): The RFC 5322 'From:' display header containing a subtle punycode typographical spoof. 

  A prominent vertical alignment plumb-line connects the three layers. The line breaks at Layer 3 with a red warning fracture icon, illustrating DMARC alignment failure. Crisp lines, technical callout geometry, clean unlabeled surfaces, no text, no letters, no words. 4:3 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 9.1: EMAIL PROTOCOL DECONSTRUCTION & DMARC ALIGNMENT`
  * **Badge:** `Email Security`
  * **Caption:** `Three-tier email header structure. While the message passes SPF and DKIM on the attacker's disposable domain, DMARC rejects the email because the authenticated domain fails to align with the visible From: header.`
  * **Interactive Overlay Pins:**
    * Pin 1 (Layer 1 Envelope): `RFC 5321 MailFrom (SPF) — Originating server IP verified against DNS TXT record for the attacker's disposable domain.`
    * Pin 2 (Layer 2 DKIM): `Cryptographic Signature — Asymmetric hash verified against sender public key; guarantees message integrity in transit.`
    * Pin 3 (Layer 3 Header Alignment): `DMARC Alignment Failure — Mismatch between technical envelope domain and display From: header triggers quarantine policy.`

---

### Episode 10: Something on the Box (Sec+ Malware)
* **Figure 10.1:** Dual Layer 1 Host Isolation & Forensic Containment
* **Format & Aspect Ratio:** `16:9` Procedural Graphic Novel Spread
* **Teaching Beat:** The Pivot (Host Isolation Under Incident Pressure)
* **Prompt:**
  ```text
  Dynamic graphic novel spread in modern DC Comics procedural style (Jorge Jimenez). Sharp inks, dramatic lighting, high tension. Inside the concrete logistics office of the Gresham warehouse terminal. 

  On the scarred laminate staging table, Ken's ruggedized corporate laptop is running at full load with cooling fans whining. A handheld barcode scanner sits discarded beside an anomalous thumb drive. 

  In the foreground, Ethan Mercer moves with deliberate diagnostic calm. With his right hand, his thumb depresses the clear plastic release tab of the blue Cat6 Ethernet cable, cleanly sliding the RJ-45 plug out of the laptop's network jack. With his left hand, he toggles the physical sliding hardware Wi-Fi cut-off switch on the side of the chassis, severing wireless radio transmission simultaneously. Behind the table, Ken leans forward with fists on the desk, tense and frustrated, watching the disconnect. Crisp linework, realistic anatomy, no speech bubbles, no text, no words. 16:9 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 10.1: DUAL LAYER 1 HOST ISOLATION`
  * **Badge:** `Incident Containment`
  * **Caption:** `Emergency host containment on the warehouse network. Ethan Mercer severs all network links via physical RJ-45 release and hardware radio kill-switch, blocking malware command-and-control beacons while preserving volatile RAM evidence.`
  * **Interactive Overlay Pins:**
    * Pin 1 (RJ-45 Disconnect): `Wired Network Isolation — Disconnecting Ethernet blocks lateral SMB propagation and automated network shares encryption.`
    * Pin 2 (Hardware Wi-Fi Cutoff): `Wireless Radio Sever — Disabling the physical Wi-Fi radio prevents automatic failover to corporate wireless networks.`
    * Pin 3 (Preserved Volatile State): `Live System Retention — System left energized under battery power to preserve volatile RAM memory for forensic capture.`

---

### Episode 11: The Air Is Shared (Sec+ Wireless)
* **Figure 11.1:** 2.4 GHz vs. 5 GHz Channel Spectrum & Rogue AP Mask
* **Format & Aspect Ratio:** `16:9` Dual-Plane RF Waveform Cutaway
* **Teaching Beat:** The Complication (Co-Channel Contention & Evil Twin Spoof)
* **Prompt:**
  ```text
  Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even studio lighting, clean neutral background. 

  Dual-plane radio frequency (RF) spectral analysis diagram:
  Top Plane (2.4 GHz ISM Band): Three clean non-overlapping bell curves represent Wi-Fi Channels 1, 6, and 11. Overlapping Channel 6 is an erratic, jagged, jagged red noise envelope representing 2450 MHz industrial microwave radiation, accompanied by an unauthorized rogue access point bell curve transmitting on Channel 6, causing complete spectral contention.

  Bottom Plane (5 GHz UNII Band): A wide, spacious frequency plane showing dozens of individual, non-overlapping channels separated by clean guard bands, illustrating superior channel capacity and zero co-channel interference. Dynamic waveform lines, clean technical callouts, clean unlabeled surfaces, no text, no letters, no words. 16:9 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 11.1: RF SPECTRUM COLLISION & ROGUE AP INTERFERENCE`
  * **Badge:** `Wireless Architecture`
  * **Caption:** `Dual-plane radio frequency spectrum analysis. The crowded 2.4 GHz band suffers severe co-channel interference from an unauthorized consumer router and breakroom microwave, while the 5 GHz band provides wide, clean channels.`
  * **Interactive Overlay Pins:**
    * Pin 1 (2.4 GHz Contention): `Channel 6 Collision — Rogue consumer router operating on Channel 6 creates massive co-channel interference on warehouse barcode scanners.`
    * Pin 2 (Microwave Interference): `2450 MHz Non-Wi-Fi Interference — Unshielded microwave magnetron radiates raw RF energy across the entire middle of the 2.4 GHz spectrum.`
    * Pin 3 (5 GHz Clean Spectrum): `UNII Band Architecture — 24 non-overlapping 20 MHz channels provide interference-free wireless capacity for mission-critical scanners.`

---

### Episode 12: When the Ticket Escalates (Sec+ Incident Response)
* **Figure 12.1:** Forensic Bench & RFC 3227 Order of Volatility
* **Format & Aspect Ratio:** `16:9` Forensic Technical Bench Cutaway
* **Teaching Beat:** The Capstone Pivot (Evidence Integrity & Cryptographic Custody)
* **Prompt:**
  ```text
  Clean technical cutaway illustration in Pacific Northwest instructional manual style, crisp uniform ink linework, bright even inspection lighting, clean ESD mat background, neutral shadows. 

  Forensic investigation bench layout:
  In the center, an energized suspect laptop is connected via a dedicated USB cable to a high-speed external storage drive running live memory acquisition software. Beside the laptop sits an analog mechanical stopwatch with an unprinted dial face, ticking elapsed seconds. 

  On the right side of the bench, a detached secondary SATA hard drive connects through a compact rectangular hardware write-blocker bridge (with an active green LED indicator) to a forensic workstation. An anti-static evidence bag, a tamper-evident adhesive security seal, and a chain-of-custody tracking log with a stainless drafting pencil rest neatly on the mat. Clean professional laboratory linework, true component colors, clean unlabeled surfaces, no text, no letters, no words. 16:9 ratio.
  ```
* **Docsify Callout-Panel Overlay Specification:**
  * **Title:** `FIGURE 12.1: THE DIGITAL FORENSIC BENCH & EVIDENCE PRESERVATION`
  * **Badge:** `Incident Response`
  * **Caption:** `Digital forensic workstation during CSIRT evidence acquisition. Volatile RAM memory is captured from the live laptop, while persistent storage is imaged through a hardware write-blocker under strict chain of custody.`
  * **Interactive Overlay Pins:**
    * Pin 1 (Live RAM Capture): `RFC 3227 Volatile Priority — Volatile system memory captured from live system before powering down to preserve active processes and network sockets.`
    * Pin 2 (Hardware Write-Blocker): `Hardware Write-Blocker Bridge — Blocks inbound write commands at the controller layer during dead-disk imaging, preserving raw evidence integrity.`
    * Pin 3 (Chain of Custody Dossier): `Cryptographic Custody — Tamper-evident evidence bag and SHA-256 verification hash document unbroken custody for law enforcement handoff.`
