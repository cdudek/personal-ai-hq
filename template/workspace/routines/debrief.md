---
type: topic
summary: Evening debrief - plan vs actual, reflection, clear inbox
status: draft
updated: {{SETUP_DATE}}
---

# Routine: debrief (weekdays, evening, by hand)

A short guided conversation: one question at a time.

1. **Plan vs actual:** from today's brief and the task store (tasks completed or created today), list planned / done / unplanned (with source). Ask the user to confirm. Also ask for two hours figures (an estimate is fine, "unknown" is allowed, never invent): hours of unplanned work and hours in meetings today (meeting hours come from the calendar). Append the result to `meta/plan-vs-actual.md` as `YYYY-MM-DD planned N, done N, unplanned N (sources: chat N, exec N, meetings N), unplanned_h N, meeting_h N`.
2. **Work debrief:** what moved, what is stuck, what to start with tomorrow.
3. **Reflection:** pick one lens. Rotate between:
   - learning
   - feeling
   - a strength seen in a team member
   - a message to myself

   Write it to `journal/YYYY-MM-DD.md`. Never quote it anywhere else.
4. **Clear the inbox:** every line in today's `inbox/` without `-> filed:` goes to the task store (Inbox), `ideas/`, `lists/`, `journal/`, or is dropped. Mark each line `-> filed: <destination>` (or `dropped`). A line that already says filed was routed by `capture` or `brief`: never route it again, and never create a second task for it.
5. **Write:** today's `daily/` note, section "Debrief" (without the journal content).
6. Build the indexes, append to `log.md`, commit.

Friction: `- YYYY-MM-DD debrief: ... -> ...` to `meta/friction.md`.
