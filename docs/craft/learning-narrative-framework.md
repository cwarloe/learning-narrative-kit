# Learning Narrative Framework: Make the Story Pay for the Lesson

This is a portable craft standard for any story in the kit, including Portland Desk, Tamarack, ITM, and whatever comes next. It grew out of an adversarial review of Portland Desk Chapters 00–2 ([PR #29](https://github.com/cwarloe/learning-narrative-kit/pull/29)), but nothing in it is specific to Ethan or to IT.

It sits on top of the rules that already exist. It does not replace them.

- `schema/README.md` is still the authoring contract, and it still wins on conflict. That contract includes beat structure (goal, complication, pivot), the cover test, and term placement.
- `schema/VOICE.md` already names the core failure as **"resolution the situation hasn't paid for."** This framework is the long version of that one paragraph, with tools for preventing it before the draft exists.
- `schema/BRIEF.md` already has `endings: cost`, and the plan gate in `AGENTS.md` already demands `cost` and `carries_forward` for each chapter. This document explains what a good answer in those fields looks like.
- Track bibles (for example `examples/PORTLAND_DESK.md` and `docs/research/PORTLAND_AUTHOR_BIBLE.md`) still own canon: who the characters are, where they work, and what happens in each episode. Where this framework and a bible disagree, the disagreement is listed in [Known conflicts](#known-conflicts-with-existing-rules) for the author to decide. It is not settled here.

## The problem in one paragraph

A learning narrative fails in a specific, repeatable way. The protagonist meets a problem, suddenly knows the right skill or finds the right answer, applies it, and the chapter ends with the problem solved and everyone fine. Every term got used. Nothing was learned, because the reader watched competence appear rather than form. Worse, the reader walks away with a false model of the work: that insight is instant, that the first fix holds, and that users comply once someone explains things. A training story teaches through its shape as well as its terms, and a tidy shape teaches something untrue.

## The six principles

### 1. Competence is earned on the page.

The protagonist may only use a skill the reader has watched them acquire, or one the story has plainly established that they already had. "He's a machinist's son" does not license a calibrated meter, perfect technique, and a tool that happens to fit exactly. A skill shows up once as a struggle before it shows up as a strength.

The same rule applies to information. **No perfect answer arrives from outside.** A search result, a vendor document, a forum post, or a manual that contains exactly the needed fact is the same cheat as a sudden skill. If the story needs outside information, make it partial, out of date, written for a different model, or correct only once the protagonist works out which half to trust.

*Test it like this:* For every competent act in the chapter, point to where the reader saw it learned or established. If you can't, the act is unearned.

### 2. Every win has a cost or leaves something behind.

This is the existing pivot rule from `schema/README.md` ("What gets decided, and what does it cost?"), applied all the way to the end of the chapter. A cost is something the decision charged. Possible costs include time, money, goodwill, a capability the user liked, a temporary patch that now has to be watched, a mark on someone's record, or a relationship that is now strained. Weather and exhaustion do not count. A bruise is texture, and texture is not a cost unless it changes what happens next.

There are two kinds, and a good chapter usually has both:

- **Cost** is what the win took. The fix took so long that a trailer missed its slot.
- **Residue** is what the win left. The fix is held together with tape, or the user is still annoyed and will be back.

*Test it like this:* Finish this sentence in a single clause: "It worked, but ___." If the blank is empty or decorative, the win is free, and a free win teaches nothing.

### 3. Help comes from people, and it leaves debts.

When the protagonist cannot get there alone, help should come from a person: a mentor, a coworker, a user, a vendor on a bad phone line, or a parent at a kitchen table. Help from people is better for learning than help from magic because people can be partly wrong, can want something in return, and can remember what happened.

Rules for helpers:

- **Mentors give direction, not the answer.** This repeats `docs/research/PEDAGOGICAL_AGENCY_ARCHITECTURE.md` ("a compass, not a cheat sheet"), and it is right.
- **A helper is allowed to be wrong.** One confident wrong fact from a senior person is one of the most useful things a story can contain. It forces the learner to weigh evidence against authority, which is a real job skill.
- **Help creates a debt.** The coworker who covered the queue wants a favor. The mentor who stepped in now watches more closely. The parent who gave the speech wants to hear how the test went. Collect the debt in a later chapter.
- **A helper does not appear, solve the chapter, and leave.** If a helper exists only to deliver the key idea, they are an oracle, and an oracle is magic wearing a person costume.

*Test it like this:* For each helper, ask what they got wrong, what they wanted, and when they come back.

### 4. Mistakes and partial fixes are where the learning happens.

The reader learns most at the moment the obvious move fails. This is already how `schema/README.md` defines the complication: the habit is the complication, and the replacement is the pivot. Build chapters so the protagonist makes at least one real wrong turn. A real wrong turn costs something and is visible to someone else. It is not a near-miss that the narrator catches in time.

Partial fixes beat clean ones. The first fix should solve part of the problem, reveal a second one, or make things worse (the pin gets straightened and the garbage on the screen gets faster). The protagonist should get it right on the second attempt rather than the first, and the reader should be able to see why the second attempt was different.

The track rule still applies: **the narrator may feel lost, but the reader must not** (`examples/PORTLAND_DESK.md`). A wrong turn has to be legible. The reader should see why it was tempting and why it was wrong, even if the protagonist only sees it later.

*Test it like this:* Name the wrong turn, who saw it, and what it cost. Then name the partial fix and what it exposed.

### 5. Chapter endings carry forward.

A chapter should not end with the problem closed, the queue empty, and the lesson stated. It should end on something unresolved that the next chapter has to deal with: a debt, a patch, a grudge, an open question, or a reputation that has to be lived up to or lived down. The Portland bible already says this well: "Let scenes end flat... an irritated user accepting a compromise."

Just as important, **the next chapter must collect it.** A cliffhanger that the following chapter resolves offstage in one subordinate clause, as a total win, is worse than no cliffhanger at all, because it teaches the reader that endings in this book are decorative. If Chapter N leaves something open, Chapter N+1 has to show its consequence, even briefly.

Do not end on a line that explains the chapter. `schema/VOICE.md` already says to cut it.

*Test it like this:* Write the "carries forward" item in one sentence, then name the scene in the next chapter where it gets collected.

### 6. Each learning objective sits on a dramatic beat, not a lecture.

Every objective the chapter is responsible for should be attached to a decision someone has to make under pressure. The concept should be what makes the obvious move wrong (the complication) or what makes the hard choice possible (the pivot). This is the existing term-placement rule, generalized from marked terms to objectives.

A lecture is any passage where the concept is explained and nothing is at stake while it is being explained. Mentors reciting frameworks, narrators summarizing a methodology, and glossary-shaped paragraphs all count. When a concept needs explaining, let it arrive as a correction to a misunderstanding someone just acted on. A misconception that is voiced and then fixed teaches better than the right answer stated cleanly (`schema/README.md`).

*Test it like this:* For each objective, name the beat, the decision, and the person who would have made the wrong call without it. An objective with no beat is a lecture, and the cover test will not always catch it.

## Keeping it proportionate

Friction is not melodrama. Portland Desk is "Goldratt-style: people talking decisions through tickets, not melodrama," and that tone is right for every track. Costs should be the size of real workplace costs: a missed trailer, an hour lost, a user who stays annoyed, a mark on an evaluation. Nobody needs to get fired in every chapter. A small, specific cost that carries forward beats a large one that is forgotten by the next page.

Early chapters can be gentler, since a beginner reader needs some safety. Gentler means smaller costs, not zero costs.

## Checklist

### Before drafting (run it on the plan or brief)

1. **Goal, complication, pivot, cost, and carry-forward are each one sentence.** If any of them is blank or vague, do not draft yet. (These match the plan fields `AGENTS.md` already gates on.)
2. **Every skill the protagonist will use is either established earlier or learned on the page in this chapter.** List them.
3. **At least one wrong turn is planned.** It is visible to someone and costs something.
4. **The first fix is planned to be partial.**
5. **Every outside source of information (search, manual, vendor) is planned to be incomplete or partly wrong.** If none is needed, so much the better.
6. **Each helper has a planned error, want, or return appearance.**
7. **Each learning objective is mapped to a beat and a decision.** None of them is mapped to an explanation.
8. **The previous chapter's carry-forward item is collected somewhere in this chapter.**
9. **Canon is checked against the track bible.** That means people, places, employer, and timeline. For Portland Desk, Ethan works at Harrowmere's Gresham warehouse and then the Portland ROC help desk under Jules, and he never relocates.

### Before merging (run it on the draft)

1. **The "It worked, but ___" sentence has a real answer** for every win in the chapter.
2. **No competent act is unexplained.** Point to where each one was earned.
3. **No search result, document, or stranger delivers exactly the needed answer.**
4. **The protagonist was wrong at least once, on the page, in front of someone.**
5. **Every helper got something wrong, wanted something, or will be back.**
6. **The ending leaves something open, and the last line does not explain the chapter.**
7. **The previous chapter's open thread was collected on the page,** not refunded in a summary sentence.
8. **Each objective lives in a decision, and no passage is a lecture with nothing at stake.**
9. **The costs are proportionate.** The chapter is not melodrama, and the reader is never lost even when the narrator is.
10. **The existing gates still pass:** `validate_unit.py`, the cover test, density, term placement, and the `schema/VOICE.md` repair pass.


## Decision (Charles, 2026-10-26): the learner is safe, Ethan is not

- "Satisfying conclusion" is not a rule. No research in the kit requires it; it was a design choice in the pedagogy doc. The learner's satisfaction comes from the workbench: they solve the worked example completely, then apply it to at least one more example there. Ethan's chapter ending does not have to be satisfying. He can learn the concept the hard way, pay for it, and move on.
- "Zero test anxiety" applies only to the learner, and the workbench already gives them a safe place to practice. Ethan can have as much test anxiety as the story needs.
- Ethan is the punching bag. He can struggle with anxiety, distraction, bad reactions to certain kinds of questions, or a learning disability he discovers along the way. Give him the problems real learners are likely to have, with real consequences, and let him work through them on the page. Keep it realistic, though: Ethan is not a "Mr. Glass" who is broken in every way. Give him a small, consistent set of personal struggles that fits who he is. Bring in other common problems vicariously, through coworkers' incidents, tickets he reads, war stories from mentors, or things he overhears. The rule of thumb is that each chapter costs Ethan something real, but not every lesson has to be his own pain.
- Keep the passive-playback guard from the pedagogy doc. Ethan's hard-won lesson should not spend the learner's discovery for them. The workbench is still where the reader solves it.

## Worked example: Portland Desk Chapters 00–2

These are short illustrations of each principle drawn from the review. The full review is in PR #29.

- **Unearned competence.** In Chapter 1, Ethan's flashcard knowledge is called an illusion, and two minutes later he has a calibrated meter, Kapton tape, and a pencil sleeve that "measured exactly 0.5 millimeters across." A better version plants one meter skill in Chapter 00 and makes the pencil trick fail once.
- **Free win.** In Chapter 00, he goes from 58% to 742 in thirty-six hours on the strength of one speech and four rubber bands. A better version has a second practice test that still comes back under the line.
- **Oracle helper.** The father gives a perfect speech and walks out of the story. A better version has him concede one point, then come back to ask about the score.
- **A refunded cliffhanger.** Chapter 1 ends at 4:20 a.m. with Seattle at risk. Chapter 2's first paragraph says the line was restored, and that is the end of it. A better version shows the delay and makes Jules ask about it.
- **A rule broken for free.** Jules says to walk her through the plan before touching settings. Ethan touches settings right away, and nothing happens. A better version has her mark it down, and he carries the mark into Chapter 3.
- **What already works.** Ken blocking the cabinet with his clipboard ("Don't guess, Ethan"), the fix that makes the screen worse, the dead phone signal, and Jules hitting the mute button. All four are people or physics getting in the way, and that is the material to build on.

## Known conflicts with existing rules

The following existing rules pull against this framework. None of them has been changed. Each needs an author decision.

1. **(Resolved 2026-10-26, see Decision above.)** **`docs/research/PEDAGOGICAL_AGENCY_ARCHITECTURE.md`, §3, Model 2, Part 2.** It says "the learner unlocks the satisfying conclusion: Ethan executes the verified fix, the motors spool up, the route is saved." Authoring checklist item 4 says to focus on "the quiet satisfaction of a saved shift." Both prescribe the clean, happy resolution this framework argues against (principles 2 and 5). A possible reconciliation is to keep the epilogue and require it to charge a cost and leave a carry-forward item.
2. **(Resolved 2026-10-26, see Decision above.)** **`docs/research/PEDAGOGICAL_AGENCY_ARCHITECTURE.md`, §3, Model 1 (Episodes 00–02).** It says "Maximum safety and zero test anxiety." That is compatible with low reader anxiety, but it is often read as "nothing goes wrong for Ethan," which conflicts with principle 4. This framework's position is that early chapters get smaller costs, not zero costs.
3. **`docs/research/PORTLAND_AUTHOR_BIBLE.md`, Episode 00 card, "Resolution & Cost."** It says "Ethan... clicks submit with sweating palms, and scores a 742/900." The PR #29 review recommends a narrower pass or a failed exam. The bible's listed cost ("His bank account is still drained") is a condition that already existed, not a cost of the decision. The canon score stays at 742 until the author decides otherwise.
4. **`docs/research/PORTLAND_AUTHOR_BIBLE.md`, Episode 01 card.** It says "The trucks depart on time." The PR #29 review suggests that one trailer should miss. Note that the bible *does* charge costs that the current chapter text drops: "ruins a fifty-dollar staging cable, severely bruises his knuckles." Restoring those costs needs no rule change. Making a truck miss does.
5. **`docs/research/PORTLAND_AUTHOR_BIBLE.md`, Episode 01 pivot.** Ethan "repairs the physical insulation, straightens a bent pin with a mechanical pencil, and matches the serial baud rate using DIP switches." He does all of it alone, and no knowledgeable second person appears. That pulls against principle 3. It does not forbid adding a helper, but it does not ask for one either.
6. **Canon scope: the Willamette River plant.** `docs/research/PORTLAND_AUTHOR_BIBLE.md` sets Episode 04 at the "Harrowmere Willamette River Plant" and makes Leah Moreno a plant employee. The approved canon given for this work names Harrowmere, the Gresham warehouse, and the Portland ROC help desk under Jules. A site visit is not a relocation, so this is probably compatible, but the author should confirm that the plant is in canon as a place Ethan visits and not a place he works.
7. **Canon scope: the Episode 12 ending.** The bible says Ethan "can no longer remain in the comfortable, familiar routine of the Portland desk." Read loosely, that implies leaving Portland, which would conflict with "Ethan never relocates." The author should confirm that it means a role change rather than a move.

These are not conflicts, but they are worth noting:

- The bible's Episode 01 card ("has earned his CompTIA A+ and is grinding... digital flashcards for Network+") resolves the "exams, plural" question raised in PR #29. The chapter text should make that explicit.
- The bible says "50-pound bags of concrete mix," while the Chapter 00 text says "eighty-pound bags of mortar." That is chapter drift from the bible, not a rule conflict.
- `docs/research/PLAIN_ENGLISH_STYLE_GUIDE.md` bans words like "pedagogy," "heuristic," and "rubric" from learner-facing material. This document is for writers, not learners, but it avoids those words anyway.
