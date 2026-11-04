---
type: topic
summary: Weekly self-improvement audit - style, vocabulary, friction, skill candidates, tips, plan vs actual
status: draft
updated: {{SETUP_DATE}}
---

# Routine: review (Friday afternoon)

Output: `weekly/YYYY-Www.md`, section "Review". Everything is a proposal. Apply only what the user approves. Every applied rule gets a dated line in `meta/learnings.md`.

If the logs are empty, ask the user for 1-2 drafts they changed and their main pain points this week.

## 1. Style and voice
- For each draft in `meta/drafts.md` from this week, find what the user actually sent: mail "Sent", or their chat messages to the same person or thread within 48 hours.
- Compare the two:
  - what they removed (filler, framing)
  - what they added (context, greeting, domain words, format)
  - how the style shifted (length, bullets, tone)
- Also learn from what the user wrote without a draft: read 10-20 of their sent mails and chat messages from this week. Note recurring patterns per channel and language: openings, closings, length, bullets, language mix, words they use and words they never use.
- Propose rules per channel. On approval, append them to `context/writing-style.md` under "Learned", each with one before/after example.

## 1b. Vocabulary
- Collect terms from this week's meetings, chat and mail that are not in `context/glossary.md`, and terms the user used differently from the glossary.
- Propose additions and corrections ("A term I didn't know, the [X]... I read [source] and understand [Y]. Save?"). On yes, write them to `context/glossary.md`.

## 2. Friction patches
- Group this week's `meta/friction.md` lines.
- For each top issue, give issue, root cause and fix. The root cause is one of:
  - missing definition or context
  - unclear format
  - wrong or missing step
- The fix goes into a routine file, a `CLAUDE.md`, or `context/`.

## 3. Skill candidates
Find sequences the user repeated by hand this week (from the `daily/` notes and the log). For each, propose a routine: trigger, inputs, output.

## 4. Done patterns
How did the user close tasks this week? Propose updates to the done signals in `inbox/CLAUDE.md`.

## 5. Tip triage
For each open line in `meta/tips.md`, run `routines/improve.md` and show the verdict (adopt, backlog, discard) with the file it would change. Apply adopted ones only after the user says yes, then tick the line with the verdict and date.

## 6. Plan vs actual
- Show the week's totals and where unplanned work came from.
- Propose how much room next week's plan leaves.

## 7. Write the page

**Labels (required):** every item in Needs attention, Replies and reviews, Waiting on others, Board proposals and on the board gets `priority` and `domain` (from `board.md`; else blocking or due today = P0, due this week = P1, otherwise P2 or P3), plus `topic` when it links to a Linear issue, project, initiative or OKR. Copy the `domains` map from `board.md` into the JSON. The renderer prints `LABEL CHECK` for anything missing; fix it and render again.

Write `views/data/review-YYYY-Www.json` (schema: `views/CLAUDE.md`, "Review view") with the proposals from sections 1 to 6: `style[]`, `glossary[]`, `fixes[]`, `tips[]`, `routines_new[]`, `plan_actual`, `start_here`, `sources[]`. Leave out any "nothing is applied until you decide" sentence from `headline`: the page says it. Every proposal must carry `evidence` (`[{quote, source, link, when}]`: draft vs sent pair, friction lines, the tip's original message, repeated steps with dates), `impact` (one line) and `change` (`{file, before, after}`, the exact text). Render it with `python3 scripts/render_view.py views/data/review-YYYY-Www.json` and `open views/review.html`. The user decides on the page and pastes the `<<<REVIEW ... >>>` block; apply `adopt` lines, apply the user's `your version` for `adjust` lines (ask for it if missing), and leave `park` lines in the queue for the next review. In the next weekly view, set `last_review` (`{adopted, open, link: "review.html"}`).

Close: build the indexes, append to `log.md`, commit.
