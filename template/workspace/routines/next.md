---
type: topic
summary: What's next - pick the next action and work through today's tasks with the user
status: draft
updated: {{SETUP_DATE}}
---

# Routine: next ("what's next?", "let's get today's stuff done")

1. Read the open tasks from the task store (follow `meta/task-store.md` and its adapter), today's `daily/` note, and the calendar for the next 2 hours.
2. Run `routines/radar.md` for anything new since the brief.
3. Pick the **one next action**:
   - First, whatever blocks others: PR changes requested, a decision someone waits on.
   - Then deep prep for a meeting starting within 2 hours.
   - Then the oldest "needs me" item.
   - Then the top ranked task in This week (rank is the order the user set). Among open tasks the order is: Priority, due date, ICE, blocks someone, age, size (smaller first). A Won't (MoSCoW) task is not offered.
4. Say what is next and the 2 after it, each with its context card, never a bare name, id or number: the What sentence, the State, who waits since when, effort and what happens if it waits. Then one recommendation with one reason. Every question that asks you to choose follows rule 10 in `CLAUDE.md` ("Context for every choice").
5. Offer to do it now, one item at a time. The user confirms each step; Claude never sends anything without a yes. What "do it" means depends on the item:
   - **A reply:** draft it with `context/writing-style.md`, log it to `meta/drafts.md`, and send after a yes.
   - **A PR:** open it, summarise the comments, propose fixes.
   - **Meeting prep:** gather the notes, the last meeting and open points into a one-page prep in `daily/`.
   - **A ticket answer:** draft the comment and post it after a yes.
6. After each item: complete it in the task store (and in the source if it has one), add a comment with what was done, say what's next, and continue until the user stops.
7. At the end, update today's `daily/` note ("Done in session"), re-render the daily view, append to `log.md`, commit.

Friction: `- YYYY-MM-DD next: ... -> ...` to `meta/friction.md`.
