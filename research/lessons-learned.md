# Lessons learned: the Tamarack track

What happened while building the Tamarack track: 24 chapters from a MindTap glossary
export, a recording kit for Excel 3, and a lecture unit from the ITM 310 Week 7 slides.
This is background, not contract. The rules it produced live in `schema/README.md`
(Working rules learned the hard way), `AGENTS.md` (Before a pull request), and
`examples/TAMARACK.md` (Timeline, Proving the story, Headings).

## What worked

**One world across every chapter.** A single company and cast let later chapters pay
off earlier ones: the buying group that kept getting shelved, Davenport from site choice
to first-month KPI, Marco's mistyped ID. Readers don't have to learn a new setting for
each module.

**Definitions copied exactly, problems written down.** Copying the course glossary word
for word, and recording its errors in `unit.yaml` instead of quietly fixing them, caught
a definition attached to the wrong term ("BI" defined as a bibliography), MODE.MULT and
ROUNDDOWN definitions that don't match Excel, and several duplicates.

**Building the artifact tested the story.** Generating the Excel 3 workbook and checking
it against the narrative caught five things no real file could produce: 81 days worked
in a quarter with 66 weekdays, an October filter on September data, MAXIFS described as
finding a "best week," an unverified claim about an upside-down lookup table, and a total
that would have shown #N/A. Fixing the last one improved the story: Eli now reaches for
IFERROR because the total broke, which makes his mistake believable.

**One source, several outputs.** `steps.yaml` produces both the human recording script
and the bot script; `tracks/tamarack.yaml` produces the contents page and every
Previous/Next link. Nothing has to be kept in sync by hand.

**Pilot, then roll out.** The heading rule was written down, tried on two chapters,
approved, then applied to the other 22. That went far better than the first draft of all
24 chapters, which was written before anyone had read one.

**Automated review found real problems.** Codex flagged the ROUNDDOWN definition and two
missing scene breaks. Re-auditing the whole book after the second fix found a third
problem nobody had flagged.

## What went wrong, and what fixed it

