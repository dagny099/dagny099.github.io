#!/usr/bin/env python3
"""Mechanics for adding a podcast episode to the /listening/ graph.

The add-listen skill (.claude/skills/add-listen/) drives this script; the
conversation decides *which* episode, guests, topics and spark, and this script
does the parts that must be identical every time: Apple lookups, id slugs,
duplicate checks, color slots, and the exact front matter of a _listens file.

Subcommands (all print JSON or the drafted file; nothing is written without --write):
    shows   "<name or id>"                    known show? else Apple search candidates
    episodes <show_id|collectionId> [--match REGEX] [--number N] [--limit K]
    person  "<Full Name>"                     slug + existing matches
    topics                                    the controlled vocabulary
    add-show   --itunes-id N --id SLUG [--name NAME] --hosts a,b [--write]
    add-person --id SLUG --name NAME --bio TEXT --source TEXT [--write]
    add-topic  --id SLUG --label TEXT --description TEXT [--write]
    listen  --show ID --track-id N [--listened-on YYYY-MM-DD] [--precision day|month|year|approximate]
            --guests a,b --topics x,y [--spark TEXT] [--spark-draft] [--notes-file F]
            [--episode-number N] [--write]
    works   ["<title words>"]                 known works (all, or close title matches)
    add-work --title T --type book|article|paper|newsletter|talk [--id SLUG]
            [--authors a,b] [--authors-outside "Name; Name"] [--year N] [--publisher P] [--url U]
            [--isbn N] [--openlibrary OL…W] [--doi D] [--source show_notes|transcript|manual]
            [--listen FILE-SLUG --kind by_guest|discussed|recommended [--by PERSON] [--from-show]]
            [--my-status want_to_read|read] [--write]
            New id: creates the work. Existing id: adds the mention and/or sets my_status.

Requires PyYAML. Network: itunes.apple.com only (catalog lookups live in works_lookup.py).
"""
from __future__ import annotations

import argparse
import datetime
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from itunes_lookup import list_episodes, search_shows  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "_data"
LISTENS = ROOT / "_listens"
MAX_SLOTS = 6  # the validated palette on /listening/ has six show colors
ZERO_WIDTH = re.compile(r"[⁠​‌‍﻿]")


# ---------- small helpers ----------

def out(obj):
    json.dump(obj, sys.stdout, indent=1, ensure_ascii=False)
    print()


def die(msg: str):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def slug_id(text: str) -> str:
    """snake_case id from a name: 'Tim O'Reilly' -> tim_oreilly, 'Dr. Luis Serrano' -> luis_serrano."""
    s = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"\b(dr|prof|mr|mrs|ms)\.?\s+", "", s)
    s = s.replace("'", "").replace("’", "")
    s = re.sub(r"\b[a-z]\.\s+", "", s)  # middle initials
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_")


def file_slug(title: str, words: int = 6) -> str:
    s = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode().lower()
    s = re.sub(r"^\d+:\s*", "", s)
    return "-".join(re.findall(r"[a-z0-9]+", s)[:words])


def clean(s: str | None) -> str:
    return re.sub(r"\s+", " ", ZERO_WIDTH.sub("", s or "")).strip()


def summary(desc: str, sentences: int = 2) -> str:
    """First sentences of the show notes, before sponsor and boilerplate blocks."""
    d = clean(desc)
    d = re.split(r"Additional materials:|Episode notes:|See omnystudio|See Privacy Policy|"
                 r"Interested in sponsoring|— Brought to you by|Brought to you by", d)[0]
    return " ".join(re.split(r"(?<=[.!?])\s+", d)[:sentences]).strip()


def episode_number(title: str) -> int | None:
    for pat in (r"^(\d+)\s*:", r"\bEpisode\s+(\d+)\b", r"\bEp\.?\s*(\d+)\b", r"#(\d+)\b"):
        m = re.search(pat, title, re.I)
        if m:
            return int(m.group(1))
    return None


def load(name: str) -> list[dict]:
    return yaml.safe_load((DATA / name).read_text()) or []


