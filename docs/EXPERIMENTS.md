# Benchmarks and evidence limits

This project separates model assessment from full agent performance. The public evidence consists of selected aggregates and descriptions of historical synthetic/mocked checks. Full implementation and tests are maintained separately. Raw captures and operational calibration data remain local.

## Exploratory memory observations

Recorded on 2026-10-18 with the same starting build in an early-wave local task. Encounter RNG was not controlled. There was one completed trial per condition in each comparison. The current planner and newer body/projectile changes were not used.

| Trial | Advice | In-combat counter gain | Final HP | CPU median ms | Source-to-ACK median ms | GPU proposals applied |
|---|---|---:|---:|---:|---:|---:|
| A baseline | Off | 22 | 16/16 | 113.115 | 192.151 | 0 |
| A memory | On | 17 | 16/16 | 112.980 | 192.646 | 0 |
| B baseline | Off | 25 | 16/16 | 115.790 | 183.775 | 1 |
| B memory | On | 23 | 16/16 | 125.985 | 208.504 | 0 |

These observations do not establish a memory benefit, a causal memory penalty or improved vision accuracy. The B baseline includes one applied GPU proposal. Unknown RNG and one trial per condition prevent controlled causal interpretation. The counter metric uses the last verified in-combat reading minus its start; post-wave effects are excluded. Counter change is not independently verified unique pickup count. ACKs are not proof of displacement. See [selected aggregates](evidence/wave1-memory-summary.json).

## What to benchmark

| Layer | Metrics | Controls needed |
|---|---|---|
| Model classifier | Scene/direction label accuracy, abstention, valid structured output, inference p50/p95 | Same held-out observations, model revision, prompt, scoring policy and image dimensions |
| Visual perception | Controlled-body localization error, object precision/recall, HUD accuracy, identity switches | Human annotations and confidence/unknown labels; synthetic tests alone are insufficient |
| Control pipeline | Capture age, decision/planning time, dispatch/ACK latency, renewal gaps and verified idle time | Common clock/reference definitions and identical capture/input settings |
| Full agent | Completion/death, collection-counter change, HP retention and visible backlog | Comparable character/build/task, geometry and randomized trial order; unknown seeds declared |
| Memory | Baseline versus advice; retrieved/used lessons, changed final actions, adverse outcomes | Frozen controller/model; separate practice/evaluation episodes; no test-set feedback leakage |
| Resources | CPU, GPU/VRAM, working set, Private memory and storage growth | Fixed workload and measurement interval; alerts are not OS memory caps |

Report p50/p95, sample sizes, missing readings and uncertainty intervals. Do not equate preview FPS with action rate or model reasoning speed. Latency under 1 ms for one helper is not sub-millisecond end-to-end control.

The [model evaluation card](evidence/model-evaluation-card.json) records dataset/model/prompt revisions and separates scene accuracy, abstention, acceptable-action-set agreement and inference latency. Its null fields are unmeasured, not zeros or successful results. Direction labels can have several acceptable answers, so a single human arrow is not always valid ground truth.

## Planned evaluation

1. Freeze code/model/prompt, current perception, input transport and geometry.
2. Separate learning episodes from held-out evaluation. Randomize or counterbalance memory ON/OFF and model variants; document uncontrolled RNG.
3. Use the same task/build constraints and preserve before/last-combat/terminal readings locally with provenance.
4. Compare the metric vector rather than maximizing collection while hiding deaths.
5. Check transfer to new appearances, layouts and task contexts separately from repeated-task practice.
6. Promote a proposed procedural lesson only after independent evidence and adverse-case testing. No current candidate auto-promotes.

## Historical validation context

The prior private-source validation included synthetic projectile tests covering crossing trajectories before stationary-player contact is imminent, ambiguous matching, source expiry and uncertain-body margins. Fake native-input tests exercised expiry and CPU/GPU handoff contracts without touching a game. These checks established specified software behavior, not a live survival gain.

The original optional Hy-Memory experiment established extraction/retrieval feasibility outside the action hot loop. It did not establish better collection, better perception or a trained policy. GPU proposal acceptance is also separate from visual execution success.

Older aggregate timing files remain examples of measurement definitions; they are fixture/version-specific, not a leaderboard of current model capabilities. The archived screenshot is an interface illustration only.
