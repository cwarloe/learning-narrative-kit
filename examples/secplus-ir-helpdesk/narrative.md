# Portland Desk — When the Ticket Escalates

*A Security+ incident response precursor • Hover over highlighted terms after they have earned their keep.*

The rain came in sideways on Wednesday, hard enough that the lobby mat was already soaked when I sat down. I had a queue full of subject lines in all caps and a USB drawer I trusted too much.

Jules's sticky still said *which decision?* I had not looked at it yet. I was looking at the first ticket.

## Maya and the laptop that must die

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

Finance this time — a different Maya, mailboxes, not laptops. She was not asking for a wipe. She was asking why her own mail was leaving without her.

I did not reach for the USB. I opened the portal the way Jules had opened the AV log. A forwarding rule to a domain that was almost ours and not ours. An MFA reset at 2:13 a.m. from an IP that had never bought coffee in Portland.

This time the scare was quiet, which is how the real ones dress.

I disabled the rule because leaving it up was still the crime in progress. I did not go hunting in the mailbox for souvenirs. I did not tell Accounting Slack to panic. I wrote what I could see without poking: rule name, destination, reset time, source IP, hostname. Those were [[ioc|indicators of compromise]] because they were facts that would still matter after I went home.

Then [[escalation|escalation]] to the [[csirt|CSIRT]] queue. Stolen mailbox plus an exfil rule earned the serious lane. Nobody asked me to feel dramatic about it.

She asked if she should warn the channel. I said no. [[need_to_know|Need-to-know]] is how you keep the person who made the rule from watching us watch them. She did not like that answer. She accepted it the way people accept a locked door.

Jules had me bag the laptop she had also brought, "just in case." Tag, time, who had it, where it sat. That boredom is [[chain_of_custody|chain of custody]] at desk volume.

I almost said I had learned the phases. I did not. I had learned that my first useful move of the day was an undo.

## After the rain

At 5:45 the queue was quieter. Jules clipped her bike lights on.

"Tell Wednesday," she said, "without listing a lifecycle."

I told her: I had nearly wiped a loud nothing. I had stopped a quiet something without turning it into a parade. I am [[first_responder|first touch]], not freelance forensics.

She nodded once, then remembered the USB on her wall. "Keep asking what it did before you decide what it is."

The queue showed one more URGENT. I opened it anyway — criteria first, adrenaline second. The subject was louder than the evidence. I left it in the queue with a note, and I left the imaging USB where she had put it.
