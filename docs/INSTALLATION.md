# Game-control installation requirements and upstream projects

This inventory covers the **Brotato game-control prototype**. The public repository contains presentation material and benchmarks; its private controller, Windows input bridge, configuration and skills must also be available to operate the complete system. Installing upstream projects alone does not install Control Room.

Local dependency manifests, installed backend packages and selected upstream documentation were inspected on **2026-10-23**. This is a dependency audit, not a fresh clean-machine installation test. Document processing and document RAG are outside its scope.

## Machines and resources

| Location | What to prepare | Purpose |
|---|---|---|
| Windows game host | User-owned Brotato, Windows Python and a selected game window | Game, native capture and scoped keyboard input |
| Linux / WSL backend | Git, Python environments and the private controller | Control Room, CPU image processing, routes and measurements |
| Model host | Compatible GPU/driver stack, vLLM and separately obtained vision-language weights/tokenizer | One resident model endpoint; may share the Linux host |
| Browser | Modern browser with WebSocket support; WebRTC for that preview mode | Preview, overlays, decisions, chat and telemetry |
| Disk | Space for weights, bounded records and SQLite experience storage | No external vector database is required for the core local gameplay store |

Native observations came from **Epic Games Store**; Steam compatibility is unverified. No universal RAM, VRAM or FPS minimum is established. Precision, context, concurrency and other GPU workloads affect requirements. CPU perception/input and GPU inference are separate workloads.

## Main upstream components

