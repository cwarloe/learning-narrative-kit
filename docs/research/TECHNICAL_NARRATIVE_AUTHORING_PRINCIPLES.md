# Technical Narrative Craft & Architecture Standard: Universal Principles for Authoring Technical Story-First Courseware

**Repository:** `learning-narrative-kit`  
**Applicability:** Universal standard across all narrative tracks (Portland Desk, Tamarack, ITM, and future courses)  
**Authors/Contributors:** Lead Curriculum Architect, Cynical Literary Editor (`prose_critic`), Adversarial Technical SME (`technical_nitpicker`)

---

## 1. Executive Manifesto: The Dual Tension of Technical Fiction

Writing technical narrative fiction is one of the most demanding tasks in instructional design. Authors face two opposing failure modes:

1. **The Dramatic Fallacy (Melodramatic Soap Opera):** The author focuses so heavily on melodrama, artificial stakes, or noir atmosphere that protocols become magical plot devices, technicians sweat blood over standard patch cables, and the technical mechanics make no sense to an actual practitioner.
2. **The Pedagogical Fallacy (The Walking Textbook):** The author pauses the story to have characters recite dictionary definitions or RFC specifications aloud while production servers burn. The dialogue turns into stilted Socratic catechism, the pace dies, and the reader falls asleep.

### The Core Law of the Learning Narrative Kit
> **The Narrative is the operational mental model; the Hover Tooltip is the lookup dictionary; the Workbench is the physical wrench.**  
> The story creates the situational forcing function that gives technical terms shared gravity. It must read like an authentic workplace incident, obey the laws of computer science and physical hardware, and teach without halting its own momentum.

---

## 2. Part I: The Literary Editor Standard (Dialogue, Voice, Pacing & Narrative Pedagogy)

*Derived from the Cynical Literary Editor (`prose_critic`)*

### Principle 1: Dialogue Under Pressure (The "Wire Is Hot" Rule)
**When production systems are failing, syllables shrink, grammar degrades, and explanations wait for post-mortems.**

Real engineers communicate in clipped operational shorthand, observable symptoms, and immediate trade-offs.

- **The Anti-"As You Know, Bob" Prohibition:** Characters must never explain foundational definitions to colleagues whose jobs require them to already know those concepts.
  - *Unacceptable:* *"As you know, Jared, Telnet is an unencrypted protocol that passes credentials in cleartext over port 23."*
  - *Acceptable:* *"Telnet, Jared? Really? In cleartext across the warehouse?"*
- **Triage Shorthand:** During active incidents, mean dialogue sentence length must drop below 12 words. Replace complete passive sentences with active verbs and brief queries.
  - *Unacceptable:* *"Ken, we are observing framing errors on the scale head due to clock desynchronization with the terminal."*
  - *Acceptable:* *"Scale's streaming garbage. Baud rate mismatch or a bent pin."*
- **End-User Translation Rule:** Technicians speak in plain functional terms when addressing non-technical staff (sales, accounting, dispatch), never in internal architecture.
  - *Unacceptable (to a payroll clerk):* *"We are booting into Safe Mode to prevent third-party kernel filter drivers from intercepting system calls."*
  - *Acceptable (to a payroll clerk):* *"We're restarting in Safe Mode. It only loads bare-bones Windows. If payroll opens there, Windows is fine and an addon is the culprit."*
- **Authentic Interpersonal Friction:** Workplaces have fatigue, friction, and territorial defensiveness. Senior admins defend their legacy scripts; warehouse supervisors worry about trailer schedules; junior technicians wrestle with imposter syndrome. Allow characters to sigh, disagree, and cut each other off.

### Principle 2: Pacing & Exposition Management (The "Division of Labor" Rule)
**Never force the narrative prose to do the tooltip’s job.**

- **The "Walking Glossary" Ban:** Characters must never recite glossary definitions aloud unless they are actively correcting a hazardous misconception on the floor (e.g., explaining why a password and a PIN do not satisfy Multi-Factor Authentication).
- **Trust the Marks:** Use `[[term_id|surface text]]`. The reader can hover for the formal exam definition. The narrative only needs to demonstrate **why that concept matters to the current operational dilemma**.
- **Teach Through Broken States, Not Lectures:** Concepts are learned fastest when students watch them fail.
  - Do not explain subnetting in the abstract; show two devices on the same switch that cannot reach each other because a `/26` mask places them in different networks.
  - Do not lecture on TCP RST vs. drop; show one client receiving an instant connection reset while another hangs for 21 seconds waiting for a silent drop.
