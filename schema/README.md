# Authoring contract

## Principle

The **narrative** is the learning object. The glossary is the vocabulary that must cohere inside it. Review decks and HTML tooltips are secondary.

If you strip the marks and the sidebar, the story should still teach relationships among the ideas. If it doesn’t, you have a glossary with fiction garnish — the 8th-grade failure mode in reverse.

## Files

| File | Role |
|------|------|
| `unit.yaml` | Metadata, sources, constraints, pointers |
| `narrative.md` | Story with `[[term_id\|surface text]]` marks |
| `glossary.yaml` | Term bank for this unit (or a shared bank) |
| `review.yaml` | Optional retrieval deck derived from the glossary |

## Mark convention

```markdown
She mapped [[five_forces|Porter's five forces]] against the foundry market.
```

1. `term_id` must exist in the glossary.
2. Surface text can differ from `title` (natural prose).
3. Use a term when the character or situation *needs* it — not to tick coverage mid-sentence.
4. Coverage still matters for exam units: every required term should appear at least once, in a place that makes sense.

## Glossary entry

```yaml
- id: five_forces
  title: "Porter's 5 Forces"
  definition: "Framework assessing industry competitiveness: ..."
  tags: [mod-1]
  aliases: []
  related: []
```

Exam study: keep definitions faithful to course materials.
Open curricula (NADF): definitions can name analytical moves; tags may include `cognitive-trap`, `telemetry`, etc.

## Density (from your prototypes)

| Specimen | Words | Terms | Marks / 100 words |
|----------|------:|------:|------------------:|
| NADF prologue one-shot | ~1400 | 44 | ~3.2 |
| ITM 310 Vanguard Edge | ~3800 | 77 | ~2.0 |

When you already have a real glossary, aim nearer the ITM density: coverage without turning every clause into a highlight.

## Cover test

Hide every `[[...]]` mark. Read the paragraph. If it still sounds like a person thinking through a real situation, keep it. If it sounds like a vocab parade, rewrite the situation until the words are necessary.


## Beat structure — where a term should sit

> Prose that passes every check here can still read as machine-written. Tells, metrics, and the repair pass: [`VOICE.md`](VOICE.md).

The cover test tells you a beat is flat. This tells you why, and what to do about it.

A learner remembers a term by the **decision it was attached to**. A term that appears
only in setup, or only in narration after the problem is solved, is a definition wearing
a costume — it will read fine and teach nothing. That is the vocab-parade failure in its
subtle form, and the cover test catches it only sometimes.

Borrowed from the scene grammar in
[`novel-builder`](https://github.com/cwarloe/novel-builder)'s `templates/E-SCENE.md`,
adapted for teaching. Every beat has:

| Part | Question |
|------|----------|
| **Goal** | What does this person want in the next ten minutes? |
| **Complication** | What makes the obvious move wrong? |
| **Pivot** | What gets decided, and what does it cost? |

**The rule: marked terms belong at the complication or the pivot.** Not in the goal, not
in aftermath narration. If an `exam` term only ever appears in setup, move it or rebuild
the beat around it.

### The habit *is* the complication

In practice this track already runs on one engine: **the obsolete habit is the
complication; the replacement is the pivot.** People arrive carrying something they
learned at an old shop, in college, from vendor docs, or at 1 a.m. in a home lab, and the
beat is talking that habit into a decision that fits here.

That maps onto secure/insecure pairs natively — the insecure term is what they already do,
the secure term is what they decide:

> **Goal** — Jared wants the VLAN fixed in ten minutes.
> **Complication** — his script speaks `telnet`; the `enable_password` crosses in
> `cleartext`, and they got burned on a packet capture last year.
> **Pivot** — `ssh` with `key_auth`, rewritten once. *"We fix the script, not the
> `firewall`."* The concession costs him a rewrite; he says so out loud.

Every exam term in that beat sits on the complication or the pivot. None is in the goal.
Same shape in Maya's mail beat (`pop3`/`imap` as the habit, `imaps` and
`smtp_submission` as the decision) and in the phishing beats
(`typo_squatting` at the complication, `phish_report_button` at the pivot).

