# Authoring brief

A brief is the author's instructions for one job: what material goes in, who it is for,
what it should teach, and the creative direction. The author writes it (or approves an
agent's draft of it). Everything downstream (plan, chapters, review) works from it.

Briefs live in `briefs/<brief_id>.brief.yaml`. Each job gets a working folder,
`workshop/<brief_id>/`, holding its plan, its progress record, review reports, and
**candidate** chapters. Nothing in `workshop/` is published; a candidate becomes part of
a track only when the author says so and it is copied into `examples/` and rendered into
`docs/` (see `AGENTS.md` → Authoring workflow).

Check a brief with:

```bash
.venv/bin/python tools/author.py brief-check briefs/<brief_id>.brief.yaml
```

## The four modes

| `mode` | Input | Output |
|---|---|---|
| `term-set` | A related set of terms (with or without definitions) | One chapter |
| `course-glossary` | A whole course glossary, in course order | A plan for a multi-chapter companion, then chapters one at a time |
| `source-material` | Lessons, slides, notes (plus any terms they define) | One chapter that demonstrates the concepts |
| `track-extension` | New material for an existing story track | One more chapter, consistent with the track's canon |

Terms and glossaries are first-class in every mode. A supplied glossary is enough; no
textbook or source document is required.

## Fields

```yaml
brief_id: tamarack-mis-companion        # required; also the workshop folder name
mode: course-glossary                   # required: term-set | course-glossary | source-material | track-extension
title: "MIS companion"                  # optional

reader:                                 # required
  who: "ITM 310 student"                #   required
  knows: "uses Excel; new to MIS"       #   optional: prior knowledge
  setting: "read alongside the MindTap MIS chapters, one chapter per module"  # optional

purpose: >                              # required: what the reader should be able to do afterwards
  Explain how each module's ideas depend on each other and apply them to a business decision.

inputs:                                 # at least one of glossaries / glossary_csv / terms / sources
  glossaries:                           # existing glossary.yaml files, in course order
    - examples/mis-01-information-systems/glossary.yaml
  glossary_csv:                         # or a course export; columns are mapped by name
    path: data/course_glossary.csv
    group_column: "Module"              #   optional: chapter grouping, kept in file order
    term_column: "Term"
    definition_column: "Definition"
  terms:                                # or terms written into the brief
    - term: "cache"
      sense: "CPU cache memory, not a browser cache"   # optional: which meaning
      definition: "…"                   # optional until drafting (see Definitions below)
      source: "course glossary"         # where the definition came from
      status: source                    # source | confirmed | proposed  (default: source if definition given)
    - "spooling"                        # a bare term: needs a definition before drafting
  sources:                              # lessons, slides, notes
    - path: research/week7-slides.md    # a file in the repo, or…
      note: "Week 7 slides: CRISP-DM phases, DAX columns vs measures"   # …a description
      kind: slides                      # slides | lesson | notes | assignment | other
  sequence: inputs                      # inputs (file order) | a list of group names in course order

scope:                                  # all optional
  chapters: auto                        # auto = one per group; or a number
  words_per_chapter: 1800               # approximate
  terms_per_chapter_max: 30             # above this, the plan flags a catalog-chapter risk

creative:                               # all optional; defaults shown
  tone: "plain, grounded workplace realism; dry humor allowed"
  pov: "third person, close to one character per chapter"
  tense: past
  setting: null                         # null = from the track, or the author decides at planning
  endings: cost                         # every chapter's pivot costs something (schema/VOICE.md)
  headings: scene                       # the scene-heading rule (examples/TAMARACK.md)
  notes: ""                             # anything else: things to avoid, a model author, a mood

track:                                  # required for track-extension; optional otherwise
  manifest: tracks/tamarack.yaml
  canon: examples/TAMARACK.md
  continuity: strict                    # strict: canon facts can't change | loose: author may revise canon

output:
  workdir: workshop/tamarack-mis-companion   # default: workshop/<brief_id>
```

## Definitions: what makes them dependable

Instructional claims in a chapter can only rest on definitions with a known source.
Every term ends up with one of these `status` values:

| `status` | Meaning | Can a chapter use it? |
|---|---|---|
| `source` | Copied from the course glossary or a supplied source | Yes |
| `confirmed` | Proposed by an agent or written by the author, then approved by the author | Yes |
| `proposed` | Drafted by an agent, not yet approved | **No.** `plan-check` blocks drafting |
| *(no definition)* | A bare term | **No.** `brief-check` lists it under "needs a definition" |

When a term could mean more than one thing (cache, model, class, key), record the
intended meaning in `sense`. When two inputs define the same term differently, the
plan lists it under conflicts. The author picks one, or keeps both and the chapter is
written so it is true under either (see `schema/README.md` → Working rules).

## What the author decides, and when

1. **The brief** (inputs, reader, purpose, creative direction): before anything else.
2. **Definitions** marked `proposed`, and any conflicts: before drafting.
3. **The plan's architecture** (groupings, story arc, cast, per-chapter situation): set
   `approved: true` in `plan.yaml` when satisfied. `plan-check` refuses to clear a
   chapter for drafting until then.
4. **Each candidate chapter**: accept, request another revision, or reject. Revision
   loops are capped (`max_revisions` in `status.yaml`, default 2) so a chapter that isn't
   converging comes back to the author instead of looping.
5. **Publishing**: copying a candidate into `examples/` and `docs/`.
