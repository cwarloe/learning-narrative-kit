# Knowledge ledger

> **Status:** Proposed. Not yet in the precedence list in `AGENTS.md`, and not run in CI.
> Charles decides whether it joins `schema/` as contract, and when the check becomes a gate.

## The point

A character knows only what the story has given them. `docs/research/CANON_DISCIPLINE.md`
already says so: plausible is not canon (Law 1), and Ethan cannot name what he has not
touched, seen or been taught (Law 2). Today those rules live in review notes. The ledger
writes them down per term, so a script can catch the slip before a reviewer has to.

Each entry answers three questions about one marked term:

1. **When** does the character pick it up? (the episode)
2. **Where** did it come from? (a person, a document, something seen, or what they knew before the story)
3. **Has the author confirmed it?** (`proposed` or `confirmed`)

The idea comes from Mossbridge, a friend's simulated town, where a resident cannot use
a finding until they have travelled to the library and read it, and every finding shows
its source and date. The ledger keeps the useful half of that, the record of who knows
what and from where, without a running simulation.

## File

One ledger per track and character. Portland Desk:
`docs/research/PORTLAND_KNOWLEDGE_LEDGER.yaml`.

```yaml
track: portland-desk
character: Ethan Mercer

entries:
  - term: apipa_address        # the id used in [[apipa_address|...]] marks
    acquired: "03"             # episode where he picks it up (two digits, quoted)
    source:
      kind: person             # person | document | observed | prior
      name: Jules Brooks
      note: "Names the 169.254 address and explains the DHCP fallback."
    status: proposed           # proposed | confirmed
```

### Source kinds

| Kind | Use it when | Required fields |
|---|---|---|
| `person` | Someone tells or shows him (Jules, Jared, Hank on the dock) | `name`; a surname, if given, must match the bible's cast registry (3.4); the first name must appear in that episode |
| `document` | He reads it: a manual, a forum thread, a NIST guide, an encyclopedia entry | `title`; if there is a `url`, also `retrieved` (date). Add `license` when the text is shown on the page |
| `observed` | He works it out from what is in front of him, on the page | `note` saying what he saw |
| `prior` | He knew it before the story starts | `note` pointing at the backstory in `PORTLAND_TIMELINE.md` section 4 |

A `document` source is the reading shelf. When a character looks something up, the
entry records the real source, so the learner can follow the same trail. Example:

```yaml
  - term: phishing
    acquired: "09"
    source:
      kind: document
      title: "Phishing (Wikipedia)"
      url: "https://en.wikipedia.org/wiki/Phishing"
      retrieved: "2026-11-18"
      license: "CC BY-SA 4.0"
      note: "Reads it on his break after the fake invoice."
    status: proposed
```

That example shows the format only; it is not in the ledger. Keep the shelf small and
picked by hand: a fixed list per track, read once by the author when added.

## What the check does

`python3 tools/check_knowledge.py`

| Finding | Meaning | Exit |
|---|---|---|
| FAIL | The ledger is wrong on its face: the term is never marked; the pickup episode never marks it; a surname disagrees with the cast registry; a person is not named in that episode; a document has no title, or a url with no date; a prior entry has no backstory note; duplicates; bad values | 1 |
| FLAG | Ethan uses the term, in narration or his own speech, before his pickup episode | 0 (1 with `--strict`) |
| REPORT | How many terms Ethan uses still have no entry (`--list` names them) | 0 |

How it tells using from hearing: narration is Ethan's (the episodes are first person), and
a quote counts as his only when its paragraph has an "I said" style tag. Any other quote
counts as hearing the term. That guess can miss an untagged line of Ethan's, so a FLAG
is a prompt to read the passage, not a verdict.

## What it does not check

- Whether the source is good, or the definition right. Definitions still follow
  "definitions before claims" in `AGENTS.md`; the ledger records where Ethan learned a
  term, not what the exam says it means.
- Unmarked mentions. A term with no `[[...]]` mark is invisible to the check.
- Labs. Portland Desk workbench files carry no marks today. If they gain marks, a lab
  for episode N should use only terms picked up by episode N.

## Rolling it out

1. Charles confirms or corrects the five Episode 3 seed entries.
2. Fill the rest of the track episode by episode (`--list` shows what is missing), all
   `proposed` until confirmed.
3. When every used term has an entry, run it with `--strict` before merge, then add it to CI.

## Other tracks

The same file shape works for Tamarack: one ledger per staff member, with `document`
sources pointing at the shelf you choose for each MIS or Excel chapter. The script reads
Portland Desk paths today; a Tamarack ledger needs those paths passed in.
