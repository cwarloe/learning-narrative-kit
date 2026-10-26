# Portland Desk — The Port That Is Open

*A Security+ ports-and-protocols precursor • Hover over highlighted terms for exam definitions and supporting desk/network jargon.*

I was a year into my tenure at the Portland Operations Center—long past the rookie freeze of my first payroll outage, but still carrying the habit of checking twice before recommending a firewall change. In my top drawer sat my red-banded index cards for Security+: service names on the front, port numbers and transport protocols on the back. I knew the numbers by heart now, but when the queue started barking, holding the paper kept my hands from jumping.

It was my second overnight week on the rotation, and I was on days again only because Jules had moved me to cover a vacation. The flood had left a list of small debts: two closet switches still running on borrowed power supplies, and Jared's pooling change still waiting for a window.

Jules Brooks glanced over from her workstation, mug in hand. On the bezel of her primary monitor, her faded yellow sticky note asked *Which decision?* under the ceiling lights.

"You already know the numbers, Ethan," she said, catching me glancing toward the drawer. "The port numbers aren't what's slowing you down. It's knowing which habits to challenge."

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

"Port twenty-two, Jared. [[ssh|SSH]]."

He sighed, shaking his head. "Yeah, yeah. Encrypted remote shell. Script's mine, I'll update it. Just don't make me touch it twice."

"Configure [[key_auth|key auth]] and a privilege-fifteen account while you're in there," I added. "Then the script won't need an enable secret or a cleartext password."

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

I called instead of typing a lecture at them. Their engineer, Dale, sounded like she was in a truck, with a radio going somewhere behind her.

"FTP is what the appliance documentation still shows," Dale said. "Twenty-one, username, done. I've done it that way on every install since sometime in the 2010s."

"The password and the filenames both ride in the clear on FTP," I said. "We can push it over [[sftp|SFTP]] instead."

"Our box doesn't do SFTP, it does FTPS. Those are the same thing, aren't they? My NAS at home does SFTP and I mix the letters up constantly."

Everybody mixes the letters up. I'd done it in front of Jules a month earlier and she drew me two arrows in red marker, helmet strap still looped around her wrist.

"They're not the same," I said. "[[sftp|SFTP]] is file transfer running as a subsystem inside SSH, so it lives on port twenty-two. [[ftps|FTPS]] is FTP secured with TLS. While legacy appliances sometimes run implicit FTPS on port 990, standard explicit FTPS negotiates TLS right on standard port twenty-one using the AUTH TLS command. Different ports, different protocol handshakes. What we are not doing is unencrypted FTP across the perimeter."

Dale exhaled. "FTPS I can turn on. I got burned once when a firewall guy opened twenty-one and then couldn't work out why the data connection hung. Active mode, port twenty, whole mess. Where do you want me to land it?"

"On a jump host we control."

Before Dale's transfer finished, Leah Moreno from Portland plant operations called from the treatment facility down by the river. Leah ran plant ops with a steel clipboard and zero patience for corporate drift, and when plant operations called the desk, it was never about a jammed printer.

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

She pointed to the queue monitor above our heads. A facilities tech was asking for unauthenticated UDP TFTP on port 69 across the user VLAN, legal could not bind to cleartext TCP LDAP on 389 across the guest SSID, and network monitoring was asking to poll edge switches using cleartext UDP SNMP on 161 with a community string of `public`.



"Six tickets, six shortcuts," Jules said, her voice dropping into operational focus. "Sam wants RDP to the open street, and five other teams want to send credentials in cleartext. Map every legacy port to its encrypted replacement, configure the jump host rule, and submit the firewall change before someone punches an uninsurable hole in our edge."

I looked at the stack of port index cards on my desk. Memorizing port numbers was easy; the hard part was standing between busy people and bad habits. I needed to build the protocol defense matrix, lock down the open sockets, and prove the secure paths before someone punched a hole in our firewall.

## The Other Half

I called Sam back. "VPN first, then remote into a jump host. We don't open 3389 to the internet, not even for an hour." He grumbled and then admitted the jump box was nicer than trusting hotel Wi-Fi. The firewall rule was narrow on purpose: VPN pool to one hardened host on 3389, nothing else.

The rest of the queue got the secure twin of whatever it had asked for. The legal tool moved from LDAP on 389 to LDAPS on 636. Dale's appliance moved from FTP to SFTP. SNMP `public` polling was replaced with SNMPv3.

Jared did not argue once he watched his own password scroll past in the capture, but he did not thank me either. Six of his older switches could not run SSH without a firmware upgrade, so we wrapped them in a management VLAN behind a jump host instead of fixing them. It was a patch, and we both knew it.

"The script's going to break the first time the jump host reboots," he said. "When it does, you're the one I'm calling."

It broke on a Saturday two weeks later, on my overnight-into-morning shift. A Gresham closet switch stopped answering, and I needed Jared to tell me which uplink fed the label printers. He took four hours to answer. In the second hour, I guessed, shut the wrong port, and dropped the Gresham pack station for thirty-five minutes while Ken's weekend crew stood around. When Jared finally called in, he traced the right port in five minutes from his kitchen.

"You should've called the on-call line instead of texting me," he said. "I'd have picked up."

"I didn't think you would."

He was quiet for a second. "Fair. Call anyway." After that, he answered my tickets the same day.

## Practice It in the Lab

```bridge-card
title: Portland Desk Lab: Protocol Triage, Port Hardening, & Perimeter Defense
target: workbench/07-the-port-that-is-open.md
domain: CompTIA Security+ SY0-701 • Domain 1.4 & 2.5
badge: The Hands-On Lab
---
The lab walks through the incident from this chapter step by step, with the answer shown, and then gives you one new problem that works the same way.
```
