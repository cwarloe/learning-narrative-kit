# The Invoice That Changed Its Bank

*Tamarack Supply • MIS Module 5: Protecting Information Resources • Hover over highlighted terms for course definitions.*

## Eighty-Six Thousand Dollars

The email came from the seed company's accounts-receivable manager, a woman Hank Pruitt had exchanged invoices with for six years. It was polite and a little apologetic. The seed company had moved its banking to a new institution, the attached letter had the new routing and account numbers, and could Tamarack please use them for the spring seed invoice, due Friday, in the amount of $86,240.

Hank had the payment set up by ten. He asked Dana Okafor to look it over only because she was walking past his office and the bank's new approval screen confused him.

Dana noticed the sender's address before she noticed anything else. The display name was right. The domain was the seed company's name with one letter doubled. She pointed at it. Hank leaned in, took his reading glasses off, put them back on, and said a word his father wouldn't have used.

"It's [[phishing|phishing]]," Dana said. "An email that looks like it's from someone you trust."

"It's not some Nigerian prince. It's Karen. She signs her emails the same way."

That was the part that worried Teo Vasquez when he came in. Whoever wrote it knew Karen's signature, knew the invoice was due Friday, and knew the amount to the dollar. That wasn't a guess. It was [[social_engineering|social engineering]] built on information that had come from somewhere inside.

## Calling Karen Back

Before anyone touched the payment, Teo made Hank call the seed company at the phone number printed on last year's paper invoice, not the one in the email.

Teo said the habit was older than email. The propane system's original dial-in line had used a [[callback_modem|callback modem]]: when a technician dialed in, the modem hung up and called back a number already on file, so a stranger who knew the dial-in number still couldn't connect. Calling Karen at a known number was the same idea with a person instead of a modem.

Hank asked whether he should at least log in to the bank and check the new account from there. Teo said yes, but by typing the bank's address himself, not by clicking the link in the email. Even that wasn't a guarantee. With [[pharming|pharming]], an attacker hijacked the official site's address itself, so a user who typed the correct address still landed on a fake page. It was rarer than phishing and much harder to notice, which was why the phone call came first.

Karen answered. The seed company had not changed banks. She asked whether Tamarack had paid the February invoice to the new account, because their February payment had never arrived.

Hank checked. Tamarack had. Fourteen thousand two hundred dollars, sent on February 19 to an account in another state, following an earlier email about the same "bank change" that Hank had forgotten about because it had seemed so ordinary. That was [[computer_fraud|computer fraud]] in the plainest sense: someone had used Tamarack's data, without authorization, to take Tamarack's money.

The bank's fraud desk said they would try. They said it in the tone of people who expected to fail.

## Where the Inside Information Came From

Teo pulled Hank's laptop that afternoon. The browser history and installed-programs list told most of the story.

In January Hank had needed to convert a PDF to a spreadsheet and had downloaded a free converter from a site that ranked well in search. The converter worked. It was also a [[trojan_programs|Trojan program]], with something else riding along inside it. Inside was a [[keystroke_loggers|keystroke logger]] that recorded everything Hank typed, including his email password, and sent it out every few hours. There was also a bundle of [[adware|adware]] that tracked his browsing to serve ads, which explained the pop-ups Hank had been complaining about and ignoring since February. Both were forms of [[spyware|spyware]], software quietly gathering information about the user.

With Hank's [[password|password]], the attacker had simply logged into his email from somewhere else, read six years of correspondence with the seed company, set a rule to hide any replies from Karen's real address, and waited for the invoice cycle.

"Can you clean it?" Hank asked.

Teo shook his head. A Trojan that had been running for two months could have installed a [[rootkit|rootkit]], a set of tools that hides an intruder's access from the operating system itself. If it had, nothing Teo ran on the laptop could be trusted to report honestly. He was wiping the machine. Hank would lose the custom toolbars and saved macros he'd built up over a decade, and the folder of templates he kept on his desktop instead of on the server.

