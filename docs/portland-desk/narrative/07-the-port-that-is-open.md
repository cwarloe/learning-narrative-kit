# Portland Desk — The Port That Is Open

*A Security+ ports-and-protocols precursor • Hover over highlighted terms for exam definitions and supporting desk/network jargon.*

It had been raining on the east side of the building since before I got in. I was three weeks into a job at a midsize MSP — long enough to say "let me look into that" more often than anyone wanted to hear. I kept index cards in the top drawer, service on the front and port number on the back, and I'd been through them enough times to run the whole stack in the shower. Nobody ever asked me to.

Jules worked two cubes over and had the desk lead title. Nine years there. A bike helmet hung off her monitor arm, rain pants dried over the back of her chair, and a note stuck to the edge of her screen said just *which decision?*

The first ticket came in and I reached for the cards, and she caught me at it.

"You already know the numbers," she said. "So that's not the part that's slowing you down."

It was an ordinary Tuesday queue. All day it was people carrying habits from somewhere else — an old shop, vendor documentation, a home lab at one in the morning — and most of my job was talking those habits into something that worked here.

## Jared and the script that still speaks Telnet

```callout-panel
title: "FIGURE 7.1: NETWORK PERIMETER & PORT SCAN VECTOR"
badge: "Perimeter Architecture"
caption: "Schematic layout: The corporate perimeter firewall. Cleartext Telnet (Port 23) and unencrypted HTTP (Port 80) bypass encrypted tunnels, exposing credentials on the wire."
prompt: "Clean technical schematic of a corporate network perimeter under bright, even lighting. Flowchart lines connect external internet router to internal firewall and server racks with port numbers highlighted in green and red. Crisp technical line art, no text, no words. 16:9 ratio."
```

Jared from network ops pinged me before nine. A switch in a closet in Building C had a VLAN set wrong, and he already had the steps on a clipboard from years of doing exactly this.

"I Telnet in, type the [[enable_password|enable password]], fix the VLAN, hang up," he said. "Ten minutes. My script expects [[telnet|Telnet]]. I wrote it back when I was still racking gear out in Hillsboro."

I was most of the way to saying *sure, twenty-three is open on that box* when Jules leaned on my cube wall with her coffee.

"Ask him what we burned on last year."

Jared answered before I could get the question out. "Packet capture on the management span. The enable password sitting there in the clear where anybody walking past the collector could read it. The boss made us rotate everything that week. I still flinch."

"So which port do we allow on the management path," I said, "and which protocol is carrying that password? Telnet sends it in [[cleartext|cleartext]]."

He sighed at me. "You're going to say [[ssh|SSH]]. Same remote shell, encrypted, twenty-two. Fine. The script's mine, I can rewrite it. Just don't make me do it twice."

"Then let's put [[key_auth|key auth]] on it now instead of passwords," I said. "You rewrite once. And we're fixing the script, not the firewall."

Eleven minutes later he pasted a screenshot of a working SSH login and added, sounding almost proud, that keys felt weird after ten years of passwords but whatever. His clipboard was one line shorter.

## Maya and the mail client that trusts the hallway

Accounting next. Maya could get her mail on the office Wi-Fi and it failed at home, and she had decided the server was broken.

I remoted into her settings while she was on the phone. Her inbound was [[pop3|POP3]] on 110, which downloads, deletes, and hopes.

"That's how my first laptop did it in college," she said. "Grab the mail and go. My coworker keeps everything on the server with [[imap|IMAP]] on 143 and I never understood why both of them still worked here."

"They both still work, and they're both cleartext," I told her. "On a coffee shop network, somebody else on that Wi-Fi can read your credentials and the body of your mail. There are secure versions of both. [[pop3s|POP3S]] on 995 if you're attached to POP. For the way you actually work, [[imaps|IMAPS]] on 993 — mailbox stays on the server, whole session inside [[tls|TLS]]."

Her outbound was pointed at [[smtp|SMTP]] on 25, which she told me IT had set years ago, before she even started.

Jules, from her cube, not looking away from whatever she was doing: "Twenty-five is how servers talk to each other. Back when clients used to submit there, we got yelled at by the ISP about once a quarter."

"So we'll use [[smtp_submission|submission]] on 587 with [[starttls|STARTTLS]]," I said, slower this time, because Maya was writing it down. "Or [[smtps|SMTPS]] on 465 if the client wants [[implicit_tls|implicit TLS]] from the first byte. Either way it's authenticated submission, and neither one of them is an open relay."

Maya laughed at me. "Say STARTTLS one more time and I'll click wherever you point. My brother runs a mail server on a Raspberry Pi and he is never going to hear about this."

We changed the profile together, sent a test message, and the red banner went away.

## The vendor whose appliance has one door

The facilities vendor needed a building controller config sent over, and the ticket said, cheerfully, to drop it on their [[ftp|FTP]] server.

I called instead of typing a lecture at them. Their engineer, Dana, sounded like she was in a truck, with a radio going somewhere behind her.

"FTP is what the appliance documentation still shows," Dana said. "Twenty-one, username, done. I've done it that way on every install since sometime in the 2010s."

"The password and the filenames both ride in the clear on FTP," I said. "We can push it over [[sftp|SFTP]] instead."

