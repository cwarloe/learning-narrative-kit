# Portland Desk — The Port That Is Open

*A Security+ ports-and-protocols precursor • Hover over highlighted terms for exam definitions and supporting desk/network jargon.*

It had been raining on the east side of the building since before I got in. I was three weeks into a job at a midsize [[msp|MSP]], which so far mostly meant I said "let me look into that" more often than anyone wanted to hear. I kept index cards in the top drawer, service on the front and port number on the back, and I'd been through them enough times that I could have run the whole stack in the shower. Nobody ever asked me to.

Jules worked two cubes over and had the desk lead title. Nine years there. A bike helmet hung off her monitor arm, a pair of rain pants dried over the back of her chair, and she'd stuck a note on the edge of her screen that just said *which decision?*

The first ticket came in and I reached for the cards, and she caught me at it.

"You already know the numbers," she said. "So that's not the part that's slowing you down."

It was an ordinary Tuesday queue. What came in all day was people carrying habits they'd picked up somewhere else, at an old shop or out of vendor documentation or in a home lab at one in the morning, and most of my job turned out to be talking those habits into something that worked here.

## Jared and the script that still speaks Telnet

Jared from network ops pinged me before nine. There was a switch in a closet in Building C with a [[vlan|VLAN]] set wrong, and he already had the steps written on a clipboard from years of doing exactly this.

"I Telnet in, type the [[enable_password|enable password]], fix the VLAN, hang up," he said. "Ten minutes. My script expects [[telnet|Telnet]]. I wrote it back when I was still racking gear out in Hillsboro."

I was most of the way to saying *sure, twenty-three is open on that box* when Jules leaned on my cube wall with her coffee.

"Ask him what we burned on last year."

Jared answered before I could get the question out. "Packet capture on the management span. The enable password sitting there in the clear where anybody walking past the collector could read it. The boss made us rotate everything that week. I still flinch."

"So which [[port|port]] do we allow on the management path," I said, "and which [[protocol|protocol]] is carrying that password? Telnet sends it in [[cleartext|cleartext]]."

He sighed at me. "You're going to say [[ssh|SSH]]. Same remote shell, encrypted, twenty-two. Fine. The script's mine, I can rewrite it. Just don't make me do it twice."

"Then let's put [[key_auth|key auth]] on it now instead of passwords," I said. "You rewrite once. And we're fixing the script, not the [[firewall|firewall]]."

Eleven minutes later he pasted a screenshot of a working SSH login and added, sounding almost proud about it, that keys felt weird after ten years of passwords but whatever. His clipboard was one line shorter than it had been.

## Maya and the mail client that trusts the hallway

Accounting next. Maya could get her mail on the office Wi-Fi and it failed at home, and she had decided the server was broken.

I remoted into her settings while she was on the phone. Her inbound was [[pop3|POP3]] on 110, which downloads, deletes, and hopes.

"That's how my first laptop did it in college," she said. "Grab the mail and go. My coworker keeps everything on the server with [[imap|IMAP]] on 143 and I never understood why both of them still worked here."

"They both still work, and they're both cleartext," I told her. "On a coffee shop network, somebody else on that Wi-Fi can read your credentials and the body of your mail. There are secure versions of both. [[pop3s|POP3S]] on 995 if you're attached to POP. For the way you actually work I'd rather put you on [[imaps|IMAPS]] on 993, where the mailbox stays on the server and the whole session sits inside [[tls|TLS]]."

Her outbound was pointed at [[smtp|SMTP]] on 25, which she told me was what IT had set years ago, before she even started.

Jules, from her cube, not looking away from whatever she was doing: "Twenty-five is how servers talk to each other. Back when clients used to submit there, we got yelled at by the ISP about once a quarter."

"So we'll use [[smtp_submission|submission]] on 587 with [[starttls|STARTTLS]]," I said, slower this time, because Maya was writing it down. "Or [[smtps|SMTPS]] on 465 if the client wants [[implicit_tls|implicit TLS]] from the first byte. Either way it's authenticated submission, and neither one of them is an [[open_relay|open relay]]."

Maya laughed at me. "Say STARTTLS one more time and I'll click wherever you point. My brother runs a mail server on a Raspberry Pi and he is never going to hear about this."

We changed the profile together and sent a test message, and the red banner in her client went away.

## The vendor whose appliance has one door

The facilities vendor needed to get a building controller config over to us, and the ticket said, cheerfully, to drop it on their [[ftp|FTP]] server.

