# Crime Documentary Production System

An evidence-led workflow for producing faceless crime documentaries from public
records, archival video, interviews, surveillance, stills, maps, and restrained
reconstruction.

The system was created after a failed proof exposed a recurring production
problem: assembling facts and attractive cards is not the same as telling a
crime story. The workflow therefore starts with story tension and evidence,
then assigns each spoken beat a moving, relevant visual.

## Non-negotiable principles

- Story before timeline: build claims, contradictions, tests, reversals, and payoffs.
- Evidence before decoration: real footage and records outrank generic atmosphere.
- Let recorded human speech finish; never cut a hook in the middle of a thought.
- Use narration to bridge missing logic, not to repeat the picture or recite caveats.
- Keep the frame alive under narration unless a still or document is itself the evidence.
- Never present generated imagery as case evidence.
- Remove or editorially reframe source captions, watermarks, and unrelated UI.
- Do not invent Western aliases for real people in a factual documentary.
- Do not use full-screen presentation cards as the default way to communicate facts.
- Every user correction and published-video result can improve the system, but a
  single observation is logged before it is promoted into a permanent rule.

## Repository map

- `docs/GOLDEN_SET_FINDINGS.md` — observed grammar from professional references.
- `docs/PRODUCTION_WORKFLOW.md` — end-to-end production stages and gates.
- `docs/VISUAL_GRAMMAR.md` — how footage, evidence, text, maps, and reconstruction behave.
- `docs/QA_GATES.md` — editorial, visual, audio, source, and export checks.
- `templates/PAPER_EDIT.md` — shot-level planning template.
- `learning/LEARNING_LOG.md` — observations and rule-promotion history.
- `skills/crime-documentary-producer` — installable Codex skill.
- `skills/documentary-brand-intro-producer` — creates, locks, reuses, and QA-checks
  recurring documentary channel intros.

## Current reference set

- CBS `48 Hours`: *The Setup Murder of Kristil Krug*.
- `60 Minutes Australia`: *Why did Henri van Breda murder his family?*
- Explore With Us: *Detective Realizes The Witness Is Actually The Killer*.
- MrBallen strong/weak samples were also inspected for hook specificity, but the
  presenter-led format is not part of the current faceless production system.

Only analyses, manifests, rules, and original tooling belong in this repository.
Downloaded copyrighted reference videos do not.
