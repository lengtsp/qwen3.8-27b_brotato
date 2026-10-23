# Recorded Danger / Wave progression

Snapshot: 2026-10-23. This is a descriptive ledger of retained local records, not an autonomous win-rate benchmark. The private recorder continues collecting local evidence; this public file is a reviewed snapshot, not an automatic per-wave upload.

A recorded completion means the archive contains `completed=true` without a recorded death. It does **not** establish that the agent controlled the entire wave. No retained record explicitly verifies full-wave control coverage. Difficulty sources are disclosed below.

## Known-label overview

| Danger | Waves with recorded completion | Waves observed without confirmed completion | Recorded death waves |
|---|---|---|---|
| 0 | 1, 2, 3, 4, 5, 6 | 7 | — |
| 2 | 1, 2, 4 | 7 | — |
| 4 | 6, 7 | 5, 8 | 8 |

No full-run victory is established by this ledger. Missing earlier waves are not inferred from reaching a later wave. For example, an unknown wave in a Danger 2 record remains unknown; it is not automatically called Wave 3.

## Per-wave completion evidence

| Danger | Wave | Completion records | Difficulty source for those records | Best recorded HP at completion | Best in-combat counter gain at completion |
|---|---|---:|---|---:|---:|
| 0 | 1 | 4 | legacy_inspected_capture_annotation | 100.00% | 25 |
| 0 | 2 | 2 | legacy_inspected_capture_annotation, verified_pause_footer | 100.00% | unknown |
| 0 | 3 | 1 | legacy_inspected_capture_annotation | unknown | unknown |
| 0 | 4 | 2 | legacy_inspected_capture_annotation, verified_pause_footer | 100.00% | 99 |
| 0 | 5 | 1 | verified_pause_footer | 100.00% | unknown |
| 0 | 6 | 1 | verified_pause_footer | 100.00% | unknown |
| 2 | unknown | 2 | operator, verified_pause_footer | 100.00% | unknown |
| 2 | 1 | 3 | operator | 100.00% | unknown |
| 2 | 2 | 1 | verified_pause_footer | 100.00% | unknown |
| 2 | 4 | 1 | verified_pause_footer | 87.97% | unknown |
| 4 | 6 | 1 | verified_pause_footer | 76.32% | 166 |
| 4 | 7 | 1 | verified_pause_footer | 31.20% | unknown |

Best HP and best counter gain are separate per-metric maxima and need not come from the same record. Missing measurements remain unknown. Counter gain is not a measured count of unique inventory items. These records span different controller versions, builds and human interventions and are not comparable score trials.

## Evidence limits and exclusions

- 80 retained controller records were read; 1 duplicate legacy baseline record was excluded, leaving 79 canonical records.
- 24 observation-only records are excluded from agent-control progression claims.
- Modern automatic records describe control segments and explicitly mark full-wave coverage as unverified. A completion endpoint is not an independent full-wave trial.
- `verified_pause_footer` means the local reader obtained the difficulty from Pause pixels; `operator` is a supplied label; `legacy_inspected_capture_annotation` is an older manually inspected record. No new visual audit of all historical screenshots was conducted for this export.
- Unknown Danger records and unknown wave records are retained separately in the JSON, without assigning them to nearby known labels.
- A `wave_completed` event name with a null completion flag remains unresolved. Danger 2 / Wave 7 and Danger 4 / Wave 5 contain such records and are not credited as completed.
- No win rate, learning gain or probability of beating the game is inferred from record counts. Retention, incomplete labels and partial control mean this is not a complete play history.

[Sanitized aggregate JSON](evidence/danger-wave-progress.json) · [Benchmark methodology](EXPERIMENTS.md) · [Existing memory comparison](evidence/wave1-memory-summary.json)


## Coverage map: Waves 1–20

| Danger | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | C | C | C | C | C | C | ? | — | — | — | — | — | — | — | — | — | — | — | — | — |
| 2 | C | C | — | C | — | — | ? | — | — | — | — | — | — | — | — | — | — | — | — | — |
| 4 | — | — | — | — | ? | C | C | D | — | — | — | — | — | — | — | — | — | — | — | — |

C = recorded completion endpoint; D = recorded death without a recorded completion; ? = observed but unresolved; — = no eligible retained record. This is not an autonomous win-rate or full-wave-control map. Unknown-Danger records stay separate in the JSON.

## Latest user report and token accounting

Danger 0 / Wave 2 has a newly retained completion, **177 command ACKs**, latest observed HP **100%**, and **313,419 recorded tokens**. See the [per-segment token table](TOKEN_USAGE.md) for input/output splits and coverage limits.

The user also reports losing **Danger 0 / Wave 7**. Its retained control segment ended with `operator_stop`, an unresolved completion flag and last observed HP48.12%; it did not capture a verified death endpoint. This user-reported loss is recorded separately from archive-verified death counts, and its last observed HP is not changed to zero. [Report](evidence/operator-reported-outcomes.json)
