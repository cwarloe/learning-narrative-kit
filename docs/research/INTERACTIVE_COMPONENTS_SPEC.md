# Interactive Web Components Specification: `lnk-terminal` & `callout-panel`
**Repository:** `learning-narrative-kit`  
**Host Framework:** Docsify v4 (Static Zero-Backend Architecture)  
**Assets:** `assets/lnk-terminal.js`, `assets/lnk-terminal.css`, `assets/lnk-panel.css`

---

## 1. Overview & Architectural Constraints

The Learning Narrative Kit deploys entirely as a static zero-backend site on GitHub Pages. To provide tactile command-line troubleshooting and graphic novel visual panels without heavy WebAssembly containers or external API servers:
1. **`lnk-terminal`:** A lightweight, client-side, vanilla JavaScript/CSS terminal emulator that simulates realistic CLI prompts (`cmd.exe`, `powershell`, `serial`), handles command matching with branchable falsifiable responses, provides an animated keystroke replay mode, and updates live objective progress pills.
2. **`callout-panel`:** A responsive graphic novel container supporting 16:9, 21:9, 4:3, and 1:1 aspect ratios, complete with titles, badges, and captions. When no image is present, it renders a styled concept art placeholder containing the Grok Imagine prompt.

---

## 2. Component Specification: `lnk-terminal`

### Markdown Authoring Syntax

```markdown
```lnk-terminal
title: "CONSOLE: TOLEDO SCALE INTERFACE (COM1 /dev/ttyS0)"
shell: "serial"
prompt: "SCALE_04# "
replay: true
objectives:
  - id: "obj-status"
    label: "Inspect UART interface status and error counts"
    trigger: "status"
  - id: "obj-dips"
    label: "Inspect SW1 DIP switch hardware clock divider"
    trigger: "read-dips"
  - id: "obj-baud"
    label: "Recalibrate baud rate clock divider to 9600"
    trigger: "set-baud 9600"
---
status: |
  Interface: COM1 (RS-232 Asynchronous)
  Baud Rate: 19200
  Framing Errors (FE): 14,892 (100% CORRUPTION)
  Warning: Framing rate desynchronized.

read-dips: |
  DIP Switch Bank SW1: [SW1-3: ON (19200 Baud), SW1-4: OFF]
  Action: Set Switch 3 OFF, Switch 4 ON.

set-baud 9600: |
  Recalibrating UART Clock Divider to 9600 Baud...
  [OK] Framing Errors: 0 / 1000 packets.
  Stream: SCALE_04: READY - 042.8 LBS - DIVERTER NORMAL
```
```

### Key Features
* **Shell Themes:**
  * `cmd`: Classic white-on-black command prompt (`C:\> `).
  * `powershell`: Blue accent prompt (`PS C:\Support> `).
  * `serial`: Amber/green VT100 serial console (`SCALE_04# `).
* **Command Matching:** Case-insensitive dictionary lookup. Unrecognized commands output an authentic error and suggest typing `help`. Special commands: `clear` / `cls`, `help`.
* **Animated Keystroke Replay:** Clicking `[Replay Triage]` automatically types the objective commands sequentially at human typing speed (45ms per keystroke) with pauses before Enter.
* **Objective Pills:** Interactive badges at the bottom of the terminal window tick green with a `[OK]` checkmark as each target command is executed.

---

### Keyboard and assistive technology

Terminal command fields have descriptive accessible names. Tab reaches the replay
button, the scrollable history region, and the command field, with visible focus.
Output appears in a separate polite live log so typing is not announced as output.
A status region announces completed objectives and replay state. During replay,
the button remains focusable and is marked unavailable; repeated activation does
not start another run. Scratchpads take their accessible names from their visible
titles, and answer disclosure controls retain native keyboard behavior.

The shared flashcard component announces the current question or answer, marks
the flip button's state, and hides the inactive face from the accessibility tree.
Its headings and band labels meet a text contrast ratio of at least 4.5:1.
Browser checks cover names, keyboard focus and activation, announcement-region
updates, and card-label contrast. Spoken output still needs a screen-reader check.

---

## 3. Component Specification: `callout-panel`

### Markdown Authoring Syntax

```markdown
```callout-panel
title: "FIGURE 1.1: PIN 2 REALIGNMENT ON THE TOLEDO SERIAL INTERFACE"
badge: "Physical Layer Schematic"
ratio: "1:1"
caption: "Macro schematic: Ethan uses the 0.5mm hollow brass sleeve of his drafting pencil as a miniature lever to realign Pin 2 (Receive Data / RXD) without snapping the brittle copper pin."
prompt: "Transform reference photo of a DB-9 male connector into a high-detail macro technical illustration..."
image: "assets/panels/ep01-serial-pin.webp"
```
```

