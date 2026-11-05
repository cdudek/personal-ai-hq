---
name: setup
description: Onboarding for the HQ plugin. Interviews the user (name, company, team, role, day to day, goals, tools, writing samples, languages, where tasks live), picks a role adapter, proposes areas and a tie-break, maps colleagues and their identities, creates the task board in the chosen tool (Asana, Notion, Monday, Trello or GitHub Projects), copies the workspace template to a folder, fills in the rules, context and tool routing, starts a local git repo, creates the scheduled tasks, and offers a first brief. Use when the user says "setup", "set up my AI workspace", "onboard me", "install HQ", "get started", or runs /hq:setup.
---

# setup

Goal: a working private workspace in about 20 minutes. Never push anything anywhere. Never put the workspace inside a synced folder (iCloud Drive, Dropbox, OneDrive, Google Drive, or an Obsidian-sync folder), because sync tools corrupt git repos and expose private notes.

## 0. Check the basics

- Is a workspace already configured? Read `~/.config/hq/workspace`, or the old `~/.config/personal-ai-os/workspace` if that is missing. If it exists and the folder has `CLAUDE.md`, ask: continue with that workspace, or create a new one. Continuing means **resuming at the first incomplete stage**, found by these checks (stop at the first that fails, say which one, and run from there):
  1. Workspace filled: `grep -rn '{{' "<workspace>" --include='*.md'` finds nothing outside `meta/task-store.md` and `meta/chat-cursor.md` is filled. Failing: steps 1 to 5 (reuse answers found in `context/`).
  2. Connectors: re-test each one named in the tool routing, and the task store's connector first (step 3). Failing connector: say which, do not go on to 5b.
  3. Task store: `meta/task-store.md` has a `store`, a `board_url` and no `{{`, and one read through the adapter works. Failing: step 5b.
  4. Git: `<workspace>/.git`, `.hq-version` and `.hq-manifest.json` exist. Failing: step 6.
  5. Schedule: ask whether the four scheduled tasks exist; if not or unsure: step 7.
- `python3 --version` and `git --version` must work. If not, tell the user what to install and stop.

## 1. Interview

Start with one line: "I'll ask 10 short questions (about 12 minutes). Say `skip` to pass on any, or `demo` to see sample pages first, no connectors needed." If the user says `demo`, run the `demo` skill, then come back.

Rules for the interview:

- **One question at a time,** with a progress marker: "3 of 10".
- **A default in brackets** that an empty answer or "ok" accepts, for example "Language for work? [English]". Use what you already know (the system language, the folder name, earlier answers).
- **`skip` is always allowed.** A skipped answer becomes "to confirm" in the files; never invent one.
- **Give an example** for the role and goals questions so people know the size of answer you want.
- Keep your own text to one or two lines per question.

The ten questions, in this order:

1. **Name** and how you want to be addressed. [the name in the system user]
2. **Role and title.** Example: "Head of Product at a 200-person software company".
3. **Company:** name and what it does in one sentence.
4. **Team:** who is in it, how big, and who you report to (a title is enough).
5. **Your day to day** in two or three lines. Example: "Roadmap reviews, 1:1s with five people, customer calls, a weekly board update".
6. **Goals this quarter,** 3 to 5, with a link to the source document if there is one. Example: "Ship the partner API by December; cut onboarding time in half".
7. **Languages** for work and which one for which channel. [English everywhere]
8. **Tools, one category at a time** (chat, mail, calendar, tasks and tickets, code, docs and files, CRM, notes and meetings, whiteboard): name the product or "none". Also: where do you share finished documents with colleagues (Google Drive, Notion, Confluence, none)? That answer is only about shared versions; your working documents always live in the workspace (`research/`). Also: is there a company data gateway? Optional. Then ask where captures come from (a DM to yourself in the work chat, a private drop folder, a voice notes app) and any fixed handling rules ("receipts go to finance"). [none] If a DM to yourself is used, ask: "The morning brief can send you one DM to yourself with the headline and your top items (never a file path). A DM to yourself that you set up here counts as authorised; nothing else is sent without your yes. Send it? [yes]"
9. **Writing samples:** paste 2 or 3 messages you sent and like, or say where to find sent items and you will read 10. Anything confidential can be anonymised.
10. **Where do your tasks live?** Your tasks go in one cloud task manager, not in a file on your computer, so you get comments, history and a phone app. Options: **Asana**, **Notion**, **Monday**, **Trello**, or **GitHub Projects (not recommended: no private personal-task semantics, tied to repositories)**. [the task tool named in question 8 if it is one of these, otherwise Asana]. A different tool: say so; HQ then has no adapter for it, and you pick one of the five.

