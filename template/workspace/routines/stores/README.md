---
type: topic
summary: The task store model every tool adapter implements (sections, properties, rules)
status: current
updated: {{SETUP_DATE}}
---

# The task store

Tasks live in one cloud tool, chosen in setup and named in `meta/task-store.md`. This page is the model; `routines/stores/<store>.md` says how the tool does it. Routines say "the task store" and use the operations below.

## Sections (fixed)

Top of mind (one task per open initiative, linking to its initiative container and to a ticket project or doc), This week, Waiting, Inbox, Agent (tasks Claude does itself). Rank is the order inside a section.

## Properties: one per question

Section, Completed and Due are the tool's own. Initiative is a container (below). Everything else is a **description line**, unless setup found a matching existing field.

- **Only what the tool's standard connector can do.** No API token, no scripts, no browser, no manual setup step. Claude never creates custom fields or select options, and never edits them: the connectors cannot, and a design that needs it breaks for everyone but the admin.
- **Existing fields are reused if setup finds them.** At setup, look in the tool's existing field library (what the connector lists; nothing is assumed to exist, and no value set is assumed). For each property (Area, Priority, Size, Source, MoSCoW, Impact, Confidence, Ease, ICE) that has a matching field, add it to the board and record its id and a mapping from its values to ours in `meta/task-store.md` (`fields`, "Field mapping"). Map whatever is found (Asana Priority High/Medium/Low: P0 and P1 = High, P2 = Medium, P3 = Low; P0 also gets due today). A value that has no counterpart goes to the description line instead.
- **Description lines** at the top of every task Claude writes, in this order, each only if not an existing field: `Area: Product · Size: M · Source: Slack · Priority: P1 · MoSCoW: Should · ICE: 7 x 8 x 5 = 280`, then `Waiting on: <name>` (only in Waiting; the person's id comes from `context/people/<slug>.md`, `ids`, never from a first name), then `Closed when: <scenario>`. The line wins when it and a mapped field disagree on Priority (it keeps P0 to P3 exact). Claude reads and writes these lines; the views show them as before.
- **What each property answers.** Priority (P0-P3): what do we work on first; set by rules or by the user. ICE: how much is it worth; Impact, Confidence and Ease are 1 to 10 each and ICE = Impact x Confidence x Ease (1 to 1000), Claude's scoring proposal for Inbox items and new tasks, always computed, never typed by hand, used to propose a Priority. MoSCoW (Must, Should, Could, Won't): is it in scope; set in the weekly plan for This week items and per initiative; Won't = explicitly out this cycle. Size (XS, S, M, L, XL): t-shirt effort. One property per question.
- **ICE comment.** Whenever Claude sets ICE it adds one task comment with the one-line why per score (`ICE: I 8 (why), C 7 (why), E 5 (why)`). A score or Priority the user edited is never overwritten.
- **Asana** is the exception to "no fields": its HQ fields (`HQ · Priority`, `HQ · Size`, `HQ · Source`, `HQ · MoSCoW`, `HQ · Impact`, `HQ · Confidence`, `HQ · Ease`, `HQ · ICE`) are shared library fields and a prerequisite, see `routines/stores/asana-fields.md`.
- **OKR** (optional) sits in the initiative container's description, not on tasks.
- Claude's reason for a priority is a task comment. Every task Claude creates carries the tag or label `ai` where the tool has one and the connector can set it.

## Initiatives are containers, not an option

An initiative is its own container in the tool, created by Claude through the connector after the user's yes. Each adapter names the container: an Asana project `🤖 <Initiative>`, a Notion page in an "Initiatives" database related to the tasks, a Monday board, a Trello card, a GitHub milestone. The container's description holds: outcome, end date, OKR if any, `Topic folder: <name>` (a name in `research/`, never a path) and shared links. A task's initiative is its membership of, or link to, that container; `meta/task-store.md` `initiatives:` maps name to container. Top of mind holds one task per open initiative, linking to the container. In view data, `initiative` is derived from that membership.

## Operations (every adapter implements)

- **list:** open tasks with all properties, in rank order, optionally one section or filter.
- **comments since:** comments added after a date, with task id and author.
- **create:** title, section, initiative container, property lines or mapped fields, closed-when line, `ai` tag.
- **move:** to a section; **set:** one property; **complete**; **comment**; **create initiative** and **close initiative** (the container, never an option).
- **team task:** a task that lives in a team's tool and concerns the user. Asana: multi-home it into the board (one task, one comment thread). Every other tool: create a task that links back, never copy content.

## Rules

- **Rank:** the user drags; Claude never reorders a task the user moved.
- **Input:** a comment on a task ("next week", "delegate to X", "P0") is an instruction; each brief reads all comments since its last run and acts on them. Dragging sets rank. Ticking off is done.
- **New initiative:** proposed when tasks pass the initiative test (`context/areas/index.md`); created only after a yes: the container (see above), its Top of mind task, and its topic folder in `research/`.
- **Closing an initiative:** proposed when all its tasks are done or the end date passed; after a yes, complete the Top of mind task, close or archive the container (the adapter says how) and set the topic README status to `complete` (moving the folder to `research/_archive/` is a second yes).
- **Documents:** a task's description or link holds the shared URL when one exists. The initiative container's description carries `Topic folder: <folder name>` (a name, not a path) plus shared links. Never write a local path into the task tool (`research/CLAUDE.md`, Shared versions).
- **Tickets:** engineering work stays in the ticket tool. The task store holds only the user's own tasks and links to the tickets.
- **Writes:** changes to the task store only after the user confirms, except new Inbox tasks from triage and Claude's own Agent tasks.
- **Missing tool capability:** if the connector cannot do an operation, say so once, use the description-line or link fallback the adapter names, and carry on; never block a brief, never ask the user for a manual step, never pretend it worked. Say "Saved" only after reading the result back.
