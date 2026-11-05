---
type: topic
summary: File one dictated or typed capture into the right place
status: draft
updated: {{SETUP_DATE}}
---

# Routine: capture (any time)

Sort each capture into one of these:

| Type | Goes to |
|---|---|
| work task for the user | Inbox of the task store, with Area, Priority, Size, Source, `closed when:` and tag `ai` |
| task for the agent | Agent section of the task store |
| tip for the system itself ("we should also...", a workflow post, a tool someone recommends) | `meta/tips.md` (evaluated Friday by `review`) |
| idea (not committed to yet; it becomes a task only when the user commits) | `ideas/YYYY-MM-DD-kebab-title.md` (frontmatter as in `ideas/CLAUDE.md`) |
| link, video, article, file | `sources/_incoming/` (processed by `ingest`); research material for a known initiative goes straight to that topic folder's `working/` in `research/` |
| shopping | `lists/shopping.md` |
| journal note | `journal/YYYY-MM-DD.md` |
| "feedback to X: ..." / "note on X: ..." | one record entry from the user's own words, appended to `context/people/<slug>/records/YYYY/MM/YYYY-MM-DD.md`: `- HH:MM [feedback-given\|feedback-received\|discussion\|decision\|commitment\|personnel] text · source: the user`. Type from their words ("feedback to X" = feedback-given; a personnel matter = personnel), never inferred or reworded into a judgement. Append only; a correction is a new entry naming the earlier date (`routines/people.md`, "Records"). Not in `inbox/` text, not in the task store |
| fact about a person, project or term | propose a `context/` change and save only on yes |

Also append one line to `inbox/YYYY-MM-DD.md`, as soon as the item is routed: `- HH:MM [voice] <text> -> filed: <destination>` (the task id in the task store, or the path under `ideas/`, `lists/`, `meta/`, `sources/_incoming/`). A capture still waiting for an answer or a yes has no `-> filed:` part, so `debrief` routes it. **Journal notes are the exception:** write only a receipt, `- HH:MM [voice] journal note -> filed: journal/YYYY-MM-DD.md`, never the text. Journal content stays inside `journal/` (an inbox line would reach indexes, the brief and chat).

Confirm in one line where each item went. If the type is unclear, ask one question.

Then build the indexes, append to `log.md`, commit.
