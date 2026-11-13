# Memory palaces, spatial memory, and technical learning: reference archive

This folder preserves a research document Charles wrote in Google Drive on 2026-11-09, together with the research it draws on, so it can be checked and reused later.

| File | What it is |
|---|---|
| [`cognitive-spatial-technical-learning-architecture.md`](cognitive-spatial-technical-learning-architecture.md) | The full source document, exported from Google Docs to Markdown and **not edited**. A header at the top gives the Drive title, link, and dates. |
| [`sources.md`](sources.md) | Bibliography of the primary research behind the document: 58 sources with full citations, DOI or URL, and a one-line note on what each contributes. All 58 were verified against Crossref, arXiv, ERIC, Open Library, ADS, or the publisher. |
| [`errata.md`](errata.md) | Corrections that apply on top of the unedited export: 10/25/15 is a per-hour guide based on task sizing, not a rule justified by a 10-minute attention span; plus two protocol nits (a TCP RST metaphor that implied a reset drops all sessions, and a TLS SNI metaphor that should be qualified for Encrypted Client Hello). The export itself is unchanged. |

## What this archive is, and is not

- **It is the reference copy.** The document is general. Its examples come from packet analysis and network security, but its principles (spatial anchoring, retrieval before re-exposure, faded guidance, direct labeling, protecting unaided skill from AI offloading) apply to any subject. That is why it lives here and not in a single domain repo.
- **It is not an active standard.** Under the precedence list in [`AGENTS.md`](../../AGENTS.md), `research/` is background that informs and does not rule. Nothing here overrides `schema/`, the craft framework, or the standards in `docs/research/`.
- **It is not yet checked line by line.** The document has no reference list of its own, and some of its claims go further than the research does. `sources.md` lists the studies that support it, the ones that qualify it, and the claims for which no source was found. Read those before turning any rule here into a requirement.

## Where the adaptations live

Domain adaptations are written separately, in the repos that use them, after an editor makes each one fit its audience. They cite this folder as their source instead of copying the document. Candidates identified on 2026-11-09 include this kit (story settings and track maps as memory anchors, retrieval and flawed-example steps in workbenches), `network-analyst-development-framework`, `stewardship-curriculum`, `Consulting`, and `knowledge-harvest`. Check each repo for its current version.
