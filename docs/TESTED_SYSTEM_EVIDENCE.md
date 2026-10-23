# Evidence behind the tested-system figures

Reviewed **2026-10-23** from retained reports. Each figure names the historical test it depicts. This documentation review sent no new game input and ran no new gameplay benchmark. Separate tests are not combined into a claim that all current features passed one integrated test.

The [sanitized manifest](evidence/tested-system-evidence.json) records selected scalars, source digests and limits. Private paths, raw traces and detailed game knowledge are omitted. A digest identifies the retained private source; it does not provide independent public reproduction.

| Evidence ID | What executed | Supported observation | Limit |
|---|---|---|---|
| **NATIVE-01**, 2026-10-19 | Native Danger 2 / Wave 1 capture, CPU routes, source checks and window-message arrow input; resident model assessments | 225 command ACKs, 211 distinct source frames; historical visual review found changed floor/body positions and completion HP16/16 | Not per-key displacement verification or autonomous coverage of the entire wave |
| **GAMEPLAY-MEMORY-01**, 2026-10-18 | Four early Wave 1 / Danger 0 trials with gameplay advice OFF/ON | Baseline/advice gains A **22/17**, B **25/23**; all final HP16/16 | One trial per condition per comparison, unknown RNG, older planner; baseline B used one GPU proposal |
| **ARCHIVE-REVIEW-01**, 2026-10-23 | Two archived segments, four real Qwen review requests, frozen reviewer feedback OFF/ON and output/reference checks | Three empty outputs, one draft marked **needs revision, do not promote** | Zero promotions, game inputs or new gameplay evaluation episodes |
| **REPLAY-01**, 2026-10-18 | Repeated-image replay with memory-only input adapter | Existing CPU/command-continuity comparison | Offline, not native input or model speedup |
| **SOFTWARE-01**, 2026-10-23 | Prior export's synthetic/mocked regression checks | Behavior under those fixtures | Not native gameplay or current integrated validation |

## Native CPU and GPU roles

NATIVE-01 recorded **26 GPU assessments**, inference median/p95 **541.877/658.279 ms**. Initial same-wave scene context was used, but **zero GPU steering directions were admitted** because they missed the source-age limit. CPU paths supplied movement. The diagram therefore shows rejected steering rather than accepted GPU movement.

CPU decision median/p95 was **45.470/109.520 ms**. Source command interval median/p95 was **63.750/132.514 ms**. Native renewal-gap median/p95/max was **0/24.916/55.371 ms**; small gaps existed. These are observations from one historical run without a matched baseline, not model accuracy, guaranteed continuity or a current-system speedup.

No character, restart, Level up or Shop choice was sent. The completed game was left for manual menu handling.

## Two distinct memory experiments

The memory figure's upper lane reports actual gameplay-advice trials from the [existing aggregate](evidence/wave1-memory-summary.json). Its lower lane reports reviewer-error feedback for archive review. It is a different memory mechanism, not a live policy-update trial.

All four archive responses passed structural checks. OFF produced no drafts in two requests; ON produced one draft in two requests. Median request wall time was **4,737.69 ms OFF** and **16,173.76 ms ON**, with only two requests per arm. Base requests were matched except for frozen feedback; the resident model process stayed unchanged. The sole nonempty draft needed revision. Format/source-reference validity is not semantic truth; independent semantic ground truth was unavailable.

Neither experiment establishes better collection, HP, survival or visual detection from memory. No Qwen weights were updated. The candidate does not feed back into the native figure. A held-out live comparison remains a [proposed benchmark method](EXPERIMENTS.md), outside the tested illustrations.

## Figure boundaries

The current illustrations omit unexecuted held-out evaluation, automatic promotion, training and a hypothetical integrated learning loop. They do not attribute later features to NATIVE-01 without that run's evidence. Browser telemetry and other implemented features are documented separately.

The images are AI-generated reconstructions of reported executed paths, not original-run diagram captures or raw evidence images. [Figures/prompts](SYSTEM_DIAGRAMS.md) · [Per-wave observations](WAVE_PROGRESS.md) · [Dependencies](INSTALLATION.md)
