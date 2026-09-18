# Portland Desk — The Port That Is Open

*A Security+ ports-and-protocols precursor • Hover over highlighted terms for exam definitions and supporting desk/network jargon.*

It has been raining on the east side of the building since before I got in. I'm three weeks into a job at a midsize [[msp|MSP]], which so far mostly means I say "let me look into that" more often than anyone wants to hear. I keep index cards in the top drawer, service on the front and port number on the back, and I've been through them enough times that I could run the whole stack in the shower. Nobody has ever asked me to do that.

Jules works two cubes over and has the desk lead title. Nine years here. There's a bike helmet hanging off her monitor arm and a pair of rain pants drying over the back of her chair, and she's stuck a note on the edge of her screen that just says *which decision?*

The first ticket comes in and I reach for the cards, and she catches me at it.

"You already know the numbers," she says. "So that's not the part that's slowing you down."

It's an ordinary Tuesday queue. What comes in all day is people carrying habits they picked up somewhere else, at an old shop or out of vendor documentation or in a home lab at one in the morning, and most of my job turns out to be talking those habits into something that works here.

## Jared and the script that still speaks Telnet

Jared from network ops pings me before nine. There's a switch in a closet in Building C with a [[vlan|VLAN]] set wrong, and he already has the steps written on a clipboard from years of doing exactly this.

"I Telnet in, type the [[enable_password|enable password]], fix the VLAN, hang up," he says. "Ten minutes. My script expects [[telnet|Telnet]]. I wrote it back when I was still racking gear out in Hillsboro."

I'm most of the way to saying *sure, twenty-three is open on that box* when Jules leans on my cube wall with her coffee.

"Ask him what we burned on last year."

Jared answers before I can get the question out. "Packet capture on the management span. The enable password sitting there in the clear where anybody walking past the collector could read it. The boss made us rotate everything that week. I still flinch."

"So which [[port|port]] do we allow on the management path," I say, "and which [[protocol|protocol]] is carrying that password? Telnet sends it in [[cleartext|cleartext]]."

He sighs at me. "You're going to say [[ssh|SSH]]. Same remote shell, encrypted, twenty-two. Fine. The script's mine, I can rewrite it. Just don't make me do it twice."

"Then let's put [[key_auth|key auth]] on it now instead of passwords," I say. "You rewrite once. And we're fixing the script, not the [[firewall|firewall]]."

Eleven minutes later he pastes a screenshot of a working SSH login and adds, sounding almost proud about it, that keys feel weird after ten years of passwords but whatever. His clipboard is one line shorter than it was.

## Maya and the mail client that trusts the hallway

Accounting next. Maya can get her mail on the office Wi-Fi and it fails at home, and she has decided the server is broken.

I remote into her settings while she's on the phone. Her inbound is [[pop3|POP3]] on 110, which downloads, deletes, and hopes.

"That's how my first laptop did it in college," she says. "Grab the mail and go. My coworker keeps everything on the server with [[imap|IMAP]] on 143 and I never understood why both of them still worked here."

"They both still work, and they're both cleartext," I tell her. "On a coffee shop network, somebody else on that Wi-Fi can read your credentials and the body of your mail. There are secure versions of both. [[pop3s|POP3S]] on 995 if you're attached to POP. For the way you actually work I'd rather put you on [[imaps|IMAPS]] on 993, where the mailbox stays on the server and the whole session sits inside [[tls|TLS]]."

Her outbound is pointed at [[smtp|SMTP]] on 25, which she tells me is what IT set years ago, before she even started.

Jules, from her cube, not looking away from whatever she's doing: "Twenty-five is how servers talk to each other. Back when clients used to submit there, we got yelled at by the ISP about once a quarter."

"So we'll use [[smtp_submission|submission]] on 587 with [[starttls|STARTTLS]]," I say, slower this time, because Maya is writing it down. "Or [[smtps|SMTPS]] on 465 if the client wants [[implicit_tls|implicit TLS]] from the first byte. Either way it's authenticated submission, and neither one of them is an [[open_relay|open relay]]."

Maya laughs at me. "Say STARTTLS one more time and I'll click wherever you point. My brother runs a mail server on a Raspberry Pi and he is never going to hear about this."

We change the profile together and send a test message, and the red banner in her client goes away.

## The vendor whose appliance has one door

The facilities vendor needs to get a building controller config over to us, and the ticket says, cheerfully, to drop it on their [[ftp|FTP]] server.

