# Portland Desk, Chapters 1–2: Adversarial Review

**Scope.** This review covers "The Paper Cert" (`examples/a-plus-hardware-helpdesk/narrative.md`, Chapter 1, Gresham warehouse) and "The Live Board" (`examples/a-plus-os-helpdesk/narrative.md`, Chapter 2, Portland ROC). They are identical to `/workspace/sorkin-desk/portland-desk/narrative/01` and `02`. I read both chapters in full. This is a story-craft review only. Technical accuracy was handled in the 2026-10-22 nitpick pass and is not reopened here.

## Verdict

These are two well-lit rooms where the problems arrive already labeled and leave without paying the check. Chapter 2 is close to working because Jules keeps taking the wheel away from Ethan, but Chapter 1 is a solo hero montage with a toolbox, and Chapter 2's opening paragraph cashes that montage in as a clean win before the reader has seen whether Ethan actually beat the clock.

## What to protect

- **Ken blocking the cabinet latch with his clipboard.** "Don't guess, Ethan." That is the best line in either chapter. It is a person, not a manual, stopping Ethan from doing something stupid, and it is exactly the kind of help Charles is asking for.
- **The second failure in Chapter 1.** The pin gets straightened, Ethan expects victory, and the screen gets *worse*: fourteen thousand framing faults per second. That is a real reversal. Keep it, and build more like it.
- **The dead phone signal.** "The signal in the high-bay metal building was weak." Someone on the team already sensed the internet-rescue problem and closed that door. Good. Lock it.
- **Jules's mute button.** Jules cutting Ethan off mid-promise to re-image Maya's machine is a mentor intervening at the moment of a bad decision, with a cost attached (two hours, certificates, Maya's shortcuts). That is the model for the whole book.
- **Both chapter endings stop on a question.** Neither ends on a hug. Chapter 1 ends with Ken's deadline running and the DIP switches untouched; Chapter 2 ends with eighteen services and the Event Viewer unopened. That instinct is right. The problem is what the *next* chapter does with it.
- **Canon.** Harrowmere is named, the Gresham warehouse comes first, the Portland ROC desk under Jules comes second, and Ethan moves from the dock to the ROC by internal referral rather than by relocating. No canon drift in the chapter bodies. (See problem 6 for two small continuity snags.)

## Problems, ranked by cost

### 1. Chapter 2 resolves Chapter 1's cliffhanger offstage, as a total win, in a subordinate clause.

Chapter 1 ends at 4:20 a.m. with Seattle forty minutes from canceling and the clock divider unknown. Chapter 2's first paragraph then tells us that Ken's letter certifies "that I had diagnosed and restored the main sorting line under live dispatch pressure." So he made it. Cleanly. Nobody lost a trailer, nobody got written up, and the cost of the night is zero. Every bit of tension Chapter 1 built is refunded at the door of Chapter 2. This is the single most expensive line in the two chapters, because it teaches the reader that cliffhangers in this book are decorative.

**Fix.** Let the night cost something and carry the bill forward. Ethan fixes the baud rate at 5:11, and Seattle rolls, but Boise does not. Or the line comes back, but the Kapton-taped ribbon cable is a field patch that fails again in week two, and the maintenance tech who has to replace it properly is not grateful. Ken's letter can still exist, but make it honest: "He got it back up. He was late. He didn't quit." Jules should read that letter, and she should notice the word "late."

### 2. Ethan arrives in Chapter 1 with a fully stocked competence kit and no explanation of how he earned it.

The chapter's premise is that Ethan's flashcard knowledge is an illusion ("That illusion shattered"). Then, two minutes later, he walks to a workbench where his father's toolbox happens to be waiting, pulls out a *calibrated* multimeter and a roll of Kapton tape, measures three rails to two decimal places, identifies the fourth conductor of a forty-conductor ribbon as the culprit, and fixes a bent RS-232 pin with a drafting pencil whose brass sleeve "measured exactly 0.5 millimeters across." The chapter tells us paper certs are worthless and then hands the paper-cert kid every skill the paper promised. The machinist father is doing a lot of quiet work here, but the page never shows Ethan learning anything from him; it only shows Ethan owning his tools.

**Fix.** Pick one competence Ethan legitimately has, and earn it on the page with a single specific memory of his father. Measuring voltage is a fair choice for a machinist's son. Then make everything after that harder. He finds the short, but it takes him three wrong places first, and in one of them he pulls a connector he should not have. The pencil trick should be his father's trick that he half remembers, and the first attempt should snap the pin, or nearly snap it, so the second attempt costs time and nerve.

### 3. Chapter 1 has no second human who knows anything.

Ken supervises, counts minutes, and makes threats. Nobody else on a graveyard warehouse floor at 2:24 a.m. knows the scale, the sorter, or the vendor. That is not how warehouses work, and it is not how this book says expertise should arrive. The track bible says expert content arrives through mentor dialogue. Chapter 1 has no mentor, so the expertise arrives through Ethan's hands alone, which is exactly the "sudden skill" pattern Charles flagged.

**Fix.** Add a maintenance tech or a scale vendor on the phone. Give that person one useful sentence and one wrong one. For example, a day-shift maintenance lead on a crackling call says, "That scale was reset to factory last month; it's probably at 9600," and he is wrong, because someone changed it to 4800 and did not write it down. Ethan has to choose between a person with seniority and the evidence on his screen. That is friction, it is human, and it sets up the lab without solving it.

### 4. Chapter 2 hands Ethan Safe Mode and BitLocker as if he has done them a hundred times.

Jules sets the rules: "You listen on the secondary channel, observe the telemetry, and walk me through your diagnostic tree before anyone touches a setting." Then Ethan immediately reboots a payroll supervisor's machine into Safe Mode without walking Jules through anything, and when BitLocker throws a recovery screen he says, "Don't worry, Maya. That's just BitLocker," and reads her the key in one clean pass. Maya's voice is "softening as I asked deliberate questions." Safe Mode works on the first try. That is three free wins in a row, and the one rule Jules set is broken without consequence.

**Fix.** Make the BitLocker screen land on Ethan, not Maya. He did not expect it, and for a few seconds he has no idea where the recovery key lives. Jules does not rescue him with the answer; she says, "Where would the company keep that?" and lets him find it, slowly, while Maya says something sharp. Then Jules should note, after the call, that he changed Maya's boot state before telling her his tree, which was the one rule she gave him. That is a partial fix with a real mark against him, and it belongs on the evaluation sheet.

### 5. Maya is a deadline, not a person.

Maya exists to be anxious, to report a symptom cleanly, and to soften when Ethan is polite. She gives him the key clue ("Windows displayed a message saying it had installed automatic maintenance updates") unprompted and in perfect order. Real users bury the clue under three wrong ones. Because Maya is frictionless, Ethan's questioning skill is never tested, and the reader never sees a help-desk call go sideways.

**Fix.** Make Maya wrong about something important. She swears nothing changed, and only later, annoyed, mentions the update message she dismissed. Or she insists the frozen screens are a hardware problem and wants a new computer today. Give her one line of her own that is not about the deadline. She will become someone the reader remembers, and the clue becomes something Ethan has to dig out rather than receive.

### 6. Small continuity snags that make the world feel assembled rather than lived in.

These are not canon drift in the chapter bodies, but they will bother careful readers.

- The course README calls Ethan twenty, and Chapter 1 says "I was twenty-one years old." Pick one.
- Chapter 2 says "fourteen months on the concrete docks." The prologue is set in July, Chapter 1 is "late-winter," and Chapter 2 is August after six months of rotation. The arithmetic can work, but only if someone writes it down once in the bible.
- Chapter 1 describes the display as "amber monochrome monitor" and later as "the amber CRT monitor." A reader who notices will stop trusting the room.
- The course README lists a "Willamette River plant" as a Harrowmere site. Nothing in Chapters 1–2 uses it, but if it shows up later as a place Ethan works, that is drift away from the approved Gresham-then-ROC path. Flag it before a later chapter takes it literally.

### 7. Jules talks like the exam guide.

"You walk the CompTIA troubleshooting methodology, and you start by forming a theory you can actually test." That is a correct sentence, and no desk lead has ever said it out loud. The track bible calls Jules a conversational coach. Here she is a narrator in a bicycle helmet. Her best moment is the mute button; her worst moments are when she recites.

**Fix.** Let Jules teach through stories and questions, and let the methodology name appear in Ethan's narration later, as the thing he realizes she was describing. "You don't burn down the house because a light switch flickers" is good. Keep the metaphors and cut the syllabus.

## Revision moves

1. **Rewrite the first paragraph of Chapter 2 so Chapter 1's night has a cost.** Ethan restores the line late, at least one trailer misses, and the Kapton patch is a known temporary fix. Ken's letter should mention the delay, and Jules should ask about it in the interview. That single change makes both chapters stronger at once.
2. **Put a second person on the warehouse floor in Chapter 1.** A maintenance lead or a scale vendor on the phone gives one useful fact and one confident wrong one. Ethan has to weigh that person against the evidence, and the wrong advice costs him ten minutes he does not have.
3. **Take away one of Ethan's tools or tricks in Chapter 1, and make another one fail on the first attempt.** He should not have a calibrated meter and Kapton tape just lying on his bench. Make him borrow the meter from maintenance, and make the pencil-sleeve trick go wrong once before it goes right.
4. **Make the BitLocker screen Ethan's problem in Chapter 2, and have Jules make him find the key himself.** After the call, Jules should mark him down for changing Maya's boot state before walking her through his tree. Ethan should carry that mark into Chapter 3 as something he is trying to live down.
5. **Give Maya one wrong belief and one line that is not about the deadline.** The update clue should come out late and grudgingly, and her frustration should be about something specific to her, not just the twenty-eight supervisors.

## Closing

The team has good instincts: they built a dead phone, a worse second failure, and a mentor who grabs the mute button. Now they need the nerve to let those choices cost something. A competent hero is fine. A hero who never pays for anything is a brochure. Make Ethan late, make him wrong in front of Jules, and make him walk into Chapter 3 with something still on his record. Readers will follow a junior tech who keeps getting knocked down a lot further than one who keeps getting lucky.
