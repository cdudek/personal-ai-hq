# Changelog

Versions follow semver. Each release is a git tag `vX.Y.Z` with an entry here. `/hq:upgrade` shows the entries between your workspace version and the installed one.

## 0.3.8 (2026-11-04)

- New initiatives get all eight HQ fields everywhere they are created: setup, upgrade, the brief's new-initiative question and the adapter.
- Area is no longer a column: it follows from the task's initiative, else the `Area:` description line.

## 0.3.7 (2026-11-04)

- Asana: every new initiative project gets all eight HQ fields, so its tasks show and filter the same columns as the board.

## 0.3.6 (2026-11-04)

- New task properties: **MoSCoW** (Must, Should, Could, Won't: scope within the week or an initiative, set in the weekly plan), **ICE** (Impact, Confidence, Ease, each 1-10, and the computed score; Claude's scoring proposal for new tasks, used to propose a Priority), and t-shirt **Size XS-XL**. One property per question: Priority = what first, ICE = how much it is worth, MoSCoW = in scope, Size = how big.
- Routines: the brief scores new Inbox items with ICE; the weekly plan sets MoSCoW and ranks by Priority, then ICE; `/hq:task` picks by Priority, due, ICE, blocks someone, age, size; the Friday review checks ICE drift.
- Pages: the task panel shows MoSCoW and ICE (with I, C, E) and lets you stage MoSCoW and Size changes; the task tables get sortable MoSCoW and ICE columns.
- Asana: the eight shared `HQ · ` fields (Priority, Size, Source, MoSCoW, Impact, Confidence, Ease, ICE) are now a prerequisite. Setup and `/hq:upgrade` check the shared field library; if any are missing they stop and tell you to create exactly those first (click path and field spec in `routines/stores/asana-fields.md`), or, in Claude Code with an `ASANA_API_TOKEN` environment variable, offer to create them once for your organisation. The token is optional and never printed. Notion, Monday, Trello and GitHub Projects get the same properties as description lines or mapped fields.
- `HQ · Source` has 17 options: Slack, Mail, Meeting, Asana, Linear, GitHub, Jira, HubSpot, Google Drive, Miro, Figma, Notion, Confluence, LinkedIn, Data, Voice, Me (Me last), each with a meaning in `routines/stores/README.md`; the pages label them.
- `/hq:upgrade` runs the migration 0.3.5 -> 0.3.6 first thing: field check, record ids, offer to score open tasks.

## 0.3.5 (2026-11-04)

- Asana: setup prefers shared library fields `HQ · Priority`, `HQ · Size`, `HQ · Source`, so a team creates them once and every colleague's setup reuses them through the standard connector.

## 0.3.4 (2026-11-04)

- Shown as "Personal AI HQ" in plugin lists; commands stay `/hq:...`.

## 0.3.3 (2026-11-04)

- Task store, no schema edits. The standard connectors cannot create custom fields or add select options, so nothing that changes over time depends on one. Initiatives are containers, not a field: an Asana project `🤖 <Initiative>` (tasks multi-homed with `🤖 Board`), a page in a Notion Initiatives database, a Monday board, a Trello card, a GitHub milestone. Created and closed by Claude after your yes; the description holds outcome, end date, OKR, `Topic folder: <name>` and links. Top of mind has one task per open initiative linking to it.
- Properties: an existing field of the tool is reused if setup finds one (nothing assumed, any values mapped, e.g. Asana Priority High/Medium/Low); every other property (Area, Size, Source, Waiting on, Closed when, OKR) is a line at the top of the task description. Claude never creates fields or options; no API token, scripts, browser or manual setup step in any adapter. `meta/task-store.md` gains `initiatives` and a field mapping.
- Setup step 5b and the adapters (`routines/stores/*`) follow this; the Chrome fallback is gone.
- Upgrade 0.3.2 -> 0.3.3: after confirmation, turns Initiative field values into initiative containers, attaches the tasks, and writes the other properties into description lines.

## 0.3.2 (2026-11-04)

- Sources check first: every brief, weekly and inbox run checks its required connectors before any other output and flags failures at the top with the fix.

