# Portland Desk — The Port That Is Open

*A Security+ ports-and-protocols precursor • Hover over highlighted terms for exam definitions and supporting desk/network jargon.*

Rain hits the east-side windows like it has opinions. I am Ethan, week three at a midsize [[msp|MSP]], index cards in the top drawer — service on the front, number on the back. I can recite them in the shower. What I still cannot do is decide.

Jules sits two cubes over. Desk lead. Bike helmet on the monitor arm, rain pants drying on the chair. She keeps a sticky on her monitor that just says *which decision?* She does not do pep talks.

"Numbers are inventory," she says when I reach for a card. "Decisions are the job."

Tuesday is a normal queue. People keep bringing me habits they learned somewhere else — old shops, vendor docs, a home lab at 1 a.m. My job is to talk each habit into a decision that fits *here*.

## Jared and the script that still speaks Telnet

Jared from network ops pings before nine. Closet switch in Building C. A [[vlan|VLAN]] is wrong. He already has the steps on his clipboard from years of closet work.

"I Telnet in, type the [[enable_password|enable password]], fix the VLAN, hang up," he says. "Ten minutes. My script expects [[telnet|Telnet]]. Wrote it when I was still racking gear in Hillsboro."

I almost say *sure, twenty-three is open on that box*.

Jules leans on my cube wall. Coffee steam. "Ask him what we burned on last year."

Jared answers before I can. "Packet capture on the management span. Enable password in the clear, sitting there like a sticky note. Boss made us rotate everything. I still flinch."

"So which [[port|port]] do we allow on the management path," I say, "and which [[protocol|protocol]] carries that password? Telnet puts it in [[cleartext|cleartext]]."

He sighs. "You're going to say [[ssh|SSH]]. Same remote shell, encrypted, twenty-two. Fine. Script's mine — I can rewrite it. Don't make me do it twice."

"SSH with [[key_auth|key auth]] where we can get it," I say. "Then you only rewrite once. We fix the script, not the [[firewall|firewall]]."

Eleven minutes later he pastes a screenshot of an SSH login that works. In Slack he adds, almost proud: *keys feel weird after ten years of passwords, but whatever.* The clipboard loses a line. That is the whole point of the card — not the number alone, but the swap we agree on out loud.

## Maya and the mail client that trusts the hallway

Accounting next. Maya can receive mail on office Wi-Fi and fails at home. She is sure our server is broken.

I remote-view her settings with her on the phone. Inbound is [[pop3|POP3]] on 110 — download, delete, hope.

"That's how my first laptop did it in college," she says. "Grab mail, leave. My coworker keeps everything on the server with [[imap|IMAP]] on 143. I never knew why both still worked here."

"Both are cleartext," I tell her. "On a coffee-shop network, credentials and message bodies are readable. We want the secure versions. [[pop3s|POP3S]] on 995 if you insist on POP. Better for how you work: [[imaps|IMAPS]] on 993 — mailbox stays on the server, whole session under [[tls|TLS]]."

Outbound is pointed at [[smtp|SMTP]] on 25. Maya says that is "what IT set years ago, before I even started."

Jules murmurs from her cube, not looking up: "Twenty-five is how servers talk to servers. Clients submitting there is how we used to get yelled at by the ISP."

"Use [[smtp_submission|SMTP submission]] on 587 with [[starttls|STARTTLS]]," I say, slower this time. "Or [[smtps|SMTPS]] on 465 if the client wants [[implicit_tls|implicit TLS]] from the first byte. Authenticated submission. Not [[open_relay|open relay]] cosplay."

Maya laughs. "Say STARTTLS again and I'll click where you point. My brother runs a home Pi mail lab and would never let me live this down."

We change the profile together. Test message lands. Red banner dies. Cleartext mail is not a preference she has to live with — it is a setting we can replace.

## The vendor whose appliance has one door

Facilities vendor. Building controller config. Ticket text, cheerful: "Drop it on our [[ftp|FTP]] server."

I call instead of typing a lecture. Their engineer, Dana, sounds busy in a truck, radio chirping in the background.

"FTP is what the appliance docs still show," Dana says. "Twenty-one, username, done. I've done it that way on every install since the 2010s."

"Passwords and filenames ride cleartext on FTP," I say. "We can push over [[sftp|SFTP]]."

