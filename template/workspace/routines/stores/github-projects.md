---
type: topic
summary: Task store adapter for GitHub Projects (not recommended for personal tasks)
status: current
updated: {{SETUP_DATE}}
---

# Task store: GitHub Projects (not recommended)

Model: `routines/stores/README.md`. Config and ids: `meta/task-store.md`.

**Why not recommended:** GitHub Projects is built for repository work, not for private personal tasks. A task you can comment on must be an issue in a repository (draft items have no comments), so personal tasks end up inside a repo and visible to its collaborators. Use it only when you already live in GitHub and accept that. Prefer Asana, Notion, Monday or Trello.

## Connector
The `gh` CLI (`gh project ...`, `gh issue ...`), which is GitHub's standard interface; it needs the `project` scope (`gh auth refresh -s project`). No API token handling by Claude, no extra scripts, no browser. List what works in this session and test one read.

## Create the board
1. A user-owned Project (v2), visibility private, "<board_name>". Items are issues in one private repository you create for this ("<board_name>-tasks").
2. Use the built-in Status field with the options Top of mind, This week, Waiting, Inbox, Agent, Done only if it already has them or `gh` can set them when the project is created; otherwise use the section as a description line (`Section: ...`) and say so in `meta/task-store.md`. Never edit field options later.
3. Properties are description lines in the issue body (README, "Properties"; Size XS-XL, MoSCoW and `ICE: I x C x E = score` included; a Number project field may hold Impact, Confidence, Ease and ICE if the user already has them); reuse existing project fields that match, with a recorded mapping.

## Initiatives
An initiative is a milestone `🤖 <Initiative>` in the tasks repository (description: outcome, end date, OKR, `Topic folder: <name>`, links; due date = end date). Its tasks are the issues assigned to it. Close the milestone after the user's yes.

## Read
`gh project item-list` for open items with all fields in board order; issue comments since a date with `gh issue view --comments` or the API.
Context card: read `What:`, `Why / who waits:`, `State:`, `Decision or next step:`, `Effort:` and `Links:` from the description lines below `Closed when:` (view fields `what`, `why`, `state`, `decision`); a task without `What:` and `State:` is incomplete and gets fixed by the brief.

## Write
- **Create:** an issue in the repo with the property lines in the body and its initiative milestone, add it to the project, label `ai` if the label exists. Then the context card (`routines/stores/README.md`, "Context card"): `What:`, `Why / who waits:`, `State:` (with dates), `Decision or next step:`, `Effort:`, `Links:`, one line each, below the `Closed when:` line. Update `State:` (and the other lines) on every move, comment or change, and when newer information is read.
- **Move:** set Status (or the `Section:` line). **Set:** rewrite the body line. **Complete:** set Status Done and close the issue.
- **Comment:** `gh issue comment`.
- **Create or close an initiative:** create or close the milestone (after the user's yes).

## Team tasks
Create an issue that links to the team's task; never copy its content.

## Deep link format
The issue URL `https://github.com/<owner>/<repo>/issues/<n>`.

## Limits
- No private personal-task semantics: tied to repositories and their access.
- Draft items cannot be commented on, so they are not used.
- Rank is the item order in the project view.
