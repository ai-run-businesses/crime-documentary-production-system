# Documentary brand intro workflow

## 1. Brand promise and duration

Write a 12–16 second promise that tells the viewer what the program does, followed
by a short CTA. Avoid slogans that could belong to any crime channel.

Use this functional sequence:

1. premise or contrast;
2. program method;
3. editorial payoff;
4. brand name;
5. CTA.

Narration must fit at a YouTube pace without rushed consonants. If the picture is
approved but the segment feels slow, retime the entire locked unit so picture,
voice, captions, typography, CTA, and music remain synchronized.

## 2. Visual action plan

Assign each complete clause one visual job. Favor staffed and observable actions:

- recording begins;
- investigators compare surveillance;
- an interview subject reacts while framed without a host face;
- a court record changes hands;
- a dossier reveals a marked fact;
- the wordmark resolves.

For every plate specify start state → action → end state. Reject empty rooms,
blank files, generic waveform screens, decorative push-ins, pseudo-text, and shots
shorter than 1.5 seconds.

Generate clean picture plates without exact text. Add captions, wordmark, red rule,
and CTA in post so typography is stable and reusable.

## 3. Voice and captions

- Keep one recurring narrator voice and a consistent performance direction.
- Write for complete spoken clauses and natural breath groups.
- Caption all narration unless the established brand system explicitly omits it.
- Align caption entry and exit to the final voice render, not the draft script.
- When accelerating, use a high-quality tempo change and retime every visual and
  text event by the identical factor.

## 4. Structured music

Lock picture and voice first. Ask for audible behavior rather than only `dark
cinematic suspense`:

- BPM or pulse range;
- full pressure on frame one or a deliberate delayed entry;
- rhythmic engine and instrumentation;
- short repeatable warning/evidence motif;
- density changes every few seconds;
- exact final sting and controlled tail;
- negative list excluding ambient drift, corporate uplift, piano sentiment,
  heroic police scoring, literal sirens, vocals, dance-pop, arbitrary fades, and
  giant trailer impacts.

Generate at least three different concepts, for example:

- forensic pulse;
- psychological testimony clock;
- denser evidence-lock rhythm.

Normalize the complete picture-sync auditions to the same integrated loudness.
Approximately -15 to -17 LUFS with true peak below -1 dBFS is a practical review
range. Select by human listening, not prompt text or standalone loudness.

## 5. Mix and ending

Protect the 1–4 kHz narration band with arrangement, EQ, or restrained music level.
Intensity comes from rhythmic pressure, not excessive loudness. The authored music
ending must land on the resolved wordmark/CTA; do not cut mid-bar or add an arbitrary
fade.

Persistent final overlays must last through the exact encoded duration. Timeline
rounding can otherwise expose one or two unintended base frames after the CTA.

## 6. Approval package

Separate:

- working plates and generation requests;
- equal-loudness auditions;
- selected music source;
- final canonical master;
- QA outputs;
- JSON manifest.

The manifest must record approval status, source master, canonical path, duration,
codec/resolution/frame rate/audio specification, checksum, selected cue, and final
frame QA result.

Run:

```bash
python scripts/validate_brand_intro.py /absolute/path/to/master.mp4 --out /absolute/path/to/qa
```

Then watch the complete export once with sound and inspect the last three encoded
frames at original resolution.
