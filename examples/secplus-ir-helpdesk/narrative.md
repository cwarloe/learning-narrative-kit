# Portland Desk — When the Ticket Escalates

*A Security+ incident response precursor • Hover over highlighted terms for exam definitions and supporting desk jargon.*

Wednesday rain arrives sideways, which is Portland's way of saying *pay attention.* I am Ethan, still week-something at the [[help_desk|help desk]], and today the queue is not malware Latin or padlock math — it is the moment a messy [[ticket|ticket]] might become a real [[security_incident|security incident]], or might just be loud.

Jules has a sticky under *which decision?* that says *ticket ≠ incident until criteria say so.* Bike helmet on the monitor arm. She is not teaching a Hollywood breach. She is keeping me from declaring war over a flaky printer and from wiping a laptop IR still needs.

"[[incident_response|Incident response]] is a process, not a mood," she says when I reach for a blank card. "Your job as [[first_responder|first responder]] is often the first touch: document, contain when told, [[escalation|escalate]] cleanly, and never freelance [[eradication|eradication]]. Curiosity is not a phase in the lifecycle."

I open the queue. Coffee. Portland doing Portland. First subject: *URGENT SECURITY BREACH — antivirus popped then cleared — CALL ME.*

## The alert that wanted a war room

Ken from sales is already half on a [[bridge_call|bridge call]] he invented in Slack. Caps lock. Screenshot of a green *quarantined successfully* banner. He wants a [[war_room|war room]] and possibly a press release.

"It said threat detected," Ken says. "Then it said cleaned. Am I compromised? Do I burn the laptop? Do I tell the whole channel?"

I pull the [[irp|incident response plan]] cheat sheet Jules laminated for the desk — criteria, not vibes. An AV [[quarantine|quarantine]] that completed on a known adware hash, no lateral movement, no odd logins: that is an [[event|event]]. Observable. Scary to a human. Not automatically a [[security_incident|security incident]].

"This looks like a [[false_positive|false positive]] on severity, or at least a true detection with a finished auto-clean," I say. "We confirm the hash in the ticket, note the time, and close as handled unless [[siem|SIEM]] or [[soc|SOC]] shows friends. We do not blast need-to-know into the sales channel because the banner was red for three seconds."

Ken deflates into a normal ticket. Jules writes on the sticky: *[[severity|severity]] and priority beat adrenaline.* A quiet [[true_positive|true positive]] can wait for process; a loud false alarm should not steal the [[on_call|on-call]] pager.

## Maya and the ticket that earns the word incident

Maya from accounting — padlock alumnus, toolbar survivor — calls with a voice that has decided to be precise.

"Someone reset my MFA at 6:12 a.m. from a city I have never visited," she says. "Then a rule forwarded my invoice folder outward. I did not create the rule. I locked the screen and called you instead of clicking anything heroic."

That is not printer drama. That is criteria.

I open the account-takeover [[playbook|playbook]] — the desk-facing pages, not the novel Legal keeps in a drawer. Jules is already looping [[soc|SOC]]. We are in [[detection_analysis|detection and analysis]]: is this real, how wide, what do we touch first?

"Document every [[ioc|indicator of compromise]] you can see without poking," Jules tells me. "Forwarding rule name, destination address, MFA reset time, source IP if the portal shows it, hostnames. Desk feeds the picture. Desk does not dissect the picture alone."

I write the IoCs into the ticket like a person who has learned that future-me will thank present-me. Then [[escalation|escalation]] to the [[csirt|CSIRT]] queue with facts, not theater. [[severity|Severity]] lands as a high-priority account compromise — not every badge is a [[p1|P1]], but stolen mailbox plus exfil rule earns the serious lane.

Maya asks if she should warn Accounting Slack.

"[[communication_plan|Communication plan]] and [[need_to_know|need-to-know]]," I say. "CSIRT and her manager get the story. The whole floor does not. Gossip is not containment."

## Containment before curious poking

SOC joins a short [[bridge_call|bridge call]]. Calm voices. No movie score.

"[[short_term_containment|Short-term containment]] first," the analyst says. "Disable the account sessions, kill the forward rule, force credential reset after we snapshot what we need. Pull her laptop to [[isolation|isolation]] — cable out, Wi-Fi off — until we say otherwise. Do not reimage. Do not 'just wipe it because it feels cleaner.'"

Maya unplugs like she has been waiting for permission. I feel the flashcard reflex to start deleting rules myself and sit on my hands.

"[[containment|Containment]] before curious poking," Jules murmurs. "If they ask for a [[forensic_image|forensic image]], power-cycling like a gamer can trash volatile [[evidence|evidence]]. If Legal whispers [[legal_hold|legal hold]], we preserve — we do not tidy."

I bag the laptop with a tag and a note: who had it, when, where it sits. That boring paperwork is [[chain_of_custody|chain of custody]] at desk volume — why you do not casually wipe a machine IR still owns.

Short-term buys time. [[long_term_containment|Long-term containment]] shows up as a temporary restricted mailbox path and extra monitoring while CSIRT hunts whether the attacker left other doors. That is still containment, not recovery theater.

## Eradication is not "reimage and ghost"

An engineer on the floor offers helpful chaos: "We can ghost her laptop from the golden image in twenty minutes. Ship a loaner. Done."

"[[recovery|Recovery]] is a phase," Jules says, "after [[eradication|eradication]]. If you reimage before you know what landed, you may erase [[evidence|evidence]] and miss the persistence. Desk does not freelance the rebuild when account takeover or malware is in play. CSIRT owns the order: contain, understand, eradicate, then recover."

The engineer nods, chastened but employed. We issue a loaner with a clean profile and no sync of the poisoned mailbox rules. Maya works from known-good while the imaged disk waits for people whose job title includes "incident."