### Diagnostic for a flat beat

Ask in order:

1. What does this person **want**? If you can't say it in one clause, there's no beat yet.
2. What **habit** are they carrying, and where did they get it? Name the old shop.
3. What does the decision **cost** them? A free decision teaches nothing — the pivot needs
   friction, even small (a rewrite, a workflow change, an admission).
4. Where do the marked terms land? If they're in the goal or the aftermath, rebuild.

### Scope

This is a **quality lever, not a gate.** It is not validated mechanically and it must not
override effectiveness: if a beat teaches well and ignores the grammar, ship it. Narrative
coherence is how a term stops floating — it is the mechanism, not the product. Do not trade
a clear explanation for a better scene.


## Two-tier glossary (exam + support)

Some units (e.g. Security+ help-desk) keep **two tiers** of marked terms:

| `tier` | Role |
|--------|------|
| `exam` | Study targets for the course/exam — the primary review deck |
| `support` | Desk/network (or other) jargon a non-specialist reader may not know — hover for readability |

```yaml
- id: ssh
  title: SSH (22/TCP)
  definition: "Encrypted remote shell..."
  tags: [remote, secure]
  tier: exam
- id: jump_host
  title: Jump host / jump box
  definition: "A hardened intermediate server..."
  tags: [support, remote, network]
  tier: support
```

**Review filters:** renderers should support **Exam-only** (`tier: exam`) vs **All** (exam + support). Include `tier` on each review card so filtering is mechanical.

**Flavor stays unmarked.** Setting details that are atmosphere rather than vocabulary (Portlandia color — pannier, MAX, bike helmet, rain pants, coffee, cubes as furniture vibe, etc.) are left for the reader on purpose. Mark supporting *technical* terms, not scenery.

## Tooltip contract (hover)

The hover is interrupt literacy: one glance, back to the story.

| Field | Where it shows | Rule |
|-------|----------------|------|
| `definition` | **Tooltip body** | Short, exam-faithful (or plain-language for `tier: support`). Aim ~1–2 sentences, ITM-style `desc`. |
| `context` | **Tooltip body** (optional) | One clause only when the bare definition would not land mid-scene (e.g. “the secure replacement for Telnet”). Omit when definition alone is enough. |
| `refs` | **Not in hover** | Citations / deeper links live on the glossary sidebar entry or an “Open in glossary” expand. |
| Unit `sources` | Sidebar / unit chrome | Course or exam provenance for the whole bank (e.g. SY0-701 secure-protocol objectives). |

### Do

- Exam terms: definitions match study materials / exam expectations; do not invent rival port numbers.
- Support terms: plain-language glosses; no fake exam authority.
- Keep tooltip text free of URLs, “see also,” and long essays.

### Don’t

- Put links or references inside the hover.
- Mark flavor/atmosphere words (setting color the reader can guess).
- Use the tooltip as a second lesson — the narrative carries pedagogy.

```yaml
- id: ssh
  title: SSH (22/TCP)
  definition: "Encrypted remote shell protocol, typically on port 22/TCP."
  context: "Secure replacement for cleartext Telnet."
  tags: [remote, secure]
  tier: exam
  refs:
    - "CompTIA Security+ SY0-701 — implement secure protocols (remote access)"
- id: jump_host
  title: Jump host / jump box
  definition: "A hardened intermediate server you log into first, then reach internal systems from there."
  tags: [support, remote, network]
  tier: support
  # no refs required — support jargon, not an exam citation target
```

Renderers: tooltip = `definition` + optional `context`. Sidebar glossary row may show `refs`, `tags`, `tier`, and unit `sources`.

## Mark rendering (HTML)

Marks are **prose tints**, not hyperlinks. Use a soft background color (exam vs support) with no underline and no link cursor. Readers should keep full sentence context if they never hover; hover/sidebar are optional lookup, not a required click path.


## Scene artifacts (optional, HTML)