| Component and source | What is used | Installation and local evidence |
|---|---|---|
| [windows-capture](https://github.com/NiiightmareXD/windows-capture/tree/main/windows-capture-python) | Windows Graphics Capture observations | Install its Python package **on Windows**. Native-worker manifest pin: `windows-capture==2.0.1`. [Python setup](https://github.com/NiiightmareXD/windows-capture/blob/main/windows-capture-python/README.md). |
| [vLLM](https://github.com/vllm-project/vllm) | Resident model serving | Separate model environment/container; follow the [official GPU setup](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/). Record engine version/image digest and driver. This publication does not establish a pinned portable engine installation. |
| [Simple-JEV](https://github.com/featherless-ai/simple-jev) | Prompt preparation and selected-label scoring | The local adapter imports upstream `common` helpers and queries the **existing vLLM model**. It does not run the upstream HF server or load a second model. Inspected checkout: `b02aa81c915a8193759b3cd33fef74721d6e005b`. |
| [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Higher-level assistant/planning turns | Separate editable environment; observed **0.21.3**, source pin `3d0bdce9f92845696233d2bc569e7f521b3ef3f3`. Restricted local tool profile. Hermes is not called per keyboard pulse. |
| Vision-language weights and tokenizer | Image interpretation/scoring | Obtain separately from a verified publisher. `Qwen3.8-27B-Uncensored-FP8` was a **local serving alias**, not verified upstream provenance. Record actual checkpoint revision and quantization for model benchmarks. |

Simple-JEV supplies classification/scoring, Hermes orchestration, and vLLM model serving. None supplies this project's complete game controller. GPU inference does not imply accepted GPU steering; see [NATIVE-01](TESTED_SYSTEM_EVIDENCE.md).

## Backend and preview packages

These versions were queried from the existing **Linux controller environment**. They are an inventory, not a lockfile for every historical trial.

| Package | Observed version | Role and source |
|---|---|---|
| Python | 3.13.15 | Backend runtime; separate environments are used |
| FastAPI | 0.141.1 | API/UI backend — [source](https://github.com/fastapi/fastapi) |
| Uvicorn | 0.53.0 | ASGI server — [source](https://github.com/encode/uvicorn) |
| HTTPX | 0.28.1 | Service requests — [source](https://github.com/encode/httpx) |
| jsonschema | 4.26.0 | Output validation — [source](https://github.com/python-jsonschema/jsonschema) |
| Pillow | 12.3.0 | Image preparation — [source](https://github.com/python-pillow/Pillow) |
| NumPy | 2.4.3 | CPU pixels/geometry — [source](https://github.com/numpy/numpy) |
| aiortc | 1.14.0 | WebRTC preview — [source](https://github.com/aiortc/aiortc) |
| PyAV | 16.1.0 | Video frames/codecs — [source](https://github.com/PyAV-Org/PyAV) |

The separate **Windows worker manifest/setup notes** specify Python 3.13.16 and `windows-capture==2.0.1`, `Pillow==12.3.0`, `numpy==2.5.4`, `opencv-python==5.0.0.93` ([OpenCV Python](https://github.com/opencv/opencv-python)). These are manifest values, not a newly queried Windows installation or proof of the versions in all historical tests. Do not combine the Linux and Windows NumPy pins in one environment.

Native key transport is custom Windows integration. PyAutoGUI/PyDirectInput is not an established prerequisite of the measured path. Browser preview does not itself deliver game input. SQLite support is included with Python in the inspected backend.

## Example upstream preparation

Run in a new working directory. These commands prepare upstream components, without starting gameplay or providing the private integration.

```bash
# Linux / WSL: scoring helpers for the local adapter.
git clone https://github.com/featherless-ai/simple-jev.git
git -C simple-jev checkout --detach b02aa81c915a8193759b3cd33fef74721d6e005b

# Higher-level assistant: isolate its dependencies from the fast loop.
git clone https://github.com/NousResearch/hermes-agent.git
git -C hermes-agent checkout --detach 3d0bdce9f92845696233d2bc569e7f521b3ef3f3
python3.13 -m venv .venv-hermes
.venv-hermes/bin/python -m pip install -e ./hermes-agent
```

In the corresponding Windows Python environment:

```powershell
python -m pip install windows-capture==2.0.1
```

Install vLLM separately using its platform guide. Point orchestration/scoring clients at the same resident endpoint. Verify image input and tokenizer/label scoring before enabling a session. Checkpoint-specific runtime configuration and operational prompts remain private.

## Optional, experimental or legacy components

| Component | Local status | Required for the reported native control result? |
|---|---|---|
| [Kubernetes](https://github.com/kubernetes/kubernetes) + [HAMi](https://github.com/Project-HAMi/HAMi) | Model-host deployment/GPU resource sharing | No portable cluster requirement is established; a compatible resident endpoint is the integration boundary |
| [Playwright](https://github.com/microsoft/playwright-python) 1.63.0 | Installed for browser automation/UI verification; Chromium is needed for those tests | Not the Windows game-input mechanism |
| [Browser Use](https://github.com/browser-use/browser-use) 0.13.10 | Retained earlier browser experiment; current assistant uses Hermes | No |
| [Ultralytics YOLO](https://github.com/ultralytics/ultralytics) | Private optional proposal-only adapter; `ultralytics` absent from inspected controller environment. Validated game-specific weights would be needed | **No measured YOLO gameplay path claimed** |
| [Hy-Memory](https://github.com/Tencent-Hunyuan/Hy-Memory) | Separate between-wave gameplay-memory experiment | No; not the mandatory live store |
| Mem0 | Studied alternative; `mem0ai` absent from inspected controller environment | No |
| [AgentGarten](https://github.com/MirroS-Lab/AgentGarten) | Research reference for review/practice ideas | No; not an engine installed inside the keyboard loop |
| [PresentMon](https://github.com/GameTechDev/PresentMon) 2.6.0 console | Optional portable frame-time measurement tool. A local trace attempt was denied by Windows permissions; no game-render FPS result was obtained | No; [measurement status](PERFORMANCE_STATUS.md) |

Only gameplay experience is relevant to the memory entries above. Document ingestion, OCR, document RAG/embeddings and document graph stores are outside this inventory.

## Integration and measurements

The complete system also requires the private capture/input bridge, CPU planner, Control Room backend/UI, scoring adapter, skills and session configuration. A dependency list cannot replace those components. Human choices cover character, weapon, difficulty, Level up, Shop and reward items; current gameplay must be verified before an enabled session resumes movement.

Measure capture FPS, preview FPS, CPU decision time, GPU inference time and input ACKs separately. Record exact versions/checkpoint provenance for each new benchmark. The [tested figures](SYSTEM_DIAGRAMS.md) describe specific historical paths, not every component in one integrated run.
