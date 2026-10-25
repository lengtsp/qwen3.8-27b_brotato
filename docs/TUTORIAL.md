# Beginner tutorial: from installation to a small first-wave example

Start with an executable CPU example, then optionally inspect your own image using Qwen. The examples teach the interfaces in the architecture diagram. They do not install the private Control Room or reproduce the complete controller and its benchmarks.

The first-wave walkthrough uses six invented observations: collect nearby loot, detour around an enemy, avoid a crossing projectile, seek healing when HP is low, increase collection incentive near the end, then wait for a human at level-up. It does not contain a game screenshot, wiki content or a recorded successful wave.

## 1. Choose the parts you want to try

| Part | Install | Purpose | Needed for the first example? |
|---|---|---|---|
| CPU planner | Python 3.12+ and Git | Score eight directions using structured observations | Yes |
| Selected-region capture | MSS and Pillow | Capture and encode one visible game region | Optional |
| Qwen inference | Compatible NVIDIA driver, Linux/WSL2, vLLM and licensed vision-model weights | Ask a GPU model to describe one image | Optional |
| Simple-JEV | Upstream HF server in a separate environment | Score a small set of direction labels | Optional |
| Image memory | EmbeddingGemma 2, SentenceTransformers and SQLite | Retrieve a similar previous image | Optional |
| Native input and Control Room | Project-specific private integration | Validated game input, continuous steering, preview and logs | Not included |
| Hermes orchestration | Separate upstream integration | Coordinate higher-level tools | Not required here |

