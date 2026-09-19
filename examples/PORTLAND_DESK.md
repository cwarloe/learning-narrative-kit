# Portland Desk track (Security+ precursor)

Ethan’s help-desk years. One cohesive SY0-701 cluster per chapter, woven into a single desk shift.

## Cast and voice

- **Ethan** — desk tech learning in public; narrator may feel lost; readers must not.
- **Jules** — Portlandia-flavored desk lead; conversational coach, not crisis commander.
- **Past tense** for narration and dialogue tags. Goldratt-style: people talking decisions through tickets, not melodrama.
- **First person**, Ethan narrating. Do not switch to third — see below.
- **Forbidden in narrative:** `Priya`, `Harrowmere`, or any foreshadowing of places/events the reader has not met (`validate_unit.py` fails on Priya/Harrowmere).


## POV and tense — decided, with its basis

Settled against `research/perplexity-2026-09/08-pov-and-tense.md`. Read the Limits section
there before reopening any of this: the honest finding is that **no direct evidence exists**
for POV or tense in instructional fiction, so these are craft calls made on adjacent
evidence, not findings.

**First person, Ethan.** Keep it. First-person narration tends to raise engagement and
identification, especially when the protagonist resembles the reader — a junior tech is who
this is for. *The Phoenix Project*, the closest analogue to this track, is first person.

The evidence is genuinely mixed rather than one-directional: third-person omniscient showed
a modest advantage on composite reading performance and macro-level coherence, and better
recall in one film study. The call weights engagement over that. It is a judgment, not a
result.

**The epistemic problem is solved by Jules, not by POV.** A week-three tech cannot
plausibly be the expert, but the fix is structural, not grammatical: the narrator stays a
novice and **expert content arrives through mentor dialogue**. That is how *The Phoenix
Project* handles it. Ethan may misunderstand or oversimplify a term on first contact; Jules
corrects or deepens it. That maps directly onto the complication/pivot rule in
`schema/README.md` — the misunderstanding is the complication, the correction is the pivot.

**Past tense.** Tense is close to an empirical non-issue: an eye-tracking study found no
difference in transportation, mental simulation, or appreciation between past and present,
and reported past tense as *slightly slower* per word with no comprehension cost. Choose
past for craft reasons — IT professionals already read postmortems and incident reports in
past tense — not because present tense is harder to process. It isn't.

Two claims that do **not** support this choice, and should not be cited as if they do:

- *Retrospective narration gives past tense a native signaling mechanism.* Plausible, and
  untested. No study treats narrator retrospection as a signaling device. Mayer's signaling
  research is about headings, outlines, arrows, and emphasis — typography, not tense.
- *Present tense imposes extra processing cost.* Contradicted. The measured difference runs
  the other way and is negligible either way.

`Present tense only. Goldratt-style` was not wrong, for the record: *The Goal* does narrate
on-scene action in present tense. Past tense here is a preference, not a correction.

**Signaling.** Marks and scene headings are the primary signaling mechanism, and that is
where the evidence actually is. Narrator retrospection ("that was the ticket where the
management path finally made sense") is secondary and optional — use it sparingly, and do
not let it become the section-final maxim that `schema/VOICE.md` warns about.

**Do not design for immersion alone.** Transportation is robustly linked to attitude and
belief change, and only weakly and indirectly to recall or transfer. An absorbing chapter
is not by itself a teaching chapter.

## Marks and flavor

| Tier | What to mark |
|------|----------------|
| `exam` | SY0-701 study targets for this chapter |
| `support` | Desk/network jargon a non-IT reader may need to hover |

**Do not mark** Portlandia / atmosphere (rain, MAX, bike, pannier, coffee, cubes-as-furniture vibe). Flavor is unmarked on purpose.

## Chapter sizing (working defaults)

| Metric | Target |
|--------|--------|
| Cover-stripped words | ~1800–2000 |
| Exam terms | ~28–35 |
| Support terms | ~6–10 |
| Density | ~2–3.5 marks / 100 words (ITM-like; justify outliers) |

## Existing units (clone structure from the nearest sibling)

| `unit_id` | Title |
|-----------|--------|
| `secplus-ports-helpdesk` | The Port That Is Open |
| `secplus-auth-helpdesk` | Prove Who You Are |
| `secplus-phishing-helpdesk` | Don't Click That |
| `secplus-malware-helpdesk` | Something on the Box |
| `secplus-wireless-helpdesk` | The Air Is Shared |
| `secplus-physical-helpdesk` | Badge, Lock, Eyes |
| `secplus-crypto-helpdesk` | Trust on Paper |
| `secplus-ir-helpdesk` | When the Ticket Escalates |

Folder pattern: `examples/<unit_id>/{unit.yaml,glossary.yaml,narrative.md,review.yaml}`.

## Sticky pedagogy check

Before ship: name 3–5 “sticky” decisions the chapter teaches (e.g. IR: not every scary ticket is an incident; containment before curious poking). If you cannot name them, the story is still a vocab parade.
