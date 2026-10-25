# Experimental resources and component roles

This is a research inventory, not a turnkey installation package or a minimum-hardware guarantee. A [beginner tutorial](TUTORIAL.md) explains installation and small teaching examples. Complete controller code, production prompts and deployment recipes are not distributed here.

| Resource | Role in the prototype |
|---|---|
| Windows game window and native capture/input bridge | Current screenshots and bounded keyboard transport |
| CPU | HUD/body/image processing, route checks, freshness, orchestration, SQLite and input delivery |
| Qwen3.8-27B-Uncensored-NVFP4 via [vLLM](https://github.com/vllm-project/vllm) | Local image/text inference and semantic scene/direction advice |
| [Simple-JEV](https://github.com/featherless-ai/simple-jev) | Bounded label/direction scoring through the resident model |
| [EmbeddingGemma 2](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2) | Native image embeddings for case retrieval |
| SQLite | Bounded historical cases and metadata |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Separate orchestration integration experiments; not a replacement for the fast native steering process |
| Human operator | Menu/build decisions and intervention |

Observed image-embedding hardware: NVIDIA RTX PRO 6000 Blackwell Workstation Edition, approximately 96 GiB VRAM. The encoder used BF16 text+vision with audio disabled and 768-dimensional vectors. Hardware capacity is not measured memory usage, and the published service latency was collected without concurrent Qwen inference.

Model weights, dependencies, the commercial game and their licenses are separate resources. They are not included in this repository.
