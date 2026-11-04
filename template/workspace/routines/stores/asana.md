---
type: topic
summary: Task store adapter for Asana (🤖 Board for sections, one project per initiative, description lines)
status: current
updated: {{SETUP_DATE}}
---

# Task store: Asana

Model: `routines/stores/README.md`. Config and ids: `meta/task-store.md`.

## Connector
The standard Asana connector only (Claude Code: `/mcp`; Cowork: Settings > Connectors). No API token, no scripts, no browser. Before relying on it, list the tools it exposes in this session and test one read. It can create projects and sections, add tasks to projects (multi-homing), read and write task descriptions and comments, and add an existing custom field to a project; it cannot create custom fields or select options, so this adapter never does. If a call fails, say so in one line and carry on without it.

## Create the board
1. One private project `🤖 <board_name>` (default `🤖 Board`) in the user's workspace. Team tasks can only be multi-homed from projects in the same workspace or organisation, so use the company workspace when team tasks matter.
2. Sections, in order: Top of mind, This week, Waiting, Inbox, Agent.
3. Properties. Look in the workspace's existing custom field library for fields that match Area, Priority, Size or Source. Prefer fields named `HQ · Priority`, `HQ · Size`, `HQ · Source` (and `HQ · Area` if present): a team that uses HQ creates these once in its library (an admin or the first user, by hand in Asana: Add field > Create new, options P0–P3 / S, M, L / Slack, Mail, Meeting, Asana, Linear, GitHub, Me) so every later setup only reuses them. Do not assume one exists or which values it has. Add each match to the board project, read its options, and record field id, option ids and the mapping to our values in `meta/task-store.md` (`fields`, "Field mapping"). For Priority, map whatever is found: a High/Medium/Low field gives P0 and P1 = High, P2 = Medium, P3 = Low, and P0 also gets due today; the description line keeps the exact P0 to P3. Every property without a match is a description line (README, "Properties"). Never create a field or an option.
4. Tag `ai` (create if missing; tags are not custom fields).
5. Initiatives: for each confirmed initiative create its project (Write, "Create an initiative project") and its Top of mind task, linking to it.
6. Views: Asana saved views are not assumed available. Tell the user the useful filters (by project = initiative, This week, Inbox) in one line; they are optional.

## Read
Open tasks of the board project with name, completed, due date, notes (the description), memberships (projects and section), any mapped custom fields, tags and permalink, in rank order. Initiative = the task's membership in a project named `🤖 <X>` other than the board (X is the initiative). Area, Size, Source, Waiting on, Closed when (and Priority exactly) come from the description lines; OKR from the initiative project's description. Comments since a date: stories of type comment on each open task after that date. Also tasks assigned to the user elsewhere (team tasks).

## Write
- **Create:** a task with name, the board project and, when it belongs to an initiative, that initiative's project as home (multi-home), section, tag `ai`, due date if known, and mapped fields where `meta/task-store.md` lists them. The description starts with the property line, then (Waiting only) `Waiting on: <name>`, then `Closed when: <scenario>`.
- **Move section:** add the task to the section within the board project.
- **Set property:** rewrite the description line (or update a mapped field by option id).
- **Initiative of a task:** add the task to, or remove it from, the initiative's project.
- **Create an initiative project** (after the user's yes): a private project `🤖 <Initiative>`, description with outcome, end date, OKR if any, `Topic folder: <name>` (a name, never a path) and shared links. Add its Top of mind task in the board, linking to it. Write name, id and url to `initiatives:` in `meta/task-store.md`.
- **Close an initiative** (after the user's yes): complete its Top of mind task and mark the project complete (archive) through the connector; remove it from `initiatives:`.
- **Documents:** put a shared URL in the task description or as a comment link. Never write a local path into the task tool.
- **Complete:** mark completed. **Comment:** add a comment (story).

## Team tasks
Multi-home: add the team task to the board project in the right section. One task, one comment thread; never copy it. Write the property line on it; it shows in the board project's view of the task.

## Deep link format
`https://app.asana.com/0/<project id>/<task id>`; the task's own permalink wins if it differs.

## Limits
- Multi-homing needs one organisation (and, for some features, a paid plan). If a project cannot hold the task, say so once and use a link.
- Rank is the order in the section; the user drags, Claude never reorders a task the user moved.
- No custom field is ever created: the connector cannot, and everything that changes over time is a project or description text.