def front_matter(path: Path) -> dict:
    return yaml.safe_load(path.read_text().split("---\n", 2)[1]) or {}


def logged_guids() -> dict[str, str]:
    return {str(front_matter(p).get("guid")): p.name for p in LISTENS.glob("*.md")}


class _Dumper(yaml.SafeDumper):
    pass


_Dumper.add_representer(type(None), lambda d, _: d.represent_scalar("tag:yaml.org,2002:null", ""))


def dump(obj) -> str:
    return yaml.dump(obj, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=1000)


def append_entry(name: str, entry: dict, write: bool) -> str:
    """Append one list item to a _data YAML file without disturbing comments above it."""
    block = dump([entry])
    if write:
        path = DATA / name
        text = path.read_text()
        path.write_text(text + ("" if text.endswith("\n") else "\n") + block)
    return block


def show_record(key: str) -> dict | None:
    key_l = key.lower()
    for s in load("podcast_shows.yml"):
        if key_l in (s["id"], str(s.get("itunes_id")), s["name"].lower()):
            return s
    return None


# ---------- subcommands ----------

def cmd_shows(a):
    known = load("podcast_shows.yml")
    names = {s["name"].lower(): s for s in known}
    close = difflib.get_close_matches(a.term.lower(), list(names), n=3, cutoff=0.55)
    exact = show_record(a.term)
    if exact or close:
        out({"known": [exact] if exact else [names[c] for c in close]})
        return
    out({"known": [], "apple_candidates": search_shows(a.term, limit=5)})


def cmd_episodes(a):
    rec = show_record(a.show)
    cid = rec["itunes_id"] if rec else int(a.show)
    eps = list_episodes(cid, match=a.match)
    if a.number is not None:
        eps = [e for e in eps if episode_number(e["trackName"]) == a.number]
    guids = logged_guids()
    rows = []
    for e in eps[: a.limit]:
        rows.append({
            "trackId": e["trackId"], "date": e["releaseDate"], "minutes": e["minutes"],
            "title": e["trackName"], "episode_number": episode_number(e["trackName"]),
            "already_logged": guids.get(str(e["guid"])),
            "description": clean(e["description"])[:600],
        })
    out({"show": rec["id"] if rec else None, "collectionId": cid, "count": len(rows),
         "note": "Apple returns only the latest 200 episodes" if not rows else None, "episodes": rows})


def cmd_person(a):
    people = load("podcast_people.yml")
    sid = slug_id(a.name)
    exact = [p for p in people if p["id"] == sid]
    close = difflib.get_close_matches(a.name.lower(), [p["name"].lower() for p in people], n=3, cutoff=0.7)
    out({"suggested_id": sid, "exists": bool(exact),
         "similar": [p for p in people if p["name"].lower() in close and p["id"] != sid]})


def cmd_topics(_a):
    out(load("podcast_topics.yml"))


def cmd_add_show(a):
    if show_record(a.id) or show_record(str(a.itunes_id)):
        die(f"show {a.id} / {a.itunes_id} already exists in podcast_shows.yml")
    hits = [r for r in search_shows(a.name or a.id, limit=10) if r["collectionId"] == a.itunes_id]
    meta = hits[0] if hits else {}
    entry = {"id": a.id, "name": a.name or meta.get("collectionName") or a.id,
             "hosts": [h for h in a.hosts.split(",") if h], "itunes_id": a.itunes_id,
             "feed_url": meta.get("feedUrl"),
             "apple_url": f"https://podcasts.apple.com/us/podcast/id{a.itunes_id}"}
    print(append_entry("podcast_shows.yml", entry, a.write))


def cmd_add_person(a):
    if any(p["id"] == a.id for p in load("podcast_people.yml")):
        die(f"person {a.id} already exists")
    print(append_entry("podcast_people.yml", {"id": a.id, "name": a.name, "bio": a.bio, "source": a.source}, a.write))


