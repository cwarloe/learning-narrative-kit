# Workshop

Working folders for authoring jobs, one per brief (`briefs/<brief_id>.brief.yaml`).
Nothing here is published. GitHub Pages serves only `docs/`.

```
workshop/<brief_id>/
  plan.yaml, plan.md    # course plan (course-glossary mode): term map, gaps, architecture
  status.yaml           # resumable record: stages, revisions used, open issues, next action
  candidates/<unit_id>/ # draft chapters, same file shapes as examples/<unit_id>/
  reviews/              # one report per review round (+ marks-stripped .cover.txt)
  preview/              # render_unit.py --out output; gitignored, rebuild any time
```

A candidate becomes part of a track only when the author accepts it. It is then copied
into `examples/` and shipped with `/ship-unit`. See `AGENTS.md` → Authoring workflow.

## Editorial review records

These are assessments of the cited revisions, not new authoring rules or records
that the proposed story changes have been applied. Both await author prioritization:

- [Portland Desk Five Commandments review](story-grid-review/reviews/portland-desk-6107625.md): all thirteen chapters at `6107625`, using the supplied Story Grid article.
- [Portland Desk dramatic and literary review](literary-review/reviews/portland-desk-1a17cc0.md): all thirteen chapters at `1a17cc0`, focusing on learning time, ordinary competence, intentions, obstacles, and premature resolution.

The narrative text is identical between these two revisions. Re-check the current
story before carrying a finding forward; a committed review is not an implemented fix.
