---
type: topic
summary: Task store adapter for Notion (one database, select and person properties)
status: current
updated: {{SETUP_DATE}}
---

# Task store: Notion

Model: `routines/stores/README.md`. Config and ids: `meta/task-store.md`.

## Connector and fallback
Use the Notion connector (Claude Code: `/mcp`; Cowork: Settings > Connectors). List the tools it exposes in this session and test one read before relying on it. Whether it can create databases, change property options or read comments is not assumed. Fallback: Claude in Chrome on notion.so. If neither works, setup prints the manual steps.

## Create the board
1. One database "<board_name>" on a page the user alone can see (a private page, not a teamspace page). Full-page database, one row per task. One database; no relation properties are needed.
2. Properties: Name (title), Section (select: Top of mind, This week, Waiting, Inbox, Agent), Done (checkbox), Due (date), Area (select), Initiative (select), OKR (select, optional), Priority (select P0-P3), Size (select S, M, L), Source (select), Waiting on (person), Closed when (text), Rank (number), AI (checkbox).
3. Section is a select, not Notion's Status property: select options can be changed through the API, Status options and groups cannot be set up reliably that way.
4. If the connector cannot create the database or its properties, setup gives the exact manual steps and then reads the property ids back.
5. Saved views: database views filtered and grouped per saved view in `meta/task-store.md`; set up by hand.

## Read
Query the database for rows where Done is unchecked, sorted by Section then Rank. Comments since a date: page comments on each open row after that date (if the connector exposes comments; otherwise the user's input comes by chat and the adapter says so in the brief's Sources line).

## Write
- **Create:** a row with Name, Section, properties, Closed when, AI checked, Rank after the last row of the section.
- **Move:** set Section and Rank. **Set:** update the property. **Complete:** check Done.
- **Comment:** add a page comment on the row.
- **Add option:** add a select option to the property.

## Team tasks
Create a row with the link to the team's task in Source and in the page body; never copy its content.

## Deep link format
The row's page URL (`https://www.notion.so/<page id without dashes>`).

## Limits
- No manual drag order that the API can read: rank is the Rank number, and a view must sort by it. If the user drags in an unsorted view, Claude cannot see it.
- Person properties accept only people in the Notion workspace.
- Whether comments can be read depends on the connector.
