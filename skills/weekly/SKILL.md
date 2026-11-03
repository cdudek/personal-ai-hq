---
name: weekly
description: Runs the weekly prep on Monday: board re-sort, meeting prep for the week, project status, team code status, insights, and the weekly view page. Use when the user says "weekly", "weekly prep", "plan my week", "week ahead", or "Monday prep".
---

# weekly

## Find the workspace

1. Read `~/.config/personal-ai-os/workspace` (one line: the absolute path of the workspace). Setup writes it.
2. If that file is missing or unreadable (for example in a sandbox), use the current folder when it contains `CLAUDE.md` and `routines/`. In Cowork, the project's folder is the workspace.
3. Otherwise ask the user for the workspace path, or tell them to run `/personal-ai-os:setup` first. Do not guess a path.

Then read `<workspace>/CLAUDE.md` and `<workspace>/index.md`. Follow the rules in `CLAUDE.md`: nothing is saved to `context/` without a yes, nothing is sent without a yes.

## Steps

1. Run `routines/weekly.md` end to end. When run on a schedule and nobody answers, write the proposals to `weekly/` and leave the board unchanged.
2. If the routine ends with building indexes, run `python3 scripts/build_index.py` from the workspace, append one line to `log.md`, and commit with `git add -A && git commit -m "weekly: <date>"`. Never push.
3. When the user corrects you, append a line to `meta/friction.md`: `- YYYY-MM-DD weekly: <what went wrong> -> <what they wanted>`.
