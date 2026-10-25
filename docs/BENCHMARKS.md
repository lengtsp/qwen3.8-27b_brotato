# Selected benchmarks and interpretation

Snapshot: 25 October 2026. This is a curated research summary, not a complete experimental export. Separate measurements retain separate denominators.

## Offline CPU replay

| Metric | Earlier path | Accelerated path |
|---|---:|---:|
| CPU pipeline median | 123.20 ms | 78.52 ms |
| Recorded steps / timing samples | 25 / 23 | 25 / 23 |

The reduction is approximately 36.27%. Recorded imagery was replayed with a memory-only input adapter. This tests CPU processing; no new live play or Qwen speedup follows from the result.

## Image embedding API

The latest probe offered five selected stored game-only fixtures repeatedly, with 100 ms between completed offers. It made 120 actual encode requests, all HTTP200. Qwen was not running concurrently.

| Metric | Result |
|---|---:|
| Successes / actual requests | 120 / 120 |
| HTTP median | 79.50 ms |
| HTTP p95, lower order statistic | 129.56 ms |
| HTTP minimum / maximum | 52.75 / 199.17 ms |
| Owner RSS after 30 / 120 offers | 2,498,068,480 / 2,498,076,672 bytes |
| Owner CUDA reserved after 30 / 120 offers | 1,035,993,088 / 1,035,993,088 bytes |

Memory initially rose with shape/runtime warmup, then RSS changed by 8 KiB over those later samples. This is a short test, not proof of long-term leak freedom. GPU allocator statistics omit some driver/context overhead.

An earlier 120-offer run completed 101 encodes and recorded 19 combined busy/unavailable offers. Their exact cause remains unresolved because the old diagnostic grouped statuses together. A later successful run does not retrospectively establish a fix for them.

## Memory and data coverage

The audited visual index has 28 cases across 8 recorded control segments. Wave is known in 28; Danger in 6; character and map in 0. No case has all four labels or a positive interval HP-drop proxy. Pickups and isolated action causation are not independently verified.

Leaving the query's entire segment out, the production known-label filter has another-segment candidates for 24/28 queries. This is candidate coverage, not 85.7% accuracy. Strict complete-build evaluation has 0 eligible queries. Recorded segments are not verified independent runs; adjacent-image random splits would overstate generalization.

Two older exploratory comparisons observed in-combat counter gains 22 / 25 for baseline and 17 / 23 with memory advice, final HP 16/16 throughout. Sample size and uncontrolled encounters prevent a causal conclusion about memory. No gameplay gain is established.

## Selected progression and tokens

| Difficulty label | Recorded completion endpoints | Other retained observations |
|---|---|---|
| Danger 0 | Waves 1–6 | Wave 7 observed; operator reported a loss |
| Danger 2 | Waves 1,2,4 | Wave 7 observed |
| Danger 4 | Waves 6,7 | Recorded death endpoint at Wave 8 |

These are historical segment endpoints, not proof of autonomous full-wave coverage. Missing earlier waves are not inferred.

One selected Danger 0/Wave 2 completion segment has 177 native command ACKs, HP last observed 100%, and 313,419 recorded tokens (313,379 input + 40 output). Across 16 attributable historical segments, recorded response totals sum to 3,034,643 tokens. These are incomplete observed-response totals, not all-run usage or a bill; cached/uncached GPU work was not established.

## Current recovery observation

After a Resume-handoff fix, a 12-second observation recorded 96 exploratory pulses and no repeated Pause cycle. Normal actor-grounded steps remained 0 during that observation. Rendered movement and changing counters were visible, but this does not establish planned pickup quality or robust player tracking.

The proposed diagonal corner-search recovery is software-tested locally. Its live benefit is unmeasured; sending a heading does not prove arrival at a corner or establish a player coordinate.