Before writing anything, show a short summary (name, role, company, team, goals, languages, tools, task store, role adapter, areas, close team, workspace folder) and ask "Write this? [yes]". Change what they correct, then continue.

## 2. Pick the role adapter

Choose from `${CLAUDE_PLUGIN_ROOT}/template/adapters/`: `product-manager`, `engineering-lead`, `sales-cs`, `founder-exec`. Propose the best fit from the role and tools, and let the user pick. If none fits, use the closest and say what differs. Read the adapter: it gives tool defaults, routine emphasis, glossary seeds and typical meeting types.

## 2b. Areas and the task store

Every task carries one Area. Propose the set; the user confirms.

1. Start from the adapter's "Default areas" and example tie-break.
2. Look at what exists and adjust: projects already in the chosen task tool (if its connector works), ticket teams (for example Linear teams), recurring meetings on the calendar, chat channels the user is in, and the goals from question 6. A recurring theme with no area is a candidate for a new one. Keep it to 4 to 7 areas, each with a one-line definition.
3. Write the tie-break as an ordered list, first match wins, ending with "Me" for the user themselves and with Admin for pure bureaucracy. Say: "Uncommitted ideas stay in `ideas/`, not in the task store."
4. Propose initiatives only from what is real (goals, projects with an end date, more than one task or longer than a week). Never invent one.
5. Show areas, tie-break and initiatives, ask "Use this? [yes]", and change what the user corrects.

## 2c. Map your colleagues

Claude needs to know who your close team is and who each person is in every tool, so briefs, 1:1 prep and "waiting on" lines name the right person. Follow `routines/people.md` in the workspace template (`${CLAUDE_PLUGIN_ROOT}/template/workspace/routines/people.md`, copied in step 5); the adapter's "Which people matter" section says which relations count for this role. Ask now, resolve after step 3 when the connectors work.

1. Ask: who is your manager? Who reports to you? Name your peers and the people outside your team you work with weekly. One line each is enough (name, role). Offer "later" for any of these; skipped means no profile yet.
2. Note the contract type where it matters for how you manage them (permanent, freelance); `unknown` otherwise.
3. After step 3 (connectors tested): propose your close team from evidence. Read, do not write: recurring 1:1s on the calendar, chat DM frequency (30 days), ticket teams and projects you lead, frequent reviewers on your code, people who report to you (HR or warehouse people table if you have one). Show one line per person with the evidence and a relation guess (manager, report, skip-level, peer, stakeholder, freelancer, external). Ask: "Who is close? Who is missing? Use this? [yes]".
4. Resolve identities for the confirmed people: chat user, ticket user, task tool user, code login, and the CRM owner only for sales and support colleagues. Match by email first, then full name; two people with the same first name or no clear match means ask, never guess. Record where each id came from.
5. Show the result as a list (name, relation, ids found, ids missing). Write profiles after a yes (step 5 does the writing); `close: true` only for the people the user confirmed. Remove the sample folder `context/people/example-jordan-rivera/` (`git rm -r`) once the user's own profiles exist.

A tool that is not connected yet leaves its ids empty; the first `routines/people.md` run fills them later.

## 3. Connectors: what to switch on

For every tool named in step 1, say which connector to enable and how, one line each:

