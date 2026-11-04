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
| link, video, article, file | `sources/_incoming/` (processed by `ingest`) |
| shopping | `lists/shopping.md` |
| journal note | `journal/YYYY-MM-DD.md` |
| fact about a person, project or term | propose a `context/` change and save only on yes |

Also append one line to `inbox/YYYY-MM-DD.md`: `- HH:MM [voice] <text>`.

Confirm in one line where each item went. If the type is unclear, ask one question.

Then build the indexes, append to `log.md`, commit.