The narrative can include **exhibits the character is looking at** — a ticket, a console, a warning dialog, a process tree — so the learner sees the same surface the desk sees. These are still part of the story, not a second lesson. If you strip them, the surrounding sentences must still teach.

Author as fenced blocks in `narrative.md`. The renderer turns them into HTML. Do not hand-write the HTML.

Example (`ticket` fence):

    ```ticket
    id: HD-4419
    priority: High
    from: Maya (Accounting)
    subject: PC slow + random ads
    ```

| Fence | Use for |
|-------|---------|
| `ticket` | Help-desk / change ticket chrome (`id`, `priority`, `from`, `subject`, …) |
| `console` / `terminal` | Command line. First line may be `caption:`. Commands starting `$ `, `PS `, or `C:\` tint as input. |
| `gui` | On-screen dialog. `kind: cert-warning` or `ransomware`; `chrome`, `heading`, `actions: Back \| Advanced` |
| `alert` | EDR / SOC alert card |
| `tree` | Indented process tree (2-space indent = child) |
| `chain` | Certificate chain. Lines: `- Name \| trusted\|missing\|expired \| note` |
| `meter` | Single bar (`label`, `value` 0–100, `note`) |
| `table` | Pipe table inside the fence, or a native markdown pipe table in the prose |

Marks (`[[id|text]]`) work inside artifacts. Keep exhibits at the **complication or the pivot** — what the person is staring at when they have to decide — not as a gallery of extra specimens.

Flavor still unmarked. A fake UI is not a reason to mark “ticket” six extra times.

## Source of truth (markdown in, HTML out)

**Author and store units as markdown + YAML.** Do not hand-edit HTML as the story source.

| Layer | Files | Role |
|-------|-------|------|
| **Source** | `unit.yaml`, `glossary.yaml`, `narrative.md`, optional `review.yaml` | What humans (and agents) write and review |
| **Generated (Pages)** | `docs/<unit_id>/index.html` via `tools/render_unit.py` | Stable GitHub Pages URLs — committed under `docs/` |
| **Generated (local scratch)** | `examples/**/*.html` | Optional local preview — gitignored; rebuild anytime |

```bash
python tools/render_unit.py examples/<unit>
# → docs/<unit_id>/index.html  (unit_id from unit.yaml)
```

GitHub Pages serves from `/docs` on `main`. Re-running the renderer replaces the page at the same URL. Do not author the chapter in HTML.

## Authoring QA checklist (done-definition)

Use this before calling a unit “done.” Drawn from kit research (see `research/perplexity-2026-09/07-authoring-rubric.md`); wording adjusted to our tiers.

1. **Cohesive term set** — One bank that belongs together; no colliding definitions; every glossary id appears ≥1 in the narrative.
2. **One forcing situation** — People with habits/pressures that make the terms interact (not a vocab parade). Per beat: the habit is the complication, the replacement is the pivot, and marked terms sit on one or the other — see [Beat structure](#beat-structure--where-a-term-should-sit).
3. **Clean marks** — Every `[[id|text]]` resolves; ids unique; surface text reads as prose.
4. **Short definitions** — Tooltip-sized (`definition` + optional `context`); `refs` only on sidebar/expand.
5. **Cover test** — Hide marks; story still makes sense and still teaches relationships.
6. **Density** — Ballpark ~2 marks per 100 words (ITM-like); justify if far off.
7. **Two tiers governed** — `exam` = study targets; `support` = readability jargon; Exam-only / All still works; flavor stays unmarked.
8. **HTML secondary** — Markdown/YAML pass QA first; then render. Never author the chapter in HTML.

**Exam tier** here means “on the study/exam list,” not a graded quiz inside the page.

## Ship steps (agents / LLMs)

Mechanical pipeline, landing-card reminder, and copy-paste prompt: see [`AGENTS.md`](../AGENTS.md) at the repo root. Portland Desk track canon: [`examples/PORTLAND_DESK.md`](../examples/PORTLAND_DESK.md).

