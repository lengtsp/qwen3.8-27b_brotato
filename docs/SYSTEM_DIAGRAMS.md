# Systems with recorded execution evidence

These figures show **specific historical executed paths**, with dates and evidence IDs. They replace conceptual figures that included an unexecuted evaluation protocol. They do not claim a new integrated test of every current feature.

## Accessible overview in Thai

![Accessible Thai workflow overview grounded in recorded historical tests](assets/workflow-overview-th.png)

One illustration for a general audience: observe pixels, plan a pickup route, send a short arrow command and inspect the result. Human menu choices and experimental memory are shown separately. The CPU/GPU caption retains the native test's zero-admitted-GPU-steering limitation, and the footer states that these are separate historical tests. It does not demonstrate an automatic learning benefit. [Prompt](assets/workflow-overview-th-prompt.txt) · [Evidence](TESTED_SYSTEM_EVIDENCE.md)

## Native game-control path

![Recorded native path: CPU movement, model assessments and explicit zero admitted GPU directions](assets/tested-control-system.png)

**NATIVE-01 · Danger 2 / Wave 1 · 2026-10-19.** Capture, CPU perception/planning, current-source validation and scoped native arrow transport executed in the retained test: **225 command ACKs**, **211 distinct source frames**. Historical visual review found changing floor/body positions and completion HP **16/16**.

The model branch executed **26 GPU assessments**. Initial scene context was used; **zero GPU steering directions applied** because of source age. CPU paths supplied movement. This is not per-key displacement verification or proof of autonomous full-wave coverage. Menus were left for the human.

[Evidence/timing](TESTED_SYSTEM_EVIDENCE.md) · [Scalar manifest](evidence/tested-system-evidence.json) · [Generation/correction prompts](assets/tested-control-system-prompt.txt)

## Executed memory experiments

![Two separate executed memory experiments: four gameplay trials and four archived-segment model requests](assets/tested-memory-experiments.png)

The upper lane is **GAMEPLAY-MEMORY-01 · 2026-10-18**, four completed gameplay-advice trials. Baseline/advice counter gains were **22/17** and **25/23**; final HP **16/16** throughout. RNG was unknown, with one observation per condition per comparison. These trials predate the current planner.

The lower lane is **ARCHIVE-REVIEW-01 · 2026-10-23**, two archived segments and four real Qwen review requests with reviewer feedback OFF/ON. Three outputs were empty; one candidate needed revision and was not promoted. There were **zero policy promotions and no game input**. Reviewer feedback and gameplay advice are distinct.

**Gameplay benefit from memory remains unestablished.** No candidate-to-live arrow, training loop or unexecuted held-out pipeline appears in the figure. [Evidence/limits](TESTED_SYSTEM_EVIDENCE.md) · [Prompt](assets/tested-memory-experiments-prompt.txt)

## Image provenance

All three diagrams were made with the built-in image generation tool on 2026-10-23 from reviewed reports and scalar observations, then visually checked. The native diagram received a narrow correction to its container label, model-input connector and records caption. These are explanatory reconstructions, not original-run screenshots or official game artwork. No game sprites or private reference catalogs are included.

The separate [archived interface screenshot](assets/control-room-live.png) does not show that all UI features were exercised in these tests. [Architecture](ARCHITECTURE.md) · [Research](RESEARCH.md) · [Danger/Wave ledger](WAVE_PROGRESS.md) · [Installation](INSTALLATION.md)
