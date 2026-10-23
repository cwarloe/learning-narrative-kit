# Portland Desk — Don't Click That

*A Security+ social-engineering precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

Wednesday started with a subject line in all caps and Jules rewriting the sticky under *which decision?* It now said *who benefits if I hurry?*

"They are not breaking our crypto," she said when I reached for a blank card. "They are borrowing our manners. Notice which manners got borrowed."

The first ticket in the help desk queue read *URGENT — mailbox locked, verify now.*

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

While Sam was still on the line, Finance Slack lit up. Dana pastes a thread: CFO asking AP to "update vendor routing before close of business, board packet depends on it." Someone in the thread had already typed *on it* — authority working before anyone checked the address.

Jules appeared at my cube wall.

"Read the From," she said. "Not the display. The actual From."

Display name: *Avery Chen, CFO*. Address: `avery.chen@c0mpany-mail[.]biz`. Reply-To somewhere else entirely. The logo in the signature was crisp.

"Spoofing the display name," I said. "Executive impersonation of our CFO. When an attacker targets the executive directly, that's [[whaling|whaling]]; when they impersonate the executive to trick accounts payable into wiring money, that is classic CEO Fraud under [[bec|business email compromise (BEC)]]. Nobody confirms wiring instructions from an email thread. Call Avery on an internal extension from the badge directory, not the phone number in that email footer."

Dana already had Avery on the real desk phone. Avery had never heard of the thread. AP froze the change. Someone un-typed *on it*. I opened an escalate ticket for the SOC with headers pasted, not vibes.

## Vishing, pretext, and the helpful stranger

Late morning the phone queue got weird. A man calling as "IT vendor refresh" wanted Nora's VPN one-time code "so we can finish the certificate push." He knew her cube number. He knew Jules's first name. He laughed at the rain like a local.

Nora had me on chat while she kept him talking. Polite delay, no secrets.

"He sounds like someone who works here," she typed. "Says he sat with help desk last quarter. Asks about the sticky on Jules's monitor like he has seen it."

"[[vishing|Vishing]]," I typed back. "Voice channel. He is doing pretexting — a story that makes the ask feel normal — and familiarity so you treat him like hallway furniture. We do not read codes to callers. Tell him to open a ticket with his company email and hang up. If he were us, he would already know that path."

She hung up. He did not open a ticket. Nora sent a note: *he tried the certificate story twice with different verbs.*

Ten minutes later Todd in sales texted a screenshot: a message claiming HR benefits enrollment seats were "almost gone," link included, only three left. The tone was HR-casual, which Ken trusts more than HR-formal.

"[[smishing|Smishing]]," I said on the follow-up call. "SMS phishing. Same scarcity trick as a fake flash sale. Open benefits from the portal tile, not from a text. Report the number if the carrier tool lets you; open a desk ticket either way."

Ken muttered, "I almost clicked because it said my teammates already finished." That is consensus — social proof as a shove. I wrote it on the sticky under Jules's: *everyone else already did* is not evidence. Jules walked by, read it, and added in smaller handwriting: *especially when 'everyone' has no names.*

## MFA pushes nobody started

Afternoon: Dev from engineering pinged that his phone was buzzing Approve/Deny even though he was not logging into anything. He had denied two. His thumb was negotiating with a third.

"I almost tapped Approve to make it shut up," he said. "It felt like clearing notifications."

"That is an [[mfa_fatigue_attack|MFA fatigue attack]]," I said. "Someone likely has a password or session path and is spamming pushes until a human gets bored. Deny, do not approve just once, and we reset the session plus rotate. If phishing harvested you earlier, fatigue is the second act."

We walked Deny, report, password rotate, then checked recent user-reported mail for his address. Nothing from Maya's campaign sat in his inbox, but a lookalike travel portal did. Dev put the phone face-down. "Deny if I did not ask. I already had that line once. Apparently I needed it twice."

Jules stepped over to my terminal. "We have a spoofed CFO email demanding a forty-eight-thousand-dollar wire change, Sam hovering over an archive attachment, and Dev's phone buzzing with credential stuffing MFA fatigue pushes. You have ten minutes before AP cuts the afternoon batch wire. Pull the raw RFC 5322 MIME headers, trace the originating IP, verify SPF, DKIM, and DMARC alignment, and get the quarantine hash to the mail gateway before money walks out the door."

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: Email Header Decomposition & Phishing Triage
target: workbench/09-dont-click-that.md
domain: CompTIA Security+ SY0-701 • Domain 1.2 & 2.4
badge: The Hands-On Lab
cta: Take the Ticket & Open the Lab ->
---
Step onto Ethan's shift. Deconstruct raw RFC 5322 email headers, trace IP hops in `Received:` lines, verify SPF/DKIM/DMARC alignment against DNS TXT records, uncover typosquatted domains, and draft the Tier 1 Phishing Incident Triage & Security Escalation dossier before the wire transfer executes.
```
