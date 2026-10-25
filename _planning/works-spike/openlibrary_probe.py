"""Open Library probe used in the works spike (2026-10-08). Retries because the endpoint drops ~1 in 3 requests from cloud sessions."""
import json, sys, time, urllib.parse, urllib.request
def get(path, **params):
    url = f"https://openlibrary.org{path}?{urllib.parse.urlencode(params)}"
    for attempt in range(5):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(2 + 2 * attempt)
    raise RuntimeError(f"failed: {url}")
def authors(name, n=8):
    d = get("/search/authors.json", q=name, limit=n)
    return d["numFound"], [{k: a.get(k) for k in ("key", "name", "top_work", "work_count", "birth_date", "top_subjects")} for a in d["docs"]]
def works_by_title(title, n=5):
    d = get("/search.json", title=title, limit=n, fields="key,title,author_name,author_key,first_publish_year,isbn,publisher")
    return d["numFound"], d["docs"]
def author_works(key, n=50):
    d = get(f"/authors/{key}/works.json", limit=n)
    return d.get("size"), [w["title"] for w in d["entries"]]
