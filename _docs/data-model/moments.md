# Moments

A moment is a playback position I marked on an episode, almost always by taking a
screenshot of the player. It is stored as an optional list on the listen file and
written only by `add_listen.py add-moment`.

```yaml
moments:
- at: '24:25'               # position in the player, M:SS or H:MM:SS
  shot_on: '2025-12-18'     # date from the screenshot's file name
  chapter: Exploring AI as the New UI and Agent Experie   # optional, as shown
```

## Rules

| Rule | Enforced by |
|---|---|
| `at` looks like `25:53` or `1:02:03` | script and validator |
| `at` is not past the end of the episode (duration plus two minutes of slack) | script and validator |
| `shot_on` is not before `published_on` | script and validator |
| Only `at`, `shot_on` and `chapter` are allowed | validator |
| A second mark within 60 seconds on the same day is the same moment: no change | script (`add-moment` reports "already marked") |
| The same `(at, shot_on)` twice is an error | validator |
| Moments are sorted by position, then date | script |

Several screenshots of one passage are one moment, and the burst's **earliest**
position is the one recorded. The burst logic lives in the private intake repository;
see [Screenshot intake](../workflow/screenshot-intake.md).

## Why position and chapter only

The site repository is public. What a screenshot shows besides the position is the
player's transcript of someone else's words, errors included ("A to a agent identity"
for A2A in one test shot). That text is not a verified quote and it is not mine to
publish. It stays in the private ledger, where it is kept "as shown". If a quote is ever
shown on the site, it will be short, checked against the audio, and linked to the
episode. The validator makes this a hard rule rather than a convention: any other key
on a moment fails the build.

## A moment is not a spark

A screenshot says "this mattered", never why. The spark is asked for afterwards, in my
words, in a batch (the "spark call" on the [roadmap](../roadmap.md)). Until then a
listen can have moments and an empty spark, which is the state of the four episodes
logged from the first screenshot batch.

## Display

As of November 2026 moments are stored and validated but **not rendered**: neither the
episode page nor the graph JSON includes them. That is a roadmap item.
