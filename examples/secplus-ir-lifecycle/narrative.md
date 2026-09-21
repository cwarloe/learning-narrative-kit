# Portland Desk — The Order You Do It In

*A Security+ incident response precursor • Hover over highlighted terms for exam definitions and supporting desk/network jargon.*

The Monday after a bad Friday, the whole building was under a [[change_freeze|change freeze]], which meant nobody could ship anything that wasn't already on fire. I had been at the desk long enough to have opinions about the queue and not long enough for anyone to want them. Jules had put me on the [[on_call|on-call]] rotation as a shadow, which is a word that means you carry the pager and somebody else carries the decision.

Her sticky note still said *which decision?* I had started to find it annoying in a way that suggested it was working.

## The alert that had cried wolf forty times

The [[soc|SOC]] handed us a queue every morning, and most of it was noise. One rule in particular had fired forty times since August, and forty times somebody had closed it as nothing. I opened the forty-first before my coffee was cool and started typing the same close-out the last person had typed.

Jules did not tell me to stop. She asked what the other forty had in common.

I said they were all the same rule, which was the answer to a different question, and I knew it while I was saying it.

She had me put them side by side in the [[siem|SIEM]], which was the first time I understood why we paid for one. Thirty-nine of them were a backup agent on the same host at the same hour, doing the thing backup agents do. Each of those had been a [[false_positive|false positive]], correctly closed, and closing them had been the right call every time.

Number forty-one was a different host, at four in the morning, on a service account nobody had touched since the last audit.

"So that one's a [[true_positive|true positive]]," I said.

"Probably. That's still you deciding, not the tool." She pulled a chair over. "This part has a name and the name is the boring part. The work is deciding which forty-one you actually look at."

The boring part is [[detection_analysis|detection and analysis]], and it is not reading alerts. It is triage — the alert, the ticket, the thing a user mentions in the hallway — sorted into *real* and *not real* on criteria you can say out loud. Our criteria lived in a table I had scrolled past a dozen times. Impact on one axis, urgency on the other, and where they crossed you got a [[severity|severity]]. A service account authenticating at four in the morning from somewhere it had never been was not the top of that table, but it was not the bottom either.

I asked if this was a [[p1|P1]].

"No. And don't reach for that word, because when you use it the phones start ringing." She logged the severity as the table said and not as the adrenaline said.

## The playbook that did not quite fit

We had a [[playbook|playbook]] for account takeover, and I was glad, because it meant I did not have to invent anything. I opened it and got four steps in before it stopped applying.

Step five said to call the account owner and confirm whether the login was theirs. The account did not have an owner. It had a team, and the team had changed twice, and the last person who had definitely understood what the account did had left in March.

My instinct was to skip step five and keep going. I said so, out loud, which is the only reason it did not happen.

"You can't skip it," Jules said. "You can escalate that it doesn't fit. Those are different."

The distinction turned out to be written down, which surprised me. A playbook is the response guide for a known incident type, so nobody has to design a process at two in the morning. A [[runbook|runbook]] is the how-to for a recurring task — isolate this kind of host, pull these logs, reset credentials in this system — and it is where the actual keystrokes live. When the playbook stops fitting, you have hit a decision the playbook's authors did not anticipate, and the [[irp|incident response plan]] is the document that says whose decision it is. Mine, it turned out, was not on the list.

That whole apparatus — the plan, the playbook, the runbook, the person whose job it is to decide — is what [[incident_response|incident response]] means when people say it like a single word. I had been hearing it as a mood.

Jules called the security lead, and the [[communication_plan|communication plan]] told her which line to use and who else got told. We ended up on a [[bridge_call|bridge call]] with four people, three of whom said almost nothing, which I learned is normal and not a sign that you have wasted their time. Nobody opened a [[war_room|war room]]. Jules said those are for when the coordination itself is the hard part, and at four people on a line it wasn't.

## The order you do it in

By ten I could see the shape of it. The service account had run a scheduled job on a warehouse box, and the box had something on it that had no business being there, and I wanted very badly to reimage the box and go to lunch.

I said that. Jules asked me what order I was planning to do it in.

I said I would clean it and put it back, which sounded fine until I heard the two verbs next to each other with nothing in front of them.

Reimaging the box would have removed the malware, which is [[eradication|eradication]], and restored the service, which is [[recovery|recovery]]. It would also have destroyed the only copy of what had happened, and it would have done nothing about the eleven hours between four in the morning and lunch, during which that account had also been talking to two other hosts.

What goes first is [[containment|containment]], which is the phase where you stop the bleeding before you deep-dive or rebuild. It has two speeds. [[short_term_containment|Short-term containment]] is the ugly fast one: we killed the account's sessions, disabled it, and pulled the warehouse box off its segment inside of ten minutes.

That broke the label printer in receiving, and receiving noticed immediately. A man named Dale called the [[help_desk|help desk]] to say his Monday was ruined, and he was right, and there was no version of the morning where he got to be wrong about that. Jules had me tell him myself. She said the person you inconvenience should hear it from someone who knows why.

Then [[long_term_containment|long-term containment]], which is the version that lets the business keep running while the rest gets planned. Receiving got the label job moved to a spare box on a segment we watched, and it was slower, and Dale said so.

Before anything got cleaned, the security lead had us take a [[forensic_image|forensic image]] of the drive. This is the reason IR tells the desk not to reimage, not to power-cycle, not to tidy up — a bit-for-bit copy is the only version of the box that can answer a question nobody has asked yet. That image, plus the SIEM logs and the ticket trail and a screenshot I had almost not bothered with, was the [[evidence|evidence]]. Because the account touched a system with contract data on it, Legal put a [[legal_hold|legal hold]] on the whole set, which meant our normal thirty-day log rotation stopped for that host and stayed stopped.

Only then did eradication happen, and recovery after it. Recovery was not a moment. The box went back rebuilt, and then it sat on a watched segment for a week to see whether it got quiet or got interesting.

## The part that did not close

At 4:30 I tried to close the ticket and Jules would not let me.

The permanent fix was to give the scheduled job a credential that expired and an owner who existed. That is a change, and the change freeze was still on until Thursday. So the real fix sat in a queue with a date on it, and the thing holding the gap shut in the meantime was a monitoring rule and my pager.

Dale's label job was still on the slow box. Somebody in receiving had started keeping a paper log, and I did not have the standing to tell them to stop.

I asked whether this counted as [[disaster_recovery|disaster recovery]], because both of them end with things being restored. Jules said no, and that people mix them up constantly. Disaster recovery is for when the building floods or the region goes dark — restoring IT after a major outage. This was one host and one account, and the fact that both processes end in the word *recovery* is a coincidence of English.

The [[lessons_learned|lessons learned]] meeting went on the calendar for the following Tuesday. I said something optimistic about it and Jules gave me a look.

"It counts if the playbook is different afterward," she said. "Otherwise it was a meeting."

The gap we found was not a clever one. Nobody knew who owned the account, and nobody had discovered that until it was four in the morning on a live incident. Finding that out earlier is [[preparation|preparation]], and the cheap way to find it is a [[tabletop|tabletop]] — everyone in a room for ninety minutes walking through a scenario, saying out loud who would do what, discovering that the answer to step five is *nobody*. We had run two that year, and neither had used a service account.

I put myself on the watch rotation for the week, because I had been the one who wanted to reimage it, and it felt like the right amount of consequence.

The queue at 5:40 had eleven things in it. Jules clipped her bike lights on and left me the pager.
