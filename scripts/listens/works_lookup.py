#!/usr/bin/env python3
"""Catalog metadata for works mentioned on the /listening/ graph.

Lookups always start from a title someone chose (from the show notes, or Barbara).
Never list a person's works from an author record: catalogs merge namesakes (see
_planning/works-spike.md, section 2). The catalog only fills in year, identifiers
and a link, and the caller checks that the catalog's author matches.

    books:  Open Library title search (no key; drops some requests, so it retries)
    papers: Crossref bibliographic search (no key)

Usage:
    python3 scripts/listens/works_lookup.py book "Thinking in Systems" --author Meadows
    python3 scripts/listens/works_lookup.py paper "Ironies of Automation" --author Bainbridge
"""
import argparse
import json
import sys
import time
import urllib.parse
import urllib.request

UA = {"User-Agent": "barbhs.com listening graph (https://barbhs.com/listening/)"}


def get(url, params):
    full = f"{url}?{urllib.parse.urlencode(params)}"
    for attempt in range(5):
        try:
            with urllib.request.urlopen(urllib.request.Request(full, headers=UA), timeout=30) as resp:
                return json.load(resp)
        except Exception as exc:  # noqa: BLE001 - network hiccup or rate limit; retry
            print(f"retry {attempt + 1}: {exc}", file=sys.stderr)
            time.sleep(2 + 2 * attempt)
    raise RuntimeError(f"lookup failed: {full}")


def author_matches(names, author):
    return not author or any(author.lower() in (n or "").lower() for n in names)


def books(title, author=None, limit=5):
    d = get("https://openlibrary.org/search.json", {
        "title": title, "author": author or "", "limit": limit,
        "fields": "key,title,author_name,first_publish_year,isbn"})
    rows = []
    for doc in d.get("docs", []):
        isbns = doc.get("isbn") or []
        rows.append({
            "title": doc.get("title"), "authors": doc.get("author_name") or [],
            "year": doc.get("first_publish_year"),
            "openlibrary": doc["key"].rsplit("/", 1)[-1],
            "isbn": next((i for i in isbns if len(i) == 13), isbns[0] if isbns else None),
            "url": f"https://openlibrary.org{doc['key']}",
            "author_match": author_matches(doc.get("author_name") or [], author),
        })
    return rows


def papers(title, author=None, limit=5):
    params = {"query.bibliographic": title, "rows": limit,
              "select": "DOI,title,author,issued,container-title"}
    if author:
        params["query.author"] = author
    d = get("https://api.crossref.org/works", params)
    rows = []
    for it in d.get("message", {}).get("items", []):
        names = [" ".join(filter(None, (a.get("given"), a.get("family")))) for a in it.get("author", [])]
        parts = (it.get("issued") or {}).get("date-parts") or [[None]]
        rows.append({
            "title": (it.get("title") or [None])[0], "authors": names, "year": parts[0][0],
            "venue": (it.get("container-title") or [None])[0], "doi": it.get("DOI"),
            "url": f"https://doi.org/{it['DOI']}" if it.get("DOI") else None,
            "author_match": author_matches(names, author),
        })
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("kind", choices=["book", "paper"])
    ap.add_argument("title")
    ap.add_argument("--author", help="surname to check the catalog's author against")
    ap.add_argument("--limit", type=int, default=5)
    a = ap.parse_args()
    rows = (books if a.kind == "book" else papers)(a.title, a.author, a.limit)
    json.dump(rows, sys.stdout, indent=1, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
