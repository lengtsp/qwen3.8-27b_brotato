# Public scope and private project boundary

The current repository is a research and benchmark showcase. It contains concepts, architecture, methodology, selected aggregate measurements, research references, the Facebook presentation text and limited illustrative images.

## Materials kept separately

- Full controller/backend/frontend implementation, native-input workers and runtime tests.
- Agent skills, operational classifier prompts, configuration and launch/install scripts.
- Detailed enemy/character/weapon facts, game-reference catalogs and schedules.
- Sprites/icons, calibration frames, appearance-reference sets and asset downloaders.
- Raw session traces, memory databases, Chat transcripts, model weights and credentials.

The running local project and its private resources are retained separately. This publication change does not remove or stop that project.

## Illustrative material

One reviewed archived Control Room screenshot remains as an interface example. The workflow infographic uses abstract symbols and contains no game sprites. Neither image is an annotation dataset or proof of improved play. A concise abstract observation can illustrate the approach without distributing game mechanics:

```json
{
  "example_type": "synthetic_not_game_data",
  "observed": {"health_fraction": 0.7, "pickup": [0.6, 0.4], "hazard": [0.5, 0.5]},
  "intent": "approach_visible_pickup_with_current_geometry_checks",
  "memory_role": "bounded_preference_only",
  "unknown": ["enemy_species", "world_speed", "hidden_state"]
}
```

The public JSON reports are selected aggregate transcriptions, not a raw evaluation dataset. Benchmark methods and missing metadata are disclosed so readers can judge the practical limits. The historical validation count refers to a prior implementation snapshot; source/tests are not distributed here.

At the owner's request, the public main branch is rebuilt from this 24-file research-only snapshot with no earlier implementation commits as ancestors. Previous development history is retained in a local private backup outside this repository. The branch-history reset does not guarantee erasure of pre-existing external clones, copies or cached/unreachable objects.
