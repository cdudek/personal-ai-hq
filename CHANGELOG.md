# Changelog

Versions follow semver. Each release is a git tag `vX.Y.Z` with an entry here. `/hq:upgrade` shows the entries between your workspace version and the installed one.

## 0.2.0 (2026-11-04)

- Renamed to Personal AI HQ: plugin `hq`, commands `/hq:<skill>`, config `~/.config/hq/workspace` (setup still reads the old `~/.config/personal-ai-os/workspace`).
- 10 skills instead of 13: `setup`, `upgrade`, `demo`, `brief [daily|weekly|update]`, `task [next|capture <text>]`, `inbox`, `meeting [name or time]`, `improve [review|tip <link>]`, `wiki [ingest <link or file>|refresh]`, `debrief`. Routines are unchanged; skills route to them.
- Marketplace is named `cdudek`: `/plugin install hq@cdudek`. `/hq:upgrade` updates the plugin through the `claude` CLI itself (or prints the two slash commands in Cowork) and then the workspace.
- New `/hq:upgrade` and a workspace `.hq-version`. Every skill checks it at the start and tells you when the workspace or the plugin is behind. Upgrades touch system files only and ask before changing a file you edited.
- New views: finished daily, weekly and review pages with embedded fonts, labels (priority, domain, topic) and the review page v2.
- Workspace files from 0.1.0: run `/hq:upgrade` once; without a manifest it shows a diff for every changed system file.

## 0.1.0

- First version: 13 skills, the workspace template with 13 routines, four role adapters, build-zip and scrub-check scripts.
