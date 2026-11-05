---
name: upgrade
description: Updates the HQ plugin to the latest release and brings the user's workspace up to it. Shows the changelog between the two versions, then updates only system files (routines, view code, scripts, folder rule files) and never user data. Files the user edited are shown as a diff and only changed on a yes. Use when the user says "upgrade", "update HQ", "new version", or after a skill says an HQ update is available.
---

# upgrade

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/version-check.md` first for the workspace lookup, but you are the one skill that acts on the result. Never run this unasked; it is the one command a user needs for updates.

## What is system and what is yours

- **System (this skill may update):** `routines/`, `scripts/`, `views/` code (`template.html`, `app.css`, `app.js`, `vendor/`, `icons/`, `CLAUDE.md`, `DESIGN.md`, `README.md`), `SYSTEM.md`, and the `CLAUDE.md` rule file in each top-level folder (not the root one).
- **System, research:** `research/CLAUDE.md` and `research/_template/` (the topic skeleton).
- **Yours (never touched):** the topic folders in `research/` (everything except `CLAUDE.md`, `_template/`), root `CLAUDE.md`, `index.md`, `context/`, `inbox/`, `daily/`, `weekly/`, `journal/`, `meta/`, `decisions/`, `ideas/`, `principles/`, `lists/`, `sources/`, `views/data/` and every rendered view page. Your tasks are not in the workspace: they live in your task store (`meta/task-store.md`).

## Author workspace

If `<workspace>/.hq-author` exists, this workspace is the author reference. `/hq:upgrade` then updates only the plugin (step 0), says "Plugin updated. This workspace has a .hq-author file, so no template files were synced." and stops. It never runs `hq_sync.py apply` (the script refuses anyway) and never writes `.hq-version`.

## Cowork

The `claude plugin` CLI is not available in Cowork's cloud session. Update the plugin there under Customize > Plugins (open the `hq` plugin and update it, or re-add the marketplace `cdudek/personal-ai-hq`), start a new session, then run `/hq:upgrade` to bring the workspace along.

## Steps

**Migration order (stated once).** The migrations below are printed newest first. Run the ones that apply from the **oldest to the newest**, never in the printed order, each fully before the next. The order matters because later ones need what earlier ones establish: `0.2.0 -> 0.3.0` creates the task store (nothing that touches tasks runs before it); `0.3.2 -> 0.3.3` creates the initiative containers; `0.3.5 -> 0.3.6` establishes the eight Asana `HQ ·` fields; `0.3.6 -> 0.3.7` needs both of those, and adds the fields to every initiative container; `0.3.7 -> 0.3.8` and later need the containers. A step that needs a prerequisite that is missing (no store, no valid HQ fields) stops and says which one.

0. **Update the plugin first.** Installed version `Y` = `version` in `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`. Latest `Z`: fetch `https://raw.githubusercontent.com/cdudek/personal-ai-hq/main/.claude-plugin/plugin.json` (`curl -fsS --max-time 3`; on failure assume `Z` = `Y`). If `Z` is newer than `Y` and you can run Bash with the `claude` CLI, run `claude plugin marketplace update cdudek`, then `claude plugin update hq@cdudek`. If the CLI says a restart is needed (it does), say: "HQ updated to Z. Restart Claude Code, then run /hq:upgrade again to bring your workspace along", and stop. If you cannot run the CLI, stop and tell the user how: in Claude Code the two commands `/plugin marketplace update cdudek` and then updating `hq` in `/plugin`; in Cowork Customize > Plugins (see "Cowork" above).
1. Find the workspace (shared file). If it has `.hq-author`, stop as described in "Author workspace". Installed version `Y` = `version` in `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`; workspace version `X` = first line of `<workspace>/.hq-version` (missing = `0.1.0`). If `X` is not older than `Y`, say "already on Y" and stop.
2. Show the `CHANGELOG.md` entries from the plugin folder for every version after `X` up to `Y`, short.
3. Classify the system files. `T` is `${CLAUDE_PLUGIN_ROOT}/template/workspace`:

   ```bash
   python3 "<T>/scripts/hq_sync.py" plan "<T>" "<workspace>"
   ```

   Statuses: `new` (file is new in the plugin), `safe` (you did not edit it), `edited` (you changed it), `same`, `obsolete` (the plugin no longer ships it). Without a `.hq-manifest.json` (a workspace from before 0.2.0) every differing file is `edited`: show the diff for each and let the user decide.
4. Apply the safe and new ones at once, and say what changed in one line per file group:

   ```bash
   python3 "<T>/scripts/hq_sync.py" apply "<T>" "<workspace>" safe
   ```
