# Personal AI HQ

A plugin for Claude Code and Cowork that turns Claude into your personal HQ. It keeps a private second brain in a local folder, manages your tasks in the cloud task manager you pick, builds a daily and a weekly briefing page from your calendar, mail, chat and tickets, and learns from your corrections. The second brain stays on your computer; nothing from it is pushed anywhere.

## Quick start (30 seconds)

```text
/plugin marketplace add cdudek/personal-ai-hq
/plugin install hq@cdudek
/hq:setup
```

Then `/hq:brief`. Not sure yet? `/hq:demo` shows sample pages first and needs no connectors.

## Install

### Claude Code

```text
/plugin marketplace add cdudek/personal-ai-hq
/plugin install hq@cdudek
```

### Cowork

Customize > Plugins > Add marketplace, enter `cdudek/personal-ai-hq`, then Install. Or run `scripts/build-zip.sh` and use Add > Upload plugin with `dist/hq-<version>.zip`. Unverified: whether Cowork accepts the root-level plugin source; if the marketplace route fails, use the zip.

## Your documents: `research/`

Every document and piece of research for an initiative lives in one place: a topic folder in `<workspace>/research/`, named `YYYY-MM-DD - Topic Name`. `/hq:setup` creates `research/` (rules in `research/CLAUDE.md`, a `_template/` skeleton, `_archive/`) and one topic folder per initiative you confirm. A topic folder has a `README.md` that opens with a "CURRENT DOCUMENT" callout and is the memory of the initiative (status, decisions, latest documents, shared links), plus `notes.md`, `working/`, `output/` (with `_archive/`) and `data/` (git-ignored). Tasks carry `Topic folder: <name>`, the pages show a task's documents, and shared versions (Google Drive, Notion, Confluence) are linked by URL, never by local path. Coming from 0.3.1? `/hq:upgrade` merges your `context/projects` and `context/topics` pages into topic READMEs after you confirm the mapping.

## Updating

`/hq:upgrade` updates the plugin and then your workspace. In Cowork the `claude plugin` CLI is not available in the cloud session: update the plugin under Customize > Plugins, start a new session, then run `/hq:upgrade`. A workspace with a `.hq-author` file is the author reference: `/hq:upgrade` updates only the plugin there and never syncs template files into it.

## Pick your task manager

Your tasks live in one tool you already use, not in a file: Asana, Notion, Monday or Trello. GitHub Projects works too but is not recommended (no private personal-task semantics, tied to repositories). `/hq:setup` asks where your tasks live, proposes areas (for example Product, Team, Company, Admin, Me) and a tie-break rule from your role, creates one private board with the sections Top of mind, This week, Waiting, Inbox and Agent, and one property per question (Area, Initiative, Priority, Size, Source, Waiting on, Closed when). Where the connector cannot create something, setup prints the exact manual steps. You steer by commenting on a task, dragging it or ticking it off; the next brief reads it. Coming from 0.2.0? `/hq:upgrade` moves `board.md` into the tool once. Each task carries Priority (what first), ICE (Claude's Impact x Confidence x Ease score, which proposes the Priority), MoSCoW (scope within the week or an initiative) and a t-shirt Size (XS-XL). With Asana, eight shared `HQ · ` fields hold these; setup checks for them and, if they are missing, has you create them once for your whole organisation (field spec and click path in `template/workspace/routines/stores/asana-fields.md`; an `ASANA_API_TOKEN` in Claude Code can do it for you, never required).

## Set up

Run `/hq:setup`. It interviews you (name, company, team, role, goals, tools, writing samples, languages, where your tasks live), tells you which connector to switch on per tool, picks a role adapter, sets up your task board, copies the workspace template to a folder you choose (default `~/ai-workspace`, never a synced folder), starts a local git repo, creates the scheduled tasks and offers a first brief. Want a preview first? Run `/hq:demo`; it needs no connectors.

## Commands

Skip the argument and the skill infers it and says what it chose.

| Command | What it does | Example |
|---|---|---|
| `/hq:setup` | Interview, workspace, scheduled tasks | `/hq:setup` |
| `/hq:upgrade` | Brings your workspace up to the installed version | `/hq:upgrade` |
| `/hq:demo` | Renders fictional sample pages | `/hq:demo` |
| `/hq:brief [daily\|weekly\|update]` | Daily brief, Monday weekly prep, mid-day update | `/hq:brief weekly` |
| `/hq:task [next\|list\|add\|move\|set\|done\|capture <text>]` | Work with your task store: next action, list, change, or file a capture | `/hq:task list this week` |
| `/hq:inbox` | What needs you and what you wait on | `/hq:inbox` |
| `/hq:meeting [name or time]` | Prep a meeting; default the next one | `/hq:meeting 1:1 Nora` |
| `/hq:improve [review\|tip <link>]` | Friday learning loop, or audit a tip | `/hq:improve tip https://example.com/post` |
| `/hq:wiki [ingest <link or file>\|refresh]` | File sources, monthly lint | `/hq:wiki ingest notes.pdf` |
| `/hq:debrief` | Evening reflection and day note | `/hq:debrief` |

Scheduled tasks (created by setup): brief weekdays 7:27, weekly Monday 6:57, review Friday 15:57, refresh first Monday of the month 7:57. Local tasks only run while your computer is awake and the app is open.

## Updates

HQ is versioned with semver. Each release is a git tag `vX.Y.Z` with an entry in `CHANGELOG.md`.

`/hq:upgrade` is the one command you need. In Claude Code it updates the plugin itself (`claude plugin marketplace update cdudek`, `claude plugin update hq@cdudek`), asks you to restart, and on the second run brings your workspace along. Where it cannot run commands (Cowork) it prints the two slash commands (`/plugin marketplace update cdudek`, then update `hq` in `/plugin`) for you. You can also enable auto-update for the `cdudek` marketplace in `/plugin` > Marketplaces. The workspace step shows what changed, updates system files only (routines, view code, scripts, folder rule files) and never your data (context, inbox, daily, weekly, journal, meta). If you edited a system file, it shows the diff and asks.

Every skill checks versions at the start and tells you in one line when your workspace or the plugin is behind; it never upgrades by itself. The latest-release check is one request a day to raw.githubusercontent.com and stays silent if it fails. Maintainers: `scripts/release.sh X.Y.Z` bumps both manifests, adds a changelog stub, commits and tags (no push).

## Privacy

- The workspace is a local folder and a local git repo. Never add a remote. Do not put it in iCloud, Dropbox or another synced folder.
- Your tasks live in the task tool you choose, under that tool's own privacy rules; setup creates a private board.
- Connectors read your data (mail, calendar, chat, tickets). Claude reads it during a run; this plugin sends nothing anywhere itself.
- Nothing is saved to your context pages without your yes, and nothing is sent or posted for you without your yes.
- Respect your company's policy on AI and connectors before you switch them on.

## Uninstall

`/plugin uninstall hq@cdudek` and `/plugin marketplace remove cdudek`. Delete the workspace folder and `~/.config/hq/` by hand if you want everything gone.

## Credits

Inspired by Daniel Bloom's "How I AI" episode on his Cowork system and by Andrej Karpathy's idea of an LLM-maintained wiki.

MIT licence, 2026 Calvin Dudek.
