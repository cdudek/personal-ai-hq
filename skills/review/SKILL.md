---
name: review
description: Runs the Friday learning loop: compares drafts with what was actually sent, learns style and vocabulary, groups friction, triages the tips queue, shows plan vs actual. Everything is a proposal. Use when the user says "review", "weekly review", "what did you learn", "improve my style file", or "Friday review".
---

# review

## Find the workspace

1. Read `~/.config/personal-ai-os/workspace` (one line: the absolute path of the workspace). Setup writes it.
2. If that file is missing or unreadable (for example in a sandbox), use the current folder when it contains `CLAUDE.md` and `routines/`. In Cowork, the project's folder is the workspace.
3. Otherwise ask the user for the workspace path, or tell them to run `/personal-ai-os:setup` first. Do not guess a path.

Then read `<workspace>/CLAUDE.md` and `<workspace>/index.md`. Follow the rules in `CLAUDE.md`: nothing is saved to `context/` without a yes, nothing is sent without a yes.

## Steps

1. Run `routines/review.md`. Apply only what the user approves, and log every applied rule in `meta/learnings.md`.
2. If the routine ends with building indexes, run `python3 scripts/build_index.py` from the workspace, append one line to `log.md`, and commit with `git add -A && git commit -m "review: <date>"`. Never push.
3. When the user corrects you, append a line to `meta/friction.md`: `- YYYY-MM-DD review: <what went wrong> -> <what they wanted>`.