5. For each `edited` file show `diff -u <workspace file> <template file>` and ask: keep mine, take the new one, or merge. Take the new one with `hq_sync.py apply "<T>" "<workspace>" <relative path>`. For `obsolete` files ask before deleting. Never decide for the user.
6. Run the migrations below for every version between `X` and `Y` that has one, oldest first, before step 7. A version without a migration needs nothing beyond step 4.
7. Changes to the root `CLAUDE.md` or `context/` that the new version expects are listed in the changelog entry; show them as a proposal and apply only on a yes.
8. Write `Y` to `<workspace>/.hq-version`, then `python3 scripts/build_index.py`, then commit in the workspace: `git add -A && git commit -m "upgrade: X -> Y"`. Never push.
9. If `views/data/` has JSON from the old version, re-render the latest daily and weekly with `python3 scripts/render_view.py <file>` and report any LINK CHECK or LABEL CHECK lines.

## Migration 0.3.12 -> 0.4.0: checks and housekeeping

Runs when `X` is older than 0.4.0. The code arrives with the sync in step 4. Nothing is written to the task tool or to your own files before the user confirms.

1. **Asana only: field spec check.** Run "Check first" in `routines/stores/asana-fields.md` on all eight fields, now including type and options (Source must have all 17 values, Size XS-XL). Invalid ones follow "Repair an invalid field"; record the result in `meta/task-store.md`.
2. **`.gitignore`:** append `research/_archive/*/data/*` and `!research/_archive/*/data/.gitkeep` if missing, so archived topics keep their data out of git.
3. **Owner id:** add `owner_id:` to `meta/task-store.md` (the user's own id in the task tool, from the connector's current-user call). Only comments by this id are instructions.
4. **Brief DM:** ask "May the brief send you one DM to yourself with the headline and top items (never a file path)? [yes/no]" and add `self_dm_notice: yes|no` to `meta/chat-cursor.md`. Without the line nothing is sent.
5. **Proposals for the root `CLAUDE.md` (step 7):** the sentence about the `[Brief]` DM exception in rule 7, and a `Critical: <connectors>` line under "Required sources" (default: calendar and the task store).

## Migration 0.3.9 -> 0.3.10: context cards on every task

Runs when `X` is older than 0.3.10. The new routines, adapters and view code arrive with the sync in step 4. Nothing is written to the task tool before the user confirms.

1. Explain in two lines: every task now carries a context card in its description (What, Why / who waits, State, Decision or next step, Effort, Links), and every question that asks the user to choose shows that context per option.
2. List the open tasks (This week, Waiting, Inbox, Top of mind) that have no `What:` or no `State:` line. Show 3 as a sample: for each, read its source (the linked mail, chat thread, ticket, PR or document) through the connectors and draft the card from what the source says. Never invent a fact; a line the source cannot support says "unknown, ask" instead.
3. Ask "Add context cards to all N open tasks like this? [yes]". On yes write the cards through the adapter, below the property, `Waiting on:` and `Closed when:` lines, and show a count. On no leave the tasks as they are; the brief completes the cards task by task when it reads their sources.
4. Re-render the latest views (step 9); the task panel now shows What, State and Decision or next step when the data carries `what`, `state`, `decision`.

## Migration 0.3.7 -> 0.3.8: Area follows the initiative (every tool)

Runs when `X` is older than 0.3.8. From now on Area is never a custom field (`routines/stores/README.md`, "Area (one rule, every tool)").

1. In `meta/task-store.md`, remove Area from `fields:` and from "Field mapping" (show the lines first, edit on a yes). The old field stays in the tool, unused; Claude does not delete it.
2. For every initiative under `initiatives:`, make sure the container's description has an `Area: <name>` line: propose the area from the tie-break (`context/areas/index.md`) and the container's tasks, show the list ("Add the Area line to these N initiatives? [yes]"), write it through the adapter on a yes.
3. Task lines `Area: ...` on tasks that have an initiative are left as they are (harmless; the container wins).

## Migration 0.3.6 -> 0.3.7: HQ fields on every initiative project (Asana only)

Runs when `X` is older than 0.3.7 and `meta/task-store.md` has `store: asana`. Initiative projects made before 0.3.7 hold none of the eight `HQ ·` fields, so their tasks show other columns than the board.

1. List the projects under `initiatives:` in `meta/task-store.md`.
2. For each, add the eight fields recorded under `fields:` to the project through the connector (a field already on it is skipped). Show the list first and ask "Add the HQ fields to these N initiative projects? [yes]".

