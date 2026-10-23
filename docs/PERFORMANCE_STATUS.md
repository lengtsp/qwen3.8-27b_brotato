# Frame-rate configuration and post-game observation

Inspected **2026-10-23** after the operator reported a loss at Danger 0 / Wave 7 and visible stutter **in both the actual game and Control Room**. No new gameplay input, model call, navigation, focus change or frame-rate setting change was made for this inspection.

## Configured ceilings versus observed rates

| Layer | Inspected configuration | What was actually observed |
|---|---|---|
| Brotato | Saved `limit_fps=false`; no `--max-fps`, `--fixed-fps` or VSync launch flag found | Rendered game FPS was not measured. Driver/VSync/display limits were not audited |
| Backend selected-window polling | `AGENT_DESKTOP_FPS=60` | A scheduling ceiling, not proof of 60 fresh captures per second |
| WebRTC preview | `AGENT_PREVIEW_FPS=50` | That transport was not active during the observation |
| Active browser preview | Auto selected direct JPEG, source size 1736 × 1035 | JPEG load-rate median **27.861 FPS**; this is reception/load cadence, not verified physical display presentation |
| Windows Graphics Capture | No explicit frame interval supplied in the inspected worker constructor | Source capture median **29.23 FPS** during this observation |

The existing owned browser was observed for **10.003 seconds / 41 samples**. Its document remained visible, but no video track was playing: actual video presentation FPS is **unknown**, not zero. Capture rates ranged **24.69–29.56 FPS**. JPEG load-rate intervals ranged **11.574–35.899 FPS**; bursty delivery can make a short reception interval exceed the source's average rate.

This was a post-game/idle preview observation with zero newly observed control commands, not a fresh combat benchmark. It cannot establish the render rate or resource load during the lost wave. The configured WebRTC value does not describe the active JPEG transport, and neither setting guarantees the achieved rate.

## Recorded control continuity in Wave 7

The retained Danger 0 / Wave 7 segment recorded **251 command ACKs**, CPU decision median **62.880 ms**, GPU assessment timing median **291.947 ms**, and source-to-ACK median **139.579 ms**. It contained **31 ACK intervals over 250 ms**, with maximum **2.330 seconds**. These are recorded command intervals, not independently verified physical key holds, standing duration or rendered displacement.

The later inspected controller state was stopped with reason `Brotato pixels are stale; movement stopped`. That is evidence of a freshness stop, not proof of what caused the operator-reported death. The retained segment itself ended with `operator_stop`, last observed HP48.12%, and no independently verified death frame.

The measurements identify two separate concerns: the preview was receiving fewer frames than its configured maximum, and the retained command stream had substantial gaps. Their root causes are not isolated by this snapshot. CPU/GPU timing medians alone do not explain the longest gaps.

A broader durable-audit time window overlapping that segment contains waits with reasons `player_not_found` and `arena_not_grounded_or_overlay`. These observations support investigating body/arena recognition handoffs as well as frame delivery. That window can include surrounding control activity, so its event counts and timings are not substituted for the retained segment's metrics. Wait events do not establish the cause of every visual stutter or the loss.

## Attempt to measure actual game presentation

The official portable [PresentMon console](https://github.com/GameTechDev/PresentMon/blob/main/README-ConsoleApplication.md), version **2.6.0**, was obtained from its [GitHub release](https://github.com/GameTechDev/PresentMon/releases/tag/v2.6.0). Its SHA-256 matched the release metadata. A bounded trace targeting only the game was attempted, with input tracking disabled and a separate trace-session name. Windows rejected trace creation with **access denied / exit code 6**. No elevation was requested, no installer/service was installed, and no game frame-time result was obtained. The binary is not distributed in this repository.

Actual-game frame timing and driver/VSync limits therefore remain unmeasured. The post-game JPEG/capture rates must not be presented as measured rendered-game FPS or as evidence that GPU load caused the stutter.

For the next comparable test, measure the actual game presentation, source capture cadence, browser reception/presentation and command intervals over the same combat window. Change one setting at a time before attributing a gain to an FPS cap, transport or model. Current settings were preserved during this read-only inspection.

[Sanitized observation](evidence/preview-observation-20261023.json) · [Per-segment tokens and timings](TOKEN_USAGE.md) · [Wave ledger](WAVE_PROGRESS.md)
