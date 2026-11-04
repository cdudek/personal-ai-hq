---
type: topic
summary: Audit a tip, post, video or article against the current setup, and check the areas for drift
status: draft
updated: {{SETUP_DATE}}
---

# Routine: improve (on demand)

Input: a link or text from the user, from the chat DM to themselves, from the drop folder, or an open line in `meta/tips.md` (Friday's `review` runs this for each).

1. Read it. Fetch the transcript for videos.
2. Summarise its core proposal in 2 sentences.
3. Check workflow fit: does the setup already do this (name the routine or file), or does it fill a real gap?
4. Check maintenance cost: what has to be built and kept alive?
5. Give a verdict:
   - **Adopt:** name the file to change and the change.
   - **Backlog:** add it to the Agent section of the task store with the reason.
   - **Discard (hype):** say why.

   It's fine to say "drop it".
6. Save the source to `sources/articles/` with the verdict in its frontmatter, append to `log.md`, commit.

## Area drift (Friday, called by `review`)
Read `context/areas/index.md` and the open tasks of the task store (adapter in `meta/task-store.md`), plus the `area misfit` lines in `meta/friction.md` and the tasks whose Area the user changed this week. Propose, never apply without a yes:
- **Misfits:** two or more `area misfit` lines, or an area that is the catch-all for most tasks: a new area or a split, with a name, one-line definition and the tasks that would move.
- **Initiatives:** tasks that pass the initiative test but have no initiative container (open one); initiatives whose tasks are all done or whose end date passed (close one).
- **Tie-break:** a rule the user keeps overriding: the corrected wording.
Each proposal goes into the review page as a `fixes[]` item with the exact change to `context/areas/index.md` or the task store. After a yes, apply it, log it in `meta/learnings.md`, and tick the friction lines.

## People data (Friday, called by `review`)
Close people with empty ids, ids without a `sources` entry, ids that no longer match (a bounced mail, a chat user that left), "Current" older than 35 days, and names that appeared in the week's items with no profile. Propose `routines/people.md` runs (Resolve, Refresh, New person) under "Claude asks". Never fix an id without the user's yes.
