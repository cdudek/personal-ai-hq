---
type: topic
summary: Everything that needs the user's action now - PRs, ticket mentions, mails and chat messages waiting for an answer
status: draft
updated: {{SETUP_DATE}}
---

# Routine: radar (what needs me?)

Use it inside `brief` and `sync`, or on its own any time ("Follow routines/radar.md"). It only reads; nothing is written to the task store without confirmation. Skip every source the tool routing marks "none"; say which were skipped. Run on its own (`/hq:inbox`), it starts with "Required sources" in `CLAUDE.md`; inside `brief` or `sync` that check has already run.

## 1. Code: pull requests that need the user

Source: the code connector. Without it, fall back to the `gh` CLI. If neither works, say so.

**Own open PRs** (author = the user, not draft) need action when one of these holds:
- review decision is CHANGES_REQUESTED
- checks failed
- merge state is DIRTY (conflict) or BEHIND
- unresolved review comments whose last comment is not the user's
- approved and CLEAN but not merged (action: merge, or arm auto-merge)
- open more than 7 days with no review (action: ping a reviewer)

**Review requests:** PRs where the user's review is requested and they have not reviewed since the last push.

With `gh`:
```bash
gh search prs --author=@me --state=open --json url,title,repository,isDraft,updatedAt
gh pr view <url> --json reviewDecision,mergeStateStatus,statusCheckRollup,comments,latestReviews
gh api graphql -f query='query($o:String!,$r:String!,$n:Int!){repository(owner:$o,name:$r){pullRequest(number:$n){reviewThreads(first:50){nodes{isResolved isOutdated comments(last:1){nodes{author{login} createdAt url}}}}}}}' -f o=<owner> -f r=<repo> -F n=<number>
gh search prs --review-requested=@me --state=open --json url,title,repository,updatedAt
```

## 2. Tickets: mentions and issues that need the user

- Notifications that mention the user and are unread or unanswered. Unanswered means the user has not commented in that ticket since the mention.
- Comments on tickets assigned to the user, created by someone else, after the user's last comment.
- Tickets assigned to the user that are due within 7 days or overdue.

## 3. Mail: mails that need an answer

Inbox mode is "new only" (see `CLAUDE.md`). A mail needs an answer when all of these hold:
- From a person. Not a newsletter, notification, calendar invite, receipt, or `noreply`.
- The user is in To, or in Cc and named in the text.
- It asks a question, a request or a decision of the user.
- There is no reply from the user later in the thread.

Older than "new only" counts only if it is starred or flagged.

## 4. Chat: messages that need an answer

- DMs and group DMs where the last message is not the user's and it asks something.
- Mentions of the user in threads where they have not replied since.
- Saved messages (saved = open).

## 5. Tasks tool: tasks that need the user

- Tasks assigned to the user, not completed, due within 7 days or overdue.
- Tasks where someone mentioned the user in a comment after their last comment.
- Tasks the user follows where the latest comment asks them something.

Each task is its own line with its own link. Many overdue tasks: list each one; never one line pointing at a task list.

## 6. Waiting on others (the user asked, nobody answered yet)

The other direction: things the user sent that still wait for someone else. Only the last 14 days.

- **Mail:** mails the user sent to a person that ask a question, a request or a decision, with no reply after 2 working days.
- **Chat:** the user's DMs and thread messages that ask something, with no reply after 1 working day.
- **Code:** the user's PRs waiting more than 24 hours for a first review (name the requested reviewer).
- **Tickets:** comments where the user asked someone, with no reply after 2 working days; tickets the user created or assigned to someone else that are overdue.
- **Tasks tool:** tasks the user assigned to someone else that are overdue.

Each line: who the user waits for, what they asked (short quote), since when, deep link. Suggested next step: "nudge <name>" (offer a draft) or "drop it". A line disappears as soon as the answer arrives. These are not tasks in the task store.

## People (every source)

Resolve every person in a line through `context/people/` ids (`routines/people.md`, "Matching people elsewhere"): code reviewers and authors, chat authors and DM partners, ticket commenters, mail senders, task assignees. Name them as in the profile. No match: the name as the source shows it, never a guess, and it is a context-gap candidate for the brief.

## Deep links (every line, every source)

Every item links to the exact thing, so one click opens it. Take the URL the connector returns; never build a list or inbox URL instead.

- **Code hosts:** the PR or issue URL; a review comment adds `#discussion_r<id>`, an issue comment `#issuecomment-<id>`.
- **Ticket trackers:** the issue URL; a comment adds its anchor. Project and initiative URLs for status items.
- **Mail:** the thread URL, not the inbox. With several accounts signed in, include the account in the URL.
- **Chat:** the message permalink; a thread reply adds the thread parameters. Never a bare channel or DM URL.
- **Task tools:** the task's permalink.
- **Calendar:** the event link. Meeting transcripts and notes: the doc URL.

Also keep the identifier itself (`repo#123`, `PROJ-45`, thread id, task id) in the item: `key` in the view data.

One thing per line: "4 review requests" becomes 4 lines, each with its PR link.

## Output

One list, sorted by urgency. Order: blockers first, then items older than 2 days, then the rest.

```
## Needs me (N)
- [Code] <repo>#<n> <title>: changes requested by <name>, 2 days -> fix and re-request review  <link>
- [Tickets] <KEY-123> <name> asked "<short quote>" -> answer  <link>
- [Mail] <sender>: "<subject>" asks for <decision> -> reply  <link>
- [Chat] <name> in <channel/DM>: "<short quote>" -> reply  <link>
- [Tasks] <task> (<project>): <name> asked "<short quote>" / due <date> -> <next step>  <link>
```

Then a second list, "Waiting on others (N)", in the same format, from section 6.

Each line names the source, who is waiting, what they need, a suggested next step and a link. Offer to draft the replies (with `context/writing-style.md`; every draft goes to `meta/drafts.md`). Each line also carries the What sentence, the State with dates, who waits since when and the effort (the task's context card when the item is a task). An item that arrives as a bare link is opened and read first, then written up; it is never listed as a name or number alone.

## Friction
When the user corrects anything in this routine, append to `meta/friction.md`: `- YYYY-MM-DD radar: <what went wrong> -> <what they wanted>`.
