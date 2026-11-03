---
type: topic
summary: Weekly prep on Monday - board re-sort, meeting prep, project status, team code status
status: draft
updated: {{SETUP_DATE}}
---

# Routine: weekly (Monday morning)

Goal: start the week with a clear board and every meeting sorted. Propose first, write after the user confirms. If the run is scheduled and nobody answers, write the proposals to `weekly/` and leave the board unchanged.

## 1. Read
- `CLAUDE.md`, `context/goals.md`
- last week's `weekly/` note and `daily/` notes
- `meta/plan-vs-actual.md`
- `board.md`
- the role adapter notes in `context/me.md` (routine emphasis), if present

## 2. Collect
- **Calendar:** the next 7 days (title, attendees, description)
- **Notes and meetings:** last week's meetings and voice notes
- **Chat:** open threads, saved messages
- **Recurring inputs:** what `CLAUDE.md` lists under "Recurring inputs" that arrived this week
- **Radar:** run `routines/radar.md`
- **Tasks and tickets:** projects and initiatives the user leads or follows: state, health, latest update, anything at risk or overdue
- **Code (optional, engineering roles):** open PRs older than 5 days, PRs waiting more than 24 hours for a first review, the 3 oldest PRs, trend vs last week. A pattern view, not a per-person list.

## 3. Board proposals
Top of mind holds every big initiative that is really active (no fixed number; if it passes about 10, ask which ones to park). Propose to add one when a subject keeps coming up in meetings, chat or tickets for 2+ weeks. Propose to remove one when it's done or nothing has happened for 3 weeks.

For each board section (Top of mind, This week, Inbox), tag each item: [Keep], [Add], [Remove], [Mark done] or [Rollover]. The proposals come from:
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

## 5. Context gaps
As in `brief.md`, max 3 questions.

## 6. Write
**Labels (required):** every item in Needs attention, Replies and reviews, Waiting on others, Board proposals and on the board gets `priority` and `domain` (from `board.md`; else blocking or due today = P0, due this week = P1, otherwise P2 or P3), plus `topic` when it links to a Linear issue, project, initiative or OKR. Copy the `domains` map from `board.md` into the JSON. The renderer prints `LABEL CHECK` for anything missing; fix it and render again.

`weekly/YYYY-Www.md`, section "Weekly prep", in this order:
1. Board proposals
2. Meeting prep table
3. Project and ticket status
4. Team code status (if collected)
5. Insights (recurring inputs: 3-5 bullets each, with link)
6. Needs me
7. Context updates

Then write `views/data/weekly-YYYY-Www.json` (schema: `views/CLAUDE.md`, "New optional fields", Weekly). It needs: `last_week` (summary, went_well, slipped, decided, stats, lever, from `meta/plan-vs-actual.md`), `capacity` (40 h minus meeting hours, goal free hours = last week's unplanned work), `proposals[]` with `effort_h` (one per board and Inbox item, kind keep | add | done | next week | remove), `top_of_mind[]` with `health` and `move`, `days[]` (meetings by day with prep level in `tag`), `linear` (project and ticket status), `insights`, `teamprs` (or `teamprs.failed` when the code host is unreachable), `sources[]`. Then render it with `python3 scripts/render_view.py`, and open `views/weekly.html`. After confirmation, apply the board changes to `board.md`.

## 7. Close
Build the indexes, append to `log.md`, commit.

## Friction
When the user corrects anything in this routine, append to `meta/friction.md`: `- YYYY-MM-DD weekly: <what went wrong> -> <what they wanted>`.
