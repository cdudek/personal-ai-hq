---
name: inbox
description: Lists everything that needs the user now (PRs, ticket mentions, mails, chat messages, tasks) and what the user is waiting on from others, each with a deep link. Read only. Use when the user says "inbox", "radar", "what needs me", "what is waiting for me" or "who am I waiting on".
---

# inbox

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/version-check.md` first (if the variable is empty, `skills/_shared/version-check.md` in the plugin folder).

Run `routines/radar.md`: it starts with the sources check ("Required sources" in `CLAUDE.md`). Every item shows what it is in a plain sentence, its state with dates, who waits since when and the effort, never only a name, number or link. Read only (the two permitted metadata writes are in `_shared/version-check.md`, "Read-only runs"): change nothing else in the workspace, send nothing.