def cmd_add_topic(a):
    if any(t["id"] == a.id for t in load("podcast_topics.yml")):
        die(f"topic {a.id} already exists")
    print(append_entry("podcast_topics.yml", {"id": a.id, "label": a.label, "description": a.description}, a.write))


def assign_color_slot(show_id: str, write: bool) -> str:
    """Give a show its first color the first time an episode of it is logged."""
    shows = load("podcast_shows.yml")
    rec = next(s for s in shows if s["id"] == show_id)
    if rec.get("color_slot"):
        return f"keeps color_slot {rec['color_slot']}"
    used = {s.get("color_slot") for s in shows if s.get("color_slot")}
    free = [n for n in range(1, MAX_SLOTS + 1) if n not in used]
    if not free:
        return f"no color slot free (all {MAX_SLOTS} used): renders in neutral ink until the palette grows"
    if write:
        path = DATA / "podcast_shows.yml"
        text = path.read_text()
        path.write_text(text.replace(f"- id: {show_id}\n", f"- id: {show_id}\n  color_slot: {free[0]}\n", 1))
    return f"assigned color_slot {free[0]}"


def cmd_listen(a):
    rec = show_record(a.show)
    if not rec:
        die(f"unknown show '{a.show}'; add it first with add-show")
    eps = {e["trackId"]: e for e in list_episodes(rec["itunes_id"])}
    ep = eps.get(a.track_id)
    if not ep:
        die(f"trackId {a.track_id} not in the latest 200 episodes of {rec['id']}")
    dup = logged_guids().get(str(ep["guid"]))
    if dup:
        die(f"already logged as _listens/{dup}")

    people = {p["id"] for p in load("podcast_people.yml")}
    topics = {t["id"] for t in load("podcast_topics.yml")}
    guests = [g for g in (a.guests or "").split(",") if g]
    tops = [t for t in (a.topics or "").split(",") if t]
    hosts_as_guests = [g for g in guests if g in (rec.get("hosts") or [])]
    if hosts_as_guests:
        die(f"{', '.join(hosts_as_guests)} host(s) {rec['id']}; hosts connect through the show, list only guests")
    missing = [f"guest {g}" for g in guests if g not in people] + [f"topic {t}" for t in tops if t not in topics]
    if missing:
        die("add these first: " + ", ".join(missing))

    title = clean(ep["trackName"])
    pub = ep["releaseDate"]
    listened = a.listened_on or datetime.date.today().isoformat()
    datetime.date.fromisoformat(listened)
    fm = {"title": title, "show": rec["id"]}
    num = a.episode_number if a.episode_number is not None else episode_number(title)
    if num is not None:
        fm["episode_number"] = num
    fm.update({
        "published_on": pub, "listened_on": listened, "listened_precision": a.precision,
        "guests": guests, "topics": tops, "duration_min": ep["minutes"] or None,
        "episode_url": ep["url"], "audio_url": ep["audio_url"], "guid": ep["guid"],
        "itunes_track_id": ep["trackId"], "summary": summary(ep["description"]),
        "spark": a.spark or None, "spark_draft": bool(a.spark and a.spark_draft),
    })
    companion = next((e for e in eps.values() if clean(e["trackName"]).lower() == f"takeaway - {title}".lower()), None)
    if companion:
        fm["related_links"] = [{"label": "Takeaway episode", "url": companion["url"]}]
    fm["provenance"] = {"metadata": "itunes", "guests": "confirmed in conversation",
                        "spark": "drafted by Claude" if fm["spark_draft"] else ("mine" if a.spark else "not yet written")}

    notes = Path(a.notes_file).read_text().strip() + "\n" if a.notes_file else ""
    body = "---\n" + dump(fm) + "---\n" + notes
    name = f"{listened}-{rec['id'].replace('_', '-')}-{file_slug(title)}.md"
    slot = assign_color_slot(rec["id"], a.write)
    if a.write:
        (LISTENS / name).write_text(body)
    out({"file": f"_listens/{name}", "written": a.write, "color": slot})
    print(body)


# ---------- works (books, articles, papers... connected to episodes and people) ----------

