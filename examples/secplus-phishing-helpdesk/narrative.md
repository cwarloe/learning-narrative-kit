# Portland Desk — Don't Click That

*A Security+ social-engineering precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

Wednesday started with a subject line in all caps and Jules rewriting the sticky under *which decision?* It now said *who benefits if I hurry?*

"They are not breaking our crypto," she said when I reached for a blank card. "They are borrowing our manners. Notice which manners got borrowed."

The first [[ticket|ticket]] in the [[help_desk|help desk]] queue read *URGENT — mailbox locked, verify now.*

## Maya and the padlock that is not ours

Maya from accounting forwarded a message with logos that looked expensive. The body said her mailbox would be deleted in two hours unless she "verified" at a link. She sounded embarrassed on the phone, which usually means she almost did the wrong thing and caught herself.

"It looks like Microsoft," she said. "Same blue. Same wording as the real banner. I almost clicked on the MAX."

I expanded the link without clicking. Display text said `login.microsoft.com`. The real host was `login-micros0ft-secure[.]ru` with a zero where an o should live. The browser status bar is honest when you let it finish talking.

"That is a [[phishing_url|phishing URL]]," I said. "[[typo_squatting|Typosquatting]] plus [[brand_impersonation|brand impersonation]]. The destination is [[credential_harvesting|credential harvesting]] — a fake login that eats your password and maybe your MFA code if you type one in because the page asked nicely."

Maya exhaled. "So this is just… [[phishing|phishing]]?"

"Classic phishing," I said. "Broad bait, [[urgency|urgency]] so you skip the hover. Use the [[phish_report_button|phish report button]], do not forward the raw message to your cousin, and we will pull a copy for the [[mail_gateway|mail gateway]] team."

She clicked Report. The ticket flipped to [[user_reported|user-reported]]. Jules, without getting up: "Good. Gateway sees it that way. Forwarding it to your brother just makes a second copy of the bait."

Maya still looked like someone who wanted credit for almost clicking. I did not argue with that.

## Spear, whale, and the invoice that moved

The next call was specific.

Sam — the contractor from the hotel RDP week — had a note that named his project code, his manager, and last Tuesday's change window. Attachment: `SOW_revision_final.iso.zip`. He was proud that he had noticed the double extension. He was less proud that he had still hovered over Open.

"It knows too much to be spam," Sam said. "Feels personal. Like someone read the project channel."

"That is the point of [[spear_phishing|spear phishing]]," I said. "Do not open the archive. That pattern is a [[malware_attachment|malware attachment]] wearing a Statement of Work. Personal detail is fuel, not proof the sender is safe."

While Sam was still on the line, Finance Slack lit up. Dana pastes a thread: CFO asking AP to "update vendor routing before close of business, board packet depends on it." Someone in the thread had already typed *on it* — [[authority|authority]] working before anyone checked the address.

Jules appeared at my cube wall.

"Read the From," she said. "Not the display. The actual From."

Display name: *Avery Chen, CFO*. Address: `avery.chen@c0mpany-mail[.]biz`. Reply-To somewhere else entirely. The logo in the signature was crisp.

"[[spoofing|Spoofing]] the display name," I said. "[[impersonation|Impersonation]] of the CFO. Aimed at money movers — that is [[whaling|whaling]] when the target is the whale, and the payment change is [[bec|business email compromise (BEC)]] with an [[invoice_scam|invoice scam]] payload. Nobody confirms wiring instructions from a surprise thread. Call Avery on a number you already have — badge directory, not the number in the email footer."

Dana already had Avery on the real desk phone. Avery had never heard of the thread. AP froze the change. Someone un-typed *on it*. I opened an escalate ticket for the [[soc|SOC]] with headers pasted, not vibes.

## Vishing, pretext, and the helpful stranger

Late morning the phone queue got weird. A man calling as "IT vendor refresh" wanted Nora's VPN one-time code "so we can finish the certificate push." He knew her cube number. He knew Jules's first name. He laughed at the rain like a local.

Nora had me on chat while she kept him talking. Polite delay, no secrets.

"He sounds like someone who works here," she typed. "Says he sat with help desk last quarter. Asks about the sticky on Jules's monitor like he has seen it."

"[[vishing|Vishing]]," I typed back. "Voice channel. He is doing [[pretexting|pretexting]] — a story that makes the ask feel normal — and [[familiarity|familiarity]] so you treat him like hallway furniture. We do not read codes to callers. Tell him to open a ticket with his company email and hang up. If he were us, he would already know that path."

She hung up. He did not open a ticket. Nora sent a note: *he tried the certificate story twice with different verbs.*

Ten minutes later Ken in sales texted a screenshot: a message claiming HR benefits enrollment seats were "almost gone," link included, only three left. The tone was HR-casual, which Ken trusts more than HR-formal.

"[[smishing|Smishing]]," I said on the follow-up call. "SMS phishing. Same [[scarcity|scarcity]] trick as a fake flash sale. Open benefits from the portal tile, not from a text. Report the number if the carrier tool lets you; open a desk ticket either way."

