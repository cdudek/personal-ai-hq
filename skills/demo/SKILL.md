---
name: demo
description: Renders the sample daily, weekly and review pages with fictional data (no connectors, no setup needed) and opens them, so you can see what the system produces. Use when the user says "demo", "show me an example", "what does the brief look like", "preview the views", or wants to see the pages before setting up.
---

# demo

Shows the daily, weekly and review pages built from fictional sample data. Needs no connectors. Renders into a temporary folder by default, so nothing in the user's workspace is touched.

## Steps

1. Find the template: `${CLAUDE_PLUGIN_ROOT}/template`. If that variable is not resolved (check with `echo "${CLAUDE_PLUGIN_ROOT}"`), look for a `template/` folder next to this `SKILL.md` (two levels up), or ask the user for the plugin folder.
2. Make a temporary copy of the workspace template and render the samples:

   ```bash
   T="$(mktemp -d)"
   cp -r "<template>/workspace/." "$T/"
   mkdir -p "$T/views/data"
   cp "<template>/sample/"*-sample.json "$T/views/data/"
   cd "$T" && for k in daily weekly review; do python3 scripts/render_view.py views/data/$k-sample.json; done
   ```
3. If `views/template.html` is missing in the copy, the view files were not synced into this version of the template: say so and stop.
4. Open `$T/views/daily-sample.html`, `$T/views/weekly-sample.html` and `$T/views/review-sample.html` (`open` on macOS, `xdg-open` on Linux, `start` on Windows). In Cowork, if you cannot open a browser, tell the user the three file paths.
5. Also show the sample topic folder in the copy: `research/2026-01-15 - Example Acme Pricing Review/` (README with the current-document callout, `output/`, `working/`, `notes.md`), and say that `/hq:setup` creates one such folder per initiative. The task panel in the sample pages shows its documents under "Documents" (open the first task).
6. End with the three-line block (Done, Where, Next) from `${CLAUDE_PLUGIN_ROOT}/skills/_shared/version-check.md`: what the pages show, that all names and data are fictional (company "Acme"), the folder they are in, and that `/hq:setup` builds the real thing.
