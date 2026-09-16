# Portland Desk — Don't Click That

*A Security+ social-engineering precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

Wednesday rain has opinions again. I am Ethan, still week-something at the [[help_desk|help desk]], and today the queue is not ports or factors — it is people being talked into bad decisions.

Jules has a new sticky under *which decision?* It says *who benefits if I hurry?* Bike helmet on the monitor arm. She is not teaching CompTIA. She is keeping Finance from wiring money to a stranger with a good font.

"[[social_engineering|Social engineering]] is the job description of half our callers," she says when I reach for a blank card. "They are not breaking our crypto. They are borrowing our manners. Your job is to notice which manners got borrowed."

I open the queue. Coffee. Portland doing Portland. First [[ticket|ticket]] subject: *URGENT — mailbox locked, verify now.*

## Maya and the padlock that is not ours

Maya from accounting — same Maya who used to run cleartext POP — forwards a message with logos that look expensive. Subject line screams. Body says her mailbox will be deleted in two hours unless she "verifies" at a link. She sounds embarrassed on the phone, which usually means she almost did the wrong thing and caught herself mid-thumb.

"It looks like Microsoft," she says. "Same blue. Same wording as the real banner. I almost clicked on the MAX. My brother would never let me live that down — he runs a home Pi lab and lectures me about padlocks."

I expand the link without clicking. Display text says `login.microsoft.com`. Real host is `login-micros0ft-secure[.]ru` with a zero where an o should live. The browser status bar is honest when you let it finish talking.

"That is a [[phishing_url|phishing URL]]," I say. "[[typo_squatting|Typosquatting]] plus [[brand_impersonation|brand impersonation]]. The theme is rented trust. The destination is [[credential_harvesting|credential harvesting]] — a fake login that eats your password and maybe your MFA code if you type one in because the page asked nicely."

Maya exhales. "So this is just… [[phishing|phishing]]? Not some advanced nation-state thing?"

"Classic phishing," I say. "Broad bait, [[urgency|urgency]] so you skip the hover. Advanced is optional. Hurry is required for their side. Use the [[phish_report_button|phish report button]], do not forward the raw message to your cousin, and we will pull a copy for the [[mail_gateway|mail gateway]] team."

She clicks Report. The ticket flips to [[user_reported|user-reported]]. Jules nods once like a referee acknowledging a clean foul call. "Reporting is not snitching," Jules adds without looking over. "Reporting is how the filter gets a second brain."

## Spear, whale, and the invoice that moved

Next call is not broad bait. It is specific.

Sam — contractor who still complains about hotel RDP — got a note that names his project code, his manager, and last Tuesday's change window. Attachment: `SOW_revision_final.iso.zip`. He is proud that he noticed the double extension. He is less proud that he still hovered over Open.

"It knows too much to be spam," Sam says. "Feels personal. Like someone read the project channel."

"That is the point of [[spear_phishing|spear phishing]]," I say. "Not a net. A harpoon with your name on it. Do not open the archive. That pattern is a [[malware_attachment|malware attachment]] story wearing a Statement of Work costume. Personal detail is fuel for [[spear_phishing|spear phishing]], not proof the sender is safe."

While Sam is still on the line, Finance Slack lights up. Dana — facilities truck energy, same as the FTP week — pastes a thread: CFO asking AP to "update vendor routing before close of business, board packet depends on it." Someone in the thread has already typed *on it* — [[authority|authority]] working before anyone checked the address.

Jules appears at my cube wall like weather.

"Read the From," she says. "Not the display. The actual From."

Display name: *Avery Chen, CFO*. Address: `avery.chen@c0mpany-mail[.]biz`. Reply-To somewhere else entirely. The logo in the signature is crisp. Crisp is not a control.

"[[spoofing|Spoofing]] the display name," I say slowly. "[[impersonation|Impersonation]] of the CFO. Aimed at money movers — that is [[whaling|whaling]] when the target is the whale, and the payment change is [[bec|business email compromise (BEC)]] with an [[invoice_scam|invoice scam]] payload. [[authority|Authority]] plus urgency. Nobody 'confirms' wiring instructions from a surprise thread. Call Avery on a number you already have — badge directory, not the number in the email footer."

