#!/usr/bin/env python3
"""Resolve podcasts and episodes through Apple's iTunes Search API.

One allowlisted domain (itunes.apple.com) covers show search, feed URLs and
the most recent 200 episodes per show, so no RSS host needs to be reachable.
Apple rate-limits to roughly 20 calls a minute; calls retry with backoff.

Usage:
    python3 scripts/listens/itunes_lookup.py show "superdatascience"
    python3 scripts/listens/itunes_lookup.py episodes 1163599059 --match "Katie Malone"
"""
import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request

API = "https://itunes.apple.com"


def get(path, params):
    url = f"{API}/{path}?{urllib.parse.urlencode(params)}"
    for attempt in range(3):
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                return json.load(resp).get("results", [])
        except Exception as exc:  # noqa: BLE001 - network or rate limit; retry
            print(f"retry {attempt + 1}: {exc}", file=sys.stderr)
            time.sleep(5 * (attempt + 1))
    return []


def search_shows(term, limit=5):
    rows = get("search", {"term": term, "media": "podcast", "entity": "podcast", "limit": limit})
    return [{k: r.get(k) for k in ("collectionId", "collectionName", "artistName", "feedUrl",
                                   "trackCount", "releaseDate")} for r in rows]


def list_episodes(collection_id, match=None, limit=200):
    rows = get("lookup", {"id": collection_id, "entity": "podcastEpisode", "limit": limit})
    eps = [r for r in rows if r.get("wrapperType") == "podcastEpisode"]
    if match:
        rx = re.compile(match, re.I)
        eps = [e for e in eps if rx.search(e["trackName"]) or rx.search(e.get("description", ""))]
    return [{"trackName": e["trackName"], "releaseDate": e["releaseDate"][:10],
             "minutes": round((e.get("trackTimeMillis") or 0) / 60000),
             "guid": e.get("episodeGuid"), "trackId": e["trackId"],
             "url": re.sub(r"[&?]uo=\d+$", "", e.get("trackViewUrl", "")),
             "audio_url": e.get("episodeUrl"), "description": e.get("description", "")}
            for e in eps]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("show", help="search shows by name")
    s.add_argument("term")
    e = sub.add_parser("episodes", help="list a show's recent episodes")
    e.add_argument("collection_id", type=int)
    e.add_argument("--match", help="regex over title and description")
    args = ap.parse_args()
    out = search_shows(args.term) if args.cmd == "show" else list_episodes(args.collection_id, args.match)
    json.dump(out, sys.stdout, indent=1, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
