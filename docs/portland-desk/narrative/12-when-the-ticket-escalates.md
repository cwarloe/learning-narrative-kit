# Portland Desk — When the Ticket Escalates

*A Security+ incident response precursor • Hover over highlighted terms after they have earned their keep.*

A gusting Wednesday rain swept across the Willamette as I stepped onto the fourth floor. Eleven months on the service desk had taught me that the quietest tickets are often the ones carrying the sharpest edges. On the bezel of her monitor, Jules's sticky note still asked *Which decision?* under the fluorescent lights.

The dispatch board read forty-two open items at eight in the morning: forgotten passwords, jammed label printers, and a conference room projector that refused to handshake over HDMI. But by two in the afternoon, the board had gone dead silent. That silence is the first thing you learn to fear on an operations floor. When the phones stop ringing, it usually means the fire has moved into the walls.

## Maya and the laptop that must die

```callout-panel
title: "FIGURE 12.1: LIVE FORENSIC MEMORY CAPTURE & ORDER OF VOLATILITY"
badge: "Incident Response"
caption: "Forensic bench diagram: An isolated, live running laptop on an ESD mat with a write-blocking USB capture tool acquiring volatile RAM (RFC 3227) before power-down and physical storage disk acquisition."
prompt: "Clean technical cutaway illustration of a computer forensic examination bench under bright laboratory lighting. A running laptop sits on an ESD mat connected via USB to a dedicated forensic memory acquisition dongle with glowing green status LEDs. Evidence tags and documentation binder nearby. Sharp technical linework, no text, no words. 16:9 ratio."
```

The day's first alarm was loud, messy, and harmless. 

At 08:30, Maya Lin from Accounting marched past the glass partition holding her Dell Latitude by the corner of the lid like a wet umbrella. Her eyes had the frantic intensity of someone who believed her machine had contracted a personal grudge.

"It is possessed, Ethan," Maya said, dropping the machine onto my staging mat with a plastic clatter. "Pop-ups. Every time I open Chrome, five tabs try to sell me Caribbean cruises. The fan is screaming. My standup with the VP is in twelve minutes. Wipe it clean and image it from the thumb drive."

Eleven months ago, I would have reached straight into the drawer for the bootable USB. Back then, "possessed" meant fire, and fire meant formatting the disk. I took the laptop, reached for the Ethernet jack to pull the copper, and had my hand on the imaging drive when Jules set her coffee mug on the divider wall with a dull *clack*.

"What did the box do, Ethan?" Jules asked, without looking up from her screen. "Besides scare Maya?"

"Ads, slowness, fan pinned," I said, reciting the panic. 

Jules did not take the imaging stick from my hand. She reached over, plugged the laptop into a standalone, air-gapped diagnostic switch port, and opened the local endpoint protection log. I hadn't even looked at the history.

The log told the entire story in two lines: a known adware installer (`CouponBlast.exe`) had been downloaded at 07:41 and immediately quarantined in user space by Windows Defender. The pop-up tabs were orphaned Chrome notification permissions left behind in the browser profile. No new local accounts. No abnormal Kerberos ticket requests. No lateral network traffic.

"You were about to destroy the only evidence of a nothingburger," Jules said, looking at me over her glasses. "And if it had actually been an active intrusion, you were about to wipe the only volatile forensic memory that could tell the incident team how the adversary got inside."

I put the bootable USB back into the drawer and shut it. My hands had been moving faster than my criteria.

"This is an [[event|event]]," Jules said, handing the laptop back across the divider. "The automated control already performed the verb. Clear Maya's browser notification permissions, verify the hash in the quarantine vault, and return the laptop so she makes her meeting."

I cleared the profile, showed Maya the green Defender checkmark, and sent her downstairs with five minutes to spare. I didn't feel heroic. I felt like an apprentice who had almost swung a sledgehammer at a loose hinge.

Jules tapped the top of the imaging drawer with her pen. "You can open that drawer again when you can tell me why an operating system's volatile memory is worth more than your convenience."

## The quiet mailbox

At 11:15, the second ticket arrived. It came without shouting or all-caps subject lines. It arrived as a polite two-line inquiry from Nora Higgins in Finance: *Can't find morning wire confirmations in my Sent folder. Also noticed an Outlook rule I don't remember creating. Low priority.*

I didn't reach for the USB drawer. I remoted into the Exchange administrative center from my console, remembering Jules's rule: *start on your side of the glass.*

I pulled Nora's mailbox audit log. At 02:13 AM Pacific time—while Nora was asleep in Sellwood—an interactive login had been validated against her Azure Active Directory account. The source IP was `198.51.100.77`, geolocating to a commercial hosting provider in Frankfurt, Germany. Nora had never left Oregon.

