---
name: task
description: Works the day's tasks or files a capture. With no argument it picks the one next action and works through today's tasks one at a time; any free text is filed as a capture (board task, agent task, tip, idea, source, shopping item, journal note or context fact). Use when the user says "what's next", "next", "let's get today's stuff done", "capture", "note this", "remember", "add a todo" or "idea:".
argument-hint: "[next|capture <text>]"
---

# task

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/version-check.md` first (if the variable is empty, `skills/_shared/version-check.md` in the plugin folder).

## Pick the variant

- No argument, or `next`: run `routines/next.md`.
- `capture <text>`, or any free text that is not the word `next`: run `routines/capture.md` with that text. Say in one line that you filed it as a capture.

Drafts and replies need the user's yes before anything is sent. Log corrections to `meta/friction.md`. Commit workspace changes locally; never push.
