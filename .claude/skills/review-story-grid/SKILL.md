---
name: review-story-grid
description: Review a supplied scene or chapter against Story Grid's Five Commandments, with evidence and proportionate revision suggestions.
argument-hint: "[narrative file, unit directory, or chapter list]"
context: fork
agent: story-grid-reviewer
---

Review $ARGUMENTS using `tools/agents/story_grid_reviewer.md`.
If no target is supplied, ask for one. Read the specified narrative and required
canon/craft sources, then return the report in that agent definition's format.
Do not edit, commit, or publish the story. State whether you used the original
PDF, its verified source notes, or the live article. Distinguish the chapter arc
from its individual scenes.
