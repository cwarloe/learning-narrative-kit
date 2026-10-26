# Portland Desk — Don't Click That

*A Security+ social-engineering precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

Wednesday morning smelled of wet pavement and burnt French roast. I was hanging my rain jacket behind workstation fourteen when Jules spun her chair around to block the aisle.

"Finance says the CFO is traveling all week," Jules said, reading from her phone. "Expect someone to know that."

I was still Tier 1. The posting I had missed in October would reopen that week, and the line in my file about tone was still there. <!-- date-ok -->

The wallboard chimed: a high-priority ticket flagged *URGENT — mailbox locked, verify now.*

## Maya and the padlock that is not ours

```callout-panel
title: "FIGURE 9.1: EMAIL MIME ARCHITECTURE & SPF CHECK"
badge: "Email Authentication"
caption: "Schematic diagram: Email envelope sender (MAIL FROM) versus message header (From:). Demonstrates how SPF verifies sending IP while DKIM cryptographically signs body hashes."
prompt: "Clean technical cutaway diagram of an email message header structure under bright lighting. Arrows connect sender IP address to DNS TXT record for SPF validation. Clean instructional manual style, crisp fine lines, no text, no words. 4:3 ratio."
```

Maya from accounting forwarded a message with logos that looked expensive. The body said her mailbox would be deleted in two hours unless she "verified" at a link. She sounded embarrassed on the phone, which usually means she almost did the wrong thing and caught herself.

"It looks like Microsoft," she said. "Same blue. Same wording as the real banner. I almost clicked on the MAX."

I expanded the link without clicking. Display text said `login.microsoft.com`. The real host was `login-micros0ft-secure[.]ru` with a zero where an o should live. The browser status bar is honest when you let it finish talking.

"That's a fake login portal," I said. "They're using [[typo_squatting|typosquatting]] with a zero instead of an 'o' to pull off [[brand_impersonation|brand impersonation]]. If you type your credentials into that page, it's straight [[credential_harvesting|credential harvesting]]—they grab your password and immediately prompt for your MFA code."

Maya exhaled. "So this is just… [[phishing|phishing]]?"

"Classic phishing," I said. "Broad bait, urgency so you skip the hover. Use the phish report button, do not forward the raw message to your cousin, and we will pull a copy for the mail gateway team."

She clicked Report. The ticket flipped to user-reported. Jules, without getting up: "Good. Gateway sees it that way. Forwarding it to your brother just makes a second copy of the bait."

Maya still looked like someone who wanted credit for almost clicking. I did not argue with that.

## Spear, whale, and the invoice that moved

The next call was specific.

Sam — the contractor from the hotel RDP week — had a note that named his project code, his manager, and last Tuesday's change window. Attachment: `SOW_revision_final.iso.zip`. He was proud that he had noticed the double extension. He was less proud that he had still hovered over Open.

"It knows too much to be spam," Sam said. "Feels personal. Like someone read the project channel."

"That is the point of [[spear_phishing|spear phishing]]," I said. "Do not open the archive. That pattern is a malware attachment wearing a Statement of Work. Personal detail is fuel, not proof the sender is safe."

While Sam was still on the line, Finance Slack lit up. Marisol pastes a thread: CFO asking AP to "update vendor routing before close of business, board packet depends on it." Someone in the thread had already typed *on it* — authority working before anyone checked the address.

Jules appeared at my cube wall.

"Read the From," she said. "Not the display. The actual From."

Display name: *Avery Chen, CFO*. Address: `avery.chen@c0mpany-mail[.]biz`. Reply-To somewhere else entirely. The logo in the signature was crisp.

"Spoofing the display name," I said. "Executive impersonation of our CFO. When an attacker targets the executive directly, that's [[whaling|whaling]]; when they impersonate the executive to trick accounts payable into wiring money, that is classic CEO Fraud under [[bec|business email compromise (BEC)]]. Nobody confirms wiring instructions from an email thread. Call Avery on an internal extension from the badge directory, not the phone number in that email footer."