"Our box doesn't do SFTP, it does FTPS. Those are the same thing, aren't they? My NAS at home does SFTP and I mix the letters up constantly."

Everybody mixes the letters up. I'd done it in front of Jules a month earlier and she drew me two arrows in red marker, helmet strap still looped around her wrist.

"They're not the same," I said. "SFTP is file transfer running inside SSH, so it's usually port twenty-two, and it's a different protocol underneath. [[ftps|FTPS]] is the old FTP wrapped in TLS, which in implicit mode is often 990 for the control connection and 989 for data. Different ports, different firewall conversation. If your appliance speaks FTPS then we'll do FTPS. What we're not doing is plain FTP across the internet."

Dana exhaled. "FTPS I can turn on. I got burned once when a firewall guy opened twenty-one and then couldn't work out why the data connection hung. Active mode, port twenty, whole mess. Where do you want me to land it?"

"On a jump host we control."

Before Dana's transfer finished, Leah Moreno from Portland plant operations called from the treatment facility down by the river. Leah ran plant ops with a steel clipboard and zero patience for corporate drift, and when plant operations called the desk, it was never about a jammed printer.

"Ethan," Leah said, industrial pumps humming through the handset. "Our telemetry gateway stopped feeding sensor metrics to the central plant board. A field contractor wants an emergency firewall rule opening Modbus and DNP3 across the inter-site WAN so the overflow alarms stop chirping. Can you just punch the ports through?"

I checked the protocol notes before answering. Port 502 for Modbus, 20000 for DNP3 — classic cleartext industrial protocols built for isolated control loops, not an open WAN span.

"Those protocols have no encryption on the wire, Leah," I said. "If someone intercepts that WAN traffic, they aren't just reading tank levels — they could inject a malicious valve command."

Jules leaned back from her monitor, listening with her coffee mug in hand. "Leah knows her plant," Jules murmured. "Give her the architecture, not just a no."

"We can't open raw cleartext across the perimeter," I told Leah. "What we can do is drop the telemetry into an encrypted VPN tunnel between the plant gateway and our concentrator. Plant ops gets the telemetry stream, and nobody outside touches the pumps."

Leah paused, the phone clicking as she made a sharp notation on her clipboard. "If the tunnel keeps the overflow alarms quiet without putting the treatment line at risk, build it. I'll hold the contractor at the gate."

I routed the request to network engineering, marked it operational priority, and Jules gave me a quick nod before turning back to her queue.

## HR's padlock and the contractor in a hotel

HR pinged right after standup. The benefits portal still loaded over HTTP on 80, which meant people were typing open-enrollment information into a page with no padlock. Marketing had meant to fix it after benefits season. Benefits season was now.

The web ops channel was already half memes about certing it after open enrollment. I opened a change ticket to terminate HTTPS on 443, redirect eighty to four-forty-three, and get the certificate renewed before Friday. Somebody dropped in a gif of a padlock.

## The hotel room and the open perimeter

While that worked its way through, a contractor named Sam wanted Remote Desktop from a hotel in Seattle to a finance workstation. He was polite about it, and late on a deliverable.

"I only need the desktop for an hour," Sam said over the phone line. "Hotel Wi-Fi, my laptop, their machine. It's TCP 3389, right? My last client just whitelisted my hotel IP on the edge firewall and called it done."

I caught myself reaching for the firewall change template, starting to draft a temporary thirty-day port forward.

Jules reached over and tapped the edge of my monitor with her pen. "Read that request back to yourself as a decision, Ethan."

"Allow inbound RDP from an unauthenticated public IP to finance-WS-14 on port 3389," I said, feeling the weight of the words.

"Right. Now read the second half of it out loud," Jules said, her voice quiet and direct. "Our cyber insurance renewal questionnaire asks whether port 3389 faces the public internet. That is a policy termination conversation, not a movie plot. Automated ransomware scripts scan that port every second of every day. And Sam is not the only ticket on the board right now."

She pointed to the queue monitor above our heads. A facilities tech was asking for unauthenticated TFTP across the user VLAN, legal could not bind to LDAP across the guest SSID, and network monitoring was asking to poll edge switches using cleartext SNMP with a community string of `public`.

"You have six different teams asking for convenience shortcuts, and automated port scanners probing our perimeter from the outside right now," Jules said, crossing her arms. "How do you lock down the perimeter, map every insecure legacy protocol to its hardened enterprise replacement, configure the jump host access rules, and draft the Tier 1 Security Escalation before the change window closes? Call your shot, Ethan."

I looked at the stack of port index cards on my desk. Memorizing port numbers was easy; the hard part was standing between busy people and bad habits. I needed to build the protocol defense matrix, lock down the open sockets, and prove the secure paths before someone punched a hole in our firewall.

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: Protocol Triage, Port Hardening, & Perimeter Defense
target: workbench/07-the-port-that-is-open.md
domain: CompTIA Security+ SY0-701 • Domain 1.4 & 2.5
badge: The Hands-On Lab
---
Take over Ethan's workstation. Triage cleartext Telnet, FTP, and HTTP traffic in packet capture drills, map insecure legacy services to encrypted replacements (SSH, SFTP, FTPS, LDAPS, SNMPv3), design the jump host firewall rule, and draft the Tier 1 Security Escalation Dossier.
```