Dana already has Avery on the real desk phone. Avery has never heard of the thread. AP freezes the change. Someone un-types *on it*. I open an escalate [[ticket|ticket]] for the [[soc|SOC]] with headers pasted, not vibes. Jules mutters, "Good font almost bought a truck of concrete. Almost."

## Vishing, pretext, and the helpful stranger

Late morning the phone queue gets weird. A man calling as "IT vendor refresh" wants Nora's VPN one-time code "so we can finish the certificate push." He knows her cube number. He knows Jules's first name. He laughs at the rain like a local.

Nora has me on chat while she keeps him talking. She is good at this — polite delay, no secrets.

"He sounds like someone who works here," she types. "Casual. Says he sat with help desk last quarter. Asks about the sticky on Jules's monitor like he has seen it."

"[[vishing|Vishing]]," I type back. "Voice channel. He is doing [[pretexting|pretexting]] — a story that makes the ask feel normal — and [[familiarity|familiarity]] so you treat him like hallway furniture. We do not read codes to callers. Ever. Tell him to open a ticket with his company email and hang up. If he were us, he would already know that path."

She hangs up. He does not open a ticket. Shocking. Nora sends me a coffee emoji and a note: *he tried the certificate story twice with different verbs.*

Ten minutes later Ken in sales texts a screenshot: a text message claiming HR benefits enrollment seats are "almost gone," link included, only three left. The tone is HR-casual, which Ken trusts more than HR-formal.

"[[smishing|Smishing]]," I say on the follow-up call. "SMS phishing. Same [[scarcity|scarcity]] trick as a fake flash sale. Open benefits from the portal tile, not from a text. Report the number if the carrier tool lets you; open a desk ticket either way."

Ken mutters, "I almost clicked because it said my teammates already finished." That is [[consensus|consensus]] — social proof as a shove. I write it on the sticky under Jules's: *everyone else already did* is not evidence. Jules walks by, reads it, and adds in smaller handwriting: *especially when 'everyone' has no names.*

## MFA pushes nobody started

Afternoon: Dev from engineering — lockout kid from the auth week — pings that his phone is buzzing Approve/Deny even though he is not logging into anything. He has denied two. His thumb is negotiating with a third.

"I almost tapped Approve to make it shut up," he says. "Thumb was halfway there. It felt like clearing notifications."

"That is an [[mfa_fatigue_attack|MFA fatigue attack]]," I say. "Someone likely has a password or session path and is spamming pushes until a human gets bored. Deny, do not approve 'just once,' and we reset the session plus rotate. If [[phishing|phishing]] harvested you earlier, fatigue is the second act — same play, different button."

We walk Deny → report → password rotate → check recent [[user_reported|user-reported]] mail for his address. Nothing from Maya's campaign hits his inbox, but a lookalike travel portal did. Jules adds: "Fatigue is a habit attack. Treat surprise pushes like surprise wires. Convenience is not a personality trait."

Dev puts the phone face-down. "Deny if I did not ask. I already had that line once. Apparently I needed it twice."

## Doors, shoulders, and the recycling bin

Facilities walks a visitor past the badge reader. The visitor smiles, holds a coffee tray for three, and waits for someone to beep in. Two people hold the door because manners. One of them is me for half a second before Jules's sticky reconstructs itself in my head.

Jules does not raise her voice. She still stops the line.

"[[tailgating|Tailgating]]," she says to me, not as a lecture to the lobby. "Coffee is not a badge. Ask them to sign in. Be polite. Be annoying on purpose. Annoying is a control."

The visitor signs in. The coffee still gets delivered. Civilization survives.

At the standing desk near the printer, I catch a contractor reading over Lila's shoulder while she types a temporary password into a shared screen. I angle my body like a human privacy filter and say, lightly, "[[shoulder_surfing|Shoulder surfing]] works in offices too, not just cafés. Screens have sides." Lila turns the laptop. The contractor blushes and finds somewhere else to be. No villain music. Just posture.

