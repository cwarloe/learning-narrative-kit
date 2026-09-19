# Voice — writing prose that doesn't read as generated

The narrative can pass every check in `schema/README.md` and still be unreadable in the
way that matters: it sounds like a machine wrote it. A reader who clocks that stops
trusting the material. For a training product that is a correctness problem, not a taste
problem.

`tools/voice_check.py` flags the countable tells. It is heuristic and produces false
positives — a reading aid, never a gate.

```bash
python3 tools/voice_check.py examples/<unit_id>/narrative.md
python3 tools/voice_check.py examples/*/narrative.md --summary
```

## The control group is in this repo

`itm310-vanguard-edge` was written before the Portland Desk house style set in. Same
author, same kit, measurably different prose:

| | ITM 310 | Portland Desk (range) |
|---|---|---|
| Mean sentence length | 19.7w | 10.7 – 13.6w |
| Sentence-length spread (sd) | 14.0 | 7.5 – 10.4 |
| Sentences ≤ 6 words | 11% | 28 – 42% |
| Em-dashes per 1k words | 5.6 | 12.6 – 20.9 |
| Section-final aphorisms | 0 | 2 – 6 |
| Antithesis constructions | 0 | 4 – 14 |

When a Portland Desk chapter reads synthetic, these numbers are where it happened. The ITM
figures are a reasonable target — not a rule, but if a chapter is at 11-word means with 40%
short sentences, that is the drumbeat talking.

## The tells

### 1. Dropped determiners

The single most recognizable one. A subject noun loses its article and the sentence takes
on a telegraphic, headline register.

> ~~Rain hits the east-side windows.~~ → The rain hits the east-side windows.
> ~~Closet switch in Building C.~~ → There's a switch in a closet in Building C.
> ~~Coffee steam.~~ → cut, or give it a verb.

English is not a language without articles. Prose that drops them reads as translated.

### 2. Verbless fragments, especially in runs

> Jules sits two cubes over. **Desk lead. Bike helmet on the monitor arm, rain pants
> drying on the chair.**

One fragment is a choice. Three consecutive is a tic. `voice_check.py` reports
`frag-runs` for exactly this.

### 3. Every beat landing on a portable moral

The most damaging and the least noticed. Real scenes end on someone leaving, or an
unresolved thing, or nothing. They do not resolve into a maxim the reader could
cross-stitch.

> *Numbers are inventory. Decisions are the job.*
> *Cleartext mail is not a preference she has to live with — it is a setting we can replace.*
> *Reporting is not snitching. Reporting is how the filter gets a second brain.*

Each is a decent line. The problem is that there is one at the end of every section, in
every chapter. **Let most beats end flat.** A beat that ends on "she said she'd think
about it" is not a failed beat.

### 4. The "X is not Y" formula

Antithesis used as a tic. Across the Sec+ chapters: *that is not a password / privileged
access is not a lifestyle / reporting is not snitching / dumpster diving is not a cartoon
raccoon / convenience is not a personality trait.* Five instances of one joke shape.

### 5. Mentors who speak only in epigrams

**The rule: a line is quotable because the narrator marks it as memorable.** If every line
is quotable, none of them is. Give the coach one or two lines per chapter that the narrator
explicitly registers — *that's the one I write down* — and make the rest of her speech
functional. The quotable line earns its weight from being singled out, not from being
well-phrased.

Beyond that, Jules almost never says a functional sentence. She delivers bare labels ("Obfuscation."
"Rootkit." "Air gap."), maxims ("Containment before curious poking"), or the formula
above — usually *without looking up*, which recurs verbatim across chapters.

Real senior people mostly say boring operational things: *did you check the ticket
history, who else is affected, I've got a call in ten.* Let the coach be wrong once, or
distracted, or ask a question because she genuinely doesn't know.

### 6. Trying too hard

> Rain hits the east-side windows **like it has opinions.**
> Jules nods once **like a referee acknowledging a clean foul call.**

