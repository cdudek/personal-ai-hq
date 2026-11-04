---
name: improve
description: Runs the learning loop. `review` compares drafts with what was sent, learns style and vocabulary, groups friction, triages the tips queue, checks the areas for drift and shows plan vs actual (everything is a proposal); `tip` audits one tip, post or link against the current setup and gives a verdict (adopt, backlog, discard). Use when the user says "review", "weekly review", "what did you learn", "improve", "should I adopt this" or pastes a link about working with AI.
argument-hint: "[review|tip <link or text>]"
---

# improve

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/version-check.md` first (if the variable is empty, `skills/_shared/version-check.md` in the plugin folder).

## Pick the variant

- `review`: run `routines/review.md`.
- `tip <link or text>` (or a pasted link or text): run `routines/improve.md` on it.
- No argument: on Friday run `review` and say so; on any other day list the open lines of `meta/tips.md` and offer to run `tip` on one.

Everything is a proposal; apply only what the user approves, and log each applied rule in `meta/learnings.md`. Commit locally; never push.
