---
type: topic
summary: Audit a tip, post, video or article against the current setup
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
   - **Backlog:** add it to Agent in `board.md` with the reason.
   - **Discard (hype):** say why.

   It's fine to say "drop it".
6. Save the source to `sources/articles/` with the verdict in its frontmatter, append to `log.md`, commit.