## Migration 0.3.5 -> 0.3.6: HQ fields MoSCoW and ICE, sizes XS-XL

Runs when `X` is older than 0.3.6. The new `routines/`, view code and `routines/stores/asana-fields.md` arrive with the sync in step 4. Standard connector for everything except the optional token path.

1. **Asana only: check the fields before anything else.** Follow `routines/stores/asana-fields.md`: "Check first", then "Create the missing fields" for any of the eight `HQ ·` fields that are missing. Continue only when all eight exist (description lines instead only when the user explicitly says to skip them).
2. Add the valid fields to the board project and record ids and option ids in `meta/task-store.md` (`fields`); update its property table to the new template rows (Priority, ICE, MoSCoW, Size XS-XL). An existing field that fails the spec check (wrong type, missing options such as XS or XL on `HQ · Size`, or a short Source list) follows "Repair an invalid field" in `asana-fields.md`; never write to it before it is valid.
3. Other tools: add MoSCoW, ICE (Impact, Confidence, Ease, score) and Size XS-XL the way the adapter now says (description lines or existing fields).
4. Offer to score the open Inbox and This week tasks with ICE (`routines/brief.md`, "ICE scoring"): show 3 as a sample and ask "Score all N tasks like this? [yes]". Never overwrite a Priority.
5. Re-render the latest views (step 9); the task tables now show MoSCoW and ICE.

## Migration 0.3.2 -> 0.3.3: initiatives become containers, properties become lines

Runs when `X` is older than 0.3.3. The new `meta/task-store.md` shape, `routines/stores/*` and the routines arrive with the sync in step 4. Nothing is written to the task tool before the user confirms. Only the standard connector is used: no API token, no scripts, no browser, no manual step.

1. **Read the store.** Through the adapter, list the open tasks with every property. Note which of Area, Initiative, OKR, Priority, Size, Source, Waiting on, Closed when were custom fields (`meta/task-store.md` `fields` has ids) and which initiatives exist (Initiative field values, plus the Top of mind tasks).
2. **Initiatives.** For each Initiative value, propose its container by the adapter (Asana project `🤖 <Initiative>`, Notion page, Monday board, Trello card, GitHub milestone) with a description from its Top of mind task and `research/` README (outcome, end date, OKR, `Topic folder: <name>`, links), attach its tasks to it (the Asana `HQ ·` fields are added to every initiative project later in this run, by migrations 0.3.5 -> 0.3.6 and 0.3.6 -> 0.3.7, because they do not exist yet here) (Asana: add the task to the project; others: the `Initiative:` line or relation). Show the list, one line per initiative with its task count, and ask "Create these N initiative containers and attach the tasks? [yes]".
3. **Properties.** For each property that is a custom field the user's connector cannot manage (Initiative, OKR, Waiting on, Closed when, and Area, Size, Source if not an existing field of the workspace), write its value into the description lines (`Area: ... · Size: ... · Source: ... · Priority: ...`, `Waiting on: <name>`, `Closed when: <scenario>`) on each task, keeping the existing text below. Priority keeps its field if it is an existing workspace field (record the mapping), else it becomes a line. Show a sample of 3 tasks first and ask "Convert all N tasks like this? [yes]".
4. **Verify and record.** Read the tasks back: count, initiative, and each line present. Fill `meta/task-store.md` (`fields`: only the existing fields still used; `initiatives`; the "Field mapping" section). Report differences and fix them first.
5. **Old fields.** Do not delete or edit the old custom fields (Claude cannot, and they do no harm). Tell the user once that they can remove the unused ones in the tool at their leisure; nothing depends on it.
6. Run `/hq:brief` once so the pages carry the new data.

## Migration 0.3.1 -> 0.3.2: documents home (`research/`)

Runs when `X` is older than 0.3.2. `research/CLAUDE.md` and `research/_template/` arrive with the sync in step 4 (system files). Nothing is moved or deleted before the user confirms the mapping.