The inanimate-object-with-attitude simile is a house style of generated prose. When a
simile is reaching, cut it — plain statement is almost always better.

### 7. Character sheets read aloud

> I am Ethan, week three at a midsize MSP, index cards in the top drawer — service on the
> front, number on the back.

Three stacked appositives delivering biography. Nobody narrates themselves this way.
Let the facts arrive when they matter.


### 8. Em-dashes as a default connector

The Portland Desk chapters ran 12.6–20.9 em-dashes per 1k words against ITM's 5.6. The
fix is not zero — a writer uses a dash sometimes, and a chapter with none reads as
carefully as one with too many. Aim near the ITM rate: **roughly one per 180 words.**

The dash earns its place three ways:

1. **Interruption or self-correction**, mostly in dialogue. Someone cuts themselves off
   or gets cut off.
2. **An appositive that already contains commas.** Commas can't hold it and parentheses
   are too quiet: *narrow on purpose — source the VPN group, destination the jump host,
   port 3389, TCP, allow — and everything else denied.*
3. **A turn the sentence didn't promise.** A reversal or a sting where a comma is too
   soft.

It does not earn its place as:

- A general connector where a comma, a period, or *and* would do the same work.
- **A hitch for a summarizing clause.** This is the tic: *download, delete, hope — and
  that's the whole problem.* The dash is how the section-final maxim (tell 3) gets
  delivered. Cut the clause, not just the dash.
- More than one per paragraph, or two in a sentence unless they are a matched pair
  bracketing one appositive.

Used well the dash also **compresses** — it replaces *which was*, *and that meant*, and
most *where* clauses at a saving of two to four words each. A tightening pass and a
dash pass are the same pass.


## Repair pass

Work a chapter in this order. The first three are mechanical; the rest need judgment.

1. **Restore articles.** Read for sentence-initial nouns. Put back the *the* and *a*.
2. **Give fragments verbs,** or delete them. Keep at most one per section, on purpose.
3. **Vary sentence length.** If everything is 8–12 words, build some 25-word sentences
   with subordinate clauses. Spread matters more than mean.
4. **Cut the closing maxim** from most sections. Let the beat stop.
5. **Deformulate the coach.** Replace at least half her lines with functional speech.
6. **Cut reaching similes.** All of them, then restore any you actually miss.
7. **Restore a few em-dashes** (tell 8) while tightening — the same edit does both.
8. **Re-run `voice_check.py`** and confirm the density moved toward the ITM numbers.

## Word targets produce this problem

Most of the tells above are compression artifacts. Dropped determiners, verbless
fragments, and dash-swallowed subjects are all what happens when prose is squeezed toward
a word count. The Portland Desk ceiling was ~1800–2000 while the chapter that reads best,
`itm310-vanguard-edge`, is 3857 words.

So: **a word target is not a reason to drop a subject, an article, or a finite verb.**

> ~~a contractor named Sam wanted RDP from a hotel in Seattle to a finance workstation —
> polite about it, and late on a deliverable.~~
>
> A contractor named Sam wanted Remote Desktop from a hotel in Seattle to a finance
> workstation. He was polite about it, and late on a deliverable.

The second is six words longer and correct. The dash in the first is not an appositive
doing work — it is a period wearing a disguise, and it swallowed *He was*. When a dash
replaces a clause and takes the subject with it, make it a sentence.

If a chapter must get shorter, cut a beat. Do not cut grammar.

## What not to trade away

Voice repair must not cost teaching. The rules in `schema/README.md` still bind:

- Marked terms stay on the complication or the pivot (Beat structure).
- Definitions stay exam-faithful; do not soften a fact to smooth a sentence.
- Cover test still has to pass.

If a plainer sentence teaches better than a livelier one, ship the plainer sentence.
Nobody is grading the prose. They are grading whether the reader can do the thing.
