# Story Grid pilot — Episode 11, The Air Is Shared

**Historical pilot:** this records a review of revision `56c303d` made before the
full article was supplied and before the subsequent story repairs. It is not a
current review or a PDF-verified assessment. The reviewer now uses
`tools/agents/references/story_grid_five_commandments.md`, verified against the
supplied PDF. Re-read the current narrative and re-check line references before
reusing these findings. In particular, useful scene fragments should not be
mistaken for complete scenes meeting all five criteria.

## Scope and basis

Reviewed narrative revision `56c303d` (before adding this reviewer):
`docs/portland-desk/narrative/11-the-air-is-shared.md`, lines 1–102.
Level: the chapter arc, with a closer example of the opening Maya scene.
This is not a review of every episode or a full scene-by-scene audit of Episode 11.

Supporting guidance consulted: `AGENTS.md`, `schema/README.md` (story-first,
beat structure, editorial judgment), `schema/VOICE.md`,
`docs/craft/learning-narrative-framework.md`, `docs/research/PORTLAND_TIMELINE.md`,
and `docs/research/PORTLAND_AUTHOR_BIBLE.md`. Episode 12's opening and after-action
review were consulted to check the wireless baseline and camera carry-forward
(`docs/portland-desk/narrative/12-when-the-ticket-escalates.md:9` and `:120`).
The lab is not used to supply missing story actions.

Reference: https://storygrid.com/articles/five-commandments-of-storytelling.
The environment blocked that page with a proxy 403. This pilot uses the agent's
working paraphrases of the established framework; it does not claim exact agreement
with the current article or quote it. This is an editorial interpretation, separate
from the repository's passing mechanical and browser checks.

## What works

- **A visible cost:** Maya uses a dock and misses her meeting
  (`docs/portland-desk/narrative/11-the-air-is-shared.md:32–34`). The safe workaround
  has an immediate human consequence without an invented catastrophe.
- **A helper with a bounded skill:** Reggie knows the physical access boundaries,
  admits he does not understand the device's network behavior, and leaves Ethan
  with work (`docs/portland-desk/narrative/11-the-air-is-shared.md:78`).
- **Residue that continues:** the unfilled camera request and saved wireless baseline
  (`docs/portland-desk/narrative/11-the-air-is-shared.md:86–90`) reappear in Episode 12.
  Keep those connections and the cost to Ken's crew.

## Chapter beat map

| Commandment | Assessment | Evidence | Interpretation |
|---|---|---|---|
| Inciting incident | Clear | `docs/portland-desk/narrative/11-the-air-is-shared.md:9–11`, `:24–26` | Ken's earlier assurance is put under pressure by Maya's failed connection and a duplicate corporate SSID. Ethan must restore access without trusting the wrong network. |
| Progressive complications and turning point | Partial | `docs/portland-desk/narrative/11-the-air-is-shared.md:54–58`, `:64–68`, `:76–80` | The open conference-room router, deauth reports, and physical lobby device broaden the problem. The bench discovery can turn the chapter from settings support to a physical-access problem. Todd's separate hotel/WEP call is useful context, but does not itself make the lobby problem worse. |
| Crisis | Partial | `docs/portland-desk/narrative/11-the-air-is-shared.md:24`, `:32–34`, `:88` | Speed versus verified access is implicit: Maya has a meeting, docking costs time, and scanner re-enrollment costs throughput. The chapter does not yet show a decisive moment in which Ethan weighs the competing costs of a particular response. This is a gap in the larger arc, not a demand for a spoken dilemma in every vignette. |
| Climax | Partial | `docs/portland-desk/narrative/11-the-air-is-shared.md:76`, `:84` | The apparent resolving action shuts a conference-room router's port, but that router was already unplugged at line 58. The malicious lobby device is a different object. The action therefore does not clearly resolve the threat that caused the chapter's main pressure. |
| Resolution | Partial | `docs/portland-desk/narrative/11-the-air-is-shared.md:84–90` | Restored clients, Ethan's lost Saturday, Ken's complaint, the unfilled camera order, and the baseline are real consequences. Their connection to the chosen containment action needs clarification; "It still slowed the dock" does not identify which change caused the scanner work. |

