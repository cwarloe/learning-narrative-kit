# Portland Desk — The Port That Is Open

*A Security+ ports-and-protocols precursor • Hover over highlighted terms for exam definitions and supporting desk/network jargon.*

I keep a stack of index cards in the top drawer of my help-desk cube in Portland — a midsize [[msp|MSP]] on the east side where the coffee tastes like burnt paper and the ticket queue never empties. On the front of each card: a service name. On the back: a number and a one-line note. Twenty-two. Twenty-three. Four-forty-three. I can recite them in the shower. What I still cannot do is decide.

Jules sits two cubes over. Desk lead. Bike helmet hanging off the monitor arm, rain pants still drying on the chair back. She has the patience of someone who has already made every mistake I am about to make, and she will not let me hide behind memorization.

"Numbers are inventory," she tells me on my second week, clipping her pannier shut like the point is already decided. "Decisions are the job."

Tuesday starts with rain on the windows and fourteen open tickets. By lunch I use every card in that drawer — not as trivia, but as a reason to say yes, no, or replace.

## Ticket 4187 — The switch that still speaks Telnet

Jared from network ops pings me before nine. He needs console access to a closet switch in Building C. The old habit is still on his clipboard: open [[telnet|Telnet]] to the management address, type the [[enable_password|enable password]], fix the [[vlan|VLAN]], hang up.

I almost type the answer from a flashcard. Port twenty-three. Cleartext. Bad. Done.

Jules leans into my cube before I hit send, coffee steam fogging her glasses for half a second. "What are you actually deciding?"

"That Telnet is insecure?"

"You're deciding which [[port|port]] we allow on the management VLAN, and which [[protocol|protocol]] carries the password. Recite the replacement."

I swallow. "We stop Telnet. We move the switch to [[ssh|SSH]]. Same remote shell job, encrypted session, port twenty-two."

She nods once. "And when Jared says his script only speaks Telnet?"

"Then we fix the script, not the [[firewall|firewall]]."

I write the ticket note carefully: deny Telnet on the management path; require SSH with [[key_auth|key auth]] where we can get it. Jared grumbles, then sends a screenshot of an SSH login that works. The enable password no longer rides the wire in [[cleartext|cleartext]]. That is the whole point of the card — not the number alone, but the swap.

## Ticket 4192 — Mail that still trusts the hallway

Accounting calls next. Maya's laptop can receive mail on the office Wi-Fi but fails at home, and she is convinced our server is broken. I remote-view her client settings and feel the flashcards rearrange themselves into a picture.

Inbound is set to [[pop3|POP3]] on port 110 — download, delete, hope. Another of her coworkers uses [[imap|IMAP]] on 143 so folders stay on the server. Both paths are cleartext. Anyone on a coffee-shop network can watch credentials and message bodies drift past.

"We need the secure versions," I tell her, walking her through the change. "[[pop3s|POP3S]] on 995 if you insist on POP. Better: [[imaps|IMAPS]] on 993 so the mailbox stays on the server and the whole session rides [[tls|TLS]]."

Outbound is worse. Her client is pointed at [[smtp|SMTP]] on port 25 — the old server-to-server relay port, the one ISPs throttle and attackers abuse. I almost say "SMTP is twenty-five" like a quiz answer. Jules's voice is already in my head: *which decision?*

"Clients shouldn't submit on twenty-five," I say aloud. "Use [[smtp_submission|SMTP submission]] on 587 with [[starttls|STARTTLS]], or [[smtps|SMTPS]] on 465 if the client wants TLS from the first byte. Authenticated submission. Not [[open_relay|open relay]] cosplay."

Maya updates the profile, sends a test to herself, and the red banner in Outlook finally goes away. I close the ticket with a one-liner for the knowledge base: cleartext mail ports are not a preference; they are a leak.

## Ticket 4199 — A vendor who asks for FTP

Midmorning, a facilities vendor needs a building controller config. Their ticket says, cheerfully, "Just drop it on our [[ftp|FTP]] server."

I know the numbers — twenty-one for control, twenty for active data — and I know they mean passwords and file names in cleartext again. I draft a polite refusal and an offer: we can push over [[sftp|SFTP]].

The vendor's reply bounces back in under a minute. "Our appliance only does FTPS, not SFTP. Aren't they the same?"

I start to type *yes* because both sound like "secure FTP," then stop. Jules drew this distinction on the whiteboard last month with a red marker, helmet strap still looped around her wrist like she might leave mid-sentence for a ride home.

"They are not the same," I write. "[[sftp|SFTP]] is file transfer inside SSH — usually port twenty-two, a different protocol entirely, not FTP with a lock sticker. [[ftps|FTPS]] is classic FTP wrapped in TLS — often 990 for control and 989 for data in [[implicit_tls|implicit mode]]. If your box speaks FTPS, we can do FTPS. We will not do plain FTP across the internet."

We land on FTPS from a [[jump_host|jump host]] we control. I log the distinction in the ticket so the next person on the desk will not smear the two together under exam pressure or vendor pressure. Same goal — move a file safely. Different protocol, different ports, different firewall story.

## Ticket 4204 — The intranet page and the open desktop

After standup, HR pings: the benefits portal on the internal web still loads as [[http|HTTP]] on port 80. People are typing open-enrollment details into a page with no padlock. Marketing "meant to fix it after benefits season." Benefits season is now.

I open a [[change_ticket|change]] with web ops: terminate [[https|HTTPS]] on 443, redirect eighty to four-forty-three, renew the cert before Friday. No lecture — just the operational fact that HTTP is the cleartext twin and HTTPS is the one we are allowed to keep.