Marisol already had Avery on the real desk phone. Avery had never heard of the thread. AP froze the change. Someone un-typed *on it*. I opened an escalate ticket for the SOC with headers pasted, not vibes.

## Smishing and the screenshot

Late morning, Todd in sales texted a screenshot: a message claiming HR benefits enrollment seats were "almost gone," link included, only three left. The tone was HR-casual, which Todd trusts more than HR-formal.

"[[smishing|Smishing]]," I said on the follow-up call. "SMS phishing. Same scarcity trick as a fake flash sale. Open benefits from the portal tile, not from a text. Report the number if the carrier tool lets you; open a desk ticket either way."

Todd muttered, "I almost clicked because it said my teammates already finished." That is consensus — social proof as a shove. I wrote it on the sticky under Jules's: *everyone else already did* is not evidence. Jules walked by, read it, and added in smaller handwriting: *especially when 'everyone' has no names.*

## MFA pushes nobody started

Dev's message arrived as a photo of his own phone, taken with someone else's. It was buzzing Approve/Deny even though he was not logging into anything. He had denied two. His thumb was negotiating with a third.

"I almost tapped Approve to make it shut up," he said. "It felt like clearing notifications."

"That is an [[mfa_fatigue_attack|MFA fatigue attack]]," I said. "Someone likely has a password or session path and is spamming pushes until a human gets bored. Deny, do not approve just once, and we reset the session plus rotate. If phishing harvested you earlier, fatigue is the second act."

We walked Deny, report, password rotate, then checked recent user-reported mail for his address. Nothing from Maya's campaign sat in his inbox, but a lookalike travel portal did. Dev put the phone face-down. "Deny if I did not ask. I already had that line once. Apparently I needed it twice."

## The padlock on the wrong name

The spoofed invoice link went to a domain one letter off from our vendor's. I opened it in the sandbox browser and stopped at the padlock. The site had a valid certificate, issued two days earlier, chained up through an intermediate to a public root my browser trusted.

"It has a padlock," Sam said behind me, a little too relieved.

"It has a certificate for the wrong name," I said. That was only half right, and I knew it as I said it. The certificate was valid for exactly the name it claimed. The name was the lie. A certificate authority had checked that whoever asked for it controlled that typo domain, which they did. The padlock meant the connection was encrypted to the attacker. It did not mean the attacker was our vendor.

I wrote the chain into the ticket: leaf certificate, intermediate, root, issue date, and the domain it was really for. Marisol, who had worked accounts payable for nine years and knew every vendor's real domain from memory, read the ticket over my shoulder and said the vendor had never used that domain. She could not tell me what an intermediate certificate was, and I could not have told her the vendor's remit-to address. We needed both.

## The Wire Run

The header trace put the "CFO" message on a mail server that had never sent us mail before, and the domain failed DMARC alignment. Marisol called Avery on the real desk phone, and Avery had never sent the request. AP cancelled the wire change, and the mail team purged Sam's zip from the spool before he could open it.

The save cost the afternoon. AP held the batch wire for three hours while Marisol called every vendor on the run to confirm their banking details, and two real payments went out a day late. The controller sent Jules a note asking why a phishing email had delayed legitimate vendors.

I saved the typo domain, the certificate serial number, and the zip's hash into the SOC's indicator list. Nobody asked me to.

Nora's vishing call went to Jordan from ops, not me, because I was still on headers. I heard at standup that the caller had known her manager's name and the date of last Tuesday's change window, and that Jordan had made her hang up and call back on the directory number. Nora said she had nearly read him the code.

Jules took back the Friday I had requested off so I could cover the AP callback queue. It was the first day off I had asked for since starting on the desk. The Tier 2 posting reopened that week. I applied again and did not hear back before the holidays.

## Practice It in the Lab

```bridge-card
title: Portland Desk Lab: Email Header Decomposition & Phishing Triage
target: workbench/09-dont-click-that.md
domain: CompTIA Security+ SY0-701 • Domain 1.2 & 2.4
badge: The Hands-On Lab
cta: Take the Ticket & Open the Lab ->
---
The lab walks through the incident from this chapter step by step, with the answer shown, and then gives you one new problem that works the same way.
```
