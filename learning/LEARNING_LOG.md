# Learning log

Rules are not changed silently. Record the observation, its evidence, and whether
it should remain a case-specific fix or become a reusable production rule.

## Promotion policy

- `Observed`: one user review, one reference, or one analytics result.
- `Candidate`: repeated in at least two independent observations or strongly supported by a professional reference set.
- `Promoted`: repeatable, actionable, and not contradicted by stronger evidence.
- `Retired`: later evidence shows the rule is harmful or too broad.

| Date | Observation | Evidence | Scope | Confidence | Status | Resulting change |
|---|---|---|---|---|---|---|
| 2026-07-21 | Static PPT cards interrupted the story and looked amateur | EP01 human review; golden-set comparison | Visual grammar | High | Promoted | Moving evidence under narration; full-screen cards become rare punctuation |
| 2026-07-21 | One-second identity/evidence images could not be understood | EP01 human review | Pacing | High | Promoted | Minimum information-shot duration rules added |
| 2026-07-21 | Default micro-zoom on stills felt artificial | EP01 human review | Motion | High | Promoted | Ban automatic movement; require information reveal or true hold |
| 2026-07-21 | Raw Chinese captions and source bugs survived into master | EP01 human review and frame audit | Source QA | High | Promoted | Source-text gate made mandatory |
| 2026-07-21 | “Two tons of water” lacked who, discovery, and meaning | EP01 script review | Writing | High | Promoted | Clue sentence schema: subject → discovery → anomaly → meaning |
| 2026-07-21 | Narrated research caveats damaged momentum | EP01 human review | Writing | Medium-high | Candidate | Move necessary caveats to precise labels, records, or description |
| 2026-07-21 | Digital presenter increases performance and uncanny-valley risk | MrBallen study plus model review | Format | Medium | Observed | Pause presenter-led format; continue faceless system |
| 2026-07-21 | A clean source in-point hid an unrelated visual near the out-point | EP01 v6 contact-sheet review | Source QA | High | Promoted | Inspect the final second of every excerpt before approval |
| 2026-07-21 | Source-burned English subtitles appeared only after the interview subject began speaking and collided with narrator captions | EP01 v6 targeted frame review at 01:10–01:13 | Caption QA | High | Promoted | Multi-frame caption handoff check; crop/reframe or replace the source shot |
| 2026-07-21 | Subject lower-third and program caption were independently correct but collided in the composite | EP01 v6 portrait review | Composite QA | High | Promoted | Collision-test lower-thirds, captions, and source-native text in the rendered frame |
| 2026-07-21 | Automated video QA confidently misidentified verified people and misunderstood intentional evidence juxtapositions | EP01 v6 Fal review compared with the fact ledger and source frames | AI QA | High | Promoted | Treat model QA as issue discovery; adjudicate identity and factual claims against verified sources before editing |
| 2026-07-21 | “Faceless channel” was incorrectly interpreted as removing approved case-participant dubbing, lip-sync, and narrative aliases | EP01 producer correction after v6.2 | Format semantics | High | Promoted | Define faceless as no recurring on-camera host; preserve explicitly approved labeled dubbing and aliases |
| 2026-07-21 | A 0.267-second orphan shot survived because a splice crossed an internal source cut | Brand intro v4 producer frame review; scene changes at 02.033 and 02.333 | Edit QA | High | Promoted | Detect internal scene cuts inside every selected range and reject accidental sub-1.5-second information shots |
| 2026-07-21 | Blurring generated pseudo-text created an unexplained censorship block | Brand intro v4 recorder shot producer review | Generative QA | High | Promoted | Regenerate or reframe defective generated plates; do not hide central artifacts with a conspicuous blur patch |