Three minutes after that logon, an automated mailbox rule titled `InvoiceProcess` had been injected into her client ruleset. The rule condition was surgical: any incoming or outgoing message containing the words *wire, routing, invoice, statement,* or *payment* was automatically redirected to an external recipient at `exfil@pay-secure-audit.com`—and then immediately deleted from Nora's Sent Items and Inbox to hide the trail.

A cold weight settled into my stomach. This wasn't adware. This was an active, coordinated Business Email Compromise.

I disabled the malicious forwarding rule in Exchange PowerShell. Disabling the rule stopped the live siphon, but I didn't touch Nora's password yet, and I didn't post an all-caps warning in the Finance department chat.

"Jules," I said, keeping my voice low. "Look at this forwarding target."

Jules wheeled her chair across the carpet until she was looking directly at my console. Her posture shifted instantly. The dry, casual mentor disappeared; the lead responder took over.

"Do not alert the user over chat," Jules whispered. "[[need_to_know|Need-to-know]] is operational hygiene. If the threat actor has an active session token, shouting in a company channel tells them we're watching. What does the host telemetry show for Nora's physical workstation?"

I opened the endpoint telemetry console for `FIN-NORA-02`. At 11:04 AM, ten minutes before Nora submitted her polite ticket, her workstation had established an outbound HTTPS socket to `185.22.112.14` on port 443. The process owning the connection was `powershell.exe`, running under an encoded Base64 commandline that had injected into `lsass.exe` memory.

Every three hundred seconds—five minutes like clockwork—the beacon sent an outbound packet and received a payload chunk.

"Host C2 beaconing," I said, feeling the hairs on my arms stand up. "They phished Nora's credentials last night, bypassed MFA with an adversary-in-the-middle proxy, and dropped an in-memory payload on her desktop this morning."

## The lateral pivot and the warehouse USB

Before Jules could answer, Jared Vance burst into our aisle from the server room, his face pale beneath the fluorescent tubes. He wasn't carrying coffee.

"Todd Miller in Inside Sales just called from the dock," Jared said, his breath short. "He found an unbranded USB stick on the floor of the shipping office labeled *Client Deck Final*. He plugged it into `TODD-SALES-14` to see whose presentation it was."

"Tell me he didn't run the file," Jules said, her voice dropping an octave.

"He clicked `SOW_final.pdf.exe`," Jared answered. "The file spawned a hidden PowerShell loop. I just checked our distribution core switch. Todd's machine is running automated SMB share sweeps across `10.100.0.0/16`, spraying harvested credentials across every administrative share it can find."

"The same hash as Sam's quarantine sample from two weeks ago," I said, pulling the SHA-256 ledger from my desk notebook: `9f2c8d1e...c41a`. "The threat actor had a physical USB drop coordinated with the cloud credential phishing."

"It's worse than that," Jared said, tapping my secondary screen. "Look at the authentication logs on `SRV-STAGE-01`."

My screen refreshed. `SRV-STAGE-01` was the dual-homed staging jump host we had hardened in Episode 07. It bridged the corporate management subnet with the isolated industrial operations network. Thirty seconds ago, Nora's compromised credentials had successfully authenticated against the jump host via SSH from `FIN-NORA-02`.

And thirty seconds after that, the network edge firewall logged an outbound connection attempt on port 8443 originating from `GW-PLANT-04`—the SCADA edge gateway at the Willamette River Water Treatment Facility—reaching out to the exact same external command-and-control IP: `185.22.112.14`.

The pieces snapped together with terrifying clarity. This was not four random help desk tickets. This was a synchronized, multi-vector enterprise intrusion: credential phishing, memory-resident C2 beaconing, physical removable media lateral movement, and a direct pivot into the critical municipal water utility grid.

## The red binder and the clock

"This is a Category One Security Incident," Jules said, standing up and shutting her laptop screen. "Jared, isolate switch ports twenty-two and twenty-three on core switch two. Cut the dual-homed jump host off the wire, but do not power it down. Do not reboot it. Leave the memory energized."

She reached into the bottom drawer of her filing cabinet and pulled out two heavy items: a thick, three-ring red binder embossed with *PORTLAND OPERATIONS CSIRT ESCALATION PROTOCOL*, and a stack of silver electrostatic shielding evidence pouches with serialized chain-of-custody tags.

She set the red binder in front of my keyboard.

"Maya Lin's machine this morning was an event, Ethan," Jules said, her voice quiet, steady, and unyielding. "This is the incident. The Enterprise CSIRT and the incident commander will be on this floor in twenty minutes. When they walk through those double doors, they don't want guesses, they don't want apologies, and they don't want wiped hard drives."