- Documents home. `<workspace>/research/` holds every document and piece of research, one topic folder per initiative (`YYYY-MM-DD - Topic Name`): `README.md` (CURRENT DOCUMENT callout, status active | complete | parked, question, decisions, latest documents, shared links, earlier work), `notes.md`, `working/`, `output/` (with `_archive/`; frontmatter status, version, last_updated, audience) and `data/` (git-ignored). `research/CLAUDE.md` holds the rules; `research/_template/` is the skeleton; `research/_archive/` takes complete or parked topics. A fictional example topic (Acme) ships in the template; delete it after setup.
- Initiative = topic folder. The README is the initiative's memory, so `context/projects/` and `context/topics/` are gone. Opening an initiative (after a yes) also creates its folder; closing sets the README to `complete` and proposes moving it to `research/_archive/`.
- Task store: Top of mind tasks carry `Topic folder: <name>` and the shared links; a task's description holds the shared URL when one exists. Never a local path in a shared place.
- Setup: no question about where documents live (always `research/`); the tools question now also asks where shared versions go (Google Drive, Notion, Confluence, none, stored in `context/places.md`). New step 5a creates one topic folder per confirmed initiative and the setup summary lists them.
- Routines: weekly lists documents changed per initiative, the brief asks about a new or unknown folder or document, refresh lints topic READMEs, capture and ingest file research material into the initiative's `working/`.
- Views: the task panel shows "Documents" from `docs: [{title, url?, path?, kind: shared | local, updated}]`; shared ones are http(s) links, local ones copyable text. Sample pages include one.
- Author marker: a workspace with a `.hq-author` file is never synced from the plugin. `/hq:upgrade` updates only the plugin, `hq_sync.py apply` refuses, and the version check does not mention workspace sync.
- Cowork: the `claude plugin` CLI is not available there; update the plugin under Customize > Plugins (README, upgrade and the version-check message say so).
- Upgrade: `research/CLAUDE.md` and `research/_template/` arrive with the sync. A migration creates `research/`, proposes a mapping from your `context/projects` and `context/topics` pages to topic folders, merges them into the READMEs after your yes, then removes the two folders and fixes links. It also asks where shared versions go.

## 0.3.1 (2026-11-04)

- People mapping. `routines/people.md` finds your close team from evidence (recurring 1:1s, chat DM frequency, ticket teams you lead, code reviewers, your reports), resolves every person's identity across your tools (email, chat, code login, ticket user, task user, CRM owner for sales and support) and keeps a derived "Current" section per close person (what you owe, what they owe, their tickets and PRs, shared threads, recurring meetings).
- Profiles in `context/people/<slug>.md` get a schema: `relation`, `contract`, `team`, `areas`, `close`, `aliases`, `ids` and a `sources` entry per id. A fictional example profile ships in the template; delete it after setup.
- Setup has a new step "Map your colleagues". Role adapters say which relations matter for the role.
- Wired in: the brief and radar match people by id (Needs me, Waiting on; Waiting on in the task store uses the task tool's user id), meeting-prep reads and refreshes "Current" before a 1:1, refresh runs a monthly people refresh and lint, improve checks stale or missing ids. The brief's "new person" context gap creates a profile with resolved ids after you confirm. `build_index.py` lists role, relation and the close flag in the people index.
- Privacy rules (in the routine and the workspace `CLAUDE.md`): only what you can already see, never private mail or others' DMs, facts only, no performance judgements by Claude, personnel matters in your own words, workspace stays local.
- Upgrade: `routines/people.md` is a system file and arrives with the sync; `context/people/*` stays yours. `/hq:upgrade` offers to add the new fields to existing profiles and to run the map.

## 0.3.0 (2026-11-04)

- Your tasks live in a cloud task manager you pick in `/hq:setup`: Asana, Notion, Monday or Trello (GitHub Projects works but is not recommended). `board.md` is gone. One mapping file per tool in `routines/stores/`; `meta/task-store.md` holds the ids.
- One flat board that Claude manages: sections (Top of mind, This week, Waiting, Inbox, Agent) and one property per question (Area, Initiative, OKR, Priority, Size, Source, Waiting on, Closed when). Comment on a task, drag it or tick it off: the next brief acts on it.
- Areas: setup proposes areas and a tie-break from your role and what exists; they live in `context/areas/`. The Friday review checks them for drift, and the brief proposes new initiatives by an initiative test.
- `/hq:task` reads and writes the task store: `list`, `add`, `move`, `set`, `done`.
- `/hq:upgrade` migrates `board.md` once: asks which tool, shows the mapping (domain becomes area and initiative), creates the board, moves every task, then removes `board.md`.
- Views: tasks show Area and Initiative (not domain) and link to the task store; staged edits copy a prompt with the task id and url; the renderer checks `priority` and `area`; area colours are stable for any area name. Sample pages use the new fields. `build_index.py` leaves a hand-written `index.md` alone.

## 0.2.0 (2026-11-04)

- Renamed to Personal AI HQ: plugin `hq`, commands `/hq:<skill>`, config `~/.config/hq/workspace` (setup still reads the old `~/.config/personal-ai-os/workspace`).
- 10 skills instead of 13: `setup`, `upgrade`, `demo`, `brief [daily|weekly|update]`, `task [next|capture <text>]`, `inbox`, `meeting [name or time]`, `improve [review|tip <link>]`, `wiki [ingest <link or file>|refresh]`, `debrief`. Routines are unchanged; skills route to them.
- Marketplace is named `cdudek`: `/plugin install hq@cdudek`. `/hq:upgrade` updates the plugin through the `claude` CLI itself (or prints the two slash commands in Cowork) and then the workspace.
- New `/hq:upgrade` and a workspace `.hq-version`. Every skill checks it at the start and tells you when the workspace or the plugin is behind. Upgrades touch system files only and ask before changing a file you edited.
- New views: finished daily, weekly and review pages with embedded fonts, labels (priority, domain, topic) and the review page v2.
- Workspace files from 0.1.0: run `/hq:upgrade` once; without a manifest it shows a diff for every changed system file.

## 0.1.0

- First version: 13 skills, the workspace template with 13 routines, four role adapters, build-zip and scrub-check scripts.
