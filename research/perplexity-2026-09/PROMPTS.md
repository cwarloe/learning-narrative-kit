# Perplexity research queue

Run in order. For each: New thread → select model → paste ONLY the prompt body → wait for full answer → copy full answer into the matching RESULTS file.

## 1 — ports accuracy — MODEL: Sonar (or Best/Pro Search with Sonar if picker differs)
FILE: 01-ports-accuracy.md
PROMPT:
CompTIA Security+ SY0-701: list the secure vs insecure protocol/port pairs commonly tested under "implement secure protocols" and firewall ports/protocols. For each pair give: common port(s)/transport, why insecure version is risky, secure replacement, and whether numbers are officially in objectives vs community study guides. Flag any disputed port numbers. Cite CompTIA objective language where possible and reputable study sources. Output as a table.

## 2 — story pedagogy — MODEL: Deep Research if available, else Claude Sonnet with Thinking
FILE: 02-story-pedagogy.md
PROMPT:
What does education research say about embedding technical vocabulary in a continuous narrative (vs flashcards/glossaries alone)? Cover: Goldratt's The Goal as informal precedent, narrative transportation, contextual vocabulary learning, worked-example / cognitive load cautions. What design rules reduce "vocab parade" failure? Practical implications for an adult IT certification precursor story with ~30–60 marked terms. Prefer peer-reviewed or strong secondary sources; cite them.

## 3 — dual-tier glossary UX — MODEL: Claude Sonnet (Thinking on if available)
FILE: 03-glossary-ux.md
PROMPT:
For an interactive learning story with inline marked terms: compare UX patterns for (a) exam/study terms vs (b) supporting jargon. Evaluate hyperlink-style underlines vs soft color tints, hover tooltips vs click, and an "Exam only / All" filter. Goal: reader keeps full sentence context if they never open a definition; definitions are optional lookup. Recommend a default pattern for mobile + desktop. Cite HCI/ed-tech sources where they exist; label speculation clearly.

## 4 — tooltip contract — MODEL: GPT (latest available)
FILE: 04-tooltip-contract.md
PROMPT:
Best practice for in-text glossary tooltips in exam study material: ideal length, whether to include examples/context, whether citations/links belong in the hover vs a sidebar. Propose a field schema: definition, optional context, refs (sidebar-only). Constraint: Security+ study — short exam-faithful defs, no invented port numbers. Give 3 good and 3 bad tooltip examples for SSH vs Telnet.

## 5 — help-desk realism — MODEL: Sonar
FILE: 05-helpdesk-realism.md
PROMPT:
What are realistic help-desk / MSP tickets that naturally force secure-vs-insecure protocol choices (Telnet/SSH, cleartext mail vs IMAPS/submission, FTP vs SFTP/FTPS, HTTP/HTTPS, RDP exposure, LDAP/LDAPS, SNMP community strings, TFTP)? For each, note common wrong "convenience" ask from a user/vendor and the correct operational decision. Prefer practitioner sources (Reddit sysadmin, MSP blogs, vendor KB) plus security guidance. No Hollywood breach plots.

## 6 — prior art — MODEL: Sonar
FILE: 06-prior-art.md
PROMPT:
Are there existing products or open projects that teach IT/certification topics via interactive narrative + inline glossary (not just gamified quizzes)? Search for story-based Security+, Network+, CCNA, or IT fundamentals learning. Summarize closest analogues to "The Goal"-style ops narrative or vocab-in-context HTML. What's missing in the market?

## 7 — authoring QA rubric — MODEL: Claude Sonnet
FILE: 07-authoring-rubric.md
PROMPT:
Given this authoring contract for a "learning narrative kit": (1) cohesive term set first, (2) one situation that forces terms to interact, (3) story-first with [[id|text]] marks, (4) short definitions, (5) cover test = story works with marks hidden, (6) HTML/review secondary — what failure modes should authors watch for? How should density (~2 marks per 100 words) and two tiers (exam vs support) be governed? Produce a one-page QA rubric.

## 8 — narrative POV and tense — MODEL: Deep Research if available; else a frontier reasoning model with Thinking ON (Claude Opus/Sonnet class or GPT-5 class). Do NOT accept a Nano/fast tier — see note below.
FILE: 08-pov-and-tense.md
PROMPT:
For instructional or educational fiction — stories written to teach domain content to adult learners, in the tradition of Eliyahu Goldratt's *The Goal* — what evidence exists on narrative point of view (first vs third person) and tense (past vs present)?

Cover each of the following, and state explicitly where evidence is absent rather than filling the gap:

1. Empirical work comparing POV or tense for comprehension, retention, or transfer in instructional narrative, case-based learning, or worked examples. If no such comparison exists, say so plainly rather than substituting adjacent findings.
2. Narrative transportation (Green & Brock and successors): does POV or tense measurably affect transportation? Separately — is transportation actually linked to *learning* outcomes, or only to attitude and persuasion change? Do not let the second follow from the first.
3. Mayer's signaling principle and cognitive load theory. A retrospective past-tense narrator can mark what mattered ("that was the conversation that changed how he thought about it"); a present-tense narrator structurally cannot, having not yet been through it. Does this give past tense a native signaling mechanism? Is there evidence for signaling delivered through narration, as opposed to typography, headings, or cueing?
4. Register markedness: is there reading-research evidence that present-tense narration in English imposes measurable processing cost relative to past tense, or is this a craft claim with no empirical backing?
5. Epistemic constraint: a first-person narrator can only know what that character knows. In a story teaching content the narrator-character is a novice at, does this force implausible expertise, awkward exposition, or a second "expert" character carrying the load? Any craft or instructional-design literature on this structural problem.
6. Fact check: what person and tense is *The Goal* (Goldratt, 1984) actually written in? Quote the opening lines. Same question for *The Phoenix Project*, *The Five Dysfunctions of a Team*, and any other widely used instructional narrative you can verify.

Context for the recommendation: ~2000-word chapters for adult IT certification learners; 30–60 vocabulary terms per chapter marked inline for hover definitions; narrator is a junior help-desk technician who does not yet know the material; a senior colleague supplies expertise. Design rule already in force: marked terms must sit on a decision or its complication, not in exposition.

Give a recommendation on POV and tense for this format, with reasoning tied to whatever evidence actually exists. Distinguish clearly between (a) findings from research, (b) established craft convention, and (c) your own inference — label each. Do not invent citations. If the literature is thin, the useful answer is a precise description of how thin it is and where the nearest adjacent evidence sits.

### Model note for this prompt
Prompt 2 (story pedagogy) was submitted to Claude Sonnet 5 and served by GPT-5 Nano; the answer skipped narrative transportation and returned no effect sizes. This question is harder — the likely finding is sparse or absent direct evidence, and a fast tier will paper over that with plausible-sounding adjacent claims. Confirm which model actually served the thread after it completes and record it in the FILE front matter, as with the other notes.
