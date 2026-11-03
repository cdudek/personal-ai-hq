---
name: refresh
description: Runs the monthly refresh: updates context pages, lints the wiki (contradictions, stale pages, orphans, broken links), and proposes a reorganisation. Use when the user says "refresh", "monthly refresh", "lint the workspace", "clean up my context", or "reorganise".
---

# refresh

## Find the workspace

1. Read `~/.config/personal-ai-os/workspace` (one line: the absolute path of the workspace). Setup writes it.
2. If that file is missing or unreadable (for example in a sandbox), use the current folder when it contains `CLAUDE.md` and `routines/`. In Cowork, the project's folder is the workspace.
3. Otherwise ask the user for the workspace path, or tell them to run `/personal-ai-os:setup` first. Do not guess a path.

Then read `<workspace>/CLAUDE.md` and `<workspace>/index.md`. Follow the rules in `CLAUDE.md`: nothing is saved to `context/` without a yes, nothing is sent without a yes.

## Steps

1. Run `routines/refresh.md`. Proposals first, apply after a yes, log every change.
2. If the routine ends with building indexes, run `python3 scripts/build_index.py` from the workspace, append one line to `log.md`, and commit with `git add -A && git commit -m "refresh: <date>"`. Never push.
3. When the user corrects you, append a line to `meta/friction.md`: `- YYYY-MM-DD refresh: <what went wrong> -> <what they wanted>`.