While that change cooks, another ticket lands from a contractor who wants [[rdp|Remote Desktop]] from a hotel in Seattle straight to a finance workstation on 3389. I feel the flashcard reflex — *RDP, thirty-three eighty-nine, TCP* — and almost approve a temporary allow.

Jules intercepts the draft firewall request on the shared board, rolling her chair over without unclipping from whatever Slack thread she was mid-sentence in.

"Read it back as a decision," she says.

"Allow RDP from any to finance-WS-14 on 3389/[[tcp|TCP]]."

"That's an invitation," she says. "Modern RDP can encrypt the session and still be a [[ransomware|ransomware]] front door if it faces the world. [[vpn|VPN]] first. Then RDP only from the VPN pool. Better: [[jump_host|jump box]]. Never raw 3389 to the internet."

I rewrite the request. The [[firewall_rule|firewall rule]] we finally submit is narrow on purpose: source = VPN address group, destination = jump host, port = 3389, protocol = TCP, action = allow; everything else to that workstation on 3389 = deny. Adjacent rules in the same change close the old mistakes people keep asking for — no [[smb|SMB]] on 445 from outside the building (file shares stay inside; worms love that port), no gratuitous anything "just for this week."

Jules initials the change. "That," she says, "is what the port numbers are *for*."

## Ticket 4211 — Password reset that will not ticket

Early afternoon, a new hire in legal cannot [[directory_bind|bind]] to the directory for a password reset tool. The app is configured for [[ldap|LDAP]] on 389. It works on the wired desk VLAN and fails over [[guest_wifi|guest Wi-Fi]] in ways that make no sense until I open the packet story: directory binds with passwords in cleartext, and our guest network is not a place we want that conversation.

"Move the bind to [[ldaps|LDAPS]] on 636," I tell the app owner. "TLS around the directory talk. Same queries, sealed path."

While we test, the new hire's laptop also keeps failing [[kerberos|Kerberos]] authentication to the [[domain|domain]] — tickets rejected, clocks skewing. Help desk ambient reality: her machine has drifted fourteen minutes off because it never got a clean time sync after a long sleep. I point it at our internal [[ntp|NTP]] servers on 123/[[udp|UDP]], watch the clock jump, and Kerberos stops sulking. Time is not a nice-to-have when tickets are time-limited.

On the same call she asks why her laptop "couldn't find the internet" until she rebooted. Classic desk noise: [[dhcp|DHCP]] on 67/68 handed her a [[dhcp_lease|lease]] that morning, [[dns|DNS]] on 53 is resolving names for everyone else, and her adapter has simply wedged. I renew the lease, flush the [[resolver_cache|resolver cache]], and send her back to onboarding. Not glamorous. The ports still matter — they are the quiet plumbing under every flashier ticket.

## Ticket 4220 — Monitoring, printers, and the end of the shift

Network monitoring opens the last real ticket of the day. They want to poll a stack of access switches with [[snmp|SNMP]] using a [[community_string|community string]] of `public` — the default everyone knows — over 161/UDP, traps on 162. I can see the cleartext community riding every poll.

"We can poll," I say, "but not like that. Turn up [[snmpv3|SNMPv3]] with auth and privacy. Same ports if we keep the defaults, different trust model. No more community strings as passwords shouted down the hallway."

Logging is the twin problem. Several closets still forward [[syslog|syslog]] in cleartext to the collector on 514/UDP. Jules already filed the long-term fix; I just have to stop a technician from opening 514 from the guest SSID "for convenience." We steer him to [[syslog_tls|syslog over TLS]] on 6514/TCP so the log stream itself is not another cleartext gossip channel.

VPN and network-device login questions stack on the same ticket thread. Remote users hitting the [[concentrator|concentrator]] authenticate through [[radius|RADIUS]] — 1812 for auth, 1813 for accounting — while the network team prefers [[tacacs|TACACS+]] on 49/TCP for switch and firewall administrator sessions because it encrypts the full payload and splits [[authz|authz]] from authentication cleanly. I do not need to configure either from the desk; I need to know which ports the firewall change should name when someone asks for "[[aaa|AAA]] access" as if that were one number.

Last ping of the shift: a facilities tech wants to push printer firmware with [[tftp|TFTP]] from his laptop on the user VLAN. No auth, 69/UDP, tiny and trusting. I almost let him "just this once." Then I picture the cover test Jules uses on my prose and on my changes alike — if you strip the excuses, what remains?

"Trusted VLAN only," I say. "Management segment, short window, then close it. TFTP does not cross a [[perimeter|perimeter]] and it does not live on the desk VLAN next to people browsing the web."

He moves to the staging switch we keep for that purpose. Firmware lands. Port closed.

## Closing the queue

At 5:40 the queue is down to noise. I pull the index cards out of the drawer and spread them on the desk — Telnet beside SSH, HTTP beside HTTPS, FTP beside the two different answers that are not the same, POP and IMAP beside their TLS twins, LDAP beside LDAPS, SNMP beside v3, syslog beside 6514. The numbers have not changed since breakfast. What has changed is the shape of the question.

Jules pauses at my cube on her way out, raincoat already on, bike lights clipped to the strap.

"How many ports did you memorize today?"

"None," I say. "I decided a few."

She almost smiles. "Good. Keep the cards if they help you start. Throw them away when the ticket already knows what to ask."

I lock the drawer, badge-swipe into the rain, and walk toward the MAX. Portland is still raining. The cards are still in the drawer. Tomorrow the queue fills again — and this time I know to ask which decision, not which number.
