---
type: topic
summary: Task store adapter for Asana (private project, sections, custom fields, multi-homing)
status: current
updated: {{SETUP_DATE}}
---

# Task store: Asana

Model: `routines/stores/README.md`. Config and ids: `meta/task-store.md`.

## Connector and fallback
Use the Asana connector (Claude Code: `/mcp`; Cowork: Settings > Connectors). Before relying on it, list the tools it exposes in this session and test one read. Which operations it covers (creating custom fields, sections, multi-homing, reading comments) varies by connector version and is not assumed here. For anything it cannot do, use Claude in Chrome on app.asana.com. If neither works, setup prints the manual steps.

## Create the board
1. One private project "<board_name>" in the user's workspace (private to the user). Team tasks can only be multi-homed from projects in the same workspace or organisation, so use the company workspace when team tasks matter.
2. Board layout with these sections, in order: Top of mind, This week, Waiting, Inbox, Agent.
3. Custom fields (single select unless noted), added to the project: Area, Initiative, OKR (optional), Priority (P0-P3), Size (S, M, L), Source, Waiting on (people), Closed when (text). Custom fields need a paid Asana plan; on a free plan, use tags with a prefix (`area:Product`) and put the rest in the description, and say so in `meta/task-store.md`.
4. If the connector cannot create sections or fields, setup gives the exact manual steps (Project > Customize > Add field) and waits for the user to confirm, then reads the field ids back.
5. Saved views (by Area, by Initiative, This week P0-P1, Waiting by person, Inbox by Source; recorded in `meta/task-store.md`) are set up by hand; do not assume the connector creates them.

## Read
Open tasks in the project with section, completed, due date and all custom fields, in rank order (the order within the section). Comments since a date: the stories of type comment on each open task after that date. Also read tasks assigned to the user elsewhere (team tasks).

## Write
- **Create:** task with name, notes (`closed when: ...`), project, section, custom fields, tag `ai`.
- **Move section:** add the task to the section within the project.
- **Set property:** update the custom field value (enum option by id).
- **Documents:** when a shared URL exists for a document, put it in the task description or as a comment link. Top of mind initiative tasks carry in the description `Topic folder: <folder name>` (a name, not a path) and the shared links. Never write a local path into the task tool.
- **Complete:** mark completed.
- **Comment:** add a comment (story) to the task.
- **Add option:** add an enum option to the Area, Initiative, OKR or Source field. Retire an Initiative option by disabling it (do not delete: tasks keep the value).

## Team tasks
Multi-home: add the team task to the user's board project in the right section. One task, one comment thread; never copy it. Set the user's own fields (Area, Priority) on it; these show only in the board project.

## Deep link format
`https://app.asana.com/0/<project id>/<task id>`; the task's own permalink from the API wins if it differs.

## Limits
- Custom fields and multi-homing need a paid plan; multi-homing only within one organisation.
- Rank is the order in the section; the API can place a task before or after another one, but a task the user dragged must not be moved.
- Saved views and rules are set up by hand.
