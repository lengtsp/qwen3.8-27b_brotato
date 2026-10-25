"""Educational decisions for a synthetic first wave; never sends game input.

Run with Python 3.12+: python examples/one_wave.py
Coordinates use a square toy arena: (0, 0) top-left, (1, 1) bottom-right.
The fixtures, speeds, radii and weights are invented teaching values.
"""

from __future__ import annotations

import json
import math
import time
from dataclasses import dataclass


DIRECTIONS = {
    "up": (0, -1), "up_right": (1, -1), "right": (1, 0),
    "down_right": (1, 1), "down": (0, 1), "down_left": (-1, 1),
    "left": (-1, 0), "up_left": (-1, -1),
}
HORIZON_S = 0.25
STEP = 0.075
MAX_FRAME_AGE_S = 0.5


def distance(a, b):
    return math.hypot(a[0] - b[0], a[1] - b[1])


def valid_point(value):
    return (
        isinstance(value, (list, tuple)) and len(value) == 2
        and all(isinstance(v, (int, float)) and not isinstance(v, bool)
                and math.isfinite(v) and 0 <= v <= 1 for v in value)
    )


def separation_during_step(start, end, hazard):
    """Closest distance between two linear motions, including crossing paths."""
    a = (hazard["x"] - start[0], hazard["y"] - start[1])
    b = (hazard["x"] + hazard.get("vx", 0) * HORIZON_S - end[0],
         hazard["y"] + hazard.get("vy", 0) * HORIZON_S - end[1])
    delta = (b[0] - a[0], b[1] - a[1])
    length_sq = delta[0] ** 2 + delta[1] ** 2
    t = 0 if length_sq == 0 else max(0, min(1, -(a[0] * delta[0] + a[1] * delta[1]) / length_sq))
    return math.hypot(a[0] + t * delta[0], a[1] + t * delta[1])


