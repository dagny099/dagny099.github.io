#!/usr/bin/env python3
"""Check _listens/ against the podcast data files.

Every show, guest, host and topic id must resolve; dates must parse; no two
listens may share a guid. Exits non-zero on any error so CI can gate on it.

Usage: python3 scripts/listens/validate.py
"""
import datetime
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = ["title", "show", "published_on", "listened_on", "topics", "guid"]  # guests may be empty (host-only episodes)
PRECISIONS = {"day", "month", "year", "approximate"}


def load_ids(name):
    rows = yaml.safe_load((ROOT / "_data" / name).read_text()) or []
    ids = [r["id"] for r in rows]
    dupes = {i for i in ids if ids.count(i) > 1}
    return rows, set(ids), dupes


def front_matter(path):
    text = path.read_text()
    if not text.startswith("---\n"):
        raise ValueError("missing front matter")
    return yaml.safe_load(text.split("---\n", 2)[1])


def as_date(value):
    if isinstance(value, datetime.date):
        return value
    return datetime.date.fromisoformat(str(value))


def main():
    errors = []
    shows, show_ids, d1 = load_ids("podcast_shows.yml")
    _, people_ids, d2 = load_ids("podcast_people.yml")
    _, topic_ids, d3 = load_ids("podcast_topics.yml")
    for label, dupes in [("show", d1), ("person", d2), ("topic", d3)]:
        errors += [f"_data: duplicate {label} id '{i}'" for i in sorted(dupes)]
    for show in shows:
        errors += [f"_data/podcast_shows.yml: {show['id']} host '{h}' not in podcast_people.yml"
                   for h in show.get("hosts", []) if h not in people_ids]

    guids = {}
    files = sorted((ROOT / "_listens").glob("*.md"))
    for path in files:
        name = path.name
        try:
            fm = front_matter(path)
        except Exception as exc:  # noqa: BLE001 - report and keep going
            errors.append(f"{name}: {exc}")
            continue
        errors += [f"{name}: missing '{k}'" for k in REQUIRED if fm.get(k) in (None, "", [])]
        if fm.get("show") not in show_ids:
            errors.append(f"{name}: unknown show '{fm.get('show')}'")
        if not isinstance(fm.get("guests", []), list):
            errors.append(f"{name}: guests must be a list (empty for host-only episodes)")
        errors += [f"{name}: unknown guest '{g}'" for g in fm.get("guests") or [] if g not in people_ids]
        errors += [f"{name}: unknown topic '{t}'" for t in fm.get("topics") or [] if t not in topic_ids]
        for key in ("published_on", "listened_on"):
            try:
                as_date(fm.get(key))
            except (TypeError, ValueError):
                errors.append(f"{name}: {key} is not YYYY-MM-DD")
        if fm.get("listened_precision", "day") not in PRECISIONS:
            errors.append(f"{name}: listened_precision must be one of {sorted(PRECISIONS)}")
        guid = fm.get("guid")
        if guid in guids:
            errors.append(f"{name}: duplicate guid, same episode as {guids[guid]}")
        guids[guid] = name

    for e in errors:
        print("ERROR", e)
    print(f"{len(files)} listens, {len(show_ids)} shows, {len(people_ids)} people, "
          f"{len(topic_ids)} topics: {'OK' if not errors else f'{len(errors)} error(s)'}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