- **The "One Beat, One Pivot" Architecture:** Every scene beat must follow: **Goal $\rightarrow$ Complication $\rightarrow$ Pivot**. Marked terms attach to the complication or pivot, never to scenic wallpaper.

### Principle 3: Character Voice & Consistency (The "Grounded Working-Class Tech" Rule)
**Anchor your protagonist in their authentic background. Prevent them from drifting between a Victorian academic and a 1940s noir detective.**

- **Eliminate the Victorian Scholar Voice:** Junior technicians do not speak in formal, 30-word compound-complex sentences.
  - *Unacceptable:* *"I evaluated each failure mode against the core building blocks, isolated the broken layer, and selected my answers with calm deliberation."*
  - *Acceptable:* *"I walked the tree from Layer 1 up, found the break, and picked the answer."*
- **Eliminate the Noir Detective Parody:** Ethan is a help desk technician, not a hard-boiled gumshoe nursing bourbon in the rain.
  - *Unacceptable:* *"Possessed is a word that wants a fire. I had a queue full of subject lines in all caps and a USB drawer I trusted too much."*
  - *Acceptable:* *"Maya had the laptop under her arm before I even opened the ticket. Her browser was crawling with coupon toolbars, and she wanted the machine nuked before standup."*
- **Natural Contractions:** Spoken American English uses natural contractions (*didn't, wasn't, couldn't, scale's, we'd*). Stiff avoidance of contractions makes characters sound robotic.
- **Physical Micro-Habits Over Melodrama:** Real technicians display tension through physical habits, not histrionics.
  - *Unacceptable:* Sweeping arms across desks to knock over flashcards; hearts pounding against ribs three times per chapter; cold sweat soaking shirts.
  - *Acceptable:* Wiping grease off knuckles with a shop rag; clicking a retractable pencil; taking a sip of lukewarm coffee; squinting at a blinking LED; checking the system clock.

### Principle 4: Descriptive Discipline (The "Break the Macro" Rule)
**Atmosphere is not established by repeating the same sensory tropes in every episode.**

- **Weather Quarantine:** Maximum of one weather opening every four episodes. Rain or temperature should only take focus if they directly cause the failure (e.g., basement storm flooding or summer HVAC failure).
- **Banish Puppet-String Entrances:** Do not open consecutive episodes with Jules wheeling her bicycle into the office, hanging her helmet on her monitor arm, and staring at her *Which decision?* sticky note. Enter scenes *in media res*—characters already troubleshooting, arguing, or reviewing the queue.
- **The AI Crutch-Word Kill List:**
  - [BLOCKED] *"steady"* (maximum once per episode)
  - [BLOCKED] *"meticulously"* / *"quietly"* / *"calm deliberation"*
  - [BLOCKED] *"hum of fluorescent ballasts"* / *"sixty-cycle buzz"*
  - [BLOCKED] *"chipped ceramic mug"* / *"lukewarm tea"*
- **Sensory Diversity:** Tap the real tactile details of IT work: the sharp scrape of a sheared zip-tie; the deafening roar of a server room return plenum; the stubborn residue of old label tape; the metallic snap of a cage nut; the glare of an uncalibrated second monitor.
- **No Participial Stacking:** Avoid opening three consecutive sentences with `-ing` clauses (*"Pulling the cable...", "Looking at the screen...", "Reaching for my tool..."*).

### Principle 5: Narrative Pedagogy (The "Show the Seam" Rule)
**The story teaches the mental model; the workbench builds operational fluency.**

- **The Non-Negotiable Cover Test:** Strip all markup brackets: `[[...]]`. If the raw prose still works as a compelling, clear workplace incident where the reader understands the root cause and the operational fix, the story passes. If the story collapses into technical jargon soup, it fails.
- **Contrast-Pair Teaching:** Clarify boundaries by contrasting paired concepts within the same scene:
  - *MAC Address (Layer 2)* vs. *IP Address (Layer 3)*: Factory serial number on the chassis vs. temporary room number on the lease.
  - *TCP RST* vs. *Silent Drop*: The host actively slamming the door shut vs. speaking into an empty void.
  - *Signature Detection* vs. *Heuristics*: Matching a known bad hash in a catalog vs. spotting an uncataloged process injecting code.
  - *Single Factor Twice* vs. *True MFA*: Entering two secrets from your memory vs. using a physical token in your hand.
- **The Clean Baton Handoff:** In cliffhanger episodes, the story must never solve the incident before the learner opens the lab. Establish the constraints, eliminate false leads, isolate the critical fork in the road, and hand the terminal to the student.

---

## 3. Part II: The Technical SME Standard (Protocol Realism & Architectural Accuracy)

*Derived from the Adversarial Technical SME (`technical_nitpicker`)*

### Principle 6: Layer Boundary Invariance (Vantage-Point Discipline)
**An endpoint or observer can only see telemetry that physically and logically exists at their specific vantage point in the network topology.**

- **The Local Boundary:** ARP (RFC 826) is strictly a Layer 2 broadcast domain protocol. Ethernet frames do not cross routers. A client endpoint’s local ARP cache only knows hosts on its local subnet and its default gateway.
- **Vantage-Point Consistency:** An administrator on Subnet A cannot run `arp -a <remote_ip>` to see a machine's MAC address on Subnet B. To inspect remote MACs, the character must query the Layer 3 switch/router ARP table (`show ip arp`) or the switch CAM table (`show mac address-table`).
- **Encapsulation Horizons:** If traffic traverses a router, Layer 2 MAC addresses are rewritten. If traffic crosses a NAT gateway, Layer 3 source IPs change. If traffic enters a TLS or IPsec tunnel, Layer 4 ports disappear. Never violate the horizon of the inspection tool.

### Principle 7: State Machine Integrity (Failure Modes Must Obey RFCs)
**Systems fail according to defined error paths in their protocol state machines, not author convenience.**

- **Respect Protocol State Transitions:** In DHCP (RFC 2131), a rebooting workstation enters `INIT-REBOOT` and sends a `DHCPREQUEST` for its current lease. A compliant server checks its active lease database, matches the client MAC (`chaddr`), and acknowledges the request with a `DHCPACK`. Active leases *protect* existing clients; they do not lock them out. Scope exhaustion occurs when *unregistered* MACs consume the dynamic unreserved pool, stranding genuine new requests in APIPA (`169.254.x.x`).
- **Trace the Error Branch:** When designing an outage, trace the formal state machine (DHCP DORA, TCP 3-way handshake, TLS ClientHello). Place complications at **valid RFC failure states** (`DHCPNAK`, TCP `RST`, `TIME_WAIT` saturation, `NXDOMAIN`), never by making a compliant daemon act contrary to its specification.

### Principle 8: Physical Geometry & Mechanical Causality
**Physical interfaces, pinouts, and hand tools possess immutable spatial dimensions.**

- **Gender and Pinout Precision:** Plugs have pins; sockets have holes. A technician cannot "unbend Pin 2 on a female socket" with a pencil tip. Furthermore, inspect real pinout diagrams (e.g., EIA/TIA-574 DE-9, RJ-45 T568A/B): on a DE-9 connector, Pin 2 (RXD) cannot short against Pin 5 (Signal Ground) due to a single bent pin, as Pin 5 sits on the opposite corner.
- **Order of Volatility (RFC 3227):** Hardware actions carry irreversible consequences. You cannot extract an NVMe SSD and attach it to a write-blocker while simultaneously capturing live volatile RAM. Powering down or pulling the drive destroys volatile memory instantly. Physical memory must always be captured before touching persistent media.

### Principle 9: Syllabus Harmony vs. Operational Ground Truth (The Double Truth Strategy)
**Satisfy introductory certification syllabi (CompTIA A+, Network+, Security+) while protecting students from oversimplified study-guide myths.**

- **Address the Nuance:** Beginner study guides often promote simplified rules that do not reflect production reality:
  - *Myth:* "MAC addresses never change." (Reality: MAC randomization is enabled by default on modern iOS, Android, and Windows Wi-Fi clients).
  - *Myth:* "FTPS always lives on Port 990." (Reality: Modern FTPS is RFC 4217 Explicit FTPS on standard Port 21 using `AUTH TLS`).
  - *Myth:* "Periodic 90-day password changes and character complexity rules are industry best practice." (Reality: NIST SP 800-63B explicitly deprecates arbitrary password rotation and complex character rules in favor of passphrases and compromised-credential screening).
- **The Senior Mentor Bridge:** Use senior character dialogue to transition students from exam memorization to operational reality:
  > *"That’s the answer that passes the multiple-choice exam, Ethan. Now look at what the RFC actually says when you open the capture..."*

### Principle 10: Telemetry, Syntax & Log Fidelity (The Black Box Rule)
**Command-line strings, flags, regex patterns, and log Event IDs must be authentic and syntactically valid for the target operating system.**

- **Channel Accuracy:** Windows Event IDs are channel-specific. For example, Service Control Manager new service installation is logged as **Event ID 7045** in the **System** channel (`System.evtx`). In the **Security** channel (`Security.evtx`), the equivalent audit event is **Event ID 4697**. Directing an analyst to look for Event 7045 in the Security log will yield zero results.
- **Command Validity:** Never invent CLI parameters (such as `net.exe view /all`). Students copy and paste commands from course narratives into real consoles; invalid syntax immediately breaks immersion.
- **Accurate Attack Terminology:** Executive impersonation directed at payroll or accounts payable to trigger wire transfers is **Business Email Compromise (BEC) / CEO Fraud**. Whaling specifically targets the executive as the victim, not the impersonated sender.

### Principle 11: Mathematical Sanity of Outages (Scaling Realism & Timer Arithmetic)
**The scale of an operational outage must align with the mathematical capacity of the underlying protocols.**

- **Ephemeral Port Depletion Arithmetic:** An operating system's ephemeral port pool (typically 49,152 to 65,535, offering ~16,384 available ports) cannot be exhausted by 400 sequential connections.
  $$\text{Concurrent Sockets in TIME\_WAIT} = \text{Connections Per Second} \times \text{2MSL Duration (default 120s)}$$
  Depleting 16,000+ ports requires high concurrency, aggressive parallel threads, sub-second polling loops, or unthrottled reconnects.
- **Sanity-Check Quantitative Claims:** Check the arithmetic behind every claimed resource failure (DHCP scope exhaustion, bandwidth saturation, switch CAM table flooding, socket exhaustion).

---

## 4. Part III: Pre-Flight Production Checklist

Before any technical narrative unit is submitted for validation and merge into the repository, audit it against these mandatory gates:

### Literary & Pacing Gates
- [ ] **Dialogue Reality Check:** Read every line of dialogue aloud. Does it sound like people speaking in a noisy, pressurized shop, or like a textbook reading itself?
- [ ] **Exposition Audit:** Are characters explaining concepts to colleagues who already know them? (Strike all instances).
- [ ] **Atmospheric Variety:** Did this episode reuse the opening weather, bike arrival, or coffee trope from the previous episode? (Rewrite the opening).
- [ ] **Voice Consistency:** Does the protagonist speak in a natural, working-class American voice with contractions, free of Victorian academic or noir detective tropes?
- [ ] **Cover Test:** Strip all `[[...]]` markup. Does the narrative still clearly convey the operational problem, the mental model, and the resolution?

### Technical & Protocol Gates
- [ ] **Layer & Vantage Point Audit:** Can the inspecting character logically see the telemetry from their physical console and network location?
- [ ] **Protocol State Machine Audit:** Does the failure follow a legitimate RFC state transition rather than an impossible protocol action?
- [ ] **Physical Hardware & Pinout Verification:** Are connector genders, pin numbers, and physical spatial relationships verified against official hardware pinouts?
- [ ] **Order of Volatility Compliance:** Are volatile artifacts (RAM, active network connections) acquired before secondary non-volatile media is touched or unpowered?
- [ ] **CLI & Log Event Accuracy:** Have all commands, flags, and Event IDs been checked against real OS documentation and channel schemas?
- [ ] **Quantitative Sanity Check:** Does the math for device count, polling frequency, and timer duration support the claimed resource exhaustion?

---

*This standard is permanently enforced across all narrative units within the Learning Narrative Kit repository.*