## The Three Things That Got Hurt

Ruth Halvorsen wanted a one-page summary for Walt by morning. Dana wrote it around three words Teo kept using.

[[confidentiality|Confidentiality]] had failed: someone not authorized to read Hank's email had read all of it. [[integrity|Integrity]] had failed too, in a quieter way. The bank details in Tamarack's vendor file were still right, but the information Hank acted on was not accurate, and the system had no way to tell him so. [[availability|Availability]] was the one that held — the systems stayed up, and Hank could still work — though wiping his laptop was about to cost him two days of it.

Walt read it in the hallway and asked who did this. Teo told him the honest answer, which was that they would probably never know. The style matched [[black_hats|black hats]] who ran payment-diversion schemes for profit, usually from outside the country. It was not the work of [[script_kiddies|script kiddies]], the inexperienced kind who had defaced the web store's homepage two summers ago using a tool somebody else wrote. Those had wanted attention. These had wanted eighty-six thousand dollars.

## The Email Nobody Answered

Dana found the other thing while searching Hank's mailbox for the attacker's rules.

In November a stranger had emailed Tamarack's general inbox. He said he had found a security hole in the web store's login page while browsing, that he meant no harm, and that he could fix it for $500. Nobody had answered. Teo read it twice.

"That's a [[gray_hats|gray hat]]," he said. "Poked at us without permission, didn't break anything, wants paying. He's not a criminal exactly, and I can't hire him." He forwarded it to the MSP, who confirmed the hole was real and patched it in an hour.

It also made the case for something Teo had wanted for a year. He brought in a [[white_hats|white hat]] firm the MSP recommended, ethical hackers paid to break in on purpose, under contract, and report everything they found.

## What the Testers Found

The penetration test took a week. The report ran to forty pages. Dana read all of it because Ruth asked her to turn it into a list Walt would read.

The worst finding was in the propane billing program. The contractor who wrote it in 2004 had left a [[backdoor|backdoor]]: a hard-coded username and password that bypassed the program's login, presumably so he could fix things remotely. It still worked. The testers also checked the code for a [[logic_bomb|logic bomb]], something set to go off on a date or an event after a programmer left, because a departing contractor with a backdoor was exactly the person who would plant one. They found none. Teo said he would have liked that sentence to be stronger than "found none."

The feed-room server was mining cryptocurrency. Its CPU had been pinned at ninety-eight percent since a public-facing service was exposed in December. That was [[cryptojacking|cryptojacking]], someone using Tamarack's electricity and hardware to make money for themselves, and it explained why the billing box had felt slow even before its disks started dying.

The testers also ran the usual social tests at two stores. At Deer Park, a USB stick labeled "Q2 Payroll" left in the break room was plugged into a register PC within forty minutes. That was [[baiting|baiting]], the promise of something worth having. At Chewelah, a tester called pretending to be from the register vendor, offering a free upgrade in exchange for the manager's login. The manager gave it. That was [[quid_pro_quo|quid pro quo]], and it worked because the offer sounded like a favor.

On the guest Wi-Fi at the Spokane Valley store, the testers ran [[sniffing|sniffing]] tools to capture traffic and found the old time-clock app sending employee PINs in plain text. They also showed they could do [[spoofing|spoofing]] on the store network, posing as the register server so a lane would send it a manager's credentials.

## The Attachment Hank Didn't Open

One more item came from Hank's quarantine folder. Besides the bank-change email, the attacker had sent a second message in February with a spreadsheet attached, "updated seed pricing." Hank's mail filter had caught it.

The testers took it apart in a sandbox. It contained a [[macro_viruses|macro virus]], written in the spreadsheet program's own macro language, that ran the moment the file was opened with macros enabled. Once running, it dropped a [[worm|worm]] that would have copied itself across the network shares on its own, without needing anyone to open anything else, and it also behaved like a classic [[virus|virus]] by attaching itself to other spreadsheets on each machine it reached. Bundled together, it was a [[blended_threat|blended threat]]: several kinds of malicious code exploiting several weaknesses at once.

