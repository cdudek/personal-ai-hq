# context/

Memory. Read by every routine. Write only after the user says yes (see top-level rule 1).

- `me.md`: role, way of working, preferences
- `goals.md`: goals and OKRs, with pointers to the source docs
- `glossary.md`: terms, abbreviations, internal names. One line each: `**term**: meaning (source, date)`. Before adding: check plurals, acronyms, casing.
- `writing-style.md`: the voice file. Every drafting routine reads it. Changes only via `review` with approval; append a dated line to its "Learned" section.
- `places.md`: where files, repos and projects live. Read it before searching the disk.
- `people/`, `projects/`, `topics/`: one file per item, frontmatter required, link with `[[...]]`.

Pages are compiled from `sources/` and the inbox. Every fact links its source: `(source: [[sources/...]])` or `(<name>, YYYY-MM-DD)`.

Split a page when it passes about 800 words or covers two subjects. Create a subfolder when a folder passes about 30 files and has a clear cluster (e.g. `people/engineering/`); give the new subfolder its own CLAUDE.md.

Status `draft` means seeded by Claude and not yet confirmed by the user.
