---
type: topic
summary: Task store adapter for Asana (🤖 Board for sections, one project per initiative, description lines)
status: current
updated: {{SETUP_DATE}}
---

# Task store: Asana

Model: `routines/stores/README.md`. Config and ids: `meta/task-store.md`.

## Connector
The standard Asana connector only (Claude Code: `/mcp`; Cowork: Settings > Connectors). No API token, no scripts, no browser. Before relying on it, list the tools it exposes in this session and test one read. It can create projects and sections, add tasks to projects (multi-homing), read and write task descriptions and comments, and add an existing custom field to a project; it cannot create custom fields or select options, so the HQ routines never do (the one-time creation of the HQ fields is a separate, optional step in `asana-fields.md`). If a call fails, say so in one line and carry on without it.

## Create the board
1. One private project `🤖 <board_name>` (default `🤖 Board`) in the user's workspace. Team tasks can only be multi-homed from projects in the same workspace or organisation, so use the company workspace when team tasks matter.
2. Sections, in order: Top of mind, This week, Waiting, Inbox, Agent.
3. Properties. The eight shared HQ fields (`HQ · Priority`, `HQ · Size`, `HQ · Source`, `HQ · MoSCoW`, `HQ · Impact`, `HQ · Confidence`, `HQ · Ease`, `HQ · ICE`) are a prerequisite: spec, check and creation are in `routines/stores/asana-fields.md`. (a) Look for each in the workspace's shared field library through the connector (no token). Found: add it to the board project, read its options, record field id and option ids in `meta/task-store.md` (`fields`). (b) Any missing: stop here, name exactly those fields, and have the user create them first, by hand (click path in `asana-fields.md`) or, in Claude Code with an `ASANA_API_TOKEN` environment variable, by an offered one-time creation for the whole organisation (never required, token never printed). Re-check the library and continue only when all eight are found. (c) Description lines instead only when the user explicitly says to skip the fields. Area is never a column: it follows from the task's initiative (its project description), else the `Area:` description line. Existing High/Medium/Low Priority fields are not used when `HQ · Priority` exists.
4. Tag `ai` (create if missing; tags are not custom fields).
5. Initiatives: for each confirmed initiative create its project (Write, "Create an initiative project") and its Top of mind task, linking to it.
6. Views: Asana saved views are not assumed available. Tell the user the useful filters (by project = initiative, This week, Inbox) in one line; they are optional.

## Read
Open tasks of the board project with name, completed, due date, notes (the description), memberships (projects and section), any mapped custom fields, tags and permalink, in rank order. Initiative = the task's membership in a project named `🤖 <X>` other than the board (X is the initiative). Priority, Size, Source, MoSCoW, Impact, Confidence, Ease and ICE come from the HQ fields in `custom_fields` by id (Area likewise when it is a field; the description line wins for Priority when both exist); Waiting on and Closed when come from the description lines; OKR from the initiative project's description. Comments since a date: stories of type comment on each open task after that date. Also tasks assigned to the user elsewhere (team tasks).

## Write
- **Create:** a task with name, the board project and, when it belongs to an initiative, that initiative's project as home (multi-home), section, tag `ai`, due date if known, and mapped fields where `meta/task-store.md` lists them. The description starts with the property line, then (Waiting only) `Waiting on: <name>`, then `Closed when: <scenario>`.
- **Move section:** add the task to the section within the board project.
- **Fields by id:** select fields (Priority, Size, Source, MoSCoW) are set with the field id and the option id from `meta/task-store.md`; number fields (Impact, Confidence, Ease, ICE) are set as numbers (`custom_fields: {"<id>": 8}`), never as text. Impact, Confidence and Ease are whole numbers 1 to 10; ICE = Impact x Confidence x Ease, computed by Claude whenever it writes any of the three, never typed by hand. Size takes XS, S, M, L, XL.
- **Set property:** rewrite the description line (or update a field by option id).
- **Initiative of a task:** add the task to, or remove it from, the initiative's project.
- **Create an initiative project** (after the user's yes): a private project `🤖 <Initiative>`, description with outcome, end date, OKR if any, `Topic folder: <name>` (a name, never a path) and shared links. Add its Top of mind task in the board, linking to it. Write name, id and url to `initiatives:` in `meta/task-store.md`. Then add every HQ field recorded under `fields` in `meta/task-store.md` (all eight `HQ ·` fields) to the new project through the connector, so its tasks show and filter the same columns as the board. Area is not added: an initiative has exactly one area, recorded in its description.
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
- The standard connector cannot create custom fields. The HQ fields are therefore created once per organisation by a person (by hand, or with the optional token path in `asana-fields.md`), never by the normal HQ routines; everything that changes over time is a project or description text.