I call instead of typing a lecture at them. Their engineer is named Dana and sounds like she's in a truck, with a radio going in the background.

"FTP is what the appliance documentation still shows," Dana says. "Twenty-one, username, done. I've done it that way on every install since sometime in the 2010s."

"The password and the filenames both ride in the clear on FTP," I say. "We can push it over [[sftp|SFTP]] instead."

"Our box doesn't do SFTP, it does FTPS. Those are the same thing, aren't they? My NAS at home does SFTP and I mix the letters up constantly."

Everybody mixes the letters up. I did it in front of Jules a month ago and she drew me two arrows on the whiteboard in red marker with her helmet strap still looped around her wrist.

"They're not the same," I say. "[[sftp|SFTP]] is file transfer running inside SSH, so it's usually port twenty-two, and it's a different protocol underneath. [[ftps|FTPS]] is the old FTP wrapped in TLS, which in implicit mode is often 990 for the control connection and 989 for data. Different ports, different firewall conversation. If your appliance speaks FTPS then we'll do FTPS. What we're not doing is plain FTP across the internet."

Dana exhales. "FTPS I can turn on. I got burned once when a firewall guy opened twenty-one and then couldn't work out why the data connection hung. Active mode, port twenty, whole mess. Where do you want me to land it?"

"On a [[jump_host|jump host]] we control."

## HR's padlock and the contractor in a hotel

HR pings right after standup. The benefits portal still loads over [[http|HTTP]] on 80, which means people have been typing open-enrollment information into a page with no padlock on it. Marketing meant to fix it after benefits season. Benefits season is now.

The web ops channel is already half memes about certing it after open enrollment. I open a [[change_ticket|change ticket]] to terminate [[https|HTTPS]] on 443, redirect eighty to four-forty-three, and get the certificate renewed before Friday. Somebody drops in a gif of a padlock.

While that's working its way through, a contractor named Sam wants [[rdp|Remote Desktop]] from a hotel in Seattle to a finance workstation. He's polite about it and he's late on a deliverable.

"I only need the desktop for an hour," Sam says. "Hotel Wi-Fi, my laptop, their machine. It's [[tcp|TCP]] 3389, right? My last client just whitelisted my home address and called it done."

I catch myself starting to draft a temporary allow rule.

Jules is already in the thread. "Read that request back to yourself as a decision."

"Allow RDP from anywhere to finance-WS-14 on 3389."

"Right. Now read the second half of it out loud," she says. "Our insurance questionnaire asks whether 3389 faces the internet. That's a renewal conversation, not a movie plot. [[ransomware|Ransomware]] crews scan that port all day long."

I call Sam back. "We'll get you onto the [[vpn|VPN]] first, into our pool, and you'll RDP from in there. Better than that, we'll point you at a [[jump_host|jump box]]. We don't open raw 3389 to the internet, not even for an hour, for the same reason we don't hang [[smb|SMB]] on 445 off the outside of the building."

Sam groans, then gives in. "I've already got the VPN from the last gig. Jump box is fine if somebody sends me the name. It's honestly nicer than hoping the hotel Wi-Fi is friendly."

The [[firewall_rule|firewall rule]] we submit is narrow on purpose. Source is the VPN address group, destination is the jump host, port 3389, TCP, allow. Everything else reaching that workstation on 3389 gets denied. Jules initials it on her way past.

## The new hire, the directory, and the quiet plumbing

Early afternoon. A new hire in legal named Lena can't [[directory_bind|bind]] to the directory from the password reset tool. The app talks [[ldap|LDAP]] on 389, it works from the wired desk VLAN, and it fails on [[guest_wifi|guest Wi-Fi]].

"I've been sitting in the lobby because my desk wasn't ready," Lena says. "And now the reset tool hates me. At my last internship everybody just said use guest, it's fine."

"Guest is exactly where we don't want a directory bind crossing in cleartext," I say. "We'll move it to [[ldaps|LDAPS]] on 636. Same queries, TLS around them."

While we're testing that, her laptop starts failing [[kerberos|Kerberos]] to the [[domain|domain]] as well, tickets coming back rejected. Her clock is fourteen minutes off after a long sleep.

Jules goes past with a granola bar. "I spent an entire Sunday once convinced I'd broken Active Directory in my home lab. It was the clock. Kerberos does not forgive you about the clock."

