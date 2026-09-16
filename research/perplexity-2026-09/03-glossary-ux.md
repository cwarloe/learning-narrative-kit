# 3 glossary UX
Model used: GPT-5 Nano (Claude Sonnet 5 was selected in the picker before submission; completed thread displayed GPT-5 Nano; no Thinking variant was available)
URL: https://www.perplexity.ai/search/f12797ed-3217-497a-9f98-dc1898e320cd

## Direct answer
For inline marked terms, treat exam/study terms as glossary-like anchors with optional definitions, and supporting jargon as non-intrusive inline hints that expand only on hover or click. The reader should be able to read the story as ordinary prose without opening anything.

## Recommended pattern (mobile + desktop)
Default: underline all marked terms, add a soft color tint, and provide a subtle hover/focus change. Show a lightweight tooltip on hover/focus; on click or tap, open a side panel (desktop) or modal/bottom sheet (mobile) with the full definition and example. Do not replace or reflow the sentence with the definition.

### Exam/study terms
- Use a distinct but consistent underline in an accessible branded color. A small “E” badge may signal exam relevance, but test this because badges add visual noise.
- Hover/focus tooltip: concise definition, approximately 120–150 characters maximum.
- Click/tap: side panel or modal with the full definition and example sentence; closing returns the reader to the same sentence.
- Keep the term visually linked while leaving the surrounding sentence fully readable if the definition is never opened.

### Supporting jargon
- Use a lighter underline or soft tint, less prominent than exam terms.
- Offer a brief micro-tooltip on hover/focus.
- On click/tap, expand a non-intrusive inline snippet or collapsible glossary row beneath the sentence, rather than interrupting the reading flow.

### “Exam only / All” filter
Place a compact toggle at the top of the term-rich section. In Exam only mode, non-exam terms render as plain text (or with minimal decoration); exam terms retain interactive affordances. In All mode, both tiers render with their respective treatments. Make the state persistent per reader, and do not alter the prose itself—only marks and affordances.

## Underlines vs. soft tints
Underlines are the primary affordance because they communicate clickability and remain discoverable without relying on color. A tint can distinguish tiers and supply a gentle hover state, but tint alone risks being mistaken for highlighting or being invisible to color-vision users. Use sufficient contrast, visible focus, and a non-color cue (underline, icon, or label). Exact hues and typography are speculation and should be validated with usability testing.

## Hover vs. click
Hover is fast on desktop but unavailable on touchscreens and can be difficult for keyboard users. Treat hover as a preview only; support focus and keyboard activation, and require click/tap for durable content. Tooltips are appropriate for brief definitions; longer explanations, examples, and references belong in a side panel or modal. Provide an explicit close control, sensible focus management, and escape-key support.

## Accessibility and context rules
- Use real interactive controls or links with accessible names that identify tier (Exam term vs supporting term).
- Support keyboard focus plus Enter/Space; do not make hover the only route.
- Keep the sentence and term in the DOM and visually stable when a definition opens.
- Ensure tooltip is not clipped by the viewport, works at mobile widths, and does not obscure the term’s context.
- Do not repeat information already visible on screen; labels and examples should add value.
- Let screen readers discover that a term has optional help without forcing the help text into the reading order.

## Evidence and limits
The answer cited Nielsen Norman Group tooltip guidance: https://www.nngroup.com/articles/tooltip-guidelines/. It reported 10 sources but rendered most as source cards without direct URLs. The recommendation to use separate visual tiers, a filter, and soft tints is a design recommendation/speculation rather than a demonstrated universal optimum; empirically test comprehension, distraction, accessibility, and recall on both phone and desktop.
