---
type: topic
summary: Task store adapter for GitHub Projects (not recommended for personal tasks)
status: current
updated: {{SETUP_DATE}}
---

# Task store: GitHub Projects (not recommended)

Model: `routines/stores/README.md`. Config and ids: `meta/task-store.md`.

**Why not recommended:** GitHub Projects is built for repository work, not for private personal tasks. A task you can comment on must be an issue in a repository (draft items have no comments), so personal tasks end up inside a repo and visible to its collaborators. Use it only when you already live in GitHub and accept that. Prefer Asana, Notion, Monday or Trello.

## Connector and fallback
Use the `gh` CLI (`gh project ...` and `gh issue ...`); it needs the `project` scope (`gh auth refresh -s project`). The GitHub connector or MCP server may cover Projects only in part; list its tools in this session before relying on it. Fallback: Claude in Chrome on github.com. If none works, setup prints the manual steps.

## Create the board
1. A user-owned Project (v2), visibility private, named "<board_name>". Items are issues in one private repository you create for this ("<board_name>-tasks"); that repository is the place for the comment threads.
2. Fields: Status (single select, built in): Top of mind, This week, Waiting, Inbox, Agent, Done. Single-select fields: Area, Initiative, OKR (optional), Priority (P0-P3), Size (S, M, L), Source. Text: Closed when. Date: Due. Waiting on: the issue assignee field is taken by the user, so use a text field.
3. If the CLI or connector cannot create a field, setup gives the exact manual steps and reads the field ids back.
4. Saved views: project views (table or board) with filters, set up by hand.

## Read
`gh project item-list` for open items with all fields in board order; issue comments since a date with `gh issue view --comments` or the API.

## Write
- **Create:** an issue in the repo, add it to the project, set fields, label `ai`.
- **Move:** set Status. **Set:** `gh project item-edit`. **Complete:** set Status Done and close the issue.
- **Comment:** `gh issue comment`.
- **Add option:** single-select options are changed in the project settings (the CLI has no command for it; setup or the user does it by hand, or the GraphQL API).

## Team tasks
Create an issue that links to the team's task; never copy its content.

## Deep link format
The issue URL `https://github.com/<owner>/<repo>/issues/<n>`.

## Limits
- No private personal-task semantics: tied to repositories and their access.
- Draft items cannot be commented on, so they are not used.
- Rank is the item order in the project view.