I called instead of typing a lecture at them. Their engineer was named Dana and sounded like she was in a truck, with a radio going in the background.

"FTP is what the appliance documentation still shows," Dana said. "Twenty-one, username, done. I've done it that way on every install since sometime in the 2010s."

"The password and the filenames both ride in the clear on FTP," I said. "We can push it over [[sftp|SFTP]] instead."

"Our box doesn't do SFTP, it does FTPS. Those are the same thing, aren't they? My NAS at home does SFTP and I mix the letters up constantly."

Everybody mixes the letters up. I'd done it in front of Jules a month earlier and she drew me two arrows on the whiteboard in red marker with her helmet strap still looped around her wrist.

"They're not the same," I said. "[[sftp|SFTP]] is file transfer running inside SSH, so it's usually port twenty-two, and it's a different protocol underneath. [[ftps|FTPS]] is the old FTP wrapped in TLS, which in implicit mode is often 990 for the control connection and 989 for data. Different ports, different firewall conversation. If your appliance speaks FTPS then we'll do FTPS. What we're not doing is plain FTP across the internet."

Dana exhaled. "FTPS I can turn on. I got burned once when a firewall guy opened twenty-one and then couldn't work out why the data connection hung. Active mode, port twenty, whole mess. Where do you want me to land it?"

"On a [[jump_host|jump host]] we control."

## HR's padlock and the contractor in a hotel

HR pinged right after standup. The benefits portal still loaded over [[http|HTTP]] on 80, which meant people had been typing open-enrollment information into a page with no padlock on it. Marketing had meant to fix it after benefits season. Benefits season was now.

The web ops channel was already half memes about certing it after open enrollment. I opened a [[change_ticket|change ticket]] to terminate [[https|HTTPS]] on 443, redirect eighty to four-forty-three, and get the certificate renewed before Friday. Somebody dropped in a gif of a padlock.

While that was working its way through, a contractor named Sam wanted [[rdp|Remote Desktop]] from a hotel in Seattle to a finance workstation. He was polite about it and he was late on a deliverable.

"I only need the desktop for an hour," Sam said. "Hotel Wi-Fi, my laptop, their machine. It's [[tcp|TCP]] 3389, right? My last client just whitelisted my home address and called it done."

I caught myself starting to draft a temporary allow rule.

Jules was already in the thread. "Read that request back to yourself as a decision."

"Allow RDP from anywhere to finance-WS-14 on 3389."

"Right. Now read the second half of it out loud," she said. "Our insurance questionnaire asks whether 3389 faces the internet. That's a renewal conversation, not a movie plot. [[ransomware|Ransomware]] crews scan that port all day long."

I called Sam back. "We'll get you onto the [[vpn|VPN]] first, into our pool, and you'll RDP from in there. Better than that, we'll point you at a [[jump_host|jump box]]. We don't open raw 3389 to the internet, not even for an hour, for the same reason we don't hang [[smb|SMB]] on 445 off the outside of the building."

Sam groaned, then gave in. "I've already got the VPN from the last gig. Jump box is fine if somebody sends me the name. It's honestly nicer than hoping the hotel Wi-Fi is friendly."

The [[firewall_rule|firewall rule]] we submitted was narrow on purpose. Source was the VPN address group, destination the jump host, port 3389, TCP, allow. Everything else reaching that workstation on 3389 was denied. Jules initialled it on her way past.

## The new hire, the directory, and the quiet plumbing

Early afternoon. A new hire in legal named Lena couldn't [[directory_bind|bind]] to the directory from the password reset tool. The app talked [[ldap|LDAP]] on 389, it worked from the wired desk VLAN, and it failed on [[guest_wifi|guest Wi-Fi]].

"I've been sitting in the lobby because my desk wasn't ready," Lena said. "And now the reset tool hates me. At my last internship everybody just said use guest, it's fine."

"Guest is exactly where we don't want a directory bind crossing in cleartext," I said. "We'll move it to [[ldaps|LDAPS]] on 636. Same queries, TLS around them."

While we were testing that, her laptop started failing [[kerberos|Kerberos]] to the [[domain|domain]] as well, tickets coming back rejected. Her clock was fourteen minutes off after a long sleep.

Jules went past with a granola bar. "I spent an entire Sunday once convinced I'd broken Active Directory in my home lab. It was the clock. Kerberos does not forgive you about the clock."

