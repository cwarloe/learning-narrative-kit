# Theming: one file sets the look

**The rule:** every color, font and corner on the published site is written down once, in
`docs/tokens.css`. Stylesheets, pages and the scripts that write pages use `var(--name)`, not a
raw value like `#38bdf8` or `Consolas, monospace`. Change a value in `tokens.css` and every unit
page, track page, glossary, the landing page and Portland Desk change with it.

`tools/check_theme.py` holds the line. It runs in CI and fails on any raw color, font list or
pixel corner outside the tokens file.

## Where things live

```
docs/tokens.css                     the values: colors, fonts, corners, the outline palettes
docs/unit.css, docs/lnk-deck.css    @import tokens.css, then use var(--name)
docs/portland-desk/assets/*.css     lnk-theme.css @imports ../../tokens.css; the rest use var(--name)
tools/build_hub_index.py            landing page: links tokens.css
tools/render_track.py               track contents page: links ../tokens.css
tools/render_glossary.py            track glossary: links ../../tokens.css
tools/render_unit.py, _track.py     inline styles in unit pages: var(--name) only
template/assets/tokens.css          the copy a new Docsify course starts from
```

Generated pages (`docs/<unit_id>/`, `docs/index.html`, track pages) are never edited by hand.
Change the stylesheet or the renderer, then re-render.

## How the names work

- **Names say what the color is for, not what it looks like.** `--surface`, `--primary`,
  `--danger`, `--paper-ink`. Not `--blue`. A name like `--blue` is wrong the day the color changes.
- **Steps share the name.** `--danger` is the main red; `--danger-soft` is lighter and
  `--danger-deep` is darker.
- **Text that sits on a color has an "-ink" partner.** Text on a `--primary` button uses
  `--primary-ink`; text on a paper card uses `--paper-ink`.
- **See-through colors are mixed where they are used**, so they follow the base color:
  `color-mix(in srgb, var(--primary) 12%, transparent)`. Use `--shade` (black) for shadows and dark
  overlays and `--glare` (white) for light ones.
- **Paper cards** (job aids, flashcards, the slates) are light cards drawn on the dark page. They use
  the `--paper-*` names, so the dark page and the cards can change separately.
- **Printing** uses `--print-paper` and `--print-ink`. Keep them white and black.

## Changing the look

| To | Do this |
|---|---|
| Change a color everywhere | Edit its value in `docs/tokens.css` (and `template/assets/tokens.css` if new courses should get it too) |
| Change a font | Edit the `--font-*` value in `docs/tokens.css` |
| Change how round the corners are | Edit the `--radius-*` values |
| Need a new kind of color | Add a name that says what it is for to `docs/tokens.css`, with a short comment, then use it |
| Change the printable outline's colors | Edit the `[data-theme]` blocks at the bottom of `docs/tokens.css` |

## When a raw value has to stay

Put `theme-ok: <reason>` in a comment on that line. The checker skips the line, and the reason
stays visible to the next person. Today there is one: the Mermaid flowchart in
`portland-desk/workbench/01-the-paper-cert.md`, whose `style` lines only accept real colors
(a `var()` there breaks the diagram).

Two other kinds of page are listed by the checker but not failed. Each has its reason in `EXEMPT`
in `tools/check_theme.py`:

- **Design mockups** (`docs/comic_card_mockup.html`, `docs/handcrafted_cards_mockup.html`). They
  show options nobody has picked yet. When one is chosen, move its colors into `tokens.css` and take
  it off the list.
- **The Wireshark video storyboard** (`docs/portland-desk/assets/video/`). It is recorded to an mp4
  by a separate playbook, so a token change could not reach the video anyway.

Mermaid's own colors on Portland Desk are read from the tokens when the page loads (see the
`mermaid.initialize` block in `docs/portland-desk/index.html`), because Mermaid needs real color
values, not `var()`.

## Checking

```bash
python3 tools/check_theme.py
```

It prints each line that breaks the rule, with the file and line number, and the exempt pages with
their counts.