I update the [[runbook|runbook]] link in the ticket: isolate host, collect IoCs, escalate, preserve when told — not "nuke from orbit because the queue is long."

## Preparation is why 2am Ethan is not inventing process

Afternoon softens. The [[siem|SIEM]] correlation that paired Maya's MFA reset with a rare outbound destination is the kind of gift that makes desk tickets look smarter than they feel. Our ticket notes are now rows in someone else's timeline. That is the deal: desk is often [[first_responder|first responder]]; CSIRT is the handoff target.

Jules slides over a one-pager from last quarter's [[tabletop|tabletop exercise]] — paper ransomware, fake phishing, the awkward silence when nobody knew who called Legal. [[preparation|Preparation]] looks boring until Wednesday sideways rain. Playbooks, contacts, who pages [[on_call|on-call]], when a [[change_freeze|change freeze]] lands so nobody "helps" by deploying mid-hunt.

"[[irp|IRP]] says who owns what," she says. "[[playbook|Playbook]] says how this flavor goes. [[runbook|Runbook]] says which button. You are not supposed to invent IR at 2 a.m. with cold coffee and a heroic streak."

I ask where [[disaster_recovery|disaster recovery]] fits, because a vendor email used the words interchangeably.

"Related cousin, different fire," Jules says. "DR is flooded building, dead datacenter, big restore. This is IR — compromise, policy violation, attacker math. Do not wait for a generator to fix a stolen mailbox."


## The printer that almost stole the pager

Before Maya's call fully settles, Facilities opens a ticket titled *SECURITY INCIDENT — badge reader offline — building unsafe!!!* The reader is blinking amber because a firmware update stalled. No tailgating report. No forced door. Just a reader that wants a reboot and a human who watched too much cable news.

"[[event|Event]]," I tell the tech on site. "Maybe even an availability headache. Not a [[security_incident|security incident]] until someone is bypassing controls or we have criteria. Reboot per the Facilities [[runbook|runbook]]. If the door fails open in a weird way, then we escalate. Caps lock in the subject line is not a severity classifier."

Jules adds the line to the wiki: *the desk protects IR attention like a scarce resource.* Every false [[p1|P1]] trains people to ignore the next one. Every calm close of a non-incident is also [[incident_response|incident response]] maturity — knowing when not to open the [[war_room|war room]].

## What desk writes so SIEM can think

While Maya's laptop sits tagged on the evidence shelf, SOC asks me to paste the ticket timeline into their case. Timestamps. Who called. What I saw in the mail portal. What I did not touch. The [[siem|SIEM]] already has auth logs; it does not have Maya's sentence *I locked the screen and called you instead of clicking anything heroic.* That sentence is desk gold.

"Correlation likes human context," the analyst says. "Your ticket is a sensor with a personality. Keep writing like someone who expects a [[lessons_learned|lessons learned]] review to read it cold on Friday."

I feel briefly like a real [[first_responder|first responder]] and then remember the sticky: escalate cleanly, do not freelance. Feeling useful is not a license to run `diskpart` for fun.

## Loaner life and the change freeze

Ops declares a soft [[change_freeze|change freeze]] on mailbox transport rules and identity providers for the afternoon — not because the building flooded ([[disaster_recovery|disaster recovery]] still sleeps), but because IR wants the glass still while they look for other doors. A developer tries to push an "emergency" SSO tweak anyway. The [[on_call|on-call]] page goes to Jules, who redirects with the kindness of a bike lock.

"Freeze means freeze," she says. "Your tweak can wait until [[containment|containment]] says the window is safe. Hero deploys during IR are how we get a second incident shaped like help."

Maya works on the loaner. She asks once more whether she should post a PSA to the all-hands channel. I shake my head and point at [[need_to_know|need-to-know]] on the sticky. CSIRT will craft the message if one is needed. Desk does not freelance the megaphone either.

## Lessons learned closes the loop

End of day, CSIRT schedules a short [[lessons_learned|lessons learned]] huddle for Friday — not a blame séance. What IoCs desk caught early. What almost got Slack-blasted. Whether short-term containment was fast enough. Whether the playbook page for mailbox rules was findable by a week-something Ethan.

I draft the desk blurb while the rain argues with the MAX outside:

Not every scary ticket is an incident — severity and criteria matter. Containment before curious poking; preserve evidence when IR says so. Desk is often first touch: document IoCs, escalate cleanly, do not freelance eradication. Recovery is not "reimage and ghost" without the IR steps when malware or account takeover is in play. Lessons learned closes the loop; playbooks exist so 2 a.m. you is not inventing process.

Maya texts that her loaner works and her real mailbox is still in timeout. Ken apologizes for the war-room cosplay. The AV false alarm ticket stays closed, correctly boring.

## The line that sticks

5:45. Queue quieter. I rewrite the sticky Jules will actually keep:

Event ≠ incident. Detect and analyze before you name it. Contain (short, then durable) before you poke. Preserve chain of custody when told. Escalate to CSIRT with IoCs, not vibes. Quarantine and isolation are verbs. Eradicate, then recover. Communicate on need-to-know. True positives earn process; false positives earn a calm close. SIEM likes your careful tickets. Tabletop and IRP are preparation. This is IR, not DR.

Jules clips her bike lights on. "How many phases did you memorize?"

"Six shapes," I say. "Preparation, detection and analysis, containment, eradication, recovery, lessons learned — and a desk rule: I am first touch, not freelance forensics."

She nods once. "When the ticket escalates, you do not escalate your ego with it."

I shut the laptop. The queue shows one more subject line starting with URGENT. I open it anyway — criteria first, adrenaline second. That, for Wednesday, is enough.
