# Per-segment model token usage

Snapshot: 2026-10-23. Totals below sum **recorded model responses**, not a complete bill for an entire game run. Each measurement is one retained control segment; a paused/restarted wave can create several segments. Verified run-wide grouping is unavailable.

## Latest reported completion

Danger **0 / Wave 2**, 2026-10-23T15:48:18+07:00: recorded completion at Level up, **177 command ACKs**, **19 GPU-guided ACKs**, latest observed HP **100%**. Counter gain is known only as a lower bound of **27**. It is not a count of inventory items.

Recorded input tokens **313,379** + output tokens **40** = **313,419 tokens**, from **38 distinct assessments / 40 question requests**. Full-wave control and a complete full-round token total remain unverified.

## Measurements with recoverable token receipts

| ID | End time (UTC+07) | Danger / Wave | Archive outcome | Input tokens | Output tokens | Recorded total | Distinct assessments |
|---|---|---|---|---:|---:|---:|---:|
| MEAS-064 | 2026-10-23T13:42:17+07:00 | unknown / 2 | recorded_completion | 78,981 | 13 | 78,994 | 13 |
| MEAS-065 | 2026-10-23T13:44:51+07:00 | unknown / 3 | recorded_completion | 59,747 | 8 | 59,755 | 8 |
| MEAS-066 | 2026-10-23T13:47:52+07:00 | unknown / 4 | recorded_completion | 117,562 | 20 | 117,582 | 18 |
| MEAS-067 | 2026-10-23T14:04:44+07:00 | 4 / 5 | unresolved_or_interrupted | 266,455 | 35 | 266,490 | 35 |
| MEAS-068 | 2026-10-23T14:06:11+07:00 | 4 / 6 | recorded_completion | 286,050 | 46 | 286,096 | 45 |
| MEAS-069 | 2026-10-23T14:07:52+07:00 | 4 / 7 | recorded_completion | 154,686 | 26 | 154,712 | 25 |
| MEAS-070 | 2026-10-23T14:09:01+07:00 | 4 / 8 | recorded_death | 151,980 | 25 | 152,005 | 23 |
| MEAS-071 | 2026-10-23T15:45:15+07:00 | unknown / 1 | recorded_completion | 215,056 | 34 | 215,090 | 29 |
| MEAS-072 | 2026-10-23T15:46:45+07:00 | 0 / 2 | unresolved_or_interrupted | 145,949 | 23 | 145,972 | 16 |
| MEAS-073 | 2026-10-23T15:47:27+07:00 | unknown / 1 | recorded_completion | 218,795 | 35 | 218,830 | 33 |
| MEAS-074 | 2026-10-23T15:48:18+07:00 | 0 / 2 | recorded_completion | 313,379 | 40 | 313,419 | 38 |
| MEAS-075 | 2026-10-23T15:49:56+07:00 | 0 / unknown | unresolved_or_interrupted | 10,020 | 2 | 10,022 | 1 |
| MEAS-076 | 2026-10-23T15:51:18+07:00 | 0 / 4 | recorded_completion | 175,966 | 29 | 175,995 | 25 |
| MEAS-077 | 2026-10-23T15:52:41+07:00 | 0 / 5 | recorded_completion | 120,486 | 20 | 120,506 | 15 |
| MEAS-078 | 2026-10-23T15:54:54+07:00 | 0 / 6 | recorded_completion | 299,737 | 51 | 299,788 | 45 |
| MEAS-079 | 2026-10-23T15:57:17+07:00 | 0 / 7 | unresolved_or_interrupted; user reports death | 419,319 | 68 | 419,387 | 64 |

Older or unattributable measurements remain `null` in the JSON. Missing receipts are not zero-token runs. Unknown Danger/wave labels are not filled from neighboring segments.

## Accounting method and limits

- Sum the server-reported `prompt_tokens` and `completion_tokens` for each distinct assessment/question response, validating `total_tokens = prompt_tokens + completion_tokens`.
- Match original GPU source timestamps against each segment's recorded GPU source span. Require the retained native window context, clock scope and Unix/monotonic mapping; a monotonic timestamp alone can collide across reboots.
- Do not multiply token counts by keyboard steps. A direction result can be reused; it is still one inference response. Shared assessments are assigned to the earliest matching retained segment for additive totals.
- These are observed-response totals. Unlogged warmups, cancelled/unreturned requests and requests outside an attributable segment may consume additional tokens. Therefore `full_round_total_tokens` remains null, even when all recorder timing jobs match.
- Input tokens include the serving engine's image-token representation. Cached-token details were unavailable; these totals do not measure uncached GPU work, cost or model quality.
- A segment's matched assessment count can differ from the recorder's timing-job count. The source span can contain logged assessments that were not sampled by its timing accumulator; the JSON reports this discrepancy. Neither count establishes complete full-round accounting.
- Codex chat, other workloads and unattributable menu/reviewer calls are excluded. No new inference or game input was used for this export.

[Sanitized per-segment JSON](evidence/round-token-usage.json) · [Danger/Wave progression](WAVE_PROGRESS.md) · [Operator-reported outcomes](evidence/operator-reported-outcomes.json) · [Frame-rate inspection](PERFORMANCE_STATUS.md)
