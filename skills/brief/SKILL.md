---
name: brief
description: Builds the briefing: the daily brief (calendar, meetings, mentions, mail, tickets, code reviews, task store, daily page), the weekly prep on Monday (task re-sort, week meetings, project and code status, weekly page), or a mid-day update after new input. Use when the user says "brief", "morning brief", "start my day", "good morning", "weekly", "plan my week", "Monday prep", "sync", "update brief" or "new priority".
argument-hint: "[daily|weekly|update]"
---

# brief

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/version-check.md` first (if the variable is empty, `skills/_shared/version-check.md` in the plugin folder).

## Pick the variant

Argument `daily`, `weekly` or `update` wins. With no argument infer, and say in one line what you inferred and why:

- `weekly`: it is Monday before noon and `<workspace>/weekly/` has no file for this ISO week.
- `update`: today's `daily/YYYY-MM-DD.md` already exists.
- otherwise `daily`.

## Run

- The task store (named in `meta/task-store.md`) is read and written through its adapter, `routines/stores/<store>.md`. If `meta/task-store.md` has no store yet, say "No task store yet: run /hq:setup or /hq:upgrade" and continue without tasks.
- `daily` runs `routines/brief.md`, `weekly` runs `routines/weekly.md`, `update` runs `routines/sync.md`. Run it end to end. On a schedule with nobody answering, write the output and leave every proposal open.
- At the end run `python3 scripts/build_index.py` from the workspace, append one line to `log.md`, and commit `git add -A && git commit -m "<variant>: <date>"`. Never push.
- When the user corrects you, append to `meta/friction.md`: `- YYYY-MM-DD <variant>: <what went wrong> -> <what they wanted>`.
