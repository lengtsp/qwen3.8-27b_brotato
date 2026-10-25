"""Behavior checks for the teaching example, not live-game validation."""

import math
import unittest

from one_wave import DIRECTIONS, Planner, demo_frames, separation_during_step


class PlannerTests(unittest.TestCase):
    def frame(self, **changes):
        return dict(demo_frames()[0][2], **changes)

    def test_moves_toward_visible_loot(self):
        self.assertEqual(Planner().decide(self.frame(), 0)["direction"], "right")

    def test_blocked_route_keeps_destination_but_changes_local_keys(self):
        planner = Planner()
        target = planner.decide(self.frame(), 0)["target"]
        decision = planner.decide(self.frame(enemies=[{"x": 0.58, "y": 0.5}]), 1)
        self.assertEqual(decision["target"], target)
        self.assertNotEqual(decision["direction"], "right")

    def test_new_reward_does_not_interrupt_existing_commitment(self):
        planner = Planner()
        target = planner.decide(self.frame(), 0)["target"]
        changed = self.frame(loot=[[0.78, 0.5], [0.8, 0.55], [0.49, 0.48]])
        self.assertEqual(planner.decide(changed, 1)["target"], target)
        self.assertEqual(planner.decide(changed, 4)["target"], (0.49, 0.48))

    def test_healing_overrides_loot_when_hp_is_low(self):
        planner = Planner()
        planner.decide(self.frame(), 0)
        decision = planner.decide(self.frame(hp_ratio=0.4, healing=[[0.5, 0.75]]), 1)
        self.assertEqual(decision["target_kind"], "healing")

    def test_all_four_edges_stay_inside_the_arena(self):
        for player in ([0.03, 0.5], [0.97, 0.5], [0.5, 0.03], [0.5, 0.97]):
            decision = Planner().decide(self.frame(player=player, loot=[[0.5, 0.5]]), 0)
            self.assertEqual(decision["status"], "recommendation_only")
            dx, dy = DIRECTIONS[decision["direction"]]
            norm = math.hypot(dx, dy)
            endpoint = (player[0] + 0.075 * dx / norm, player[1] + 0.075 * dy / norm)
            self.assertTrue(all(0.025 <= v <= 0.975 for v in endpoint))

    def test_crossing_projectile_is_not_missed_by_endpoint_checks(self):
        hazard = {"x": 0.55, "y": 0.4, "vx": 0, "vy": 0.8}
        self.assertLess(separation_during_step((0.5, 0.5), (0.6, 0.5), hazard), 0.001)

    def test_menus_and_uncertain_observations_never_recommend_keys(self):
        bad_frames = [self.frame(phase=phase) for phase in ("level_up", "shop", "pause", "unknown")]
        bad_frames += [self.frame(player=None), self.frame(frame_age_s=1),
                       self.frame(frame_age_s=float("nan")), self.frame(hp_ratio=None),
                       self.frame(player=[float("nan"), 0.5]), self.frame(time_left_s=0),
                       self.frame(bullets=[{"x": 0.5, "y": 0.5, "vx": float("nan")}])]
        for frame in bad_frames:
            with self.subTest(frame=frame):
                self.assertEqual(Planner().decide(frame, 0)["keys"], [])


if __name__ == "__main__":
    unittest.main()