I point Lena at our internal [[ntp|NTP]] on 123/[[udp|UDP]], her clock jumps, and Kerberos stops sulking.

She asks why the laptop couldn't find the internet at all until she rebooted earlier, which turns out to be ordinary desk noise sitting underneath the directory problem. [[dhcp|DHCP]] on 67 and 68 handed her a [[dhcp_lease|lease]] that morning, [[dns|DNS]] on 53 is resolving fine for everybody else, and her adapter had simply wedged. We renew the lease, flush the [[resolver_cache|resolver cache]], and send her back to onboarding.

## Monitoring, AAA, and the community string everybody knows

Network monitoring opens a ticket that looks routine on its face. Dee wants to poll the access switches with [[snmp|SNMP]] on 161/UDP, traps on 162, using a [[community_string|community string]] of `public`.

"It's what the vendor template ships with," Dee says. "We just need graphs before the weekend change window. I've got a Raspberry Pi at home that still answers to `public`. Don't tell Jules."

"Jules already knows," Jules says, two cubes over, still typing.

Dee puts her forehead down on her desk.

"We can poll," Jules says. "We're not doing it with `public` in the clear. Turn up [[snmpv3|SNMPv3]] with authentication and privacy. Same ports if we leave the defaults alone, completely different trust model. I found `public` on a customer's core switch during an after-hours walkthrough once. It was like finding the spare key under the mat."

Dee mutters something about templates, then asks for the v3 checklist, and Jules drops it into the channel without saying anything else about it.

Logging has the same habit attached to it. The closets are still forwarding [[syslog|syslog]] in cleartext to the collector on 514/UDP, and a technician named Marco wants 514 opened from the guest SSID so he can finish a closet without walking upstairs.

"It's just for convenience," Marco says. "I used to debug printers that way at my last MSP."

"Convenience for you is cleartext logs riding the guest network," I say. "Use [[syslog_tls|syslog over TLS]] on 6514/TCP. Jules already filed the long-term fix and this matches it."

He takes the walk upstairs, grumbling, and mentions on the way that 6514 is the one he always forgets on flashcards. Same.

VPN and device login questions pile onto the same thread. Remote users authenticate to the [[concentrator|concentrator]] through [[radius|RADIUS]], 1812 for authentication and 1813 for accounting, and the network team would rather use [[tacacs|TACACS+]] on 49/TCP for switch and firewall admin sessions, because it encrypts the whole payload and splits [[authz|authorization]] cleanly away from authentication.

"People say [[aaa|AAA]] like it's one port," Jared says, dropping into the thread still riding his SSH win. "RADIUS for the VPN crowd, TACACS for those of us touching the boxes. I had them mixed up for about a year."

I don't configure either one from the desk. I name the ports when somebody asks.

## TFTP and the printer that will not wait

The last real ping of the shift is a facilities tech named Owen, who needs to get firmware onto a printer and wants to do it with [[tftp|TFTP]] from his laptop on the user VLAN. No authentication, 69/UDP, tiny and trusting.

"The MAX leaves in twenty minutes and the printer is dead," Owen says. "Just this once from here. I PXE boot lab gear with TFTP at home all the time, it's fine if you know the room."

"Management segment only," I say. "Short window, and then we close it. TFTP doesn't cross a [[perimeter|perimeter]] and it doesn't belong on the desk VLAN next to people browsing the web. Your home lab is one room you know everything about. This floor isn't."

Owen looks at the clock, then at me. "Is the staging switch still up? The one we used for the badge reader flash last month?"

"Still up."

He moves fast. The firmware lands and I close the port behind him. He makes his train. In the ticket note he writes *staging only, Owen knows why now*, which is more honest than most of the notes I wrote in week one.

## Closing the queue

By 5:40 the queue is down to noise. The index cards are still out on my desk, and I notice I've been pairing them off all afternoon without meaning to: Telnet next to SSH, HTTP next to HTTPS, FTP next to two answers that are not the same answer, POP and IMAP next to their TLS versions, LDAP next to LDAPS, SNMP next to v3, syslog next to 6514. None of the numbers changed today.

Jules stops at my cube on her way out, raincoat on, bike lights already clipped to the strap.

"How many ports did you memorize today?"

"None. I collected some war stories and made a few swaps."

"Keep the cards if they help you get started," she says. "Throw them out when the person on the phone already knows the number, and what they actually need from you is the other half."

That's the one I write down. I lock the drawer and go out into the rain to catch the MAX.
