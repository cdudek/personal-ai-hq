---
type: topic
summary: Task store adapter for Notion (task database plus Initiatives database, description lines)
status: current
updated: {{SETUP_DATE}}
---

# Task store: Notion

Model: `routines/stores/README.md`. Config and ids: `meta/task-store.md`.

## Connector
The standard Notion connector only (Claude Code: `/mcp`; Cowork: Settings > Connectors). No API token, no scripts, no browser. List the tools it exposes in this session and test one read. Creating pages and databases and adding rows is what it does; whether it can read comments is not assumed. Claude never edits an existing database's properties or options afterwards.

## Create the board
1. On a page only the user can see (private, not a teamspace page), create two databases in the create call, with their properties defined once: **Initiatives** (Name, Status select Open/Closed, Outcome, End date, OKR, Topic folder, Links as text) and the task database "<board_name>" with Name (title), Section (select: Top of mind, This week, Waiting, Inbox, Agent), Done (checkbox), Due (date), Rank (number), AI (checkbox) and Initiative (relation to Initiatives). Properties exist only so Notion can sort and filter; all of them are fixed at creation and never changed.
2. Existing-field reuse: if the user already has a task database they want to use, take it and map its properties as in the README (Priority, Area, Size, Source, MoSCoW, Impact, Confidence, Ease, ICE if present; number properties are set as numbers); do not add or edit any property in it. Without a relation property, the initiative is a line `Initiative: <page link>`.
3. Area, Size (XS-XL), Source, Priority, MoSCoW, ICE (Impact, Confidence, Ease and the score), Waiting on and Closed when are description lines in the page body (README, "Properties"), unless a mapped property exists.
4. If the connector cannot create databases at all, say so once and propose another tool; do not ask for manual steps.

## Initiatives
An initiative is a page in the Initiatives database (outcome, end date, OKR, `Topic folder: <name>`, links in the page), related to its tasks through the Initiative relation. The API creates pages, so no option editing is ever needed. Close it by setting Status to Closed.

## Read
Query the database for rows where Done is unchecked, sorted by Section then Rank. Comments since a date: page comments on each open row after that date (if the connector exposes comments; otherwise the user's input comes by chat and the adapter says so in the brief's Sources line).

## Write
- **Create:** a row with Name, Section, Initiative relation, AI checked, Rank after the last row of the section, and the property lines at the top of the page body (Closed when included).
- **Move:** set Section and Rank. **Set:** rewrite the body line. **Complete:** check Done.
- **Comment:** add a page comment on the row.
- **Create or close an initiative:** add a page to Initiatives, or set its Status to Closed (after the user's yes).

## Team tasks
Create a row with the link to the team's task in the page body; never copy its content.

## Deep link format
The row's page URL (`https://www.notion.so/<page id without dashes>`).

## Limits
- No manual drag order that the API can read: rank is the Rank number, and a view must sort by it. If the user drags in an unsorted view, Claude cannot see it.
- Person properties accept only people in the Notion workspace.
- Whether comments can be read depends on the connector.