Later Jordan from ops dumps a box of old printouts next to the open recycling — org chart with cellphone scribbles, a page with a VPN URL and a handwritten password scratched out but still readable under the scribble, a badge access list from a retired closet.

"[[dumpster_diving|Dumpster diving]] is not a cartoon raccoon," Jules says. "It is that bin. Shredder for anything that still has a secret, even a dead one. Dead secrets still teach attackers who sits where."

Jordan takes the box back. No speech. Just a better bin decision. He leaves a sticky on the shredder that says *if you can still read it, it still counts.*

## Quid pro quo and the watering hole rumor

A caller offers me a "free security scan gift card" if I confirm our external mail gateway brand and the name of our [[sandbox|sandbox]] vendor. Helpful tone. Soft sell. He even offers to "credit the help desk team" in a write-up, which is a weird bribe shaped like LinkedIn.

"[[quid_pro_quo|Quid pro quo]]," I say after I hang up and type the note. "Gift for a detail. We do not trade architecture for coupons. If he needs a vendor list, he can go through procurement like a person."

Slack, meanwhile, is circulating a blog post from a niche local-devops forum everyone here actually reads — the one with the bad ASCII art header and the good outage threads. Commenters claim a browser extension "everyone on the floor already installed" fixes a fake outage. The site looks familiar because it is familiar — until Security flags the admin account takeover from last night.

"[[watering_hole|Watering hole]]," Jules says. "Poison the place the herd already drinks. Not a cold email. A trusted hangout. That is why 'I only click things from our forum' is not a strategy." She posts the official advisory and kills the extension rumor before it becomes policy by screenshot.

Someone replies with a chain-letter PDF about "FBI mandatory password reset tonight or criminal liability." No ticket. No SOC banner. Just panic fuel and a font that wants to be official.

"[[hoax|Hoax]]," I write in the channel. "False warning designed to make you do something stupid. If it mattered, it would arrive on the [[reporting_path|reporting path]] we already trust — not a viral PDF with liability cosplay."

Jules pins one more line: coordinated scare-posts and fake consensus threads are how light [[influence_campaigns|influence campaigns]] show up at desk scale — pressure on opinions, not just one inbox. We are not a newsroom. We are still a hallway where [[social_engineering|social engineering]] rumors try to become policy.

## Quarantine, gateway, and the path that counts

End of day we sit with a SOC analyst on a short bridge call. Not because I am becoming an investigator. Because the desk is where the humans land, and humans are the sensor the gateway cannot fully replace.

"[[mail_gateway|Mail gateway]] caught a sibling of Maya's message after her report," the analyst says. "We dropped the campaign into [[quarantine|quarantine]], detonated the zip in the [[sandbox|sandbox]], and tuned the rule. User-reported beat the first filter by twelve minutes. That matters. Filters are late sometimes. People who hover are early."

I update the wiki blurb the desk actually reads — short, mean, reusable: hover the link, check the real host, never read codes to callers, never approve surprise MFA, never change wire instructions from a thread, badge your own door, shred the bin, and when something feels like borrowed manners — use the [[phish_report_button|report button]]. That is the [[reporting_path|reporting path]]. The definition on the exam is shorter. The habit is the same.

5:40. Queue noise. Rain louder. I close notes: Maya reported, Sam did not open the zip, Avery wire frozen, Nora hung up on the pretext, Ken ignored the text, Dev denied the pushes, lobby stopped a tailgate, Jordan shredded, gift-card caller got nothing.

Jules clips her bike lights on. "How many attack names did you memorize?"

"None," I say. "I collected a few pressures — [[urgency|urgency]], [[authority|authority]], [[scarcity|scarcity]], [[familiarity|familiarity]], [[consensus|consensus]] — and a few channels — mail, voice, SMS, door, bin — and made people swap hurry for a check."

She almost smiles. "Good. Tomorrow someone will call a [[spoofing|spoofed]] CFO 'probably real because the logo is crisp.' You already have the line."

I badge into the rain and walk toward the MAX. Portland is still raining. The cards in my drawer are still about ports. Today's decisions were about not clicking, not approving, not holding the door, and not treating a story like a ticket that already earned trust.