Install [Python](https://www.python.org/downloads/) and [Git](https://git-scm.com/downloads/) first. Capture runs on the computer and desktop session showing the game. A Windows game can use a Windows capture client with a separate Linux/WSL model server. MSS captures visible pixels; this example does not capture an obscured window or keep the game focused in the background.

## 2. Clone and run the CPU example

```bash
git clone https://github.com/lengtsp/qwen3.8-27b_brotato.git
cd qwen3.8-27b_brotato
```

On Linux/macOS, create a small environment:

```bash
python3.12 -m venv .venv
.venv/bin/python examples/one_wave.py
.venv/bin/python -m unittest discover -s examples -p 'test_*.py'
```

On Windows PowerShell:

```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe examples/one_wave.py
.venv\Scripts\python.exe -m unittest discover -s examples -p 'test_*.py'
```

No packages, model, GPU, game installation or API key are needed for these commands. The program prints decisions and CPU processing time; it never presses a key. `model_calls: 0` and `model_tokens: 0` describe this CPU-only walkthrough, not the research project's gameplay token usage.

## 3. Understand one simple wave

Read [the teaching planner](../examples/one_wave.py). Its reasoning is deliberately small:

1. Require a gameplay label, a confirmed player point, HP/time and a fresh observation. Otherwise recommend no keys.
2. Choose a nearby loot point, favoring small groups. Below 50% HP, prefer visible healing.
3. Keep the destination for at least four seconds while it remains available. Urgent healing, a collected/unavailable target or a menu can end that commitment.
4. Score eight short moves. Favor progress toward the destination, subtract enemy/projectile risk and reject routes through the arena edge.
5. Change the short movement segment to avoid danger while keeping the destination. A four-second plan commitment does **not** mean holding a key for four seconds.
6. Recommend a short key interval; at level-up, return `keys: []` and hand control to the human.

The output includes a case like this; the exact CPU timing is machine-dependent:

```json
{
  "source": "synthetic_tutorial",
  "scene": "Enemy blocks the direct route; keep the destination",
  "status": "recommendation_only",
  "direction": "up_right",
  "keys": ["up", "right"],
  "hold_ms": 150,
  "target": [0.78, 0.5],
  "target_locked_until_s": 4
}
```

The scoring idea is `collection_weight * progress - hazard_risk`, with hard boundary and immediate-collision checks. Moving diagonally is normalized to the same distance as a single-axis move. Projectile checks compare both moving paths, so a crossing bullet can matter even when its final point is distant.

All toy speeds, hit distances, weights and coordinates are educational choices. They are not measured Brotato mechanics. The fixture velocities were written by hand; one screenshot cannot establish velocity. Live integration additionally needs reliable detection, multi-frame tracking, arena/crop coordinate transforms, input acknowledgments and current-window checks. This example neither learns a policy nor proves that its route is optimal.

## 4. Optionally install a Qwen/vLLM server

Skip installation if a compatible server is already running. Check its `/v1/models` endpoint and reuse it; starting another copy of a large model consumes additional GPU memory.

For a new NVIDIA setup, use a separate Linux/WSL environment. Follow the current [vLLM GPU installation guide](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/) for your driver/CUDA combination:

```bash
python3.12 -m venv .venv-vllm
source .venv-vllm/bin/activate
python -m pip install uv
uv pip install vllm --torch-backend=auto
vllm download-kernels
```

Download a vision-capable checkpoint that your hardware and installed loader support. [Qwen's official model card](https://huggingface.co/Qwen/Qwen3.8-27B) documents the base model. The research used a separate NVFP4 checkpoint; this tutorial does not distribute it or promise that every quantized variant runs with the same package versions.

Set your local checkpoint directory, then launch a small **example** context and concurrency budget:

```bash
GAME_MODEL_PATH="/path/to/your/downloaded/vision-model"
vllm serve "$GAME_MODEL_PATH" \
  --served-model-name game-vision \
  --host 127.0.0.1 --port 18130 \
  --tensor-parallel-size 1 --max-num-seqs 1 \
  --max-model-len 8192 --gpu-memory-utilization 0.70 \
  --limit-mm-per-prompt '{"image":1}'
```

In another terminal, check readiness:

```bash
curl http://127.0.0.1:18130/health
curl http://127.0.0.1:18130/v1/models
```

An 8K context is a tutorial starting point, not the research deployment's 220K configuration or a minimum-VRAM guarantee. Model weights, GPU KV cache and inference buffers all need space; two models sharing a GPU need a joint budget. Package support varies by checkpoint. See [vLLM serving](https://docs.vllm.ai/en/latest/serving/online_serving/).

## 5. Optionally inspect one image

Return to the small client environment from step 2. On Linux:

```bash
.venv/bin/python -m pip install -r examples/requirements-vision.txt
.venv/bin/python examples/inspect_frame.py --image /path/to/your-own-frame.png
```

On Windows, capture one selected visible region instead. Replace all four numbers with your game region's actual desktop coordinates and dimensions:

```powershell
.venv\Scripts\python.exe -m pip install -r examples/requirements-vision.txt
.venv\Scripts\python.exe examples/inspect_frame.py --capture 100 100 1280 720
```

Use the game's actual client area, and take a new frame after moving/resizing it. Crops must map back to source coordinates; excluded HUD/black bars and non-square arenas need explicit geometry in a real controller. The CPU toy arena in step 3 is square, so its coordinates are not a drop-in mapping for an arbitrary desktop capture.

The [one-frame client](../examples/inspect_frame.py) sends a base64 image to vLLM and writes `output/tutorial-observation.json`. It records image dimensions, request latency, total capture-to-result time and the token usage returned by the server. File images are labeled archival. It does not save a raw screenshot, detect a named game window, OCR the HUD independently, track bullets, validate the model's coordinates or send keyboard input.

The payload uses Qwen's non-thinking settings and a JSON response request; another model may require changes. Unknown fields should remain unknown. A valid JSON object is still an unverified observation. Late or incomplete output is not a movement command. The endpoint must be reachable from the capture client; `127.0.0.1` refers to that client's network context. Optional server authentication uses the local `GAME_MODEL_API_KEY` environment variable.

## 6. Optionally try Simple-JEV

The upstream [Simple-JEV installation and API](https://github.com/featherless-ai/simple-jev) are separate from vLLM chat completions. Its HF server scores next-token choices; installing it does **not** automatically add a classifier route to a resident vLLM process.

For a small standalone CPU exercise, use a separate terminal/environment:

```bash
git clone https://github.com/featherless-ai/simple-jev.git
cd simple-jev
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -e './hf-server'
python hf-server/hf_server.py \
  --model Qwen/Qwen3.5-0.8B --device cpu --dtype float32 \
  --port 18174 --classifier-prompt-policy baseline \
  --max-model-len 4096 --max-batch-size 1 --max-batch-tokens 4096
```

From this research repository in another terminal:

```bash
curl http://127.0.0.1:18174/health
curl http://127.0.0.1:18174/v1/classifier \
  -H 'Content-Type: application/json' \
  --data-binary @examples/jev_request.json
```

The [request fixture](../examples/jev_request.json) asks for one of eight directions in a synthetic state. Inspect `answers.direction.choice`, its distribution and reported token usage; confidence is not a measured chance of avoiding damage. This CPU server is an API-learning alternative, not the project's shared GPU integration. The tutorial does not implement that custom integration or benchmark this optional server.

## 7. Optionally explore visual Memory

Install in another environment to keep inference dependencies separate:

```bash
python3.12 -m venv .venv-memory
source .venv-memory/bin/activate
python -m pip install -U sentence-transformers transformers Pillow
```

Following the [EmbeddingGemma 2 model card](https://ai.google.dev/gemma/docs/embeddinggemma/model_card_2), this CPU illustration compares two local images:

```python
import torch
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer(
    "google/embeddinggemma-2", device="cpu",
    model_kwargs={"torch_dtype": torch.float32},
    config_kwargs={"audio_config": None},
)
first = encoder.encode({"image": ["/path/to/your-first-frame.png"]}, normalize_embeddings=True)
second = encoder.encode({"image": ["/path/to/your-second-frame.png"]}, normalize_embeddings=True)
print(float(encoder.similarity(first, second).item()))
```

It prints image similarity, not game skill or retrieval accuracy. For persistent experience, SQLite is included with Python. Store bounded thumbnails/vectors with scene labels, observed HP/time and outcome provenance; filter compatible situations before retrieval. A retrieved record is advice and cannot establish current player coordinates. Measure Memory on/off gameplay outcomes separately. The public benchmark's encoder ran on GPU; this CPU illustration has no matching latency claim. The optional model setup is not rerun as part of this documentation update.

## 8. Know what was checked

Ten checks passed locally with Python 3.12.3, Pillow 13.0.0 and MSS 10.2.0 installed. Seven test CPU behavior, including stable targets, local detours, all four boundaries, a crossing projectile and menu/unknown/stale rejection. Three check the HTTP client with a local mock server, including token reporting, bounded responses and rejection of truncated output. The image-client check needs Pillow and skips when it is absent. These checks do not validate live gameplay or desktop capture. Optional upstream model/server installs are documentation recipes, not an end-to-end reproduction claim. For real measured results, read [benchmark conditions](BENCHMARKS.md).

The repository intentionally stops before an automatic game-input loop. Continuous play additionally requires phase handoff, fresh actor tracking, bounded key delivery/release, focus handling and an emergency stop. Those remain part of the private experimental controller and its unresolved limitations.
