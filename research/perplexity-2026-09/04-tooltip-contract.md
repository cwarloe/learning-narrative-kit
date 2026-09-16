# Prompt 4 — Tooltip Contract

- **Title:** Best practice for in-text glossary tooltips in exam study material
- **Model used:** GPT-5.6 Terra
- **URL:** https://www.perplexity.ai/search/35655266-27d8-4232-82b2-b788e6c0c2de

## Full answer

Direct answer:

In-text glossary tooltips should be concise (ideally 1–2 sentences, under 150 characters, or 2–3 bullets), self-contained, and avoid duplicating on-screen content; use a separate, accessible hover/focus trigger.

Include optional context only if it meaningfully clarifies the term for the exam; avoid lengthy narratives.

Citations/links belong in the sidebar (not in the hover) to keep the tooltip lightweight and the main text clean.

Proposed field schema:

- **definition:** short, exam-faithful definition (1–2 sentences, 40–180 chars recommended, no port numbers).
- **optional_context:** concise background or example (optional; 1–2 sentences, no overload).
- **refs_sidebar_only:** list of references or citations to place in the sidebar; not shown in the hover.

### 3 good tooltip examples (SSH vs Telnet)

- **SSH:** “Secure Shell (SSH) provides encrypted remote login and command execution.”
- **Telnet:** “Telnet is an insecure remote login protocol that transmits data in plaintext.”
- **SSH (note):** “SSH uses public-key cryptography; protects confidentiality and integrity of sessions.”

### 3 bad tooltip examples

- **SSH:** “SSH is the thing you use for logging in.” (too vague)
- **Telnet:** “Telnet is fast.” (irrelevant, missing definition)
- **SSH:** “SSH port 22.” (incorrect; port number disclosure not required and not a definition)
