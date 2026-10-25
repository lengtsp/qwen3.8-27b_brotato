"""Inspect ONE selected frame through vLLM. No game input or capture loop."""

import argparse
import base64
import io
import json
import os
from pathlib import Path
import time
import urllib.request


PROMPT = """Inspect this one game image. Return one JSON object, no markdown:
{"phase":"gameplay|pause|level_up|shop|item_selection|character_selection|unknown",
 "player_center_1000":[x,y] or null, "hp_ratio":number or null,
 "time_left_s":number or null, "visible_loot_centers_1000":[[x,y]],
 "visible_enemy_centers_1000":[[x,y]], "uncertainty":"brief explanation"}.
Coordinates are 0..1000 over THIS complete supplied image, not another frame.
Use null or an empty list when uncertain. Do not mistake held weapons for the
body. Do not infer projectile velocity, identity or HP from a historical image.
Report observation only; do not press keys or claim successful collection.
"""


def request_json(url, payload=None, api_key=""):
    data = None if payload is None else json.dumps(payload).encode()
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = "Bearer " + api_key
    req = urllib.request.Request(url, data=data, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        # Keep a bad endpoint from returning an unbounded response.
        raw = response.read(2 * 1024 * 1024 + 1)
    if len(raw) > 2 * 1024 * 1024:
        raise ValueError("Response is larger than this tutorial allows")
    return json.loads(raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--image", type=Path, help="Your own local image; treated as archival")
    source.add_argument("--capture", nargs=4, type=int, metavar=("LEFT", "TOP", "WIDTH", "HEIGHT"), help="One region on the visible desktop")
    parser.add_argument("--base-url", default="http://127.0.0.1:18130/v1")
    parser.add_argument("--model", help="Required only when the endpoint lists multiple models")
    parser.add_argument("--out", type=Path, default=Path("output/tutorial-observation.json"))
    args = parser.parse_args()
    from PIL import Image

    started = time.perf_counter()
    captured_at = time.time()
    if args.capture:
        left, top, width, height = args.capture
        if width <= 0 or height <= 0 or width * height > 8_294_400:
            parser.error("Use a positive region of at most 8,294,400 pixels")
        import mss
        with mss.mss() as capture:
            shot = capture.grab({"left": left, "top": top, "width": width, "height": height})
            image = Image.frombytes("RGB", shot.size, shot.rgb)
        source_kind = "selected_desktop_region"
    else:
        if args.image.stat().st_size > 16 * 1024 * 1024:
            parser.error("Local image exceeds the 16 MiB tutorial limit")
        with Image.open(args.image) as opened:
            if opened.width * opened.height > 8_294_400:
                parser.error("Local image exceeds the tutorial pixel limit")
            image = opened.convert("RGB")
        source_kind = "archival_image_not_current_game_state"
    size = image.size
    with io.BytesIO() as buf:
        image.save(buf, format="JPEG", quality=90)
        data_url = "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()
    image.close()
    base = args.base_url.rstrip("/")
    key = os.environ.get("GAME_MODEL_API_KEY", "")
    model = args.model
    if not model:
        models = request_json(base + "/models", api_key=key).get("data", [])
        if len(models) != 1:
            parser.error("Set --model to one ID returned by /v1/models")
        model = models[0]["id"]
    before_model = time.perf_counter()
    response = request_json(base + "/chat/completions", {
        "model": model, "temperature": 0.7, "top_p": 0.8, "top_k": 20,
        "min_p": 0.0, "presence_penalty": 1.5, "repetition_penalty": 1.0,
        "max_tokens": 512,
        "chat_template_kwargs": {"enable_thinking": False, "preserve_thinking": False},
        "response_format": {"type": "json_object"},
        "messages": [{"role": "user", "content": [
            {"type": "text", "text": PROMPT},
            {"type": "image_url", "image_url": {"url": data_url}},
        ]}],
    }, api_key=key)
    elapsed_ms = (time.perf_counter() - started) * 1000
    usage = response.get("usage", {})
    if response["choices"][0].get("finish_reason") == "length":
        raise ValueError("Output reached its token limit; no usable observation")
    observation = json.loads(response["choices"][0]["message"]["content"])
    if not isinstance(observation, dict):
        raise ValueError("Expected a JSON observation object")
    result = {"source": source_kind, "captured_at_unix_s": captured_at,
              "image_size": size, "model": model,
              "model_request_ms": round((time.perf_counter() - before_model) * 1000, 3),
              "capture_to_result_ms": round(elapsed_ms, 3),
              "usage": usage, "observation": observation,
              "actionable": False,
              "note": "Unvalidated single-frame observation; no keyboard input sent"}
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "observation"}, indent=2))
    print("Observation saved to", args.out)


if __name__ == "__main__":
    main()