1. **Create the home.** If `<workspace>/research/` has no `_archive/`, create it (`mkdir -p research/_archive && touch research/_archive/.gitkeep`). Append `research/*/data/*` and `!research/*/data/.gitkeep` to the workspace `.gitignore` if missing.
2. **Map existing pages.** List `context/projects/*.md` and `context/topics/*.md` (ignore `index.md`). For each page propose a topic folder: an initiative of the task store gets `research/YYYY-MM-DD - <Initiative>/` (date = the page's first date or today), a standalone project or topic gets its own folder. Show the mapping as a list (page -> folder, "merge" or "new") and ask "Use this mapping? [yes]". Apply the user's corrections.
3. **Create and merge.** For each confirmed folder: copy `research/_template` to the new name, then merge the page into the README: the page body goes under "Where it stands" / "Decisions" / "Key findings" (keep every fact and its source), links to documents go under "Shared links" (shared URLs) or "Earlier work" (named folders elsewhere, by name). Fill question, status `active`, started. Never copy a local path into "Shared links".
4. **Initiatives without a page.** For every open initiative in the task store with no folder yet, offer to create an empty topic folder the same way (after a yes). Add `Topic folder: <name>` to its Top of mind task description through the adapter (`Documents` in the Write section) after a yes.
5. **Remove the old folders** only after the user checks the READMEs: `git rm -r context/projects context/topics` (content stays in git history). Fix every `[[projects/...]]` and `[[topics/...]]` link (grep) to point at the topic folder, and propose the new root `CLAUDE.md` rows ("Documents" section, `research/` folder row, `context/` row without projects and topics) as a proposal (step 7).
6. **Shared destination.** Ask once "Where do shared versions of documents go? [Google Drive, Notion, Confluence, none]" and add `Shared versions: <answer>` to `context/places.md`.
7. Show the result: the topic folders created, one line each, and check each README has the CURRENT DOCUMENT callout.

## Migration 0.3.0 -> 0.3.1: people mapping

Runs when `X` is older than 0.3.1. `routines/people.md` arrives with the sync in step 4 (a system file). `context/people/*` is yours and is never overwritten.

1. For each existing profile in `context/people/` that lacks the `ids` block, show the new frontmatter (see `routines/people.md`) as a proposal and add it on a yes, keeping the body. Do not invent ids or relations.
2. If no profile has `close: true`, offer to run `routines/people.md` mode Map now (propose the close team from evidence, resolve identities). The root `CLAUDE.md` gains a "People" section with the privacy rules: show it as a proposal (step 7).

## Migration 0.2.0 -> 0.3.0: board.md moves to a cloud task store

Runs when `X` is older than 0.3.0 and `<workspace>/board.md` exists (or `meta/task-store.md` has no `store`). Nothing is written to the task tool or deleted before the user confirms the mapping.

1. **Which store?** Ask "Where do your tasks live?" with the options Asana, Notion, Monday, Trello, GitHub Projects (not recommended: no private personal-task semantics, tied to repositories). Read the adapter `routines/stores/<store>.md` (new in this version, copied in step 4) and test the connector with one read.
2. **Read `board.md`.** Every task line (`- [ ] <task> · id · P0-P3 · size · domain · status · closed when · source · link · added`), its indented notes, the Top of mind initiatives and the `domains` map. Tasks under "Done (this week)" are listed but not migrated.
3. **Areas and tie-break.** Run the setup step "2b. Areas and the task store" (`${CLAUDE_PLUGIN_ROOT}/skills/setup/SKILL.md`), with the role adapter's defaults and the old `domains` as the starting point. Write `context/areas/index.md` and `context/areas/<slug>.md` from the template.
4. **Show the mapping before any write**, one line per task, in a list (not a wide table):
   - section: Top of mind initiative -> an initiative container plus a Top of mind task; This week -> This week; Inbox -> Inbox; Agent -> Agent; status Waiting -> Waiting, with Waiting on from the notes if named.
   - priority P0-P3 and size XS-XL stay exactly as they are (XS is a valid size again); source maps to the Source list (unknown -> Me).
   - domain -> Area (by the tie-break, as a description line) and initiative (the container of the Top of mind item it belongs to, if any).
   - `closed when` -> the `Closed when:` description line; `link` and notes -> the task description; `added` -> a first comment "migrated from board.md, added YYYY-MM-DD".
   Ask "Migrate these N tasks like this? [yes]" and apply the user's corrections.
5. **Create the board** with the adapter's "Create the board" (as in setup step 5b; no manual steps), fill `meta/task-store.md` from the template (copy it from `<T>/meta/task-store.md` first), then create the tasks. Tag every task `ai`.
6. **Verify:** read the board back through the adapter and check the count and that each title, section, Area and Priority match the mapping. Report any difference and fix it before going on.
7. **Remove `board.md`** only after the verify passes and the user says yes: `git rm board.md`. The old content stays in git history. Remove every other mention of it in the user's own files as a proposal: the root `CLAUDE.md` rows and rule 4 (see the "Task store" section in the new template `CLAUDE.md`) and `context/` pages that link it.
8. The view pages need new data: tell the user to run `/hq:brief` once so the pages carry task links; old data files with `domain` still render with a LABEL CHECK note.
