---
name: documentary-brand-intro-producer
description: Create, revise, package, reuse, or QA premium short brand intros for YouTube crime, bodycam, investigative, and documentary channels. Use when Codex needs to build a recurring channel ident from narration, generated or filmed visual plates, post-produced typography, CTA, and structured music; compare equal-loudness score candidates; retime an approved intro; prevent pseudo-text, sub-second shots, or accidental black tail frames; or retrieve and integrate the canonical AFTER THE ALIBI brand master.
---

# Documentary Brand Intro Producer

## Operating rule

Treat the brand intro as a locked recurring asset, not a per-episode montage. Once
the producer approves a master, reuse the canonical file without rebuilding,
revoicing, recoloring, retiming, or replacing music unless explicitly requested.

For `AFTER THE ALIBI`, read `references/after-the-alibi.md` and use its canonical
master. Do not pull a file from an audition or working directory.

For a new or revised intro, read `references/workflow.md` and follow the complete
picture, voice, music, mixing, and version-lock procedure.

## Workflow

1. Define one brand promise and one short CTA.
2. Lock narration before generating picture.
3. Assign each complete clause one documentary action with a start state, visible
   change, and end state.
4. Generate or film picture plates without logos or readable typography. Add exact
   captions, wordmark, and CTA in post-production.
5. Lock picture duration and dialogue before generating music.
6. Generate at least three structurally different music candidates and compare
   complete picture-sync mixes at equal integrated loudness.
7. Choose by human listening. Prefer the least aggressive cue that still supplies
   forward pressure and a deliberate ending sting.
8. Package the approved master in a stable `brand/approved/` location with a
   manifest, checksum, duration, media specification, approval date, and source
   lineage.
9. Run `scripts/validate_brand_intro.py` on the canonical file.

## Hard gates

- Keep every information-bearing shot at least 1.5 seconds.
- Use people and observable documentary actions; do not fill the intro with empty
  rooms, blank files, generic microphones, or mood-only objects.
- Do not hide generated pseudo-text or anatomy defects with unexplained central
  blur. Regenerate, replace, or truthfully crop the plate.
- Keep narration, captions, picture cuts, word reveals, CTA, and music synchronized
  when changing speed.
- Extend persistent final title and CTA overlays through the exact encoded
  duration, not an independently rounded timeline value.
- Inspect the final three encoded frames. Reject a master that exposes a base
  plate, pseudo-text, black gap, player UI, or incomplete wordmark.
- Keep narration intelligible and preserve a true-peak margin.
- Do not call a cue approved without at least three equal-loudness picture-sync
  auditions and human listening.

## Delivery

Return the canonical master path, duration, checksum, approval state, and any
episode-integration timecode. Preserve working files separately from the approved
asset.
