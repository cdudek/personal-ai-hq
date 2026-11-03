# routines/

One file per routine. Each file is the full instruction a run follows. Scheduled tasks say only: "Follow routines/<name>.md".

Every routine ends with the same three steps:
1. `python3 scripts/build_index.py`
2. Append one line to `log.md`.
3. `git add -A && git commit -m "<routine>: <date>"`.

Changes to these files come only from `review` proposals the user approves, or from the user directly. Every routine has a "Friction" section: when the user corrects the routine, log it to `meta/friction.md`.
