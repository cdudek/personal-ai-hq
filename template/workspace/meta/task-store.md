---
type: topic
summary: Where the tasks live (which tool, board ids, field ids). Routines read this and follow the adapter.
status: draft
updated: {{SETUP_DATE}}
store: {{STORE}}
board_name: {{BOARD_NAME}}
board_url: {{BOARD_URL}}
board_id: {{BOARD_ID}}
fields: {}
initiatives: {}
sections:
  top_of_mind: {{SECTION_TOP_OF_MIND}}
  this_week: {{SECTION_THIS_WEEK}}
  waiting: {{SECTION_WAITING}}
  inbox: {{SECTION_INBOX}}
  agent: {{SECTION_AGENT}}
---

# Task store

The one place tasks live. Routines never name the tool: they say "the task store" and follow `routines/stores/{{STORE}}.md`. The rules shared by every tool are in `routines/stores/README.md`.

- `fields:` lists the properties that are existing custom fields of the tool, found at setup (name, id, and how its values map to ours). Every property not listed is a line at the top of the task description. The routines never create fields or options. For Asana the eight shared `HQ · ` fields are a prerequisite (`routines/stores/asana-fields.md`).
- `initiatives:` maps each open initiative to its container in the tool (project, page, board, card or milestone: id and url), filled when it is created.

## One property per question

| Question | Property | Values here |
|---|---|---|
| When / what state? | Section | Top of mind, This week, Waiting, Inbox, Agent |
| Done? | Completed | the tool's own done state |
| Due? | Due date | the tool's own due date |
| Which responsibility? | Area (description line) | {{AREA_VALUES}} |
| Which initiative? | The task's initiative container (the tool's adapter says which) | {{INITIATIVE_VALUES}} |
| Which OKR? | On the initiative container (optional) | {{OKR_VALUES}} |
| What do we work on first? | Priority (a listed field with its mapping, else a description line) | P0, P1, P2, P3: the order of work, set by rules or by the user |
| How much is it worth? | ICE: Impact, Confidence, Ease (1-10 each) and ICE (= Impact x Confidence x Ease, 1-1000) | Claude's scoring proposal for Inbox items and new tasks, used to propose a Priority; computed, never typed by hand |
| Is it in scope? | MoSCoW | Must, Should, Could, Won't: scope within an initiative or the week, set in the weekly plan; Won't = explicitly out this cycle |
| How big? | Size | t-shirt XS, S, M, L, XL (rough effort) |
| Where from? | Source | {{SOURCE_VALUES}} (default: Slack, Mail, Meeting, Asana, Linear, GitHub, Jira, HubSpot, Google Drive, Miro, Figma, Notion, Confluence, LinkedIn, Data, Voice, Me; meanings in `routines/stores/README.md`) |
| Waiting on whom? | Description line `Waiting on: <name>` | a person (the task tool's id from `context/people/` when known); only in section Waiting |
| When is it closed? | Description line `Closed when: <scenario>` | the done scenario in words |

## Field mapping

{{FIELD_MAPPING}}

## Saved views

{{SAVED_VIEWS}}

## Areas

Definitions, tie-break and initiative test: `context/areas/index.md`.
