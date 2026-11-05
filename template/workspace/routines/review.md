---
type: topic
summary: Weekly self-improvement audit - style, vocabulary, friction, skill candidates, tips, plan vs actual
status: draft
updated: {{SETUP_DATE}}
---

# Routine: review (Friday afternoon)

Output: `weekly/YYYY-Www.md`, section "Review". Everything is a proposal. Apply only what the user approves. Every applied rule gets a dated line in `meta/learnings.md`.

If the logs are empty, ask the user for 1-2 drafts they changed and their main pain points this week.

## 1. Style and voice (always runs; the draft feedback loop)
Run this section every Friday, not only when logs look full.
- **Drafts of the week:** read `meta/drafts/` for the last 7 days. The daily brief has already appended an `outcome:` to each entry (`routines/brief.md` step 0b); fill any that is missing now (mail Sent, chat messages from the user in that DM, channel or thread).
- **Edited or rewritten:** for every draft with outcome `edited` or `rewritten`, compare draft and sent text and extract concrete differences: wording, length, tone, language, greeting, sign-off, what was cut, what was added, format (bullets or prose). Quote both in `evidence`.
- **Where each rule goes:** a general rule to `context/writing-style.md` under "Learned" (with one before/after example); a recipient-specific rule to that person's `context/people/<slug>/profile.md`, section "How I write to them"; a new or differently used term to `context/glossary.md` (see 1b).
- **Not sent:** for every draft with outcome `not sent`, note it and ask once whether the timing or the idea was wrong ("Wrong timing or wrong idea?"). Learn from the answer; never ask twice for the same draft.
- **Written without a draft:** also read 10-20 of the user's sent mails and chat messages from this week. Note recurring patterns per channel and language: openings, closings, length, bullets, language mix, words they use and words they never use.
- **Write after the page:** everything above is a proposal on the review page (section 7). Write a rule only after the user's Adopt, or their Adjust version. Not now stays in the queue.
- Never quote draft or sent text outside the workspace; the evidence on the review page is local.

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

## 3a. Audits (every review, whether or not there are tips)
Run all four audits in `routines/improve.md`: Area drift, ICE drift, People data, Context cards. Fix proposals join section 2's fixes as `fixes[]`; people and card repairs go under "Claude asks". An audit with nothing to report says so in one line.

## 4. Done patterns
How did the user close tasks this week? Propose updates to the done signals in `inbox/CLAUDE.md`.

## 5. Tip triage
For each open line in `meta/tips.md`, run `routines/improve.md` and show the verdict (adopt, backlog, discard) with the file it would change. Apply adopted ones only after the user says yes, then tick the line with the verdict and date.

## 6. Plan vs actual
- Show the week's totals and where unplanned work came from.
- Propose how much room next week's plan leaves.

## 7. Write the page

**Labels (required):** every item gets `priority` and `area`, and board items also `id` and `url` from the task store; the rules and the list of items are in `views/CLAUDE.md`, "Labels". The renderer prints `LABEL CHECK` for anything missing; fix it and render again.

Write `views/data/review-YYYY-Www.json` (schema: `views/CLAUDE.md`, "Review view") with the proposals from sections 1 to 6: `style[]`, `glossary[]`, `fixes[]`, `tips[]`, `routines_new[]`, `plan_actual`, `start_here`, `sources[]`. Leave out any "nothing is applied until you decide" sentence from `headline`: the page says it. Every proposal must carry a stable `id` (required: the page refuses to stage an item without one, and the renderer prints `LABEL CHECK` for it), `evidence` (`[{quote, source, link, when}]`: draft vs sent pair, friction lines, the tip's original message, repeated steps with dates), `impact` (one line) and `change` (`{file, before, after}`, the exact text). Render it with `python3 scripts/render_view.py views/data/review-YYYY-Www.json` and `open views/review.html`. The user decides on the page and pastes the `<<<REVIEW ... >>>` block; apply `adopt` lines, apply the user's `your version` for `adjust` lines (ask for it if missing), and leave `park` lines in the queue for the next review. In the next weekly view, set `last_review` (`{adopted, open, link: "review.html"}`).

Close: build the indexes, append to `log.md`, commit.
