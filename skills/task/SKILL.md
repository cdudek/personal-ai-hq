---
name: task
description: Works with the task store (the cloud task manager chosen in setup). With no argument it picks the one next action and works through today's tasks; `list` shows the ranked open tasks; `add`, `move`, `set` and `done` change a task; any other free text is filed as a capture (task, tip, idea, source, shopping item, journal note or context fact). Use when the user says "what's next", "next", "my tasks", "list tasks", "add a task", "mark done", "move to this week", "set P0", "capture", "note this", "remember", "add a todo" or "idea:".
argument-hint: "[next|list [section]|add <text>|move <task> <section>|set <task> <property> <value>|done <task>|capture <text>]"
---

# task

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/version-check.md` first (if the variable is empty, `skills/_shared/version-check.md` in the plugin folder).

## The task store

Read `meta/task-store.md`: it names the tool and holds the ids. Follow the adapter `routines/stores/<store>.md` for every read and write, and `routines/stores/README.md` for the rules. If `meta/task-store.md` is missing or its `store` is empty, say "No task store yet: run /hq:setup (new workspace) or /hq:upgrade (workspace from 0.2.0)" and stop. Name the tool in your output only through what the file says.

## Pick the variant

- No argument, or `next`: run `routines/next.md`.
- `list [section]`: show the open tasks in rank order, grouped by section (or one section), each as one line: priority, title, area, initiative, due, deep link. Read only.
- `add <text>`: create a task in Inbox with Area (by the tie-break in `context/areas/index.md`), Priority, Size, Source `Me`, a `Closed when:` description line and tag `ai`. Show what you set and the link.
- `move <task> <section>`, `set <task> <property> <value>`, `done <task>`: find the task by title or id (ask if more than one matches), make the change through the adapter, read it back and confirm in one line. `done` also adds a comment with how it was closed. Never reorder a task the user moved.
- `capture <text>`, or any free text that is none of the above: run `routines/capture.md` with that text. Say in one line that you filed it as a capture.

Writes to the task store follow rule 4 in `CLAUDE.md`: when the user typed the command, that is the yes. Drafts and replies need the user's yes before anything is sent. Log corrections to `meta/friction.md`. Commit workspace changes locally; never push.
