# Personal AI HQ

Claude reads your inboxes every morning, tells you what needs you, and keeps your tasks and notes in order. You stay in charge: nothing is sent, posted or saved without your yes.

Built for anyone with too many inboxes: engineers, product managers, sales, founders.

## What you get

- **Morning brief.** What needs you today, your meetings with prep, who waits on you.
- **Weekly plan.** Every Monday Claude proposes your week. You accept or change it.
- **Your tasks in your tool.** Asana, Notion, Monday or Trello. Claude keeps the board tidy.
- **Meeting prep.** Docs read, last meeting's action items, open points for 1:1s.
- **A memory that grows.** Goals, people, decisions and research, as files on your computer.
- **Gets better every week.** On Friday it shows what it learned and asks what to keep.

## Install

**Claude desktop app (Cowork):** Customize > Plugins > Add marketplace, enter `cdudek/personal-ai-hq`, click Install. Then type `/hq:setup` in a new task.

**Claude Code:** paste these one at a time.

```text
/plugin marketplace add cdudek/personal-ai-hq
```

```text
/plugin install hq@cdudek
```

```text
/hq:setup
```

Setup asks about your job, goals and tools, connects them, and sets up your board. Just want a look? `/hq:demo` shows sample pages.

Week one costs you time. It has to learn your work before it saves you any.

## Daily use

| Type | You get |
|---|---|
| `/hq:brief` | Your brief now |
| `/hq:task` | Your next task |
| `/hq:inbox` | What needs you |
| `/hq:meeting` | Prep for your next meeting |
| `/hq:upgrade` | The latest version |

The brief, the Monday plan and the Friday review also run on their own while your computer is on.

## Your data

Your notes stay on your computer. Your tasks stay on a private board in your tool. Claude only sees what the connectors you switch on can see. A tool you have not connected is skipped and listed, nothing breaks. Check your company's AI rules before connecting work accounts.

## More

Details on fields, folders and updates: [docs/reference.md](docs/reference.md). Questions: open an issue or find Calvin Dudek on LinkedIn.

Inspired by Daniel Bloom (How I AI) and Andrej Karpathy's AI-kept wiki. MIT licence, Calvin Dudek.