WORK_TYPES = ["book", "article", "paper", "newsletter", "talk"]
MENTION_KINDS = ["by_guest", "discussed", "recommended"]
MY_STATUS = ["want_to_read", "read"]
WORKS_HEADER = """\
# Works connected to the /listening/ graph: books, articles, papers, newsletters, talks.
# Managed by scripts/listens/add_listen.py (add-work); schema and decisions in
# _planning/works-spike.md. Rewritten whole on every add, so keep notes out of this file.
#
# mentions[].kind:  by_guest (the guest wrote it) | discussed (came up in the episode or
#                   its notes) | recommended (a recommendation segment; `by` names who).
#                   All three count the same.
# from_show: true   the show linking its own content; kept, but drawn quieter.
# source:           show_notes | transcript | manual (added by Barbara, may have no mentions)
# my_status:        want_to_read | read (optional)
"""


class _Flow(dict):
    """A mapping dumped inline, so each mention stays on one line."""


_Dumper.add_representer(_Flow, lambda d, m: d.represent_mapping("tag:yaml.org,2002:map", m, flow_style=True))


def load_works() -> list[dict]:
    path = DATA / "podcast_works.yml"
    return (yaml.safe_load(path.read_text()) or []) if path.exists() else []


def works_text(rows: list[dict]) -> str:
    out_rows = []
    for w in rows:
        w = dict(w)
        if w.get("ids"):
            w["ids"] = _Flow(w["ids"])
        if w.get("mentions"):
            w["mentions"] = [_Flow(m) for m in w["mentions"]]
        out_rows.append(w)
    return WORKS_HEADER + "\n" + dump(out_rows).replace("\n- id:", "\n\n- id:")


def listen_slugs() -> set[str]:
    return {p.stem for p in LISTENS.glob("*.md")}


def cmd_works(a):
    rows = load_works()
    if a.term:
        titles = {w["title"].lower(): w for w in rows}
        close = difflib.get_close_matches(a.term.lower(), list(titles), n=5, cutoff=0.5)
        sub = [w for w in rows if a.term.lower() in w["title"].lower()] or [titles[c] for c in close]
        out({"suggested_id": slug_id(a.term), "matches": sub})
    else:
        out([{"id": w["id"], "title": w["title"], "type": w["type"],
              "mentions": len(w.get("mentions") or [])} for w in rows])