### Parameter Reference
* `title`: The figure header displayed in the top bar.
* `badge`: Component category badge (e.g. `Physical Layer Schematic`, `Hardware Anatomy`).
* `ratio`: Canvas aspect ratio (`16-9`, `21-9`, `4-3`, `1-1`).
* `caption`: Explanatory text rendered in the panel footer.
* `prompt`: The concept art generation prompt. Rendered in the placeholder box when `image` is omitted.
* `image`: Relative path to the rendered artwork (e.g. `assets/panels/ep01-serial-pin.webp`).

---

## 4. Component Specification: `lnk-deck` (flashcard decks)

A deck of flip cards: click, Space or Enter flips; Previous / Next, the arrow keys,
and the dots move between cards; Shuffle reorders the deck. Write every new deck as a
fence. Do not hand-write deck HTML in markdown (see "Why a fence" below).

The deck is one shared component that works on every page in the kit:

| Piece | File | Job |
|---|---|---|
| Behavior | `docs/lnk-deck.js` | Builds and runs every deck on the page. A MutationObserver finds decks added after load (Docsify route changes, unit pages that fetch their narrative), so pages don't call anything |
| Look | `docs/lnk-deck.css` | Self-contained card styles, all scoped under `.lnk-deck`; no page stylesheet needed |
| Portland Desk | `docs/portland-desk/index.html` | The Docsify hook parses the fence; the page loads `../lnk-deck.css` and `../lnk-deck.js` |
| Unit pages (Tamarack, ITM) | `tools/render_unit.py`, `tools/_deck.py` | `narrative.md` uses the same fence; the renderer emits the placeholder and adds the two files only to pages that have a deck |

Both parsers turn the fence into `<div class="lnk-deck" data-deck="…">`, where `data-deck`
is the deck as URL-encoded JSON. Keep the JavaScript parser in `index.html` and the Python
one in `tools/_deck.py` in step.

### Markdown Authoring Syntax

````markdown
```lnk-deck
title: RED BAND // ATOMIC RECALL DECK
meta: Spaced Retrieval Warmup • CompTIA A+ Core 1
size: 3x5
band: red
---
tag: BOUNDARY // VOLATILITY
Q: Power cuts abruptly during an office outage. Does data in RAM survive the drop?
back_tag: GROUND TRUTH // THE LAW
A: NO. Dynamic RAM is 100% volatile.
why: DRAM stores bits as charges that need constant refresh; when power drops, they're gone.
---
band: green
Q: You run `ping 127.0.0.1` and get replies. Does that prove the cable works?
A: No. Loopback never leaves the machine.
```
````

| Field | Where | Meaning |
|---|---|---|
| `title`, `meta` | header | Deck badge text and the small line beside it |
| `size` | header | `3x5` (trivia, 5:3) or `4x6` (concepts, 3:2). Default `3x5` |
| `band` | header or card | `red`, `green`, `yellow`, `blue` (the Four Rubber Bands). A card's `band` overrides the deck's |
| `Q`, `A` | card | Front prompt and back answer. Both required |
| `why` | card | One or two sentences under the answer |
| `tag`, `back_tag` | card | Highlight-bar labels on the front and back (back defaults to "Answer") |
| `hint` | card | Replaces the front footer's flip hint |

- Cards are separated by a line containing only `---`. Blank lines anywhere are fine.
- A long value can continue on the next line; it joins the field above. Don't start a
  continuation line with `Word:`, or it will be read as a new field
  (`tools/check_decks.py` catches this).
- Card text is plain text. `Backticks` become inline code; HTML is shown as typed.

### Why a fence (the bug this replaced)

The first deck was hand-written HTML inside the workbench markdown, and it rendered as
one card instead of three. Docsify's markdown parser ends an HTML block at the first blank
line; the next card's indented markup was then treated as an indented code block, so cards
2 and 3 appeared as raw HTML text and the deck held one card. Separately, `index.html` and
`lnk-shell.js` each bound a click handler that toggled `flipped`, so every click flipped the
card and flipped it straight back. The fence turns the whole deck into one line of HTML that
carries the cards as data, so markdown never parses card markup, and one script (now
`docs/lnk-deck.js`) is the only code that binds deck events.

### Behavior and layout notes

- One listener per deck on the deck element handles clicks and keys. Nothing is bound on
  `document`, so revisiting a page doesn't stack handlers.
- The two faces share one CSS grid cell with an invisible spacer whose padding is a
  percentage of the card's width (60% for 3x5, 66.67% for 4x6). The card keeps index-card
  proportions when the text is short and grows taller when it isn't (on phones). Don't use
  `aspect-ratio` here: it fixed the height and long answers spilled over the buttons.
- Check: `python3 tools/check_decks.py` (also runs in CI). With no arguments it checks the
  Portland Desk pages and every `examples/*/narrative.md`.
- Worked example: `examples/itm310-exam2-cards/`, 137 cards in 11 decks, generated from
  `cards.yaml` by `build_cards.py`.

