---
type: topic
summary: The whole Personal AI HQ on one page
status: current
updated: {{SETUP_DATE}}
---

# The system on one page

Details are in `CLAUDE.md` and `routines/`.

## The board: three areas plus the agent's list, in `board.md`, shown in the views

| Area | What it holds | Who changes it | Where |
|---|---|---|---|
| **Top of mind** | 3-7 big initiatives you are carrying right now | `weekly` proposes add or remove; you confirm | `board.md` -> Top of mind |
| **This week** | priorities of the week, deep-prep tasks for meetings | `weekly` sets it, `brief` and `sync` re-plan it daily | `board.md` -> This week |
| **Inbox** | everything that came in and is not sorted yet | `brief`, `sync`, `capture` add; `weekly` sorts | `board.md` -> Inbox |
| **Agent** | tasks the agent does itself | agent | `board.md` -> Agent |

Rules for the board:

- You only read it, in the views, and give input in chat. Asking "what's next?" runs `routines/next.md`.
- Every task carries a `closed when:` line.
- A Top-of-mind item links to its ticket, project or research folder when one exists.

## The four parts

| Part | What it is | Where |
|---|---|---|
| Storage (second brain) | wiki pages with a one-line summary each, generated indexes per folder | `context/`, `sources/`, `index.md` |
| Tasks | one board with a done signal per task | `board.md`, `inbox/` |
| Visualise | read-only daily and weekly pages | `views/` |
| Dashboard | the weekly page: board proposals, team and project status, drift | `views/weekly.html` |

## The four loops

| Loop | When | What runs | What you do |
|---|---|---|---|
| Daily | weekdays morning | `brief` (plus `sync`, `radar`, `next`, `capture` on demand) | read it, answer up to 3 questions, confirm swaps |
| Weekly | Monday morning, Friday afternoon | `weekly`, then `review` | confirm board changes; approve or reject learning proposals |
| Monthly | first Monday | `refresh` | approve cleanups |
| Improvement | continuous | friction and drafts logged by every routine; `review` and `improve` turn them into rule changes | approve rule changes |

## A week

| When | What runs |
|---|---|
| Monday | `weekly`: board re-sort, meeting prep for the week |
| Weekdays | `brief`: radar, meetings, re-plan, daily note |
| During the day | `sync`, `radar`, `next`, `capture` on demand |
| Evening | `debrief` by hand |
| Friday | `review`: style, vocabulary, friction, tips |
| First Monday of the month | `refresh`: context refresh, lint, reorganise |
