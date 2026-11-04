---
name: upgrade
description: Updates the HQ plugin to the latest release and brings the user's workspace up to it. Shows the changelog between the two versions, then updates only system files (routines, view code, scripts, folder rule files) and never user data. Files the user edited are shown as a diff and only changed on a yes. Use when the user says "upgrade", "update HQ", "new version", or after a skill says an HQ update is available.
---

# upgrade

Follow `${CLAUDE_PLUGIN_ROOT}/skills/_shared/version-check.md` first for the workspace lookup, but you are the one skill that acts on the result. Never run this unasked; it is the one command a user needs for updates.

## What is system and what is yours

- **System (this skill may update):** `routines/`, `scripts/`, `views/` code (`template.html`, `app.css`, `app.js`, `vendor/`, `icons/`, `CLAUDE.md`, `DESIGN.md`, `README.md`, `styleguide.template.html`), `SYSTEM.md`, and the `CLAUDE.md` rule file in each top-level folder (not the root one).
- **Yours (never touched):** root `CLAUDE.md`, `index.md`, `board.md`, `context/`, `inbox/`, `daily/`, `weekly/`, `journal/`, `meta/`, `decisions/`, `ideas/`, `principles/`, `lists/`, `sources/`, `views/data/` and every rendered view page.

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
6. Changes to the root `CLAUDE.md` or `context/` that the new version expects are listed in the changelog entry; show them as a proposal and apply only on a yes.
7. Write `Y` to `<workspace>/.hq-version`, then `python3 scripts/build_index.py`, then commit in the workspace: `git add -A && git commit -m "upgrade: X -> Y"`. Never push.
8. If `views/data/` has JSON from the old version, re-render the latest daily and weekly with `python3 scripts/render_view.py <file>` and report any LINK CHECK or LABEL CHECK lines.
