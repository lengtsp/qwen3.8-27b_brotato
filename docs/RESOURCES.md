# Resource context of the local prototype

This is experimental context, not an installation guide. The operational code, agent policies, templates and private datasets are maintained separately from this research showcase.

| Resource | Role | Reproducibility limitation |
|---|---|---|
| User-owned Windows game installation | Interactive visual task | Observed distribution: Epic Games Store; Steam unverified |
| Selected-window capture worker | Frames, geometry and original timestamps | Transport and capture settings affect latency |
| CPU / Python / NumPy | HUD/body/object estimates, geometry, route planning and input validation | CPU timing is not model inference time |
| GPU / separately served vision-language checkpoint | Asynchronous semantic assessment via vLLM | Record actual checkpoint/revision, precision, context and concurrent load |
| Simple-JEV | Structured classification and scoring of selected labels | Adapter/prompt/tokenizer compatibility affects comparisons; no second model |
| Local disk / SQLite | Bounded experience, aggregates and candidate review | Raw memory databases and session traces are private |
| Browser Control Room | Preview, overlays, decision history, Chat and RAM telemetry | Preview FPS differs from decision/action frequency |
| Human operator | Build/menu choices and clarification | Scope and intervention frequency affect full-agent outcomes |

No universal hardware minimum, VRAM requirement or FPS guarantee is established. A local Qwen serving alias is not sufficient checkpoint provenance. RAM alert thresholds are monitoring values, not an operating-system allocation cap.

For a model comparison, record model revision and quantization, prompt/scoring policy, image dimensions, context length, warmup treatment, device/load, timeout and source-clock definitions. For full-agent comparisons, also hold perception, planner, capture, input, build/task and human intervention scope comparable. Unknown values must remain unknown.

See [benchmark protocol](EXPERIMENTS.md) and [model evaluation card](evidence/model-evaluation-card.json). Reproducing the entire local controller from this repository alone is not supported by the published materials.