She pointed to the anti-static evidence pouches on my desk.

"You have two compromised endpoints on this floor, an active exfiltration pipeline, and a live connection into the plant SCADA network. If you pull the power plugs, the adversary's encryption keys and volatile process handles in [[ram_memory|RAM]] evaporate into zero bits forever. If you leave them on the network, the exfiltration script drains the water plant telemetry. 

You are the first responder on this shift. Follow the [[order_of_volatility|Order of Volatility]]. Isolate the endpoints from the wire, execute a forensically sound live memory capture, compute the cryptographic SHA-256 hashes before you touch storage, establish the legal chain of custody, and build the formal CSIRT Escalation Dossier before the clock runs out."

I looked down at the red binder. Eleven months ago, I was a twenty-year-old kid on the Gresham loading dock, clutching an eight-hundred-page textbook and terrified of failing a multiple-choice test in a Beaverton strip mall. 

Today, there were no multiple-choice questions. The municipal grid was on the line, and the desk had handed me the pen.

---

> [!IMPORTANT]
> ### The Book 0 Crucible: The CSIRT Escalation Gate
> Multi-vector indicators have aligned across finance, sales, and industrial plant telemetry. Nora's C2 beacon is live, Todd's host is enumerating lateral shares, and the Willamette River gateway is attempting external egress.
> 
> **Your Turn at the Console:** Step up to the Incident Console on the Workbench. Execute the live memory acquisition, preserve the Order of Volatility, compute the cryptographic SHA-256 verification hashes, and deliver the formal CSIRT Escalation Dossier to Jules Brooks before the incident command team takes the floor.
> 
> [Take the Ticket & Open the Lab →](workbench/12-when-the-ticket-escalates.md)

## Vocabulary & Concepts

The following desk translation table contrasts textbook certification definitions with the physical realities encountered on an active operational floor:

| Technical Concept | CompTIA Security+ Exam Specification | Shop-Floor Reality & Triage Ground Truth |
| :--- | :--- | :--- |
| **[[security_incident|Security Incident]]** | An occurrence that actually or potentially jeopardizes the confidentiality, integrity, or availability of an information system. | A threshold distinction: an *event* is an observable anomaly (quarantined adware); an *incident* is an active, confirmed breach requiring formal containment and legal escalation. |
| **[[order_of_volatility|Order of Volatility]]** | The sequence in which digital evidence must be preserved based on its rate of decay, from CPU registers to persistent disk storage. | RFC 3227 hierarchy: CPU registers $\rightarrow$ Cache $\rightarrow$ RAM $\rightarrow$ Network Sockets $\rightarrow$ Hard Disk. If you power down an infected host before dumping memory, volatile decryption keys and injected processes are lost forever. |
| **[[chain_of_custody|Chain of Custody]]** | The chronological documentation showing the custody, control, transfer, analysis, and disposition of physical and electronic evidence. | A legal paper trail proving who collected the artifact, the exact second it was acquired, where it was stored, and who had physical access, backed by immutable cryptographic hashes. |
| **[[isolation|Network Isolation]]** | Severing an infected host's communication channels while maintaining electrical power to preserve volatile state. | Unplugging the Ethernet cable or asserting an EDR software isolation rule. Halts outbound C2 beaconing and lateral movement without terminating running processes in RAM. |
| **[[ioc|Indicator of Compromise (IoC)]]** | Forensically identified artifact or telemetry signature that signals an active or historical computer intrusion. | Actionable operational data: exact SHA-256 file hashes, C2 IP addresses, unauthorized listening ports, and registry persistence keys that allow SOC analysts to hunt across enterprise telemetry. |
| **[[csirt|CSIRT]]** | Computer Security Incident Response Team: dedicated multidisciplinary group responsible for handling enterprise security incidents. | The specialized incident command team that assumes operational authority during a confirmed breach. Tier 1 desk technicians triage, contain, preserve evidence, and hand off a verified dossier. |

```bridge-card
title: Portland Desk Lab: The Incident Escalation & SOC Handoff Crucible
target: workbench/12-when-the-ticket-escalates.md
domain: CompTIA Security+ SY0-701 • Domain 4.0 Incident Response & Operations
badge: Final Capstone Lab
cta: Take the Ticket & Open the Lab ->
---
Step onto Ethan's shift for the Book 0 Final Capstone: navigate multi-stage incident triage, execute Order of Volatility and cryptographic evidence hashing, master the 5-case CBYT prediction gate, and deliver the formal CSIRT Incident Handoff Dossier to Jules Brooks.
```
