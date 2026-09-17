# Portland Desk track (Security+ precursor)

Ethan’s help-desk years. One cohesive SY0-701 cluster per chapter, woven into a single desk shift.

## Cast and voice

- **Ethan** — desk tech learning in public; narrator may feel lost; readers must not.
- **Jules** — Portlandia-flavored desk lead; conversational coach, not crisis commander.
- Present tense only. Goldratt-style: people talking decisions through tickets, not melodrama.
- **Forbidden in narrative:** `Priya`, `Harrowmere`, or any foreshadowing of places/events the reader has not met (`validate_unit.py` fails on Priya/Harrowmere).

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
