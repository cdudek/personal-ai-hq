---
type: topic
summary: The whole Personal AI HQ on one page
status: current
updated: {{SETUP_DATE}}
---

# The system on one page

Details are in `CLAUDE.md` and `routines/`.

## The task store: five sections in your task manager, shown in the views

| Section | What it holds | Who changes it | Where |
|---|---|---|---|
| **Top of mind** | 3-7 big initiatives you are carrying right now | `weekly` proposes add or remove; you confirm | task store -> Top of mind |
| **This week** | priorities of the week, deep-prep tasks for meetings | `weekly` sets it, `brief` and `sync` re-plan it daily | task store -> This week |
| **Inbox** | everything that came in and is not sorted yet | `brief`, `sync`, `capture` add; `weekly` sorts | task store -> Inbox |
| **Waiting** | what you wait on others for | you or `brief` (from your comments) | task store -> Waiting |
| **Agent** | tasks the agent does itself | agent | task store -> Agent |

Rules for the task store (the tool and its ids are in `meta/task-store.md`):

- You read it in your task manager and in the views. Input: comment on a task, drag it, tick it off, or tell Claude in chat. Asking "what's next?" runs `routines/next.md`.
- Every task carries a `Closed when:` description line and one Area (`context/areas/index.md`).
- A Top-of-mind item links to its ticket, project or research folder when one exists.

## The four parts

| Part | What it is | Where |
|---|---|---|
| Storage (second brain) | wiki pages with a one-line summary each, generated indexes per folder | `context/`, `sources/`, `index.md` |
| Tasks | one task store in the cloud with a done signal per task | `meta/task-store.md`, `inbox/` |
| Visualise | read-only daily and weekly pages | `views/` |
| Dashboard | the weekly page: task proposals, team and project status, drift | `views/weekly.html` |

## The four loops

| Loop | When | What runs | What you do |
|---|---|---|---|
| Daily | weekdays morning | `brief` (plus `sync`, `radar`, `next`, `capture` on demand) | read it, answer up to 3 questions, confirm swaps |
| Weekly | Monday morning, Friday afternoon | `weekly`, then `review` | confirm task changes; approve or reject learning proposals |
| Monthly | first Monday | `refresh` | approve cleanups |
| Improvement | continuous | friction and drafts logged by every routine; `review` and `improve` turn them into rule changes | approve rule changes |

## A week

| When | What runs |
|---|---|
| Monday | `weekly`: task re-sort, meeting prep for the week |
| Weekdays | `brief`: radar, meetings, re-plan, daily note |
| During the day | `sync`, `radar`, `next`, `capture` on demand |
| Evening | `debrief` by hand |
| Friday | `review`: style, vocabulary, friction, tips |
| First Monday of the month | `refresh`: context refresh, lint, reorganise |
