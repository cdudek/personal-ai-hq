# meta/

Logs the learning loop reads. Append only.
- `friction.md`: `- YYYY-MM-DD <routine>: <what went wrong> -> <what the user wanted>`
- `drafts/YYYY/MM/YYYY-MM-DD.md`: the drafts ledger, one file per day, append-only. Sensitive: local only, never quoted outside the workspace. Entry:
  ```
  ## HH:MM <channel> to <recipient> · id: d-YYYYMMDD-HHMM-<n>
  thread: <deep link, if known>
  task: <task link, if any>
  <the draft text>
  outcome: <sent as is | edited | rewritten | not sent | replied by <name>> · <link to the sent message or reply>
  ```
  The draft text never changes. `outcome:` lines are the one allowed append to an old entry, written only by the daily outcome check (`routines/brief.md` step 0b) and read by the Friday review. Logging rule: `CLAUDE.md` rule 6.
- `plan-vs-actual.md`: per day planned, done, unplanned (with source)
- `learnings.md`: rules adopted by `review`, with date
- `tips.md`: queue of suggestions for the system (tips, tools, colleague ideas), evaluated every Friday by `review` via `improve`
- `chat-cursor.md`: timestamp of the last self-DM message processed
