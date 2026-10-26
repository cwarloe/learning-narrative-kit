# Repo structure recommendation: the Ethan Mercer series

*Status: proposal, 2026-10-21. Docs only; nothing has moved.*

## The situation

One story runs across two repos in three beats:

| Beat | Title | Where it lives | Format | Pages URL |
|---|---|---|---|---|
| Book 0 | *Zero-to-One*: Portland Help Desk, Ep 00–12 (A+, Net+, Sec+) | `learning-narrative-kit/portland-desk/` (copy in `docs/portland-desk/`) | LNK units: narrative + workbench + glossary | https://cwarloe.github.io/learning-narrative-kit/portland-desk/ |
| Book 1 | *Learning to See*: narrative 00–09 + lessons 01–09 + capstone | `network-analyst-development-framework/narrative/`, `lessons/` | Markdown + real pcaps | https://cwarloe.github.io/network-analyst-development-framework/ |
| Book 2 | *The Hunter's Eye*: narrative 10–14 + Hunt 01–05 | same NADF repo | Markdown + Security Onion telemetry | same NADF site |

Canon is split. Book 0's is in `docs/research/PORTLAND_AUTHOR_BIBLE.md` and `PORTLAND_TIMELINE.md` here. Books 1 and 2 use `narrative/author-bible/` in NADF (cast, Harrowmere history, beat matrix). The research is split the same way: `docs/research/` + `research/` here, and NADF's `docs/research/R004–R010` plus the evidence index.

Names were unified on 2026-10-21, but the bible's §1.3 still lists six open conflicts: Ethan's age and timeline, the employer (Portland ROC vs. Harrowmere), Nia's title, Leah's role, the two Danas, and the validator rule that fails any narrative mentioning Harrowmere or Priya. Those conflicts came from having two canons. No repo layout fixes them; one canon does.

## What else is in each repo

- **LNK is a kit, not just the Ethan story.** It also holds Excel 01–12, MIS 01–10, BI, ITM310/Vanguard Edge, the Tamarack track, the generic Sec+/Net+/A+ examples, `schema/`, `template/` and the render/validate `tools/`. Portland Desk is one track among many.
- **NADF is a course.** It has pcaps, a capture generator, Zeek/Wireshark validation, lesson-command checks, governance and a research protocol. Its tooling has nothing in common with LNK's YAML renderer.
- **CI and Pages differ.** LNK runs `validate.yml` (unit validation, the Ep07 capture check, hub links) and serves `docs/`. NADF runs `checks.yml` (links, tshark/Zeek, lesson commands) and serves `/` through a docsify shell.

## Options considered

1. **Merge everything into one repo.** You'd get one place to look. But you'd also mix two toolchains and two CIs (pip+YAML with apt tshark/Zeek). The Excel/MIS/Tamarack content would sit next to a network-analyst course. One Pages URL would break, and the history and issues of one repo would be lost or awkwardly imported. **Rejected.**
2. **Three repos:** a new `ethan-mercer-series` repo for story and canon, plus the two course repos. Canon would have a clean home. But the story text is bound to its lessons (each NADF chapter "leads into" a lesson, and each Portland episode pairs with a workbench). Pulling the prose out splits every chapter from its exercise, which needs a third CI and cross-repo links in both directions. **Rejected.** It adds overhead without fixing the canon conflicts.
3. **Move Book 0 into NADF** (NADF becomes the series repo). The story would be in one place. But Book 0 is built on LNK's unit format and tooling, so you'd have to port the renderer or both toolchains would live in NADF. LNK would also lose its showcase track. **Not now.** Revisit if LNK ever stops being a general kit.
4. **Keep two repos, single-source the canon, and present one series. Recommended.**

## Recommendation: two repos, one canon, one front door

**Split by tool and audience, not by story.** Book 0 stays in LNK because it is made with LNK. Books 1–2 stay in NADF. The story is joined up by three things:

1. **A single series canon in NADF.** Create `network-analyst-development-framework/narrative/series-bible/`:
   - `characters.yaml`, a machine-readable cast list: canonical name, former names, role in each book, first appearance, age per book.
   - `SERIES_BIBLE.md`: the world (Harrowmere and its Portland site), the three-book timeline, and the arc.
   - The existing `author-bible/` files stay where they are as the Book 1 working notes.

   NADF owns two of the three books and the company world, so it should own the canon. Book 0's bible here shrinks to Book-0-only episode architecture, with a pointer at the top: "Series canon: NADF `narrative/series-bible/`. If this file disagrees, that one wins."
