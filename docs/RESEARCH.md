# Research concepts and local adaptations

This project adapts selected ideas. It does not reproduce the full cited systems, their training procedures or their published performance.

| Source | Concept used here | Implementation/evidence boundary |
|---|---|---|
| [Cradle: General Computer Control](https://arxiv.org/abs/2403.03186) | Observe screenshots and act through keyboard/mouse interfaces | Motivates the interaction setting. It does not establish this controller's real-time combat performance. |
| [MIRIX](https://arxiv.org/abs/2507.07957) | Visual and episodic memory organized for retrieval | Inspires source-linked visual cases. The full six-memory multi-agent system is not integrated. |
| [Reflexion](https://arxiv.org/abs/2303.11366) | Reflect on feedback and retain textual experience without changing model weights | Local lesson drafts remain candidates; reliable improvement and automatic promotion are unproven. |
| [Prioritized Experience Replay](https://arxiv.org/abs/1511.05952) | Experiences differ in potential information value | Local retention favors observed HP-change examples. It has no TD-error replay training or importance-sampling algorithm. |

Google's [EmbeddingGemma 2 model card](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2) supports the model choice for native image embeddings. Image similarity retrieves candidates; it is neither a calibrated safety probability nor proof that one action caused an outcome.

## Experimental reasoning

The project evaluates three different questions: whether a component works, how fast it runs, and whether it improves a gameplay outcome. A successful API, more memory records, a high cosine score or more software tests answer none of those other questions automatically.

Meaningful future comparisons require verified run groups, matched declared builds/difficulty/wave, reviewed retrieval relevance, and Memory-on/off outcome measurements. HP/material counters need clear observation scope; incomplete tokens and unverified pickups remain labeled as such.

## Focused image inspection and preview overlays

Region-of-interest crops isolate HUD or candidate-body areas, and local zoom supports a closer body/weapon inspection. The crop remains tied to its original screenshot; being inside a crop does not prove a player identity. Wrong crop selection and occlusion remain failure modes.

Control Room draws detection boxes, candidate targets and planned paths on a separate preview layer. This makes the controller's interpretation visible for debugging; the display markings do not supply new world evidence or replace the source screenshot. This is an engineering aid, not a measured accuracy improvement.

The published CPU replay speedup measures the combined pipeline. No controlled crop-only or overlay-only ablation establishes their individual latency, detection or gameplay effect.
