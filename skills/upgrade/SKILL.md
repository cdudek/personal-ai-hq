---
name: upgrade
description: Updates the HQ plugin to the latest release and brings the user's workspace up to it. Shows the changelog between the two versions, then updates only system files (routines, view code, scripts, folder rule files) and never user data. Files the user edited are shown as a diff and only changed on a yes. Use when the user says "upgrade", "update HQ", "new version", or after a skill says an HQ update is available.
---

# upgrade

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/version-check.md` first for the workspace lookup, but you are the one skill that acts on the result. Never run this unasked; it is the one command a user needs for updates.

## What is system and what is yours

- **System (this skill may update):** `routines/`, `scripts/`, `views/` code (`template.html`, `app.css`, `app.js`, `vendor/`, `icons/`, `CLAUDE.md`, `DESIGN.md`, `README.md`, `styleguide.template.html`), `SYSTEM.md`, and the `CLAUDE.md` rule file in each top-level folder (not the root one).
- **Yours (never touched):** root `CLAUDE.md`, `index.md`, `context/`, `inbox/`, `daily/`, `weekly/`, `journal/`, `meta/`, `decisions/`, `ideas/`, `principles/`, `lists/`, `sources/`, `views/data/` and every rendered view page. Your tasks are not in the workspace: they live in your task store (`meta/task-store.md`).

## Steps

0. **Update the plugin first.** Installed version `Y` = `version` in `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`. Latest `Z`: fetch `https://raw.githubusercontent.com/cdudek/personal-ai-hq/main/.claude-plugin/plugin.json` (`curl -fsS --max-time 3`; on failure assume `Z` = `Y`). If `Z` is newer than `Y` and you can run Bash with the `claude` CLI, run `claude plugin marketplace update cdudek`, then `claude plugin update hq@cdudek`. If the CLI says a restart is needed (it does), say: "HQ updated to Z. Restart Claude Code, then run /hq:upgrade again to bring your workspace along", and stop. If you cannot run the CLI (for example in Cowork), print the two commands for the user to run, `/plugin marketplace update cdudek` and then updating `hq` in `/plugin`, and stop.
1. Find the workspace (shared file). Installed version `Y` = `version` in `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json`; workspace version `X` = first line of `<workspace>/.hq-version` (missing = `0.1.0`). If `X` is not older than `Y`, say "already on Y" and stop.
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
6. Run the migrations below for every version between `X` and `Y` that has one, in order, before step 7.
7. Changes to the root `CLAUDE.md` or `context/` that the new version expects are listed in the changelog entry; show them as a proposal and apply only on a yes.
8. Write `Y` to `<workspace>/.hq-version`, then `python3 scripts/build_index.py`, then commit in the workspace: `git add -A && git commit -m "upgrade: X -> Y"`. Never push.
9. If `views/data/` has JSON from the old version, re-render the latest daily and weekly with `python3 scripts/render_view.py <file>` and report any LINK CHECK or LABEL CHECK lines.

## Migration 0.2.0 -> 0.3.0: board.md moves to a cloud task store

Runs when `X` is older than 0.3.0 and `<workspace>/board.md` exists (or `meta/task-store.md` has no `store`). Nothing is written to the task tool or deleted before the user confirms the mapping.

1. **Which store?** Ask "Where do your tasks live?" with the options Asana, Notion, Monday, Trello, GitHub Projects (not recommended: no private personal-task semantics, tied to repositories). Read the adapter `routines/stores/<store>.md` (new in this version, copied in step 4) and test the connector with one read.
2. **Read `board.md`.** Every task line (`- [ ] <task> · id · P0-P3 · size · domain · status · closed when · source · link · added`), its indented notes, the Top of mind initiatives and the `domains` map. Tasks under "Done (this week)" are listed but not migrated.
3. **Areas and tie-break.** Run the setup step "2b. Areas and the task store" (`${CLAUDE_PLUGIN_ROOT}/skills/setup/SKILL.md`), with the role adapter's defaults and the old `domains` as the starting point. Write `context/areas/index.md` and `context/areas/<slug>.md` from the template.
4. **Show the mapping before any write**, one line per task, in a list (not a wide table):
   - section: Top of mind initiative -> a Top of mind task plus an Initiative option; This week -> This week; Inbox -> Inbox; Agent -> Agent; status Waiting -> Waiting, with Waiting on from the notes if named.
   - priority P0-P3 stays; size XS becomes S, S/M/L stay; source maps to the Source list (unknown -> Me).
   - domain -> Area (by the tie-break) and Initiative (the Top of mind item it belongs to, if any).
   - `closed when` -> Closed when; `link` and notes -> the task description; `added` -> a first comment "migrated from board.md, added YYYY-MM-DD".
   Ask "Migrate these N tasks like this? [yes]" and apply the user's corrections.
5. **Create the board** with the adapter's "Create the board" (as in setup step 5b, manual steps where the connector cannot), fill `meta/task-store.md` from the template (copy it from `<T>/meta/task-store.md` first), then create the tasks. Tag every task `ai`.
6. **Verify:** read the board back through the adapter and check the count and that each title, section, Area and Priority match the mapping. Report any difference and fix it before going on.
7. **Remove `board.md`** only after the verify passes and the user says yes: `git rm board.md`. The old content stays in git history. Remove every other mention of it in the user's own files as a proposal: the root `CLAUDE.md` rows and rule 4 (see the "Task store" section in the new template `CLAUDE.md`) and `context/` pages that link it.
8. The view pages need new data: tell the user to run `/hq:brief` once so the pages carry task links; old data files with `domain` still render with a LABEL CHECK note.