"If he'd opened that one," Teo said, "we'd be having a different meeting."

## The Controls Walt Agreed To

Teo's list of fixes was long. Ruth made him rank it. Walt approved the top of it on a Thursday and argued about the rest.

[[access_controls|Access controls]] came first: nobody would share a login, store managers would get their own accounts, and changing a vendor's bank details would require two people. Every login to email and the bank would require an [[authentication_tokens|authentication token]] after the password, so that one stolen password wouldn't be enough. Hank complained about the token for a week.

The vendor bank-change process got a real fix. Tamarack would accept bank changes only through a signed form from the vendor portal. The portal used [[pki_public_key_infrastructure|PKI]], with key pairs issued through a trusted authority, so a change request could be verified as coming from the vendor. Teo explained the two kinds of encryption underneath. [[symmetric_encryption|Symmetric encryption]] used one shared secret key for both locking and unlocking, which was fast but meant both sides had to agree on the key and keep it secret. [[asymmetric_encryption|Asymmetric encryption]] used a public key anyone could have and a private key only the owner held. Signing with the private key gave [[nonrepudiation|nonrepudiation]]: the seed company couldn't later claim it hadn't sent a change, and nobody else could send one in its name.

The web store already used [[transport_layer_security_tls|TLS]] for checkout. The MSP pointed out that one old supplier integration still negotiated the older [[secure_sockets_layer_ssl|SSL]] protocol, and turned it off; the supplier's integration broke for two days.

Store managers who worked from home would connect through a [[virtual_private_network_vpn|VPN]], a secure tunnel to the office network. The office [[firewall|firewall]] would block everything else coming in. An [[intrusion_detection_system_ids|intrusion detection system]] would watch traffic for attack patterns and alert Teo. Teo said the alerts would go to a shared mailbox this time, not a person who'd left.

## The Things That Got Deferred

Some items didn't make the cut.

The MSP pitched a [[zero_trust_security|zero trust]] design, where every device and person had to prove they were secure on every connection, inside the building or out. Teo wanted it. It meant replacing the register network, and Walt deferred it to next year.

The DC already used fingerprint readers on the time clock, a form of [[biometric_security_measures|biometric security]]. The vendor's sales rep pitched extending it to the office, and then went further, describing [[zero_login|zero login]] systems that would recognize users by voice and typing pattern, [[dna_identification|DNA identification]] that built an "eDNA" behavioral profile, and a [[brain_password|brain password]] that read brain activity through a special hat. Walt said he would wear a hat to log in the day the seed company paid back his fourteen thousand dollars.

The feed-room closet got a lock with a keypad, the cheapest of the [[physical_security_measures|physical security measures]] on the list. The billing box got wiped, rebuilt, and moved to the new NAS-backed setup from the spring. That brought up [[fault_tolerant_systems|fault-tolerant systems]] again, and from there Ruth asked for the thing she had been meaning to ask for since the server failed: a written [[business_continuity_planning|business continuity plan]] covering how Tamarack would keep selling feed and propane if head office's systems went down for a week. Dana was assigned to draft it. Nobody gave her a deadline, which she took to mean she should set her own.

## The Fourteen Thousand

The bank's fraud desk called back in April. The receiving account had been emptied the day after the February deposit. The money was gone.

The web store went down once more that spring, for forty minutes on a Saturday, from a [[denial_of_service_dos_attack|denial-of-service attack]] that flooded it with requests. Nobody ever knew whether it was connected. The MSP put the store behind a filtering service and added it to the monthly bill.

Hank used the token every morning and said he hated it every morning. In June the seed company's real accounts-receivable office received an email, from an address with one letter doubled, asking whether Tamarack's bank had changed. Karen forwarded it to Hank with one line: "Is this you?" Hank called her back at the number on the paper invoice.
