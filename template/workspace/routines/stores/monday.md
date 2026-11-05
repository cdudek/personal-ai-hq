---
type: topic
summary: Task store adapter for Monday (board, groups as sections, an initiative board per initiative, update lines)
status: current
updated: {{SETUP_DATE}}
---

# Task store: Monday

Model: `routines/stores/README.md`. Config and ids: `meta/task-store.md`.

## Connector
The standard Monday connector or Monday MCP server only (Claude Code: `/mcp`; Cowork: Settings > Connectors). No API token, no scripts, no browser. List its tools and test one read. Creating boards, groups and items and posting updates is assumed to work; creating or changing columns and labels is not used. Claude never adds columns or labels.

## Create the board
1. One private board "<board_name>" (kind private).
2. Groups as sections, in order: Top of mind, This week, Waiting, Inbox, Agent, Done (Monday has no native completed state). Due date uses the board's date column if the board has one; otherwise the due date is a `Due:` description line.
3. Properties: Monday items have no description, so the property lines (including Size XS-XL, MoSCoW and `ICE: I x C x E = score`) are the first update on the item (README, "Properties"), pinned. If the board already has columns that match Priority, Size, Source, MoSCoW, Impact, Confidence, Ease or ICE (numbers columns hold numbers), reuse them and record the mapping in `meta/task-store.md`; do not add any.

## Initiatives
Monday has no multi-homing, so an initiative is a separate private board `🤖 <Initiative>` holding one group "About" with items for outcome, end date, OKR, `Topic folder: <name>` and links. Its Top of mind item on the main board links to it. A task belongs to an initiative through the line `Initiative: <name>` in its first update. Close an initiative by archiving its board (after the user's yes).

## Read
Items of the board with group, column values, in item order within the group. Comments since a date: the updates on each item after that date.
Context card: read its lines from the description below `Closed when:` (`routines/stores/README.md`, "Context card"; view fields `what`, `why`, `state`, `decision`).

## Write
- **Create:** item in a group, first update with the property lines (Closed when included), `ai` noted in it. Then the context card below the `Closed when:` line (`routines/stores/README.md`, "Context card"), kept current on every move, comment or change.
- **Move:** move the item to a group. **Set:** rewrite the first update's line. **Complete:** move to Done.
- **Comment:** post an update on the item.
- **Create or close an initiative:** create or archive the initiative board (after the user's yes).

## Team tasks
Create an item that links to the team's task (link in the first update); never copy its content.

## Deep link format
`https://<account>.monday.com/boards/<board id>/pulses/<item id>`.

## Limits
- Rank is the item order inside the group.
- Items have no description and no multi-homing: that is why properties and the initiative are update lines and the initiative board is separate.
