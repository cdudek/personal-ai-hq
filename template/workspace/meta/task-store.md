---
type: topic
summary: Where the tasks live (which tool, board ids, field ids). Routines read this and follow the adapter.
status: draft
updated: {{SETUP_DATE}}
store: {{STORE}}
board_name: {{BOARD_NAME}}
board_url: {{BOARD_URL}}
board_id: {{BOARD_ID}}
fields:
  area: {{FIELD_AREA}}
  initiative: {{FIELD_INITIATIVE}}
  okr: {{FIELD_OKR}}
  priority: {{FIELD_PRIORITY}}
  size: {{FIELD_SIZE}}
  source: {{FIELD_SOURCE}}
  waiting_on: {{FIELD_WAITING_ON}}
  closed_when: {{FIELD_CLOSED_WHEN}}
sections:
  top_of_mind: {{SECTION_TOP_OF_MIND}}
  this_week: {{SECTION_THIS_WEEK}}
  waiting: {{SECTION_WAITING}}
  inbox: {{SECTION_INBOX}}
  agent: {{SECTION_AGENT}}
---

# Task store

The one place tasks live. Routines never name the tool: they say "the task store" and follow `routines/stores/{{STORE}}.md`. The rules shared by every tool are in `routines/stores/README.md`. Ids above are filled when the board is created; a field the tool cannot hold says `none` and the adapter says what replaces it.

## One property per question

| Question | Property | Values here |
|---|---|---|
| When / what state? | Section | Top of mind, This week, Waiting, Inbox, Agent |
| Done? | Completed | the tool's own done state |
| Due? | Due date | the tool's own due date |
| Which responsibility? | Area | {{AREA_VALUES}} |
| Which initiative? | Initiative | {{INITIATIVE_VALUES}} |
| Which OKR? | OKR (optional) | {{OKR_VALUES}} |
| How important? | Priority | P0, P1, P2, P3 |
| How big? | Size | S, M, L |
| Where from? | Source | {{SOURCE_VALUES}} |
| Waiting on whom? | Waiting on | set only in section Waiting |
| When is it closed? | Closed when | the done scenario in words |

## Saved views

{{SAVED_VIEWS}}

## Areas

Definitions, tie-break and initiative test: `context/areas/index.md`.
