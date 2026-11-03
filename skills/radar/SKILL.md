---
name: radar
description: Lists everything that needs the user now (PRs, ticket mentions, mails, chat messages, tasks) and what the user is waiting on from others, each with a deep link. Read only. Use when the user says "radar", "what needs me", "what's waiting for me", or "who am I waiting on".
---

# radar

## Find the workspace

1. Read `~/.config/personal-ai-os/workspace` (one line: the absolute path of the workspace). Setup writes it.
2. If that file is missing or unreadable (for example in a sandbox), use the current folder when it contains `CLAUDE.md` and `routines/`. In Cowork, the project's folder is the workspace.
3. Otherwise ask the user for the workspace path, or tell them to run `/personal-ai-os:setup` first. Do not guess a path.

Then read `<workspace>/CLAUDE.md` and `<workspace>/index.md`. Follow the rules in `CLAUDE.md`: nothing is saved to `context/` without a yes, nothing is sent without a yes.

## Steps

1. Run `routines/radar.md`. It only reads; offer drafts for replies and log each draft in `meta/drafts.md`.
2. If the routine ends with building indexes, run `python3 scripts/build_index.py` from the workspace, append one line to `log.md`, and commit with `git add -A && git commit -m "radar: <date>"`. Never push.
3. When the user corrects you, append a line to `meta/friction.md`: `- YYYY-MM-DD radar: <what went wrong> -> <what they wanted>`.
