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
She mapped [[five_forces\|Porter's five forces]] against the foundry market.
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