"Our box doesn't do SFTP. It does FTPS. Aren't those the same? My own lab NAS does SFTP and I always mix the letters up."

Jules's whiteboard sketch from last month is still in my head: two arrows, red marker, helmet strap looped around her wrist while she drew. She caught me calling them "secure FTP" like one animal.

"Not the same," I say. "[[sftp|SFTP]] is file transfer inside SSH — usually port twenty-two, a different protocol entirely. [[ftps|FTPS]] is classic FTP wrapped in TLS — often 990 for control and 989 for data in implicit mode. Different firewall story, different ports. If your appliance speaks FTPS, we do FTPS. We don't do plain FTP across the internet."

Dana exhales. "FTPS I can turn on. Got burned once when a firewall guy opened twenty-one and wondered why data hung — active mode, port twenty, whole mess. Where do you want me to land?"

"From a [[jump_host|jump host]] we control." Same goal — move a file safely. Talking the gotcha through keeps us from smearing the two names under schedule pressure.

## HR's padlock and the contractor in a hotel

HR pings after standup. Benefits portal still loads as [[http|HTTP]] on 80. People typing open-enrollment into a page with no padlock. Marketing meant to fix it after benefits season. Benefits season is now.

Web ops Slack is already half a meme about "we'll cert it after open enrollment." I open a [[change_ticket|change]]: terminate [[https|HTTPS]] on 443, redirect eighty to four-forty-three, renew the cert before Friday. HTTP is the cleartext twin. HTTPS is the one we keep. Someone drops a gif of a padlock. Desk humor.

While that cooks, a contractor — Sam — wants [[rdp|Remote Desktop]] from a Seattle hotel to a finance workstation on 3389. He is polite and late for a deliverable.

"I only need the desktop for an hour," Sam says. "Hotel Wi-Fi, my laptop, their machine. Port's [[tcp|TCP]] 3389, right? Last client just whitelisted my home IP and called it done."

I feel the flashcard reflex and almost draft a temporary allow.

Jules is already in the thread. "Read the request back as a decision, Ethan."

"Allow RDP from any to finance-WS-14 on 3389/TCP."

"Sam needs the desktop," Jules says. "He does not need a hotel network to have a straight line to finance. Our insurer's questionnaire asks whether 3389 faces the world — that's how [[ransomware|ransomware]] talks show up in renewals, not in movie plots. Talk him through the path we actually use."

I call Sam. "[[vpn|VPN]] first, into our pool. Then RDP only from there. Better: a [[jump_host|jump box]]. We don't open raw 3389 to the internet — not even for an hour. Same reason we don't hang [[smb|SMB]] on 445 outside the building. File shares stay inside; worms love that port and the insurance people know the number too."

Sam groans, then softens. "VPN I already have from the last gig. Jump box is fine if someone sends the name. Honestly nicer than hoping hotel Wi-Fi is friendly."

The [[firewall_rule|firewall rule]] we submit is narrow on purpose: source = VPN address group, destination = jump host, port = 3389, protocol = TCP, allow; everything else to that workstation on 3389 = deny.

Jules initials it. "That is what the port numbers are *for*."

## The new hire, the directory, and the quiet plumbing

Early afternoon. New hire in legal — Lena — cannot [[directory_bind|bind]] to the directory for a password-reset tool. The app is on [[ldap|LDAP]] on 389. It works on the wired desk VLAN and fails over [[guest_wifi|guest Wi-Fi]].

"I sat in the lobby because the desk wasn't ready," Lena says. "Now the reset tool hates me. At my last internship they just said 'use guest, it's fine.'"

"Guest isn't where we want directory binds with passwords in cleartext," I say. "We move the bind to [[ldaps|LDAPS]] on 636. TLS around the directory talk. Same queries, sealed path."

While we test, her laptop also fails [[kerberos|Kerberos]] to the [[domain|domain]] — tickets rejected. Clocks skewing. Fourteen minutes off after a long sleep.

Jules rolls by with a granola bar. "Home lab tip that became a desk tip: I once spent a Sunday convinced I'd broken Active Directory. Clock was wrong. Kerberos does not forgive."

I point Lena at our internal [[ntp|NTP]] on 123/[[udp|UDP]]. The clock jumps. Kerberos stops sulking.

