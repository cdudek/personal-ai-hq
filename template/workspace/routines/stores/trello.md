---
type: topic
summary: Task store adapter for Trello (board, lists as sections, initiative cards, description lines)
status: current
updated: {{SETUP_DATE}}
---

# Task store: Trello

Model: `routines/stores/README.md`. Config and ids: `meta/task-store.md`.

## Connector
The standard Trello connector only (Claude Code: `/mcp`; Cowork: Settings > Connectors). No API token, no scripts, no browser. List its tools and test one read. Creating boards, lists and cards, editing descriptions and adding comments is assumed; custom fields and labels are not used, so no Power-Up is needed. If the board already has labels or custom fields that match Priority, Size, Source, MoSCoW, Impact, Confidence, Ease or ICE (number fields are set as numbers), reuse them and record the mapping in `meta/task-store.md`.

## Create the board
1. One private board "<board_name>".
2. Lists as sections, in order: Top of mind, This week, Waiting, Inbox, Agent, Done.
3. Properties are description lines on the card (README, "Properties"). Done is the card's due-complete checkbox plus a move to Done.

## Initiatives
Lists are sections, so an initiative is not a list. An initiative is a card in Top of mind whose description holds outcome, end date, OKR, `Topic folder: <name>` and links. A task belongs to it through the line `Initiative: <name>` in its description and a link to the initiative card. This needs no board edit; a separate board per initiative is not used because tasks would lose their sections. Close an initiative by completing and archiving its card (after the user's yes).

## Read
Open cards per list in card order, with labels or custom fields, due date and description. Comments since a date: card comment actions after that date.
Context card: read its lines from the description below `Closed when:` (`routines/stores/README.md`, "Context card"; view fields `what`, `why`, `state`, `decision`).

## Write
- **Create:** card in a list with the property lines and Initiative line in the description, label `ai` if the board has one. Then the context card below the `Closed when:` line (`routines/stores/README.md`, "Context card"), kept current on every move, comment or change.
- **Move:** move the card to a list. **Set:** rewrite the description line. **Complete:** set due complete and move to Done.
- **Comment:** add a card comment.
- **Create or close an initiative:** add or archive its Top of mind card (after the user's yes).

## Team tasks
Create a card with the link to the team's task; never copy its content.

## Deep link format
The card's short link `https://trello.com/c/<shortLink>`.

## Limits
- Waiting on is text (members must belong to the board).
- Rank is the card position in the list.