| What went wrong | How it was found | What prevents it now |
|---|---|---|
| All 24 chapters written before the author read one; 183 headings, most of them topics | The author's read of the finished set | Pilot before batch (`schema/README.md`) |
| Figures written by feel: loan sign conventions, CUMIPMT signs, 412.6875 needing a real base amount, populations | Recomputing, building the workbook | Prove the story; every figure from a calculation |
| Dates that disagreed across chapters (Davenport opening in March vs. May; Eli's course length) | Reading chapters side by side | Timeline in `TAMARACK.md` |
| A wrong source definition repeated in the prose as fact (ROUNDDOWN) | Automated review | Source errors stay quoted, never repeated |
| Claims nobody checked ("everyone came out Tier 3," neural networks "like the brain") | Rereading with a skeptical eye | Don't state what you haven't checked |
| Transition sentences that created new scene changes without breaks | Automated review, then a full audit | Heading check in `validate_unit.py` |
| Large modules reading as tours (MIS 10's trade show, MIS 5's deferred list) | Rereading | Watch for the catalog chapter; still open for MIS 5 and MIS 10 |
| `pkill -f` killing the agent's own shell; LibreOffice missing Calc; spreadsheets re-saved with only a new timestamp | Commands failing | Environment notes in `AGENTS.md` |

## Showing, not only telling (from the Week 7 Power BI unit)

The Week 7 unit was the first to lean on scene artifacts, and two new ones were built
for it: a formula bar (`formula`) and a numbered steps panel (`steps`).

**What the exhibits did better than prose**

- **A comparison table showed the data problem before the prose explained it.** Putting
  the first row of each dealer's export side by side made "nothing matched" visible in
  one glance. The paragraph after it only had to name what the reader had already seen.
- **The formula bar made the column-versus-measure difference concrete.** Two bars, each
  with its result underneath ("Every one of the 1,412 rows says 1,930.0" against "On a
  card: 1,930. On a bar chart by dealer: …") show the concept faster than a paragraph
  about row context could.
- **Repeating the whiteboard showed that CRISP-DM loops.** The same six-phase panel
  appears twice: first with Business Understanding highlighted, later with Data
  Preparation highlighted again after Evaluation. The second panel teaches that the
  process goes backward without anyone saying so.
- **The Applied Steps panel doubled as a procedure.** It looks like the real Query
  Editor pane, and a student can follow it in their own copy of Power BI.
- **A small table made an abstract phase concrete.** "Business understanding" is vague
  as a phrase. Three rows (objective, BI objective, success criteria) turn it into
  something the characters sign and later test against.

**What didn't work**

- **The star schema was drawn as a tree.** A tree implies hierarchy; a star schema is a
  hub with spokes, and the dimensions aren't children of the fact table. It needs a real
  diagram: boxes and lines, keys labeled on each line.
- **The most visual scene was told in prose.** The evaluation meeting describes a card,
  a bar chart, a line chart, and a slicer, and the moment Gene clicks his own name and
  every visual changes. That is the one place a picture of the report would teach the
  most, and there isn't one. The same is true of the "(Blank)" bar from the failed
  relationship.
- **Some exhibits were repeated in prose.** A few paragraphs restated what the panel just
  showed. When an exhibit carries the "what," the prose should carry only the "why" and
  the cost, or the reader reads the same thing twice.
- **The exhibits' numbers weren't machine-checked.** The result lines were computed by
  hand, which breaks the "prove the story" rule this same file argues for.
- **Color carries the formula highlighting.** On a Kindle's e-ink screen, or for readers
  who can't distinguish the colors, function names and column references look the same.
  The planned book edition needs a second cue (bold or italic), not color alone.

**Rules of thumb that came out of it**

1. **Match the exhibit to the shape of the idea.** A sequence is a steps panel; a
   comparison is a table; a relationship is a diagram; a calculation is a formula with
   its result; a transformation is before and after.
2. **Show what the character is looking at, at the moment they decide.** Exhibits belong
   at the complication or the pivot (the same rule as marked terms), not as a gallery.
3. **Let the exhibit carry the what and the prose carry the why.** Don't narrate the
   picture.
4. **Show a concept that moves by showing it twice.** Loops, filters, and before/after
   changes teach best as the same exhibit in two states.
5. **Exhibits are claims too.** Their numbers get checked like the prose's numbers.

**Still to build:** a `diagram` fence for schemas and flows, a mock report canvas
(cards, bars, slicer) for Power BI and dashboard scenes, and a before/after table for
transformations.

## When the review tool starts writing the story (MIS 10 candidate, October 2026)

The first course-companion run used `tools/author.py review` between revisions. It helped
once: it caught the rewrite of MIS 10 sliding back into a booth-by-booth tour (seven
paragraphs in a row, each introducing a term with no one speaking). Then it hurt once. To
shorten an "exposition run," a short, funny keynote beat was folded into the paragraph
before it, and the passage read worse. The numbers improved, and the story didn't.

The author's correction became two working rules (`schema/README.md` 8 and 9):

- A character, or the narrator, may explain in technical detail when the scene gives a
  reason. It works best as an exchange with a concrete case that tests it. The rewritten
  edge-computing beat (a truckload sold at Republic at ten, the line down at ten past, and
  what Colville sees) teaches more than the narrated version, and it sets up the ending.
- Metrics point; they don't decide. A passage that reads well and is accurate stays,
  with a line in the review saying why.

The author also restated the kit's place: the story supports the course and doesn't carry
it. Students still have the textbook and their own tools. A minor term can pass with a
sentence of context; the cover test is about the chapter's central relationships.

## The flashcard deck that held one card (Portland Desk, October 2026)

**What broke.** The Episode 00 workbench deck was written for three cards. On the live
page it showed one, Next had nowhere to go, and clicking the card did nothing. Anyone
building a new deck by copying it would hit the same wall.

**Three causes, stacked:**

1. **Markdown ate the HTML.** The deck was hand-written HTML inside a markdown page.
   Docsify's markdown parser ends an HTML block at the first blank line. The next card's
   markup was indented, and an indented line after a blank line is a markdown code block,
   so cards 2 and 3 appeared on the page as raw HTML text. Card 1 survived only because it
   sat in the same unbroken block as the deck's opening tag.
2. **Two scripts owned one click.** `index.html` and `lnk-shell.js` each bound a click
   handler that toggled `flipped`. Every click flipped the card and flipped it straight
   back. The Flip button worked only because it stopped the click from reaching the card.
3. **Key listeners piled up.** The deck added a document-wide key listener every time a
   page rendered, so they accumulated as a reader moved around the site.

**How it was found.** By reproducing it in a headless browser before changing anything,
and checking what was in the page, not what the source said: the source held three cards
and the page held one, with the other two inside a `<pre>`. Two later checks mattered:
- A test that only checks the `flipped` class passes even when the wrong face shows, so the
  suite also checks which face is actually under the pointer.
- The phone-width run caught a layout bug (text spilling over the buttons) that desktop
  never showed.

**The fix.**
- A `lnk-deck` fence. Cards are written as plain `Q:` / `A:` / `why:` text; the page script
  turns the whole deck into one line of HTML carrying the cards as data, and `lnk-shell.js`
  builds it. Markdown never parses card markup.
- One owner for deck events (`lnk-shell.js`), with one listener per deck and none on the
  document.
- 3x5 and 4x6 sizes for the Four Rubber Bands (trivia and concept cards), with band colors.
  The card keeps index-card proportions but grows when the text needs room.
- `tools/check_decks.py`, run in CI. It flags indented HTML after a blank line anywhere in
  the Docsify pages, and malformed deck fences. Run against the original file, it points
  at exactly the two lines where cards 2 and 3 were lost.

**The rule to carry forward:** if a widget has repeating parts, don't hand-write it as
HTML in markdown. Give it a fence, the way terminals and panels already work, and keep one
script in charge of its events.

**Still open:**
- On a phone turned sideways, every Portland Desk page keeps the 300px sidebar open and
  scrolls sideways. That's site layout, not the deck; the deck fits the screen height.
- Ethan's story decks (the 3x5 trivia and 4x6 slates in the Episode 00 narrative) work,
  but their cards are hard-coded in `lnk-shell.js`. They could move to `lnk-deck` fences.
- CLAUDE.md still asks for parity between `portland-desk/` and `docs/portland-desk/`, but
  the root copy was archived (commit 611e5e4); `docs/portland-desk` is the only source.

**Follow-up: one deck for every page (October 27, 2026).** The fix above lived inside
Portland Desk (`lnk-shell.js` and Portland's stylesheet), so the Tamarack and ITM unit
pages couldn't use it. The deck is now one shared component: `docs/lnk-deck.js` and
`docs/lnk-deck.css`, with their own class names and no dependence on either site's styles.
`render_unit.py` reads the same fence (parser in `tools/_deck.py`) and adds the two files
only to pages that have a deck, so no other unit's output changed. The script finds decks
with a MutationObserver, because neither kind of page has its content at load: unit pages
fetch the narrative afterward, and Docsify swaps pages on every route change. The first real
user is `examples/itm310-exam2-cards/`: 185 Exam 2 terms, 137 cards in 11 decks, every card
checked on both faces at phone, sideways-phone and desktop widths.
The lesson: a component isn't shared until a second kind of page uses it. Test it there
before calling it reusable.
