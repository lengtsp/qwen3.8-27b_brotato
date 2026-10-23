# Research notes behind the Facebook post

Primary sources checked on 2026-10-23. The Thai draft follows this sequence: problem/objective → closed-loop implementation → five research mechanisms → human handoff → evaluation → current evidence and project link.

| Source | Original mechanism | Attribution in the post |
|---|---|---|
| [VideoAgent, 2024](https://arxiv.org/abs/2403.11481) | Structured temporal events and object-centric tracking memory for video understanding | Motivation for timestamped short visual history; no reproduction or transfer of its video QA scores |
| [JARVIS-1, 2023](https://arxiv.org/abs/2311.05997) | Multimodal memory-augmented planning and goal-conditioned controllers in Minecraft | Motivation for experience-conditioned planning; original controllers/results are not transferred |
| [Reflexion, 2023](https://arxiv.org/abs/2303.11366) | Linguistic feedback in episodic memory without model-weight updates | Motivation for source-linked reflection; local reviewer output remains a candidate |
| [Voyager, 2023](https://arxiv.org/abs/2305.16291) | Curriculum, an executable skill library and iterative feedback in Minecraft | Motivation for reusable conditional procedures and transfer tests; generated code cannot enter the key executor |
| [AgentGarten, 2026, v2](https://arxiv.org/html/2610.12374v2) | Code worlds, neural rendering and practice rounds with written playbooks, especially Section 5.3 | Adaptation of bounded post-segment review and candidate playbooks; no renderer/simulator reproduction |

[Simple-JEV](https://github.com/featherless-ai/simple-jev) is the classification/scoring tool, listed separately from research papers. Closed-loop observation/action and asynchronous fast/slow control describe engineering structure; the post does not attribute them as new inventions of these five papers.

The post does not transfer published performance gains to this prototype. It distinguishes model classification, perception accuracy, pipeline latency and full-agent collection/HP/survival. A memory comparison must hold the controller/model fixed, declare uncontrolled RNG and separate practice from held-out evaluation. Existing exploratory observations establish neither a causal memory benefit nor improvement after every playthrough.

The checkpoint must be documented for model benchmarks; a local Qwen serving alias does not verify upstream provenance. The observed distribution was Epic Games Store; Steam remains unverified. Preview FPS is separate from reasoning/action latency. No Qwen fine-tuning is claimed.

The current [system figures](SYSTEM_DIAGRAMS.md) reconstruct specific historically executed native-control and memory-review tests, with dates, evidence IDs and prompts. The unexecuted held-out protocol remains a textual [research method](EXPERIMENTS.md), outside these figures. See the [evidence crosswalk](TESTED_SYSTEM_EVIDENCE.md) and [research mapping](RESEARCH.md).

## Techniques, functional changes and measured improvement

The Facebook draft distinguishes mechanisms in the private local prototype, historical synthetic behavior checks and measured replay timing. The public repository contains the research presentation and aggregates, not the full implementation. See [technique/evidence mapping](TECHNIQUES_AND_EVIDENCE.md). Intended benefits are not presented as measured score or survival improvements.

The only numeric speed comparison added is the existing [continuity replay aggregate](evidence/continuity-replay-continuity.json): scalar versus accelerated CPU median 123.20 → 78.52 ms, a reduction of approximately 36.27%; command interval median 145.406 → 100.994 ms; renewal-gap steps 14 → 0. Each mode recorded 25 steps with timing for 23. This was offline repeated-image replay with a memory-only input adapter, not a new live game run, model-inference benchmark or causal memory comparison. Do not combine these numbers with the separate acceleration microbenchmark.

Eight directions, retained objectives, alternative current paths and projectile crossing checks are capability changes. Their existence does not establish increased collection or HP retention. Player/weapon separation is an additional heuristic, not a measured detector accuracy gain. Reflection adds source-linked inspectability; it has no demonstrated positive gameplay effect in the available memory trial.

## Presentation versions

The post's **3,034,643-token** figure is the sum of attributable response receipts from **16 control segments**, across different Danger levels, repeated attempts and unknown-label records. It includes 3,034,168 input and 475 output tokens; it is not one full run or all historical gameplay. Proposal reuse does not create another inference count. [Accounting table and limitations](TOKEN_USAGE.md) · [Aggregate source](evidence/round-token-usage.json).

The concise [Facebook draft](FACEBOOK_POST_TH.txt) keeps the objective, major techniques, the existing offline CPU result, human handoff and evidence limits. The longer technical/research explanation is preserved in the [Thai project review](PROJECT_REVIEW_TH.md). Additional [system views](SYSTEM_DIAGRAMS.md) and [Danger/Wave ledger](WAVE_PROGRESS.md) provide detail in the research repository without distributing controller code.