- **Claude Code:** `/mcp` lists connectors; add a missing one with `claude mcp add` (see the tool's own docs) or install the tool's plugin from `/plugin`.
- **Cowork and Claude Desktop:** Settings > Connectors (or Customize > Connectors), pick the tool, sign in.
- Common ones: Slack, Gmail, Google Calendar, Google Drive and Docs, Linear, Asana, Monday, Trello, Jira and Confluence (Atlassian), GitHub (or the `gh` CLI), Notion, HubSpot, Miro, Granola, Fireflies. The connector for the task store chosen in question 10 is required for step 5b. If it is missing or fails its test, say which one to switch on and how, finish the other steps, and tell the user to run `/hq:setup` again once it works (step 0 then continues at 5b). There is no local task file.
- No connector for a tool: mark it in the routing as "none" (or "browser" if the user explicitly wants Claude in Chrome for it); the task store never uses the browser.

Test each enabled connector with one read (today's calendar, one mail, one ticket) and list what works and what is missing. Ask which connectors the brief cannot run without (default: calendar and the task store) and write them as a line `Critical: <list>` under "Required sources" in `CLAUDE.md`. A missing non-critical one is not a blocker: routing says "none" and routines skip it; a missing critical one is flagged first, and the run asks once whether to wait or go ahead (`CLAUDE.md`, "Required sources"). Never claim a connector exists without checking that its tools are available in this session.

## 4. Choose the folder

Default `~/ai-workspace`. Check the path: it must not be under `~/Library/Mobile Documents`, `~/Library/CloudStorage`, `~/Dropbox`, `~/Documents` when Documents is synced, or any other synced folder. If it is, propose `~/ai-workspace` instead. Refuse to overwrite a non-empty folder.

## 5. Copy the template and fill it

1. Copy: `cp -R "${CLAUDE_PLUGIN_ROOT}/template/workspace/." "<workspace>/"`.
   - If `${CLAUDE_PLUGIN_ROOT}` is not resolved (run `echo "${CLAUDE_PLUGIN_ROOT}"`; empty means it is not, which can happen in Cowork), locate the template next to this file: the `template/workspace` folder two levels above this `SKILL.md`. If you cannot find it, ask the user for the folder where the plugin is installed (in Claude Code usually under `~/.claude/plugins/`) or where they unzipped it.
2. Fill the placeholders. Find them with `grep -rn '{{' "<workspace>" --include='*.md'`. Fill:
   - `CLAUDE.md`: `{{NAME}}`, `{{ROLE}}`, `{{COMPANY}}`, `{{LANGUAGES}}`, the whole tool routing table (`{{TOOL_*}}`, one product per row, "none" where there is none, "browser" for no connector; the gateway row says "none" unless step 1 named one), `{{INBOX_CUTOFF}}` (today's date), `{{RECURRING_INPUTS}}` ("None yet." unless the user named some), `{{REF_*}}` (where to look up company, handbook and numbers; "ask the user" if unknown), `{{PHONE_*}}` from step 1 question 8 (captures) (write "not used" for options they skipped). Add the handling rules from step 1 question 8 (handling rules) as a short section "Standing handling rules".
   - `context/me.md`: name, company and description, team, role, day to day, languages; `{{NEVER}}` from the user's own rules (ask for 1-3 things Claude must never do; always include "send or publish anything without asking").
   - `context/goals.md`: the goals, each with its source link.
   - `context/glossary.md`: the adapter's glossary seeds plus company terms the user mentioned, each marked "to confirm" until confirmed.
   - `context/writing-style.md`: `{{STYLE_RULES}}` from the writing samples: tone, length, greeting and closing, bullets, language per channel, words used and avoided, each rule with a short quote. Mark the file `status: draft` until the user confirms.
   - `context/places.md`: the workspace path, where code and other documents live, and `{{SHARED_DEST}}` = where shared versions go (Google Drive, Notion, Confluence, or "none, no shared destination yet").
   - `meta/chat-cursor.md`: `{{PHONE_WORK_CHANNEL}}` (or "not used") and `{{SELF_DM}}` (`yes` only when the user said yes to the brief DM to themselves, else `no`).
   - everywhere: `{{SETUP_DATE}}` = today.
   - Append a "Role adapter" block to `context/me.md` with the chosen adapter's routine emphasis and typical meeting types.
3. If a tool has no row in the folder (for example no code tool), remove that source's mention only if the routine would otherwise fail; the routing "none" already makes routines skip it.
4. People: for each mapped colleague write `context/people/<slug>/profile.md` from the schema in `routines/people.md`, with an empty `records/` next to it (the confirmed relation, contract, team, areas, `close`, aliases, the ids resolved in step 2c and one `sources` line per id; `status: draft`). Everything the user did not confirm stays empty.
5. Areas: write `context/areas/index.md` from step 2b (`{{AREAS_TABLE}}` rows `| Area | definition | examples |`, `{{TIE_BREAK}}` as the numbered list) and one `context/areas/<slug>.md` per area (frontmatter `type: topic`, `summary`, `status: draft`; body: definition, examples, people, recurring meetings; each marked "to confirm" where you guessed).
6. Re-run the grep: only `meta/task-store.md` may still hold `{{` (step 5b fills it).
7. Create the drop folder if the user wants one, and write the config: `mkdir -p ~/.config/hq && printf '%s\n' "<workspace>" > ~/.config/hq/workspace`.
8. **Cowork:** tell the user to create a project that points at the workspace folder and to put this project instruction in it: "Read CLAUDE.md first, then index.md. Follow the rules there. Routines live in routines/." Scheduled tasks must be created inside that project. **Claude Code:** nothing to create; the user starts Claude Code inside the workspace folder, which reads `CLAUDE.md` itself.

## 5a. Documents home (`research/`)

The template copy already created `<workspace>/research/` with `CLAUDE.md` (the rules), `_template/` (the topic skeleton: README with the CURRENT DOCUMENT callout, status, question, output index; `notes.md`; `working/`; `output/` with `_archive/`; `data/`) and `_archive/`. Documents never live anywhere else, so do not ask where to keep them. Check those three exist; if the copy skipped them, copy them from `${CLAUDE_PLUGIN_ROOT}/template/workspace/research/`.

1. For every initiative the user confirmed in step 2b, create a topic folder: `cp -R "research/_template" "research/YYYY-MM-DD - Initiative Name"` (today's date, name in Title Case with real spaces), then fill its README: title, question (the initiative's outcome), `Status: active`, `Started`, and "Earlier work" with any document the user named (by name, not path, unless it is a local file the user wants listed).
2. Delete the sample topic `research/2026-01-15 - Example Acme Pricing Review/` once the user's first topic exists (or right away if they have no initiative yet and say so).
3. Remember the names: step 5b puts `Topic folder: <name>` into each Top of mind task.
4. Naming, status, `output/` frontmatter, versioning and the shared-versions rule are in `research/CLAUDE.md`. With Drive or Notion as the shared destination, the same structure works as subfolders or subpages there: one per topic, with `output` documents inside. Local stays the home.

## 5b. Create the task store

Read `routines/stores/<store>.md` (the adapter for the tool from question 10) and `routines/stores/README.md`.

1. Test the connector with one read. Say which operations you could verify. Do not claim an operation works before you have used it.
2. Create the board by the adapter's "Create the board": the five sections, the properties as the adapter says: Asana: the eight shared `HQ ·` fields are a prerequisite, so first run "Check first" in `routines/stores/asana-fields.md` (found: add them to the board and record the ids; any missing: stop, tell the user exactly which ones to create first and follow "Create the missing fields" there, then re-check; continue only when all eight exist; description lines instead only if the user explicitly says to skip the fields). Area is never a column: it follows from the task's initiative (its project description), else the `Area:` description line. Other tools: look for existing fields or columns that match Priority, Size, MoSCoW, Impact, Confidence, Ease, ICE and Source (assume none and no value set), add and map those found, and make every other property a description line; never create a field or option. Create each confirmed initiative as the adapter's container (description: outcome, end date, OKR from the goals if any, `Topic folder: <name>` from step 5a, shared links; never a local path) plus its Top of mind task.
3. Anything the connector cannot do: say so once, use the adapter's fallback (a description line or a link) and carry on. Apart from the Asana fields above, there is no manual step and nothing blocks.
4. Fill `meta/task-store.md`: `store`, `board_name`, `board_url`, `board_id`, `owner_id` (the user's own id in the task tool, from the connector's current-user call; only comments by this id count as instructions later), `fields` (for Asana the eight HQ fields with their ids and option ids; for other tools only the existing fields found) and `initiatives` (name to container id and url; each initiative container is created by the adapter's "Create an initiative project", which for Asana adds all eight `HQ ·` fields to it), `sections`, `{{FIELD_MAPPING}}` (value mapping of each existing field, or "none: every property is a description line"), `{{AREA_VALUES}}` and the other value lists, `{{SAVED_VIEWS}}` (the adapter's recipe, or "none"). Re-run the grep: no `{{` may remain anywhere.
5. Read the board back and show the user the link. Nothing is moved or created beyond this without a yes.

## 6. Git, indexes, first commit

`<plugin version>` is `version` in `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`. `.hq-version` tells `/hq:upgrade` which version the workspace is on; `.hq-manifest.json` records the system files as installed, so an upgrade can tell your edits from untouched files.

```bash
cd "<workspace>"
python3 scripts/build_index.py
printf '%s\n' "<plugin version>" > .hq-version
python3 scripts/hq_sync.py manifest .
git init
git add -A
git commit -m "setup: initial workspace"
```

If the commit fails because git does not know who you are, ask for a name and email and set them for this folder only (`git config user.name`, `git config user.email`), then commit again. Never add a remote, never push. If `views/template.html` is missing, say that the view pages need the files synced into the template (the brief still works as a note).

## 7. Scheduled tasks

Scheduled tasks are only prompts. Create these four tasks yourself, inside the user's workspace project (Cowork: the project that points at the workspace folder; Claude Desktop: the workspace folder). Prompt for each: "Follow routines/<name>.md".

| When | Prompt |
|---|---|
| Weekdays 7:27 | `Follow routines/brief.md` |
| Monday 6:57 | `Follow routines/weekly.md` |
| Friday 15:57 | `Follow routines/review.md` |
| First Monday of the month 7:57 | `Follow routines/refresh.md` |

Use the scheduled-task tool available in this session. Odd minutes avoid the busy top of the hour. If creating a task fails or no such tool exists, print each one as a ready-to-paste block (time, then the prompt). **Cowork:** the user adds them under Scheduled > New task, inside their project. **Claude Code:** a cron or launchd entry that runs `claude -p "Follow routines/<name>.md"` inside the workspace folder (a cloud routine cannot read a local workspace). Say clearly that local tasks only run while the computer is awake and, in Cowork, the app is open.

## 8. You're set

Show this block, filled in:

> **You're set.**
> **Your workspace:** `<path>` (a local git repo, never pushed)
> **Your tasks:** `<board url>` in `<tool>`, with the areas `<list>`
> **Your documents:** `<workspace>/research/`, one topic folder per initiative: `<list of folder names>` (shared versions go to `<destination>`)
> **Try first:** `/hq:brief` (today's brief), `/hq:task` (what to do next), `/hq:inbox` (what needs you and what you wait on)
> **Still missing:** each connector that did not work, with how to add it (Claude Code: `/mcp`; Cowork: Settings > Connectors). Everything else works without it.
> **Schedule:** the tasks you created (or the ones to add by hand), with times. They only run while the computer is awake and the app is open.

Then offer to run `/hq:brief` now. If the user agrees, run it. Afterwards ask what was wrong or missing and log each answer to `meta/friction.md`.

## Rules

- Do not invent facts about the company, the team or the user. Unknown means a question, or "to confirm".
- Everything you write into `context/` is a draft until the user says yes (workspace rule 1).
- Keep the workspace free of company secrets: references, not copies.
