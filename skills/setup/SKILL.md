---
name: setup
description: Onboarding for the personal-ai-os plugin. Interviews the user (name, company, team, role, day to day, goals, tools, writing samples, languages), picks a role adapter, copies the workspace template to a folder, fills in the rules, context and tool routing, starts a local git repo, creates the scheduled tasks, and offers a first brief. Use when the user says "setup", "set up my AI workspace", "onboard me", "install the personal operating system", "get started", or runs /personal-ai-os:setup.
---

# setup

Goal: a working private workspace in about 20 minutes. Ask one block of questions at a time, not all at once. Never push anything anywhere. Never put the workspace inside a synced folder (iCloud Drive, Dropbox, OneDrive, Google Drive, or an Obsidian-sync folder), because sync tools corrupt git repos and expose private notes.

## 0. Check the basics

- Is a workspace already configured? Read `~/.config/personal-ai-os/workspace`. If it exists and the folder has `CLAUDE.md`, ask: continue with that workspace (go to step 7 to repair or extend), or create a new one.
- `python3 --version` and `git --version` must work. If not, tell the user what to install and stop.

## 1. Interview

Ask in this order, 2-4 questions per message. Keep answers short; use what the user already told you.

1. **You:** name; role and title; languages for work (and which language for which channel, for example German internally, English with customers).
2. **Company:** name; what it does in one or two sentences; your team (who is in it, how big); who you report to (a title is enough).
3. **Work:** what you do day to day; your goals this quarter (3-5; ask for a link to the source document).
4. **Tools, per category** (name the product, or "none"): chat, mail, calendar, tasks and tickets, code, docs and files, CRM, notes and meetings, whiteboard. Also: is there a company data gateway (an internal connector for the warehouse, CRM and meetings)? Optional.
5. **Writing samples:** ask for 2-3 messages or mails they sent and like (paste them, or say where to find sent items: then read 10 from "Sent"). These seed `context/writing-style.md`. Never ask for anything confidential; the user can anonymise.
6. **Phone input:** work captures through a DM to yourself in the work chat, private captures through a drop folder (in a synced folder is fine, only the drop folder, never the workspace), a voice notes app. Which do they want?
7. **Handling rules:** anything Claude must always handle in a fixed way (for example "invoices go to finance", "ignore mail older than X"). Optional; becomes a rule in `CLAUDE.md`.

## 2. Pick the role adapter

Choose from `${CLAUDE_PLUGIN_ROOT}/template/adapters/`: `product-manager`, `engineering-lead`, `sales-cs`, `founder-exec`. Propose the best fit from the role and tools, and let the user pick. If none fits, use the closest and say what differs. Read the adapter: it gives tool defaults, routine emphasis, glossary seeds and typical meeting types.

## 3. Connectors: what to switch on

For every tool named in step 1, say which connector to enable and how, one line each:

