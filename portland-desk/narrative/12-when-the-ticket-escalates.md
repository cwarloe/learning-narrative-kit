# Portland Desk — When the Ticket Escalates

*A Security+ incident response precursor • Hover over highlighted terms after they have earned their keep.*

A gusting Wednesday rain swept across the Willamette as I stepped onto the fourth floor. Eleven months on the service desk had taught me that the quietest tickets are often the ones carrying the sharpest edges. On the bezel of her monitor, Jules's sticky note still asked *Which decision?* under the fluorescent lights.

## Maya and the laptop that must die

```callout-panel
title: "FIGURE 12.1: LIVE FORENSIC MEMORY CAPTURE & ORDER OF VOLATILITY"
badge: "Incident Response"
caption: "Forensic bench diagram: An isolated, live running laptop on an ESD mat with a write-blocking USB capture tool acquiring volatile RAM (RFC 3227) before power-down and physical storage disk acquisition."
prompt: "Clean technical cutaway illustration of a computer forensic examination bench under bright laboratory lighting. A running laptop sits on an ESD mat connected via USB to a dedicated forensic memory acquisition dongle with glowing green status LEDs. Evidence tags and documentation binder nearby. Sharp technical linework, no text, no words. 16:9 ratio."
```

The subject was *PC possessed — ads, slowness, standup in twelve — please wipe.*

Maya stood at the glass with the machine under her arm. "Just reimage it. I have a meeting."

I believed her. Possessed is a word that wants a fire. I took the laptop, [[isolation|yanked the Ethernet]], and I was already in the imaging USB drawer when Jules set her coffee mug on my cube wall.

"What did it do," she said, "besides scare you?"

I told her ads, slowness, AV popped something. She did not take the USB. She took the laptop, plugged it into a throwaway dongle, and opened the AV history I had not opened.

Known adware hash. Quarantine completed at 7:41. No odd logins. No new local admins. No other hosts talking to it.

"You were about to kill the only copy of a nothingburger," she said. "And if it had been something, you were about to kill the only copy of the something."

I put the USB back. My hands had been too fast for my criteria.

She made me write the [[ticket|ticket]] again, slower. Observable. Scary to a human. Not a [[security_incident|security incident]] until the plan said so. This one was an [[event|event]]: the [[quarantine|quarantine]] had already done the verb. I returned Maya her laptop with the adware gone and her standup intact. I did not get to feel heroic. I got to feel like I had almost paid for a feeling.

Jules put the imaging USB on her side of the wall. "You can have it back when you can say why you should not."

## The quiet mailbox

The next subject line was almost polite. *Can't see my Sent. Also a rule I did not make.*

Finance this time — Elena from payroll audit, mailboxes, not laptops. She was not asking for a wipe. She was asking why her own mail was leaving without her.

I did not reach for the USB. I opened the portal the way Jules had opened the AV log. A forwarding rule to a domain that was almost ours and not ours. An MFA reset at 2:13 a.m. from an IP that had never bought coffee in Portland.

This time the scare was quiet, which is how the real ones dress.

I disabled the rule because leaving it up was still the crime in progress. I did not go hunting in the mailbox for souvenirs. I did not tell Accounting Slack to panic. I wrote what I could see without poking: rule name, destination, reset time, source IP, hostname. Those were [[ioc|indicators of compromise]] because they were facts that would still matter after I went home.

Then [[escalation|escalation]] to the [[csirt|CSIRT]] queue. Stolen mailbox plus an exfil rule earned the serious lane. Nobody asked me to feel dramatic about it.

She asked if she should warn the channel. I said no. [[need_to_know|Need-to-know]] is how you keep the person who made the rule from watching us watch them. She did not like that answer. She accepted it the way people accept a locked door.

Jules had me bag the laptop she had also brought, "just in case." Tag, time, who had it, where it sat. That boredom is [[chain_of_custody|chain of custody]] at desk volume.

I almost said I had learned the phases. I did not. I had learned that my first useful move of the day was an undo.

Jules set a red binder and an anti-static evidence pouch onto my desk. "We have an active credential compromise, a live exfiltration rule, and an endpoint that was touched," Jules said, handing me an anti-static pouch. "Remember your Order of Volatility, Ethan. If you pull the plug, live RAM evaporates. If you leave the NIC up, the adversary moves. Isolate the interface, dump volatile memory to the forensic drive, hash the image, and get the chain of custody logged before the CSIRT team arrives."

## The Handoff Gate

```bridge-card
title: Portland Desk Lab: The Incident Escalation & SOC Handoff Crucible
target: workbench/12-when-the-ticket-escalates.md
domain: CompTIA Security+ SY0-701 • Domain 4.0 Incident Response & Operations
badge: Final Capstone Lab
cta: Take the Ticket & Open the Lab ->
---
Step onto Ethan's shift for the Book 0 Final Capstone: navigate multi-stage incident triage, execute Order of Volatility and cryptographic evidence hashing, master the 5-case CBYT prediction gate, and deliver the formal CSIRT Incident Handoff Dossier to Jules Brooks.
```
