# Research mapping

Reviewed primary sources on 2026-10-23. This maps ideas used or proposed in the private local prototype; the full implementation is maintained separately. It is not a claim to reproduce the original systems or their benchmark scores.

| Source | Mechanism | Application and limit in this project |
|---|---|---|
| [Simple-JEV](https://github.com/featherless-ai/simple-jev) | Turns an existing model endpoint into a structured classifier/scorer | Pinned source plus selected-label log probabilities; scores are preferences, not calibrated survival probabilities |
| [Reflexion](https://arxiv.org/abs/2303.11366) | Linguistic feedback retained in episodic memory instead of model-weight updates | Motivates outcome-bearing reflection; local candidate review is not a reproduced Reflexion benchmark or proof of online RL success |
| [Voyager](https://arxiv.org/abs/2305.16291) | Curriculum, reusable skills and iterative feedback without parameter fine-tuning | Motivates reusable conditional procedures and transfer tests; executable generated skills are not connected to this key executor |
| [JARVIS-1](https://arxiv.org/abs/2311.05997) | Memory-augmented multimodal planning with goal-conditioned control | Motivates experience-conditioned intent; its game/controller results cannot be transferred to this prototype |
| [VideoAgent](https://arxiv.org/abs/2403.11481) | Structured temporal/object memory queried for video understanding | Motivates timestamped visual working memory; QA performance does not establish better game detection |
| [AgentGarten](https://arxiv.org/html/2610.12374v2) | Code worlds, renderer and practice/playbook research | Inspires bounded post-segment playbook review; no renderer/world simulator is reproduced here, and candidate lessons do not auto-promote |

Closed-loop observation/action and fast/slow hierarchical control are engineering principles used to separate asynchronous semantic assessment from immediate current-geometry decisions. Short relative-motion forecasts resemble a bounded receding-horizon check; the project does not implement a learned world model or a full model-predictive controller with an identified dynamics model.

## Memory is several different mechanisms

- Short observation history supports object association and motion estimates.
- Gameplay experience stores observed action/outcome context and can supply bounded rank advice.
- A post-control reviewer produces source-linked candidate procedures, stored separately from live advice.
- Reviewer-error feedback is a distinct, default-OFF experiment after an unconvincing small pilot.

Gameplay Memory is ON by default in the UI; switch it OFF for baseline comparisons. More stored episodes do not establish stronger skill. The system has no justified scalar “brain intelligence” score or proven probability of winning. No Qwen weight fine-tuning is performed. Any limited local policy/table adaptation is separate from LLM training.

## Honest public terminology

Describe this as a hybrid vision-based computer-use agent prototype with memory experiments and human menu handoff. “Self-improvement” denotes a research goal evaluated with frozen held-out trials. Do not imply that every playthrough improves the model, that Simple-JEV is a second trained network, that all processing runs on GPU, or that a storage package itself supplies reinforcement learning.

Model-only, perception-only and full-agent comparisons answer different questions. See [the benchmark protocol](EXPERIMENTS.md) before reporting gains.
