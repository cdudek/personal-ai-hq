---
type: topic
summary: Task store adapter for Monday (board, groups as sections, columns, updates as comments)
status: current
updated: {{SETUP_DATE}}
---

# Task store: Monday

Model: `routines/stores/README.md`. Config and ids: `meta/task-store.md`.

## Connector and fallback
Use the Monday connector or the Monday MCP server if one is available (Claude Code: `/mcp`; Cowork: Settings > Connectors). List its tools in this session and test one read first. Which operations it covers (creating columns and groups, reading updates) is not assumed here. Fallback: Claude in Chrome on monday.com. If neither works, setup prints the manual steps.

## Create the board
1. One private board "<board_name>" (board kind private, so only the user sees it).
2. Groups as sections, in order: Top of mind, This week, Waiting, Inbox, Agent, plus a group Done for finished items (Monday has no native completed state).
3. Columns: Area (status or dropdown), Initiative (dropdown), OKR (dropdown, optional), Priority (status P0-P3), Size (status S, M, L), Source (dropdown), Waiting on (people), Closed when (text), Due (date), AI (checkbox).
4. If the connector cannot create groups or columns, setup gives the exact manual steps and then reads the ids back.
5. Saved views: board views with filters and groupings, set up by hand.

## Read
Items of the board with group, column values, in item order within the group. Comments since a date: the updates on each item after that date.

## Write
- **Create:** item in a group with column values, Closed when, AI checked.
- **Move:** move the item to a group. **Set:** change a column value. **Complete:** move to Done.
- **Comment:** post an update on the item.
- **Add option:** add a label to the status or dropdown column.

## Team tasks
Create an item that links to the team's task (link in Closed when or a link column); never copy its content.

## Deep link format
`https://<account>.monday.com/boards/<board id>/pulses/<item id>`.

## Limits
- Rank is the item order inside the group.
- Adding labels to a status column may need board-owner rights; if the connector cannot, setup gives the manual step.
- A "People" column accepts only users in the Monday account.
