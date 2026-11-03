---
name: improve
description: Audits a tip, post, video or article against the current setup and gives a verdict: adopt, backlog or discard. Use when the user says "improve", "should I adopt this", "check this tip", "does my setup already do this", or pastes a link about working with AI.
---

# improve

## Find the workspace

1. Read `~/.config/personal-ai-os/workspace` (one line: the absolute path of the workspace). Setup writes it.
2. If that file is missing or unreadable (for example in a sandbox), use the current folder when it contains `CLAUDE.md` and `routines/`. In Cowork, the project's folder is the workspace.
3. Otherwise ask the user for the workspace path, or tell them to run `/personal-ai-os:setup` first. Do not guess a path.

Then read `<workspace>/CLAUDE.md` and `<workspace>/index.md`. Follow the rules in `CLAUDE.md`: nothing is saved to `context/` without a yes, nothing is sent without a yes.

## Steps

1. Run `routines/improve.md` on the link or text the user gave, or on the open lines in `meta/tips.md`.
2. If the routine ends with building indexes, run `python3 scripts/build_index.py` from the workspace, append one line to `log.md`, and commit with `git add -A && git commit -m "improve: <date>"`. Never push.
3. When the user corrects you, append a line to `meta/friction.md`: `- YYYY-MM-DD improve: <what went wrong> -> <what they wanted>`.