2. **A canon check in both CIs.** A small script (`tools/check_series_canon.py` here, `lab/check-canon.py` there) reads `characters.yaml` and fails on any former name (Ethan Brooks, Jules Mercer, Marcus Vance) or a canon-listed forbidden term. LNK fetches the file from NADF's raw URL at a pinned commit, so no network flakiness lands on `main`. It replaces the current validator rule that bans Harrowmere and Priya. That rule blocks the crossover, and once the employer conflict is resolved it is wrong.
3. **One front door.** Add a "Read the series in order" page to NADF's site (Book 0 → Book 1 → Book 2) and link to it from:
   - LNK's hub card for Portland Desk,
   - the end of Portland Ep 12 ("Ethan's story continues in Book 1 →"),
   - the NADF prologue ("Ethan's first two years: Book 0 →").

   That way a reader experiences one series, whichever repo it lives in.

**Research** stays with what it informs: NADF R-series with NADF, and LNK pedagogy and style research here. Add a short `docs/research/README.md` index in each repo that links the other's research, so the "what we learned" trail is findable from either side. Nothing gets copied.

## What moves where

| Item | From | To |
|---|---|---|
| Cross-book canon (cast, ages, employer, timeline) | LNK `PORTLAND_AUTHOR_BIBLE.md` §1.3, `PORTLAND_TIMELINE.md` (series parts); NADF `author-bible/cast-and-relationships.md` (series parts) | NADF `narrative/series-bible/` |
| Book 0 episode architecture | stays in LNK `PORTLAND_AUTHOR_BIBLE.md` | (trimmed, points to series bible) |
| Portland episodes, workbenches | stay in LNK | — |
| Books 1–2 narrative, lessons, labs | stay in NADF | — |
| Harrowmere/Priya validator rule | LNK `AGENTS.md` / validator | replaced by the canon check |

## Pages and URL impact

No published page moves, so **no redirects are needed** and both Pages URLs keep working. The only new URLs are additive: the NADF series page and NADF `narrative/series-bible/`. The links to the old bible stay valid because the file stays, trimmed.

Unrelated cleanup to schedule: `docs/portland-desk/` and `docs/portland-desk/` are full duplicate copies. Keep one as the source and generate the other in the build step so they can't drift.

## Migration plan (each step is its own PR; none merges without Charles's OK)

1. **Decide the six open conflicts** (bible §1.3). Proposed defaults:
   - **Employer:** Portland ROC *is* Harrowmere's Portland site. Book 0 never names the parent company until Ep 12.
   - **Age:** Book 0 covers ages 20 to 23 (`PORTLAND_TIMELINE.md` section 4). NADF Book 1 opens at 23, turning 24. NADF's bible must match.
   - **Titles:** Nia and Leah are promoted between books, so their titles differ on purpose.
   - **Dana:** rename Book 0's vendor and finance Danas.

   Charles signs off; this is a story call.
2. **NADF PR:** add `narrative/series-bible/` (`characters.yaml` + `SERIES_BIBLE.md`) and `lab/check-canon.py`, and wire the canon check into `checks.yml`.
3. **LNK PR:** trim `PORTLAND_AUTHOR_BIBLE.md` and `PORTLAND_TIMELINE.md` to Book 0, add the pointer, and add `tools/check_series_canon.py` to `validate.yml`. Retire the Harrowmere/Priya rule. Apply the Book 0 rewrites from step 1, such as the Dana renames.
4. **NADF PR:** add the "Read the series in order" page plus sidebar entry. Add the prologue back-link.
5. **LNK PR:** add the hub card link, the Ep 12 forward link and the research cross-index. Rebuild `docs/` and make sure `check_hub_links.py` passes.
6. **Later, optional:** generate `docs/portland-desk/` from `docs/portland-desk/` and remove the duplicate.

## Why this and not a merge

The cost Charles feels is "two separate stories," but the real cause is two canons and no shared entry point. Merging would mix two unrelated toolchains to fix a problem that a 1-file canon and three links fix. If NADF ever adopts LNK's unit format, or LNK spins its other tracks out, option 3 (one series repo) becomes cheap. Revisit then.
