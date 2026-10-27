# Portland Desk — When the Ticket Escalates

*A Security+ incident response precursor • Hover over highlighted terms after they have earned their keep.*

A gusting Wednesday rain swept across the Willamette as I stepped onto the fourth floor. Twenty-two months on the service desk had taught me that the quietest tickets are often the ones carrying the sharpest edges. Jules's monitor bezel was bare now. The sticky note had gone into her drawer months ago, and since then she had written the question on my tickets instead.

The dispatch board read forty-two open items at eight in the morning: forgotten passwords, jammed label printers, and a conference room projector that refused to handshake over HDMI. But by two in the afternoon, the board had gone dead silent. That silence is the first thing you learn to fear on an operations floor. When the phones stop ringing, it usually means the fire has moved into the walls.

Jules had made me keep the wireless baseline from April, and she checked it every Friday. Against it, the morning's quiet tickets looked wrong. <!-- date-ok: back-reference to the April wireless baseline and Friday checks -->

## Maya and the laptop that must die

```callout-panel
title: "FIGURE 12.1: LIVE FORENSIC MEMORY CAPTURE & ORDER OF VOLATILITY"
badge: "Incident Response"
caption: "Forensic bench diagram: An isolated, live running laptop on an ESD mat streaming volatile system RAM to an external forensic SSD (RFC 3227) while a standalone hardware write-blocker sits staged for Step 2 dead-disk storage imaging."
prompt: "Clean technical cutaway illustration of a computer forensic examination bench under bright laboratory lighting. A running laptop sits on an ESD mat connected via high-speed USB-C to a rugged external forensic SSD actively capturing live volatile memory. Staged on the ESD mat beside the laptop sits a standalone hardware write-blocker bridge with disconnected SATA/NVMe adapter cables and anti-static evidence bags ready for secondary persistent disk acquisition. Sharp technical linework, no text, no words. 16:9 ratio."
```

The day's first alarm was loud, messy, and harmless. 

At 08:30, Maya from Accounting marched past the glass partition holding her Dell Latitude by the corner of the lid like a wet umbrella. Her eyes had the frantic intensity of someone who believed her machine had contracted a personal grudge.

"It is possessed, Ethan," Maya said, dropping the machine onto my staging mat with a plastic clatter. "Pop-ups. Every time I open Chrome, five tabs try to sell me Caribbean cruises. The fan is screaming. My standup with the VP is in twelve minutes. Wipe it clean and image it from the thumb drive."

Twenty-two months ago, I would have reached straight into the drawer for the bootable USB. Back then, "possessed" meant fire, and fire meant formatting the disk. I took the laptop, reached for the Ethernet jack to pull the copper, and had my hand on the imaging drive when Jules said my name once, without turning around.

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

At 11:15, the second ticket arrived. It came without shouting or all-caps subject lines. It arrived as a polite two-line inquiry from Nora in Finance: *Can't find morning wire confirmations in my Sent folder. Also noticed an Outlook rule I don't remember creating. Low priority.*

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

Before Jules could answer, I saw Jared coming down the aisle from the server room, walking faster than I had ever seen him walk. He wasn't carrying coffee.

"Todd in Inside Sales just called from the dock," Jared said. "He found an unbranded USB stick on the floor of the shipping office labeled *Client Deck Final*. He plugged it into `TODD-SALES-14` to see whose presentation it was."

"Tell me he didn't run the file," Jules said, her voice dropping an octave.

"He clicked `SOW_final.pdf.exe`," Jared answered. "The file spawned a hidden PowerShell loop. I just checked our distribution core switch. Todd's machine is running automated SMB share sweeps across `10.100.0.0/16`, spraying harvested credentials across every administrative share it can find."

Jared found the link first, in the switch logs. Todd's workstation had opened a session to the staging jump host four minutes after the USB went in. "Same jump host Nora's account just hit," he said. "This is one intrusion, not two."

"It's worse than that," Jared said, tapping my secondary screen. "Look at the authentication logs on `SRV-STAGE-01`."

My screen refreshed. `SRV-STAGE-01` was the dual-homed staging jump host Jared had hardened the summer before. It bridged the corporate management subnet with the isolated industrial operations network. Thirty seconds ago, Nora's compromised credentials had successfully authenticated against the jump host via SSH from `FIN-NORA-02`.

