---
name: crime-documentary-producer
description: Build, revise, or QA evidence-led faceless crime documentaries from archival footage, interviews, emergency calls, surveillance, public records, stills, maps, and restrained reconstruction. Use when Codex needs to select a crime case for story potential; distinguish a raw chronology from an edited storyline; write a suspenseful but factual paper edit or narration; match voiceover to moving visuals; remove source captions and watermarks; design evidence graphics; review pacing, transitions, captions, sound, or authenticity; or update a self-learning crime-video production workflow from human feedback and YouTube results.
---

# Crime Documentary Producer

## Operating principle

Build the story from recorded behavior, contradiction, independent evidence,
and state changes. Do not substitute attractive cards, generic atmosphere, or
research caveats for story logic.

## Workflow

1. Audit the case package before scripting.
   - Require a strong recorded human moment, multiple evidence modes, at least
     three state changes, and a central question with an evidentiary payoff.
   - Separate primary sources, official releases, reporting, commentary, and reconstruction.
2. Write the raw chronology.
   - Record who claims each fact, when it became known, and what later evidence changed it.
3. Build the edited storyline.
   - Prefer: recorded statement/action → contradiction → central question →
     chronology reset → claim → independent test → narrowing → breakthrough →
     consequence → recontextualized opening.
4. Write narration by function.
   - Orient, connect cause and effect, distinguish claim from fact, interpret a
     state change, or open/close a question.
   - Delete description of visible action, production disclaimers, vague trailer
     language, and caveats that belong in labels or notes.
5. Create a semantic paper edit.
   - Plan by thought and state change, not equal-duration slots.
   - For every beat record audio, story function, source/timecode, picture,
     start/end state, cleanup, readable hold, and audio bridge.
6. Build the rough cut from moving evidence first.
   - Let consequential dialogue finish.
   - Keep relevant footage moving under narration.
   - Use J-cuts and L-cuts to connect spaces and evidence modes.
7. Add graphics only where they clarify evidence.
   - Prefer lower thirds, document highlights, route traces, tracked crops, and
     labels over full-screen slides.
8. Run source, relevance, authenticity, caption, sound, and export QA.
9. Log human feedback and published metrics before promoting a new permanent rule.

Read `references/story-and-paper-edit.md` before selecting or restructuring a case.
Read `references/visual-and-source-qa.md` before building or reviewing picture.
Read `references/music-and-sound.md` before generating, replacing, or approving
music for a cold open, brand ident, or episode.
Read `references/self-learning.md` when feedback or analytics should update the workflow.

## Hard rules

- Do not cut a raw speaker in the middle of a consequential sentence.
- Do not invent Western aliases for real people as a default editorial device.
- Do not show a second person merely because they are related to the subject being discussed.
- Do not introduce a clue without subject → discovery → anomaly → meaning.
- Do not use automatic micro-shake, fake handheld motion, or decorative zoom on stills.
- Do not use sub-1.5-second shots for information the viewer must identify or read.
- Do not leave unrelated source captions, Chinese text, broadcaster bugs, app UI,
  or another creator's overlays in the final frame.
- Do not use a full-screen title card when an overlay on relevant moving footage works.
- Do not alter a real person's mouth to fabricate speech. A translated-lipsync
  experiment is allowed only with explicit production-owner approval, a locked
  faithful translation, a non-imitative licensed voice, continuous on-screen
  labeling, and the post-render verification gate in
  `references/visual-and-source-qa.md`.
- Do not present generated footage as case evidence.
- Do not narrate long disclaimers; use precise visual labels, sourcing notes, or the description.

## Clue-writing gate

Reject:

`Then one clue seemed to explain everything: two tons of water.`

Require all four parts:

1. Who found or reported it?
2. What exactly was found?
3. Why was it abnormal?
4. What did it change, if anything?

If the record does not support one part, rewrite the line or remove the clue.

## Visual decision

Choose the highest available layer:

1. primary moving evidence or recorded speech;
2. primary still, photograph, or document;
3. verified location/context footage;
4. editorial crop, map, timeline, highlight, or diagram built from verified facts;
5. continuously labeled generic reconstruction;
6. atmosphere only for brief connective tissue.

The viewer must understand why the current image is on screen without an explanation from the editor.

## QA utility

Run:

```bash
python scripts/audit_video.py /absolute/path/to/video.mp4 --out /absolute/path/to/audit
```

Inspect the generated contact sheet, regular samples, and scene-change samples.
The script is an inspection aid, not a replacement for watching the export.

## Self-learning boundary

Treat one review comment as an observation, not universal law. Promote a rule
only when it is repeatable, actionable, and supported by multiple independent
observations or a strong professional reference set. Never change factual or
authenticity gates merely to improve engagement metrics.