I pointed Lena at our internal [[ntp|NTP]] on 123/[[udp|UDP]], her clock jumped, and Kerberos stopped sulking.

She asked why the laptop couldn't find the internet at all until she rebooted earlier, which turned out to be ordinary desk noise sitting underneath the directory problem. [[dhcp|DHCP]] on 67 and 68 had handed her a [[dhcp_lease|lease]] that morning, [[dns|DNS]] on 53 was resolving fine for everybody else, and her adapter had simply wedged. We renewed the lease, flushed the [[resolver_cache|resolver cache]], and sent her back to onboarding.

## Monitoring, AAA, and the community string everybody knows

Network monitoring opened a ticket that looked routine on its face. Dee wanted to poll the access switches with [[snmp|SNMP]] on 161/UDP, traps on 162, using a [[community_string|community string]] of `public`.

"It's what the vendor template ships with," Dee said. "We just need graphs before the weekend change window. I've got a Raspberry Pi at home that still answers to `public`. Don't tell Jules."

"Jules already knows," Jules said, two cubes over, still typing.

Dee put her forehead down on her desk.

"We can poll," Jules said. "We're not doing it with `public` in the clear. Turn up [[snmpv3|SNMPv3]] with authentication and privacy. Same ports if we leave the defaults alone, completely different trust model. I found `public` on a customer's core switch during an after-hours walkthrough once. It was like finding the spare key under the mat."

Dee muttered something about templates, then asked for the v3 checklist, and Jules dropped it into the channel without saying anything else about it.

Logging had the same habit attached to it. The closets were still forwarding [[syslog|syslog]] in cleartext to the collector on 514/UDP, and a technician named Marco wanted 514 opened from the guest SSID so he could finish a closet without walking upstairs.

"It's just for convenience," Marco said. "I used to debug printers that way at my last MSP."

"Convenience for you is cleartext logs riding the guest network," I said. "Use [[syslog_tls|syslog over TLS]] on 6514/TCP. Jules already filed the long-term fix and this matches it."

He took the walk upstairs, grumbling, and mentioned on the way that 6514 was the one he always forgot on flashcards. Same.

VPN and device login questions piled onto the same thread. Remote users authenticate to the [[concentrator|concentrator]] through [[radius|RADIUS]], 1812 for authentication and 1813 for accounting, and the network team would rather use [[tacacs|TACACS+]] on 49/TCP for switch and firewall admin sessions, because it encrypts the whole payload and splits [[authz|authorization]] cleanly away from authentication.

"People say [[aaa|AAA]] like it's one port," Jared said, dropping into the thread still riding his SSH win. "RADIUS for the VPN crowd, TACACS for those of us touching the boxes. I had them mixed up for about a year."

I didn't configure either one from the desk. I named the ports when somebody asked.

## TFTP and the printer that will not wait

The last real ping of the shift was a facilities tech named Owen, who needed to get firmware onto a printer and wanted to do it with [[tftp|TFTP]] from his laptop on the user VLAN. No authentication, 69/UDP, tiny and trusting.

"The MAX leaves in twenty minutes and the printer is dead," Owen said. "Just this once from here. I PXE boot lab gear with TFTP at home all the time, it's fine if you know the room."

"Management segment only," I said. "Short window, and then we close it. TFTP doesn't cross a [[perimeter|perimeter]] and it doesn't belong on the desk VLAN next to people browsing the web. Your home lab is one room you know everything about. This floor isn't."

Owen looked at the clock, then at me. "Is the staging switch still up? The one we used for the badge reader flash last month?"

"Still up."

He moved fast. The firmware landed and I closed the port behind him. He made his train. In the ticket note he wrote *staging only, Owen knows why now*, which was more honest than most of the notes I'd written in week one.

## Closing the queue

By 5:40 the queue was down to noise. The index cards were still out on my desk, and I noticed I'd been pairing them off all afternoon without meaning to: Telnet next to SSH, HTTP next to HTTPS, FTP next to two answers that are not the same answer, POP and IMAP next to their TLS versions, LDAP next to LDAPS, SNMP next to v3, syslog next to 6514. None of the numbers had changed that day.

Jules stopped at my cube on her way out, raincoat on, bike lights already clipped to the strap.

"How many ports did you memorize today?"

"None. I collected some war stories and made a few swaps."

"Keep the cards if they help you get started," she said. "Throw them out when the person on the phone already knows the number, and what they actually need from you is the other half."

That was the one I wrote down. I locked the drawer and went out into the rain to catch the MAX.
