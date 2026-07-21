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
