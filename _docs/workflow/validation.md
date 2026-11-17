# Validation and tests

Nothing reaches a pull request without `validate.py` printing `OK`. Two test files cover
the parts of the toolchain that have rules worth locking in.

## `validate.py`

```bash
python3 scripts/listens/validate.py
```

Exits non-zero on any error so a CI job could gate on it. It reads the three entity
files, every file in `_listens/`, and `podcast_works.yml`, and checks:

**Entities**

- No duplicate `id` in shows, people or topics.
- Every `hosts` entry on a show is a person id.

**Each listen**

- Front matter exists and parses.
- `title`, `show`, `published_on`, `listened_on`, `topics` and `guid` are present
  (`guests` may be empty).
- `show`, every guest and every topic resolve to an id.
- `guests` is a list.
- Both dates parse as `YYYY-MM-DD`.
- `listened_precision` is one of `day`, `month`, `year`, `approximate`.
- No two listens share a `guid`.

**Moments**

- `moments` is a list of mappings.
- Only `at`, `shot_on` and `chapter` are present. The error message says why: the file
  is public, so passage text and notes stay in the private ledger.
- `at` looks like `25:53` or `1:02:03` and is not past the end of the episode.
- `shot_on` parses and is not before `published_on`.
- No moment is listed twice.

**Works**

- Required fields (`id`, `title`, `type`, `source`); `type`, `source` and `my_status`
  within their vocabularies; no duplicate ids.
- Every `authors` entry is a person id (outside authors go in `authors_outside`).
- A work with no mentions has an on-graph author (or it cannot appear) and is
  `source: manual`.
- Every mention points at a real listen, no listen is mentioned twice by one work,
  `kind` is valid, a `recommended` mention names `by`, and `by` is a person id.

The last line is a summary: `17 listens, 9 shows, 26 people, 12 topics, 13 works: OK`
(numbers as of this writing).

## `test_moments.py`

```bash
python3 -m unittest scripts/listens/test_moments.py
```

Nine tests for `add-moment` and the moments checks in the validator. They run on a copy
of the real `_listens/` folder in a temporary directory, touch nothing in the
repository and make no network calls. The fixture is the first real listen that has no
moments yet, so the assertions start from zero. Covered: a moment is written and
sorted, a second mark within a minute is ignored, a mark on a different day is kept,
positions past the end and dates before publication are refused, and the validator
rejects extra keys and duplicates.

## `test_intake.py` (private repository)

```bash
cd ~/PROJECTS/podcast-ingest-agent/screenshots && python3 -m unittest test_intake
```

Twenty tests, no network. Described on the
[screenshot intake](screenshot-intake.md#tests-and-findings) page.

## The Jekyll build

A full build is optional before a PR, since the Pages workflow builds every PR as a
check. Locally:

```bash
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 bundle exec jekyll build
```

Without the UTF-8 locale the build fails on non-ASCII characters in the content. More
in [Environment](../reference/environment.md).

## What is not automated

The pilot plan said `validate.py` would run in a GitHub Action on PRs that touch
`_listens/` or the data files. As of November 2026 the only workflow is `pages.yml`,
which builds the site and does not run the validator. Running it locally before each
PR is the current practice; wiring it into CI is on the [roadmap](../roadmap.md).