And thirty seconds after that, the network edge firewall logged an outbound connection attempt on port 8443 originating from `GW-PLANT-04`—the SCADA edge gateway at the Willamette River plant—reaching out to the exact same external command-and-control IP: `185.22.112.14`.

The pieces snapped together with terrifying clarity. This was not four random help desk tickets. This was a synchronized, multi-vector enterprise intrusion: credential phishing, memory-resident C2 beaconing, physical removable media lateral movement, and a direct pivot toward the Willamette River plant's control network.

## The red binder and the clock

"This is a Category One Security Incident," Jules said, standing up and shutting her laptop screen. "Jared, isolate switch ports twenty-two and twenty-three on core switch two. Cut the dual-homed jump host off the wire, but do not power it down. Do not reboot it. Leave the memory energized."

She reached into the bottom drawer of her filing cabinet and pulled out two heavy items: a thick, three-ring red binder embossed with *PORTLAND OPERATIONS CSIRT ESCALATION PROTOCOL*, and a stack of silver electrostatic shielding evidence pouches with serialized chain-of-custody tags.

She set the red binder in front of my keyboard.

"Maya's machine this morning was an event, Ethan," Jules said, her voice quiet, steady, and unyielding. "This is the incident. Senior CSIRT Lead Nia Alvarez and the incident command team from Chicago are bridging onto our operations floor in twenty minutes. When Nia joins this bridge, she doesn't want guesses, she doesn't want apologies, and she doesn't want wiped hard drives."

She pointed to the anti-static evidence pouches on my desk.

I started the memory capture on Todd's workstation while Jared pulled the port list for the jump host. Nia joined the bridge at 2:52 and asked for the hashes before she asked for anything else. I read them off the capture log while the second capture was still running.

## What It Cost

By 4:30 the rain had eased to a mist over the Willamette. Jules signed the receiving line on Evidence Pouch `#EVD0007701-01` and slid the red binder into the CSIRT handoff rack.

The intrusion was contained, but not cleanly. To cut the attacker's path into the plant, we had isolated the Willamette River gateway, and Leah's crew ran the treatment line on manual override for the rest of the shift. She called at six to say they had held it, and that three operators were working a double because of it. She did not sound angry. She sounded tired, and she wanted to know when the gateway was coming back. It came back nine days later, after Jared rebuilt it.

## The After-Action Review

The review was the following Tuesday, with Nia on the bridge from Chicago and Jules, Jared, Leah, and me in the fourth-floor conference room. On the table were the timeline printout, the evidence log, Jared's rebuild ticket for the gateway, and a list of the indicators I had saved since December. <!-- date-ok: review day and back-reference to December indicators -->

Leah started before Nia did. "I found out my gateway was going dark from a phone call, not from a plan."

"There was no plan," Jules said. "That's on us, not on Ethan."

"Then whose is it?" Leah asked. Nobody answered quickly enough. Nia wrote *plant isolation playbook, owner TBD* at the top of the preparation list, and under it Owen's lobby camera, which was still on order.

Nia ran down the indicator list next. None of my saved hashes or domains from December or February had matched anything in this intrusion. "Keep saving them," she said. "Just don't expect them to be the thing that catches the next one." <!-- date-ok: back-reference to December and February incidents -->

Then she got to containment, and my name came up. I had isolated Todd's workstation before the second memory capture finished, because I saw it start enumerating shares and wanted it off the wire. The first capture was good. The second would have shown whether the attacker had moved a tool into memory after the first. We would never know.

"It was a defensible call," Nia said. "It was also a call that cost us evidence. Write down why you made it, and what you would need to see next time to wait sixty more seconds." I wrote it down. It went into the lessons-learned section with my name on it, next to the missing plant playbook.

## The Posting

The analyst opening on Harrowmere's security operations team posted the Monday after the review. It sat one floor up, in the same building.

I opened the application that night at the kitchen table and stared at the box that asked for a recent incident. I could have written about the indicators I had saved, or the binder, or the bridge with Chicago. I wrote about the second memory capture instead: what I had seen, why I had pulled the cable, and what I would need to see next time to wait sixty more seconds.

Then I read it again, cut the sentence where I explained that it had been a defensible call, and clicked submit.

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
The lab walks through the incident from this chapter step by step, with the answer shown, and then gives you one new problem that works the same way.
```
