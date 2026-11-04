---
type: topic
summary: The task store model every tool adapter implements (sections, properties, rules)
status: current
updated: {{SETUP_DATE}}
---

# The task store

Tasks live in one cloud tool, chosen in setup and named in `meta/task-store.md`. This page is the model; `routines/stores/<store>.md` says how the tool does it. Routines say "the task store" and use the operations below.

## Sections (fixed)

Top of mind (the initiatives themselves, one task each, linking to a ticket project or doc), This week, Waiting, Inbox, Agent (tasks Claude does itself). Rank is the order inside a section.

## Properties (fixed): one per question

Section, Completed, Due, Area, Initiative, OKR (optional), Priority P0-P3, Size S-L, Source, Waiting on (only in Waiting; the person's id comes from `context/people/<slug>.md`, `ids`, never from a first name), Closed when. Nothing is stored twice. Claude's reason for a priority is a task comment, not a field. Every task Claude creates carries the tag or label `ai` where the tool has one.

## Operations (every adapter implements)

- **list:** open tasks with all properties, in rank order, optionally one section or filter.
- **comments since:** comments added after a date, with task id and author.
- **create:** title, section, properties, closed-when, `ai` tag.
- **move:** to a section; **set:** one property; **complete**; **comment**; **add option** (Area, Initiative, OKR, Source value).
- **team task:** a task that lives in a team's tool and concerns the user. Asana: multi-home it into the board (one task, one comment thread). Every other tool: create a task that links back, never copy content.

## Rules

- **Rank:** the user drags; Claude never reorders a task the user moved.
- **Input:** a comment on a task ("next week", "delegate to X", "P0") is an instruction; each brief reads all comments since its last run and acts on them. Dragging sets rank. Ticking off is done.
- **New initiative:** proposed when tasks pass the initiative test (`context/areas/index.md`); created only after a yes (Top of mind task with `Topic folder: <name>`, a new Initiative option, and its topic folder in `research/`).
- **Closing an initiative:** proposed when all its tasks are done or the end date passed; after a yes, complete the Top of mind task, retire the option and set the topic README status to `complete` (moving the folder to `research/_archive/` is a second yes).
- **Documents:** a task's description or link holds the shared URL when one exists. Top of mind tasks carry `Topic folder: <folder name>` (a name, not a path) plus shared links. Never write a local path into the task tool (`research/CLAUDE.md`, Shared versions).
- **Tickets:** engineering work stays in the ticket tool. The task store holds only the user's own tasks and links to the tickets.
- **Writes:** changes to the task store only after the user confirms, except new Inbox tasks from triage and Claude's own Agent tasks.
- **Missing tool capability:** if the connector cannot do an operation, say so once and give the exact manual step; never pretend it worked. Say "Saved" only after reading the result back.
