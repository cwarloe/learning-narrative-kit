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