@dataclass
class Planner:
    target: tuple | None = None
    committed_until_s: float = 0
    target_kind: str = "loot"

    def decide(self, frame, now_s):
        """Keep a destination while changing the short local movement segment."""
        def wait(reason):
            self.target = None
            return {"status": "wait", "keys": [], "reason": reason}

        if frame.get("phase") != "gameplay":
            return wait("human_menu_or_unknown_phase")
        age = frame.get("frame_age_s", math.inf)
        if not isinstance(age, (int, float)) or not math.isfinite(age) or not 0 <= age <= MAX_FRAME_AGE_S:
            return wait("fresh_observation_required")
        player = frame.get("player")
        hp = frame.get("hp_ratio")
        remaining = frame.get("time_left_s")
        if not valid_point(player):
            return wait("player_position_not_confirmed")
        if (not isinstance(hp, (int, float)) or isinstance(hp, bool)
                or not math.isfinite(hp) or not 0 < hp <= 1
                or not isinstance(remaining, (int, float)) or isinstance(remaining, bool)
                or not math.isfinite(remaining) or remaining <= 0):
            return wait("current_hp_and_time_required")
        loot, healing = frame.get("loot", []), frame.get("healing", [])
        enemies, bullets = frame.get("enemies", []), frame.get("bullets", [])
        for points in (loot, healing):
            if not isinstance(points, list) or len(points) > 64 or not all(valid_point(p) for p in points):
                return wait("invalid_or_excessive_points")
        for hazards in (enemies, bullets):
            if not isinstance(hazards, list) or len(hazards) > 64:
                return wait("invalid_or_excessive_hazards")
            for h in hazards:
                if not isinstance(h, dict) or not valid_point([h.get("x"), h.get("y")]):
                    return wait("invalid_hazard_position")
                if any(not isinstance(h.get(k, 0), (int, float))
                       or isinstance(h.get(k, 0), bool) or not math.isfinite(h.get(k, 0))
                       or abs(h.get(k, 0)) > 5 for k in ("vx", "vy")):
                    return wait("invalid_hazard_velocity")

        kind = "healing" if hp < 0.5 and healing else "loot"
        candidates = healing if kind == "healing" else loot
        target_present = self.target is not None and any(distance(self.target, p) < 0.03 for p in candidates)
        # A threat changes the local detour, not the destination. A collected or
        # unavailable target, menu or urgent healing need can end a commitment.
        if self.target_kind != kind or not target_present or now_s >= self.committed_until_s:
            if not candidates:
                return wait("no_observed_target")
            def value(point):
                nearby = sum(distance(point, p) < 0.15 for p in candidates)
                return nearby / (0.1 + distance(player, point))
            self.target = tuple(max(candidates, key=value))
            self.target_kind = kind
            self.committed_until_s = now_s + 4

        collection_weight = 7 if remaining <= 12 and hp > 0.5 else 4
        scored = []
        for name, (dx, dy) in DIRECTIONS.items():
            norm = math.hypot(dx, dy)  # Diagonal steps have the same speed.
            end = (player[0] + STEP * dx / norm, player[1] + STEP * dy / norm)
            if not all(0.025 <= v <= 0.975 for v in end):
                continue
            risk = 0.0
            blocked = False
            for hazards, radius, weight in ((enemies, 0.055, 8 + 10 * (1 - hp)),
                                            (bullets, 0.025, 30)):
                for h in hazards:
                    clearance = separation_during_step(player, end, h)
                    # Permit an escape if the actor is already overlapping a
                    # hazard and this step increases their final separation.
                    future = (h["x"] + h.get("vx", 0) * HORIZON_S,
                              h["y"] + h.get("vy", 0) * HORIZON_S)
                    escaping = distance(player, (h["x"], h["y"])) < radius and distance(end, future) > distance(player, (h["x"], h["y"]))
                    if clearance < radius and not escaping:
                        blocked = True
                        break
                    risk += weight * max(0, (radius + 0.05 - clearance) / (radius + 0.05))
                if blocked:
                    break
            if blocked:
                continue
            progress = distance(player, self.target) - distance(end, self.target)
            scored.append((collection_weight * 10 * progress - risk, name))
        if not scored:
            return {"status": "wait", "keys": [], "reason": "no_clear_candidate", "target": self.target}
        score, direction = max(scored)
        return {
            "status": "recommendation_only", "direction": direction,
            "keys": direction.split("_"), "hold_ms": 150,
            "target": self.target, "target_kind": self.target_kind,
            "target_locked_until_s": self.committed_until_s,
            "reason": "advance_toward_target_with_local_risk_check", "score": round(score, 3),
        }


def demo_frames():
    """A short first-wave walkthrough, NOT recorded game data or a benchmark."""
    base = {"phase": "gameplay", "frame_age_s": 0.03, "hp_ratio": 0.9,
            "time_left_s": 30, "player": [0.5, 0.5],
            "loot": [[0.78, 0.5], [0.8, 0.55]], "healing": [], "enemies": [], "bullets": []}
    return [
        (0, "Loot on the right", dict(base)),
        (1, "Enemy blocks the direct route; keep the destination", dict(base, player=[0.56, 0.5], enemies=[{"x": 0.65, "y": 0.5}])),
        (2, "A projectile crosses the approach", dict(base, player=[0.61, 0.43], bullets=[{"x": 0.67, "y": 0.3, "vx": 0, "vy": 0.8}])),
        (3, "Low HP makes a visible healing target urgent", dict(base, player=[0.67, 0.43], hp_ratio=0.4, healing=[[0.66, 0.7]])),
        (8, "More collection incentive near the end", dict(base, player=[0.68, 0.65], hp_ratio=0.8, time_left_s=8, loot=[[0.79, 0.68]])),
        (9, "Wave ends; the human chooses the upgrade", dict(base, phase="level_up", player=None)),
    ]


def main():
    planner = Planner()
    for now_s, scene, frame in demo_frames():
        started = time.perf_counter()
        decision = planner.decide(frame, now_s)
        print(json.dumps({"source": "synthetic_tutorial", "scene": scene,
                          "cpu_ms": round((time.perf_counter() - started) * 1000, 3),
                          "model_calls": 0, "model_tokens": 0, **decision}))


if __name__ == "__main__":
    main()