Ken muttered, "I almost clicked because it said my teammates already finished." That is [[consensus|consensus]] — social proof as a shove. I wrote it on the sticky under Jules's: *everyone else already did* is not evidence. Jules walked by, read it, and added in smaller handwriting: *especially when 'everyone' has no names.*

## MFA pushes nobody started

Afternoon: Dev from engineering pinged that his phone was buzzing Approve/Deny even though he was not logging into anything. He had denied two. His thumb was negotiating with a third.

"I almost tapped Approve to make it shut up," he said. "It felt like clearing notifications."

"That is an [[mfa_fatigue_attack|MFA fatigue attack]]," I said. "Someone likely has a password or session path and is spamming pushes until a human gets bored. Deny, do not approve just once, and we reset the session plus rotate. If [[phishing|phishing]] harvested you earlier, fatigue is the second act."

We walked Deny, report, password rotate, then checked recent [[user_reported|user-reported]] mail for his address. Nothing from Maya's campaign sat in his inbox, but a lookalike travel portal did. Dev put the phone face-down. "Deny if I did not ask. I already had that line once. Apparently I needed it twice."

## Doors, shoulders, and the recycling bin

Facilities walked a visitor past the badge reader. The visitor smiled, held a coffee tray for three, and waited for someone to beep in. Two people held the door because manners. One of them was me for half a second.

Jules did not raise her voice. She still stopped the line.

"[[tailgating|Tailgating]]," she said to me, not as a lecture to the lobby. "Ask them to sign in. Be polite. Be annoying on purpose."

The visitor signed in. The coffee still got delivered.

At the standing desk near the printer, I caught a contractor reading over Lila's shoulder while she typed a temporary password into a shared screen. I angled my body and said, "[[shoulder_surfing|Shoulder surfing]] works in offices too. Screens have sides." Lila turned the laptop. The contractor found somewhere else to be.

Later Jordan from ops dumped a box of old printouts next to the open recycling — org chart with cellphone scribbles, a page with a VPN URL and a handwritten password scratched out but still readable under the scribble, a badge access list from a retired closet.

Jules looked in the box. "Shredder for anything that still has a secret, even a dead one. [[dumpster_diving|Dumpster diving]] is that bin."

Jordan took the box back. He left a sticky on the shredder that said *if you can still read it, it still counts.*

## Quid pro quo and the watering hole rumor

A caller offered me a "free security scan gift card" if I confirmed our external mail gateway brand and the name of our [[sandbox|sandbox]] vendor. Helpful tone. Soft sell. He even offered to "credit the help desk team" in a write-up.

"[[quid_pro_quo|Quid pro quo]]," I said after I hung up and typed the note. "Gift for a detail. We do not trade architecture for coupons. If he needs a vendor list, he can go through procurement like a person."

Slack, meanwhile, was circulating a blog post from a niche local-devops forum everyone here actually reads. Commenters claimed a browser extension "everyone on the floor already installed" fixed a fake outage. The site looked familiar because it was familiar — until Security flagged the admin account takeover from last night.

"[[watering_hole|Watering hole]]," Jules said. "Poison the place the herd already drinks. That is why 'I only click things from our forum' is not a strategy." She posted the official advisory and killed the extension rumor before it became policy by screenshot.

Someone replied with a chain-letter PDF about "FBI mandatory password reset tonight or criminal liability." No ticket. No SOC banner. Just panic fuel.

"[[hoax|Hoax]]," I wrote in the channel. "If it mattered, it would arrive on the [[reporting_path|reporting path]] we already trust — not a viral PDF."

Jules pinned one more line: coordinated scare-posts and fake consensus threads are how light [[influence_campaigns|influence campaigns]] show up at desk scale. We are still a hallway where [[social_engineering|social engineering]] rumors try to become policy.

## Quarantine, gateway, and the path that counts

End of day we sat with a SOC analyst on a short bridge call. Not because I was becoming an investigator. Because the desk is where the humans land.

"[[mail_gateway|Mail gateway]] caught a sibling of Maya's message after her report," the analyst said. "We dropped the campaign into [[quarantine|quarantine]], detonated the zip in the [[sandbox|sandbox]], and tuned the rule. User-reported beat the first filter by twelve minutes. Filters are late sometimes. People who hover are early."

I updated the wiki blurb the desk actually reads: hover the link, check the real host, never read codes to callers, never approve surprise MFA, never change wire instructions from a thread, badge your own door, shred the bin, and when something feels like borrowed manners, use the [[phish_report_button|report button]]. That is the [[reporting_path|reporting path]].

At 5:40 I closed notes: Maya reported, Sam did not open the zip, Avery's wire frozen, Nora hung up on the pretext, Ken ignored the text, Dev denied the pushes, the lobby stopped a tailgate, Jordan shredded, the gift-card caller got nothing.

Jules clipped her bike lights on. "Tomorrow someone will call a [[spoofing|spoofed]] CFO probably real because the logo is crisp."

I said I already had the line. I locked the drawer and went out into the rain.