def cmd_add_work(a):
    rows = load_works()
    wid = a.id or (slug_id(a.title) if a.title else None)
    if not wid:
        die("give --title (new work) or --id (existing work)")
    people = {p["id"] for p in load("podcast_people.yml")}
    split = lambda s, sep=",": [x.strip() for x in (s or "").split(sep) if x.strip()]  # noqa: E731

    mention = None
    if a.listen:
        if a.listen not in listen_slugs():
            die(f"no _listens/{a.listen}.md (use the file name without .md)")
        if a.kind not in MENTION_KINDS:
            die(f"--kind must be one of {MENTION_KINDS}")
        if a.kind == "recommended" and not a.by:
            die("a recommended mention needs --by <person id> (who recommended it)")
        if a.by and a.by not in people:
            die(f"--by {a.by} is not in podcast_people.yml; add the person first")
        mention = {"listen": a.listen, "kind": a.kind}
        if a.by:
            mention["by"] = a.by
        if a.from_show:
            mention["from_show"] = True
    elif a.kind or a.by or a.from_show:
        die("--kind/--by/--from-show describe a mention; give --listen too")

    existing = next((w for w in rows if w["id"] == wid), None)
    if existing:
        if mention:
            if any(m["listen"] == a.listen for m in existing.get("mentions") or []):
                die(f"{wid} already has a mention for {a.listen}")
            existing.setdefault("mentions", []).append(mention)
        if a.my_status:
            existing["my_status"] = a.my_status
        if not (mention or a.my_status):
            die(f"work {wid} already exists; pass --listen to add a mention or --my-status to mark it")
        entry, action = existing, "updated"
    else:
        if not (a.title and a.type):
            die("a new work needs --title and --type")
        authors = split(a.authors)
        unknown = [p for p in authors if p not in people]
        if unknown:
            die(f"--authors must be person ids in podcast_people.yml ({', '.join(unknown)}); "
                "use --authors-outside for people not on the graph")
        if a.source == "manual" and not mention and not authors:
            print("note: a manual work with no mention and no on-graph author won't appear on the graph",
                  file=sys.stderr)
        entry = {"id": wid, "title": a.title, "type": a.type}
        if authors:
            entry["authors"] = authors
        if a.authors_outside:
            entry["authors_outside"] = split(a.authors_outside, ";")
        for key in ("year", "publisher", "url"):
            if getattr(a, key):
                entry[key] = getattr(a, key)
        ids = {k: getattr(a, k) for k in ("isbn", "openlibrary", "doi") if getattr(a, k)}
        if ids:
            entry["ids"] = ids
        entry["source"] = a.source
        if a.my_status:
            entry["my_status"] = a.my_status
        if mention:
            entry["mentions"] = [mention]
        rows.append(entry)
        action = "created"

    if a.write:
        (DATA / "podcast_works.yml").write_text(works_text(rows))
    out({"work": wid, "action": action, "written": a.write})
    print(dump([entry]))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("shows"); p.add_argument("term"); p.set_defaults(fn=cmd_shows)
    p = sub.add_parser("episodes"); p.add_argument("show"); p.add_argument("--match")
    p.add_argument("--number", type=int); p.add_argument("--limit", type=int, default=8); p.set_defaults(fn=cmd_episodes)
    p = sub.add_parser("person"); p.add_argument("name"); p.set_defaults(fn=cmd_person)
    p = sub.add_parser("topics"); p.set_defaults(fn=cmd_topics)
    p = sub.add_parser("add-show"); p.add_argument("--itunes-id", type=int, required=True)
    p.add_argument("--id", required=True); p.add_argument("--name"); p.add_argument("--hosts", default="")
    p.add_argument("--write", action="store_true"); p.set_defaults(fn=cmd_add_show)
    p = sub.add_parser("add-person")
    for f in ("--id", "--name", "--bio", "--source"):
        p.add_argument(f, required=True)
    p.add_argument("--write", action="store_true"); p.set_defaults(fn=cmd_add_person)
    p = sub.add_parser("add-topic")
    for f in ("--id", "--label", "--description"):
        p.add_argument(f, required=True)
    p.add_argument("--write", action="store_true"); p.set_defaults(fn=cmd_add_topic)
    p = sub.add_parser("listen"); p.add_argument("--show", required=True); p.add_argument("--track-id", type=int, required=True)
    p.add_argument("--listened-on"); p.add_argument("--precision", default="day", choices=["day", "month", "year", "approximate"])
    p.add_argument("--guests", default=""); p.add_argument("--topics", default="")
    p.add_argument("--spark"); p.add_argument("--spark-draft", action="store_true"); p.add_argument("--notes-file")
    p.add_argument("--episode-number", type=int); p.add_argument("--write", action="store_true"); p.set_defaults(fn=cmd_listen)
    p = sub.add_parser("works"); p.add_argument("term", nargs="?"); p.set_defaults(fn=cmd_works)
    p = sub.add_parser("add-work"); p.add_argument("--id"); p.add_argument("--title")
    p.add_argument("--type", choices=WORK_TYPES); p.add_argument("--authors"); p.add_argument("--authors-outside")
    p.add_argument("--year", type=int); p.add_argument("--publisher"); p.add_argument("--url")
    p.add_argument("--isbn"); p.add_argument("--openlibrary"); p.add_argument("--doi")
    p.add_argument("--source", default="show_notes", choices=["show_notes", "transcript", "manual"])
    p.add_argument("--listen"); p.add_argument("--kind", choices=MENTION_KINDS); p.add_argument("--by")
    p.add_argument("--from-show", action="store_true"); p.add_argument("--my-status", choices=MY_STATUS)
    p.add_argument("--write", action="store_true"); p.set_defaults(fn=cmd_add_work)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