She asks why the laptop "couldn't find the internet" until a reboot earlier. Classic desk noise under the directory work: [[dhcp|DHCP]] on 67/68 handed a [[dhcp_lease|lease]] that morning, [[dns|DNS]] on 53 resolves for everyone else, her adapter wedged. We renew the lease, flush the [[resolver_cache|resolver cache]], and send her back to onboarding. Not glamorous. Still a conversation — guest and cleartext directory do not share a room, and the quiet ports still matter.

## Monitoring, AAA, and the community everyone knows

Network monitoring opens a ticket that looks routine. Dee wants to poll access switches with [[snmp|SNMP]] using a [[community_string|community string]] of `public` — the default everyone knows — over 161/UDP, traps on 162.

"It's what the vendor template ships," Dee says. "We just need graphs before the weekend change window. I still have a Raspberry Pi at home that answers to `public`. Don't tell Jules."

"Jules already knows," Jules says from two cubes over, without turning around. "We can poll. Not with `public` in cleartext. Turn up [[snmpv3|SNMPv3]] with auth and privacy. Same ports if we keep the defaults. Different trust model. I found `public` on a customer's core once during an after-hours walkthrough — felt like finding the spare key under the mat."

Dee mutters about templates, then asks for the v3 checklist. Jules drops it in the channel without commentary.

Logging is the twin habit. Closets still forward [[syslog|syslog]] in cleartext to the collector on 514/UDP. A technician — Marco — asks to open 514 from the guest SSID so he can finish a closet without walking upstairs.

"For convenience," Marco says. "I used to debug printers that way at my last MSP. Guest, syslog, done."

"Convenience for you is cleartext logs on guest," I say. "Use [[syslog_tls|syslog over TLS]] on 6514/TCP. Jules already filed the long-term fix; this is the path that matches it."

He takes the upstairs walk. Grumpy. On the way he mutters that 6514 is "the one I always forget on flashcards." Same.

VPN and device-login questions stack on the same thread. Remote users hit the [[concentrator|concentrator]] through [[radius|RADIUS]] — 1812 for auth, 1813 for accounting. Network prefers [[tacacs|TACACS+]] on 49/TCP for switch and firewall admin sessions because it encrypts the full payload and splits [[authz|authz]] from authentication cleanly.

"People say [[aaa|AAA]] like it's one port," Jared drops into the thread, still riding his SSH win. "RADIUS for the VPN crowd, TACACS for us touching the boxes. I mixed them up for a year."

I do not configure either from the desk. I name the ports when someone asks. The work is naming the replacement while they are still on the line — templates, shortcuts, and the stories attached to them.

## TFTP and the printer that will not wait

Last real ping of the shift. Facilities tech — Owen — needs printer firmware. He wants [[tftp|TFTP]] from his laptop on the user VLAN. No auth. 69/UDP. Tiny and trusting.

"MAX leaves in twenty and the printer is dead," Owen says. "Just this once from here. I PXE-boot lab gear with TFTP at home all the time — it's fine if you know the room."

"Trusted VLAN only," I say. "Management segment, short window, then close it. TFTP does not cross a [[perimeter|perimeter]] and it does not live on the desk VLAN next to people browsing the web. Home lab room is a room. This floor is not."

Owen looks at the clock, then at me. "Staging switch still up? That's the one we used for the badge reader flash last month."

"Still up."

He moves. Firmware lands. Port closed. He still catches the MAX. In the ticket note he writes *staging only — Owen knows why now*, which is more honest than most of my notes from week one.

## Closing the queue

5:40. Queue down to noise. Index cards on the desk — Telnet beside SSH, HTTP beside HTTPS, FTP beside two answers that are not the same, POP and IMAP beside their TLS twins, LDAP beside LDAPS, SNMP beside v3, syslog beside 6514. The numbers have not changed since breakfast. The stories have.

Jules pauses at my cube, raincoat on, bike lights clipped to the strap.

"How many ports did you memorize today?"

"None," I say. "I collected a few war stories and made a few swaps."

She almost smiles. "Good. Keep the cards if they help you start. Throw them away when the person on the line already knows what they need — and you know what to replace."

I lock the drawer, badge-swipe into the rain, and walk toward the MAX. Portland is still raining. Tomorrow the queue fills again — and this time I know to ask which decision, not which number.