- **Claude Code:** `/mcp` lists connectors; add a missing one with `claude mcp add` (see the tool's own docs) or install the tool's plugin from `/plugin`.
- **Cowork and Claude Desktop:** Settings > Connectors (or Customize > Connectors), pick the tool, sign in.
- Common ones: Slack, Gmail, Google Calendar, Google Drive and Docs, Linear, Asana, Jira and Confluence (Atlassian), GitHub (or the `gh` CLI), Notion, HubSpot, Miro, Granola, Fireflies.
- No connector for a tool: the browser (Claude in Chrome) covers it, slower. Mark it in the routing as "browser".

Test each enabled connector with one read (today's calendar, one mail, one ticket) and list what works and what is missing. A missing one is not a blocker: routing says "none" and routines skip it. Never claim a connector exists without checking that its tools are available in this session.

## 4. Choose the folder

Default `~/ai-workspace`. Check the path: it must not be under `~/Library/Mobile Documents`, `~/Library/CloudStorage`, `~/Dropbox`, `~/Documents` when Documents is synced, or any other synced folder. If it is, propose `~/ai-workspace` instead. Refuse to overwrite a non-empty folder.

## 5. Copy the template and fill it

1. Copy: `cp -R "${CLAUDE_PLUGIN_ROOT}/template/workspace/." "<workspace>/"`.
   - If `${CLAUDE_PLUGIN_ROOT}` is not resolved (run `echo "${CLAUDE_PLUGIN_ROOT}"`; empty means it is not, which can happen in Cowork), locate the template next to this file: the `template/workspace` folder two levels above this `SKILL.md`. If you cannot find it, ask the user for the folder where the plugin is installed (in Claude Code usually under `~/.claude/plugins/`) or where they unzipped it.
2. Fill the placeholders. Find them with `grep -rn '{{' "<workspace>" --include='*.md'`. Fill:
   - `CLAUDE.md`: `{{NAME}}`, `{{ROLE}}`, `{{COMPANY}}`, `{{LANGUAGES}}`, the whole tool routing table (`{{TOOL_*}}`, one product per row, "none" where there is none, "browser" for no connector; the gateway row says "none" unless step 1 named one), `{{INBOX_CUTOFF}}` (today's date), `{{RECURRING_INPUTS}}` ("None yet." unless the user named some), `{{REF_*}}` (where to look up company, handbook and numbers; "ask the user" if unknown), `{{PHONE_*}}` from step 1 question 6 (write "not used" for options they skipped). Add the handling rules from step 1 question 7 as a short section "Standing handling rules".
   - `context/me.md`: name, company and description, team, role, day to day, languages; `{{NEVER}}` from the user's own rules (ask for 1-3 things Claude must never do; always include "send or publish anything without asking").
   - `context/goals.md`: the goals, each with its source link.
   - `context/glossary.md`: the adapter's glossary seeds plus company terms the user mentioned, each marked "to confirm" until confirmed.
   - `context/writing-style.md`: `{{STYLE_RULES}}` from the writing samples: tone, length, greeting and closing, bullets, language per channel, words used and avoided, each rule with a short quote. Mark the file `status: draft` until the user confirms.
   - `context/places.md`: the workspace path and where code and documents live.
   - `meta/chat-cursor.md`: `{{PHONE_WORK_CHANNEL}}` (or "not used").
   - everywhere: `{{SETUP_DATE}}` = today.
   - Append a "Role adapter" block to `context/me.md` with the chosen adapter's routine emphasis and typical meeting types.
3. If a tool has no row in the folder (for example no code tool), remove that source's mention only if the routine would otherwise fail; the routing "none" already makes routines skip it.
4. Re-run the grep: no `{{` may remain.
5. Create the drop folder if the user wants one, and write the config: `mkdir -p ~/.config/personal-ai-os && printf '%s\n' "<workspace>" > ~/.config/personal-ai-os/workspace`.
6. In Cowork, tell the user to create a project that points at the workspace folder and to put this project instruction in it: "Read CLAUDE.md first, then index.md. Follow the rules there. Routines live in routines/." Scheduled tasks must be created inside that project.

## 6. Git, indexes, first commit

```bash
cd "<workspace>"
python3 scripts/build_index.py
git init
git add -A
git commit -m "setup: initial workspace"
```

Never add a remote, never push. If `views/template.html` is missing, say that the view pages need the files synced into the template (the brief still works as a note).

## 7. Scheduled tasks

Scheduled tasks are only prompts. Create these four tasks yourself, inside the user's workspace project (Cowork: the project that points at the workspace folder; Claude Desktop: the workspace folder). Prompt for each: "Follow routines/<name>.md".

| When | Prompt |
|---|---|
| Weekdays 7:27 | `Follow routines/brief.md` |
| Monday 6:57 | `Follow routines/weekly.md` |
| Friday 15:57 | `Follow routines/review.md` |
| First Monday of the month 7:57 | `Follow routines/refresh.md` |

Use the scheduled-task tool available in this session. Odd minutes avoid the busy top of the hour. If creating a task fails or no such tool exists, print each one as a ready-to-paste block (time, then the prompt) and tell the user to add them under Scheduled > New task, inside their project. Say clearly that local tasks only run while the computer is awake and the app is open.

## 8. Offer the first brief

Show a summary (workspace path, adapter, connectors that work and that are missing, tasks created or printed) and offer to run `/personal-ai-os:brief` now. If the user agrees, run it. Ask afterwards what was wrong or missing and log each answer to `meta/friction.md`.

## Rules

- Do not invent facts about the company, the team or the user. Unknown means a question, or "to confirm".
- Everything you write into `context/` is a draft until the user says yes (workspace rule 1).
- Keep the workspace free of company secrets: references, not copies.
