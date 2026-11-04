---
type: topic
summary: Task store adapter for Trello (board, lists as sections, custom fields or labels)
status: current
updated: {{SETUP_DATE}}
---

# Task store: Trello

Model: `routines/stores/README.md`. Config and ids: `meta/task-store.md`.

## Connector and fallback
Use the Trello connector (Claude Code: `/mcp`; Cowork: Settings > Connectors). List its tools in this session and test one read first. Which operations it covers (custom fields, comments, label changes) is not assumed. Fallback: Claude in Chrome on trello.com. If neither works, setup prints the manual steps.

## Create the board
1. One private board "<board_name>" (visibility private).
2. Lists as sections, in order: Top of mind, This week, Waiting, Inbox, Agent, Done.
3. Properties: with the Custom Fields Power-Up (available on some plans only; check), use dropdown fields Area, Initiative, OKR, Priority, Size, Source and text fields Waiting on, Closed when. Without it, use labels named `Area: Product`, `Initiative: X`, `Priority: P0`, `Size: M`, `Source: Mail` and put `Waiting on:` and `Closed when:` as the first lines of the card description. Record which of the two is used in `meta/task-store.md`.
4. Done: the card's due-complete checkbox (native) and move the card to Done.
5. If the connector cannot create lists, fields or labels, setup gives the exact manual steps and reads the ids back.
6. Saved views: board filters (by label or field); Trello does not store them, so the filter is described in `meta/task-store.md`.

## Read
Open cards per list in card order, with labels or custom fields, due date and description. Comments since a date: card comment actions after that date.

## Write
- **Create:** card in a list with properties, description, label `ai`.
- **Move:** move the card to a list. **Set:** change the custom field or swap the label. **Complete:** set due complete and move to Done.
- **Comment:** add a card comment.
- **Add option:** a new dropdown option or a new label.

## Team tasks
Create a card with the link to the team's task; never copy its content.

## Deep link format
The card's short link `https://trello.com/c/<shortLink>`.

## Limits
- Labels are board-wide, coloured and limited in number; many initiatives on labels get crowded. Custom fields avoid this.
- Waiting on is text (members must belong to the board).
- Rank is the card position in the list.
