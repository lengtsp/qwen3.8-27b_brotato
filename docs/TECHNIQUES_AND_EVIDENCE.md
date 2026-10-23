# Techniques and what has improved

This document maps concepts to evidence while the full local implementation remains private. Capability descriptions and historical synthetic checks are separate from measured gameplay gains.

| Technique | Problem addressed and capability described | Evidence boundary |
|---|---|---|
| Asynchronous fast/slow control and latest-observation replacement | Continue checked local actions between model answers without an unbounded outdated-frame backlog | Architecture of the local prototype; no new isolated GPU-speed result |
| Goal commitment / hysteresis, grid search with retained-goal A*, current main/backup intent | Keep a collectible objective while checking detours and alternate immediate legs | Local functional design and historical synthetic checks; increased live collection remains unproven |
| Temporal association and short projectile-path prediction | Consider a projectile crossing the intended path before stationary-player contact is imminent | Historical synthetic crossing checks; ambiguous observations supply no invented velocity; no live HP gain established |
| Weapon-independent body evidence | Add body/outline cues so weapon position need not determine actor center | Narrow local heuristic; no published universal-detector precision/recall gain |
| Eight-direction arrow chords | Add diagonal action choices and matching visual plans | Capability change; more directions do not establish a better score |
| Bounded contextual retrieval and source-linked candidate reflection | Inspect the source of advice while keeping untested procedures separate | Local memory/review mechanisms; existing observations establish no positive gameplay effect |
| NumPy vectorization and horizontal-run connected components | Reduce Python per-pixel queue work while retaining geometric outputs | Existing whole-pipeline offline comparison below; not an isolated model benchmark |

## Existing measured CPU / continuity result

The historical comparison replayed recorded imagery with a memory-only input adapter. Each mode recorded 25 steps, with timing for 23. This is interpretation of an existing [aggregate](evidence/continuity-replay-continuity.json), not a new experiment. The full source and raw captures are not distributed in this showcase.

| Metric | Scalar mode | Accelerated mode |
|---|---:|---:|
| CPU time median | 123.20 ms | 78.52 ms |
| Command interval median | 145.406 ms | 100.994 ms |
| Renewal gap median | 5.407 ms | 0 ms |
| Steps with a recorded renewal gap | 14 | 0 |

CPU median decreased by approximately **36.27%**: `(123.20 - 78.52) / 123.20`. This is a latency reduction in this CPU/replay comparison, not a 36% model inference speedup, a guarantee of current live continuity or a collection/survival gain. Confidence intervals and a generalized hardware effect are not established by these selected aggregates.

## Gameplay and memory remain separate questions

Exploratory memory conditions recorded less collection-counter gain than their corresponding baselines (17 versus 22; 23 versus 25), with final HP 16/16 in all four observations. Unknown RNG, one trial per condition and one applied GPU proposal in one baseline prevent causal conclusions. Those trials predate the current local planner. [Methods](EXPERIMENTS.md) · [Memory aggregates](evidence/wave1-memory-summary.json)

A claim that memory or a model improves play requires repeated held-out trials with comparable perception, planner, task/build, capture, input and human intervention. Report model accuracy, counter change, HP/survival, idle time and source-to-input latency separately.