## Opening scene example — Maya

| Commandment | Assessment | Evidence and interpretation |
|---|---|---|
| Inciting incident | Clear | `docs/portland-desk/narrative/11-the-air-is-shared.md:24`: Maya cannot connect before a meeting. |
| Complication / turning point | Clear | `docs/portland-desk/narrative/11-the-air-is-shared.md:26`: the duplicate corporate SSID invalidates treating this as an ordinary wrong-password call. |
| Crisis | Partial | `docs/portland-desk/narrative/11-the-air-is-shared.md:24–32`: quick wireless access competes with the safer dock workaround, but Ethan's competing pressure is mostly inferred. |
| Climax | Clear | `docs/portland-desk/narrative/11-the-air-is-shared.md:32`: Ethan chooses docking and escalation instead of trusting the duplicate. |
| Resolution | Clear | `docs/portland-desk/narrative/11-the-air-is-shared.md:34`: Maya docks, is late, and the twin remains active. |

This small service vignette already does useful work. Its implicit crisis alone
is not a blocker or a reason to inflate the scene. A modest clarification could
serve the whole chapter; preserve its briskness and Maya's concrete cost.

## Causal chain and value change

Observed: an assurance about wireless safety meets a failed connection; additional
wireless and physical-access problems appear; equipment is disconnected; clients
return; Ethan and the dock pay in time, and a physical security gap remains.

Interpretation: the chapter could move from **confident reassurance to accountable,
costly caution**. That movement is supported by Ken's question at line 9 and his
in-person complaint at line 88. The weak connection is between the distinct devices,
Ethan's consequential choice, and the scanner re-enrollment. The paper trail and
baseline provide a credible carry-forward once that connection is clear.

## Prioritized findings

1. **Must address — resolving action targets the wrong device.**
   `docs/portland-desk/narrative/11-the-air-is-shared.md:58`, `:76`, `:84`.
   The conference-room router is removed twice while the lobby twin is left
   without an explicit disposition. Readers cannot connect the apparent climax
   to the initiating threat. Smallest useful direction: distinguish the two
   devices and show what actually happens to the lobby device. Do not merge
   them silently or invent a new incident.

2. **Consider — put the existing operational tradeoff at the decision.**
   `docs/portland-desk/narrative/11-the-air-is-shared.md:84–88`.
   The chapter charges a scanner-enrollment cost after the fact, but does not
   explain which action required it or what pressure Ethan faced when choosing.
   Smallest useful direction: connect the already-described response to its
   expected effect on the dock, then let the existing Saturday and Ken scene
   collect that cost. No larger danger or explanatory moral is needed.

3. **Consider — give the related tickets a clearer causal relationship.**
   `docs/portland-desk/narrative/11-the-air-is-shared.md:38–76`.
   Some calls illustrate different wireless concepts rather than complicate the
   same situation. Smallest useful direction: keep necessary separate calls,
   but show how the lobby investigation changes Ethan's priorities or available
   time. Do not pretend the unrelated hotel call caused the local attack.

## Author decisions and limits

- Decide whether the two devices are intentionally separate threats or whether
  the later paragraph accidentally names the wrong device. The source supports
  the contradiction, not an unambiguous replacement plot.
- Decide whether this remains an intentionally episodic day-in-the-queue chapter
  or gets a stronger central incident. Neither requires five explicit beats in
  every teaching paragraph.
- Certificate validation and other protocol claims need technical review; the
  beat map does not certify them. No technical correction or story rewrite was
  performed by this pilot, and it does not establish reader learning outcomes.

**Verdict: targeted revision recommended.** Preserve the opening workaround,
bounded helper, operational costs, and later carry-forwards. Repair the device
causality before considering a larger structural rewrite.
