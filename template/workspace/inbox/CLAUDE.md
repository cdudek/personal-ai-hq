# inbox/

Raw captures, one file per day: `YYYY-MM-DD.md`. One line per item: `- HH:MM [source] text`, plus `-> filed: <destination>` once it is routed (then no routine routes it again). A journal note leaves only a receipt here, never its text. Sources: chat, mail, calendar, meeting, voice, tickets, code, tasks, phone. `debrief` clears it: each item goes to the task store (Inbox), `ideas/`, `lists/`, `journal/` or is dropped.

**Done signals** (the user's habits, used to close items; adjust them via `review`):
- Chat: a saved message that is no longer saved = done. A reply from the user in the thread = handled.
- Mail: replied, archived, or labelled done = done. Inbox mode is "new only" (see top-level CLAUDE.md).
- Tickets and code: ticket closed or PR merged = done.
- Tasks tool: ticked off by the user = done.

**Closed when:** every task that goes to the task store gets one line saying what "closed" looks like, e.g. `closed when: the numbers are in the chat thread`. The agent checks this line on each run and learns from how the user closed similar tasks.
