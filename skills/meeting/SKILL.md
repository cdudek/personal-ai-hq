---
name: meeting
description: Preps a meeting: reads attached docs and links, last time's action items (mine and others'), 1:1 context and where a topic stands. Use when the user says "prep my meeting", "meeting prep", "prepare for the 1:1", "what is this meeting about" or names a meeting.
argument-hint: "[meeting name or time]"
---

# meeting

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/version-check.md` first (if the variable is empty, `skills/_shared/version-check.md` in the plugin folder).

Run `routines/meeting-prep.md` for the meeting in the argument (a name or a time). With no argument prep the next meeting on today's calendar and say which one you picked. Nothing is sent without a yes.
