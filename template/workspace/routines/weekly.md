---
type: topic
summary: Weekly prep on Monday - task store re-sort, meeting prep, project status, team code status
status: draft
updated: {{SETUP_DATE}}
---

# Routine: weekly (Monday morning)

Goal: start the week with a clear task store and every meeting sorted. Propose first, write after the user confirms. If the run is scheduled and nobody answers, write the proposals to `weekly/` and leave the task store unchanged.

## 1. Read
- `CLAUDE.md`, `context/goals.md`
- last week's `weekly/` note and `daily/` notes
- `meta/plan-vs-actual.md`
- the task store: open tasks and comments since the last weekly (follow `meta/task-store.md` and its adapter), and `context/areas/index.md`
- the role adapter notes in `context/me.md` (routine emphasis), if present

## 2. Collect
- **Calendar:** the next 7 days (title, attendees, description)
- **Notes and meetings:** last week's meetings and voice notes
- **Chat:** open threads, saved messages
- **Recurring inputs:** what `CLAUDE.md` lists under "Recurring inputs" that arrived this week
- **Radar:** run `routines/radar.md`
- **People:** match every person in the collected items by id (`context/people/`, `routines/people.md`). Unresolved close people or unknown names go under "Claude asks".
- **Tasks and tickets:** projects and initiatives the user leads or follows: state, health, latest update, anything at risk or overdue
- **Code (optional, engineering roles):** open PRs older than 5 days, PRs waiting more than 24 hours for a first review, the 3 oldest PRs, trend vs last week. A pattern view, not a per-person list.

## 3. Task proposals
Top of mind holds every initiative that is really active (no fixed number; if it passes about 10, ask which ones to park). Propose a new one when a subject keeps coming up in meetings, chat or tickets for 2+ weeks and passes the initiative test (`context/areas/index.md`); creating it means a Top of mind task plus an Initiative option, only after a yes. Propose closing one when all its tasks are done, the end date passed, or nothing has happened for 3 weeks (complete the task, retire the option, after a yes).

For each section (Top of mind, This week, Waiting, Inbox), tag each task: [Keep], [Add], [Remove], [Mark done] or [Rollover]. The proposals come from:
- goals
- the radar
- project and ticket status (at risk or off track)
- meetings
- last week's plan vs actual, which shows how much room to leave for unplanned work

## 4. Meeting prep
Run `routines/meeting-prep.md` for the next 7 days. Summarise it as:

| Day | Meeting | Prep category | Proposed prep action |
|---|---|---|---|

If a meeting is unclear, ask instead of guessing.

## 4b. Documents per initiative
For every initiative in Top of mind, list the documents changed in its topic folder in `research/` last week (`git log --since="1 week ago" --name-only -- "research/<folder>"`, or file mtime). One line each: file, what changed. Put them under the initiative's `updates[]` in the weekly data and `docs[]` on its Top of mind entry. An initiative whose folder has not changed in 4 weeks is a candidate for "Paused". An initiative without a topic folder goes under "Claude asks".

## 5. Context gaps
As in `brief.md`, max 3 questions (including the new topic folder or document question, step d2).

## 6. Write
**Labels (required):** every item in Needs attention, Replies and reviews, Waiting on others, Task proposals and on the board gets `priority` and `area` (from the task store; else blocking or due today = P0, due this week = P1, otherwise P2 or P3; area by the tie-break in `context/areas/index.md`), plus `initiative` and `okr` when they apply. Board items also carry `id` and `url` from the task store. The renderer prints `LABEL CHECK` for anything missing; fix it and render again.

`weekly/YYYY-Www.md`, section "Weekly prep", in this order:
1. Task proposals
2. Meeting prep table
3. Project and ticket status
4. Team code status (if collected)
5. Insights (recurring inputs: 3-5 bullets each, with link)
6. Needs me
7. Context updates

Then write `views/data/weekly-YYYY-Www.json` (schema: `views/CLAUDE.md`, "New optional fields", Weekly). It needs: `last_week` (summary, went_well, slipped, decided, stats, lever, from `meta/plan-vs-actual.md`), `capacity` (40 h minus meeting hours, goal free hours = last week's unplanned work), `proposals[]` with `effort_h` (one per open task in This week, Waiting and Inbox, kind keep | add | done | next week | remove), `top_of_mind[]` with `health` and `move`, `days[]` (meetings by day with prep level in `tag`), `linear` (project and ticket status), `insights`, `teamprs` (or `teamprs.failed` when the code host is unreachable), `sources[]`. Then render it with `python3 scripts/render_view.py`, and open `views/weekly.html`. After confirmation, apply the changes to the task store through the adapter.

## 7. Close
Build the indexes, append to `log.md`, commit.

## Friction
When the user corrects anything in this routine, append to `meta/friction.md`: `- YYYY-MM-DD weekly: <what went wrong> -> <what they wanted>`.
