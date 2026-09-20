# Portland Desk — When the Ticket Escalates

*A Security+ incident response precursor • Hover over highlighted terms after they have earned their keep.*

Wednesday rain arrives sideways. I am Ethan, week-something at the desk. The queue is already yelling.

Jules's sticky still says *which decision?* I have not read it yet. I am reading subject lines.

## Maya and the laptop that must die

First ticket: *PC possessed — ads, slowness, standup in twelve — please wipe.*

Maya is at the glass with the machine under her arm like a guilty dog. "Just reimage it. I have a meeting."

I believe her. Possessed is a word that wants a fire. I take the laptop, yank the Ethernet, and I am already in the imaging USB drawer when Jules's coffee mug appears on my cube wall.

"What did it do," she says, "besides scare you?"

I tell her ads, slowness, AV popped something. She does not take the USB. She takes the laptop, plugs it into a throwaway dongle, and opens the AV history I did not open.

Known adware hash. Quarantine completed at 7:41. No odd logins. No new local admins. No other hosts talking to it.

"You were about to kill the only copy of a nothingburger," she says. "And if it had been something, you were about to kill the only copy of the something."

I put the USB back. My hands were too fast for my criteria.

She makes me write the ticket again, slower. Observable. Scary to a human. Not a [[security_incident|security incident]] until the plan says so. This one is an [[event|event]]: the [[quarantine|quarantine]] already did the verb. I return Maya her laptop with the adware gone and her standup intact. I do not get to feel heroic. I get to feel like I almost paid for a feeling.

Jules puts the imaging USB on her side of the wall. "You can have it back when you can say why you should not."

## The quiet mailbox

The next subject line is almost polite. *Can't see my Sent. Also a rule I did not make.*

Finance Maya this time. She is not asking for a wipe. She is asking why her own mail is leaving without her.

I do not reach for the USB. I open the portal the way Jules opened the AV log. A forwarding rule to a domain that is almost ours and not ours. An MFA reset at 2:13 a.m. from an IP that has never bought coffee in Portland.

This time the scare is quiet, which is how the real ones dress.

I disable the rule because leaving it up is still the crime in progress. I do not go hunting in the mailbox for souvenirs. I do not tell Accounting Slack to panic. I write what I can see without poking: rule name, destination, reset time, source IP, hostname. Those are [[ioc|indicators of compromise]] because they are facts that will still matter after I go home.

Then [[escalation|escalation]] to the [[csirt|CSIRT]] queue. Not theater. Stolen mailbox plus an exfil rule earns the serious lane.

Finance Maya asks if she should warn the channel. I say no. Need-to-know is not rudeness. It is how you keep the person who made the rule from watching us watch them.

Jules has me bag the laptop Finance Maya also brought, "just in case." Tag, time, who had it, where it sits. Boring. That boredom is [[chain_of_custody|chain of custody]] at desk volume.

I almost say *I learned the phases.* I do not. I learned that my first useful move today was an undo.

## After the rain

5:45. Queue quieter. Jules clips her bike lights on.

"Tell Wednesday," she says, "without listing a lifecycle."

I tell her: I nearly wiped a loud nothing. I stopped a quiet something without turning it into a parade. I am first touch, not freelance forensics.

She nods once. "When the ticket escalates, you do not escalate your ego with it."

The queue shows one more URGENT. I open it anyway — criteria first, adrenaline second. That, for Wednesday, is enough.
