# Production workflow

## Stage 0 — Case feasibility

Do not greenlight from a case summary alone. Confirm that the public asset package
can support a story.

Required checks:

- At least one strong recorded human moment: interview, emergency call, interrogation, courtroom statement, confrontation, or family testimony.
- At least three independent evidence modes: moving footage, document, photograph, map/location, audio, surveillance, or official statement.
- At least three meaningful state changes: claim challenged, route closes, identity changes, search narrows, evidence appears, confession, ruling, or consequence.
- A central question that can be paid off with evidence.
- Enough usable, legally and editorially defensible material to avoid long filler sections.

## Stage 1 — Source ledger

Record each asset with:

- source URL and publisher;
- local path and checksum;
- capture date and access date;
- whether it is primary, secondary, commentary, or reconstruction;
- production permission/risk notes;
- visible source text, watermarks, captions, and privacy issues;
- exact useful ranges and what each range proves.

Commentary-channel uploads may help discover an asset, but the production ledger
should locate the original or official source wherever possible.

## Stage 2 — Raw story map

Write the event chronology without trying to entertain:

- verified fact;
- source;
- time;
- person making the claim;
- confidence;
- contradiction or unresolved gap.

Do not start the script until facts, claims, and later findings are separated.

## Stage 3 — Edited storyline

Reorder the raw story around viewer questions while preserving factual meaning.

Recommended structure:

1. Recorded statement or consequential action.
2. One fact that changes its meaning.
3. Central question.
4. Short brand punctuation.
5. Date/place chronology reset.
6. Suspect or witness claim.
7. Independent test.
8. First failed explanation or narrowing.
9. Escalation through new evidence modes.
10. Breakthrough and consequence.
11. Recontextualize the opening statement.

## Stage 4 — Narration pass

Every sentence must perform one function:

- orient;
- connect cause and effect;
- distinguish claim from fact;
- interpret a state change;
- open or close a question;
- compress time without hiding an essential step.

Delete narration that:

- merely describes the visible image;
- explains a production disclaimer;
- repeats a date already legible on screen;
- adds vague trailer language without subject, action, or meaning;
- states a suspicion as proof;
- summarizes the full case during the hook.

Clue sentences must pass:

> subject → discovery → anomaly → meaning

Bad: `Then one clue seemed to explain everything: two tons of water.`

Better: `Investigators later examined the apartment's water use and found an
unusual spike. The number became famous online, but it was only one part of a
much larger search.`

Use the second form only when the evidence ledger supports every clause.

## Stage 5 — Paper edit

Use `templates/PAPER_EDIT.md`. Segment by semantic beat, not arbitrary seconds.

For every beat specify:

- foreground audio;
- story function;
- visual evidence or atmosphere;
- source and exact timecode;
- start state and end state;
- why the viewer understands the connection;
- text cleanup and privacy work;
- minimum readable hold;
- transition audio bridge.

No shot enters the edit without a function.

## Stage 6 — Rough cut

- Build picture first from real moving sources.
- Let original consequential dialogue finish.
- Use L-cuts and J-cuts to move between evidence modes.
- Keep narration over moving footage when the footage remains relevant.
- Use a still only when the still itself is the evidence or emotional focus.
- Add graphics only after the underlying story cut works.

## Stage 7 — Graphics and reconstruction

- Prefer lower thirds, highlighted crops, route traces, document excerpts, and
  labels over full-screen cards.
- Keep exact text and typography in post-production, never inside a generated plate.
- Label reconstruction continuously and keep it visually distinct from source evidence.
- Never synthesize a real person's speech or lip movement in evidentiary footage.

## Stage 8 — Sound

- Original speech and room tone take priority.
- Use music as an evolving pressure curve, not an uninterrupted wallpaper loop.
- Duck music for low-level dialogue only when intelligibility requires it.
- Remove music before a crucial raw line or final factual sentence when silence adds weight.
- Use transition sound to connect spaces sparingly; do not decorate every cut.

## Stage 9 — QA and review

Run every gate in `docs/QA_GATES.md`. Generate a time-coded contact sheet and
listen to the entire export without watching once, then watch once muted.

## Stage 10 — Publish and learn

Archive title, thumbnail, description, restrictions, impressions, CTR, average
view duration, first-30-second retention, and audience comments. Log observations
in `learning/LEARNING_LOG.md` before changing permanent rules.
