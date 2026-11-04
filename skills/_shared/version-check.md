# Start of every HQ skill

Do this first, before the skill's own steps. It never changes anything by itself.

## Find the workspace

1. Read `~/.config/hq/workspace` (one line: the absolute path of the workspace). If it is missing, read the old `~/.config/personal-ai-os/workspace`.
2. If neither is readable (for example in a sandbox), use the current folder when it contains `CLAUDE.md` and `routines/`. In Cowork the project's folder is the workspace.
3. Otherwise ask for the workspace path, or tell the user to run `/hq:setup`. Do not guess.

Then read `<workspace>/CLAUDE.md` and `<workspace>/index.md`. Follow the rules there: nothing is saved to `context/` without a yes, nothing is sent without a yes.

## Version check (at most two lines, never blocking)

1. **Workspace behind the plugin.** Installed version `Y` = `version` in `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/plugin.json` (if the variable is empty, the `.claude-plugin/` folder two levels above this file). Workspace version `X` = the first line of `<workspace>/.hq-version` (missing = `0.1.0`). If `Y` is a newer semver than `X`, say: "Your HQ workspace is on X, the plugin is on Y: run /hq:upgrade".
2. **Plugin behind the latest release.** Read `<workspace>/.hq-update-check` (`{"checked": "YYYY-MM-DD", "latest": "Z"}`). If `checked` is not today, run `curl -fsS --max-time 3 https://raw.githubusercontent.com/cdudek/personal-ai-hq/main/.claude-plugin/plugin.json`, take its `version`, and write the file. On any failure, stay silent and write nothing. If the cached `latest` `Z` is newer than `Y`, say: "HQ Z is out (you have Y): run /hq:upgrade. What's new: <first line of the CHANGELOG entry for Z>" (fetch `https://raw.githubusercontent.com/cdudek/personal-ai-hq/main/CHANGELOG.md` the same way; if that fails, leave the last sentence out).

Compare as numbers per part (0.10.0 is newer than 0.9.0). Never run an upgrade yourself.

## Voice and ending (every skill)

- Plain, short sentences. No jargon, no hype.
- When the argument was left out, say in one line what you inferred and how to choose another, for example: "No argument: it's Monday morning, running the weekly brief. Use /hq:brief daily for the daily."
- Errors are actionable: say what failed, why if you know, and the exact next step. A missing connector never stops a run: skip that source, list it under "Sources" with how to enable it (Claude Code: `/mcp`; Cowork: Settings > Connectors), and carry on.
- End every command with one short block of three lines, no more:
  - **Done:** what happened.
  - **Where:** the page you opened or the path of the result.
  - **Next:** the one command to try next, for example `/hq:inbox`.
