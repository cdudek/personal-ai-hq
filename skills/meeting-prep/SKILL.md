---
name: meeting-prep
description: Preps one meeting or all meetings of a day or week: reads attached docs and links, last time's action items (mine and others'), 1:1 context, and where a topic stands. Use when the user says "prep my meeting", "meeting prep", "prepare for the 1:1", "what is this meeting about", or names a meeting to prepare.
---

# meeting-prep

## Find the workspace

1. Read `~/.config/personal-ai-os/workspace` (one line: the absolute path of the workspace). Setup writes it.
2. If that file is missing or unreadable (for example in a sandbox), use the current folder when it contains `CLAUDE.md` and `routines/`. In Cowork, the project's folder is the workspace.
3. Otherwise ask the user for the workspace path, or tell them to run `/personal-ai-os:setup` first. Do not guess a path.

Then read `<workspace>/CLAUDE.md` and `<workspace>/index.md`. Follow the rules in `CLAUDE.md`: nothing is saved to `context/` without a yes, nothing is sent without a yes.

## Steps

1. Run `routines/meeting-prep.md` for the meeting, day or week the user names. Ask if the meeting is unclear; never guess.
2. If the routine ends with building indexes, run `python3 scripts/build_index.py` from the workspace, append one line to `log.md`, and commit with `git add -A && git commit -m "meeting-prep: <date>"`. Never push.
3. When the user corrects you, append a line to `meta/friction.md`: `- YYYY-MM-DD meeting-prep: <what went wrong> -> <what they wanted>`.
