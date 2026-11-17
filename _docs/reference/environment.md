# Environment

Things that cost a session time before they were written down.

## Python

The site scripts need PyYAML. On this machine the system `python3` does not have it;
the pyenv interpreter does:

```bash
~/.pyenv/versions/3.10.12/bin/python3 scripts/listens/validate.py
```

In zsh, a variable holding a command with arguments (`A="python add_listen.py"`) is not
word-split, so `$A shows x` fails with "no such file or directory". Use a function:

```bash
A() { ~/.pyenv/versions/3.10.12/bin/python3 scripts/listens/add_listen.py "$@"; }
A shows "practical ai"
```

The private intake tests run under a newer interpreter (3.14 bytecode is in the repo's
cache); they have no dependencies.

## Jekyll

```bash
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 bundle exec jekyll build
LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 bundle exec jekyll serve
```

Ruby defaults to ASCII without the locale and the build fails on non-ASCII content.
In a cloud session there is more: `bundle exec jekyll` cannot find the binary, the
GitHub metadata plugin calls an API the proxy blocks, and cdnjs is blocked. The pilot
plan's "Building locally in a cloud session" section has the stub-API recipe.

## Network

| Host | Needed by | Status |
|---|---|---|
| `itunes.apple.com` | show and episode lookups | Allowed in the cloud environment; about 20 calls a minute |
| podcast RSS hosts | episodes older than Apple's 200 | Blocked in the cloud environment; fine locally and in GitHub Actions |
| `openlibrary.org` | book metadata | Allowed after allowlisting; drops about one request in three |
| `api.crossref.org` | paper metadata | Keyless; the paper fallback |
| `api.openalex.org` | papers | Needs a key now |

## Git and GitHub

- No `gh` CLI locally. PRs are opened through the browser pane on github.com after
  signing in, or by the GitHub tool in a cloud session.
- Branches are cut from `origin/master` and named `listen/<slug>`; `master` is never
  pushed to directly.
- CLAUDE.md asks before commits, pushes, deletions, and changes to `_config.yml` or the
  `Gemfile`.

## MkDocs (these docs)

```bash
~/miniconda3/bin/mkdocs build --strict
~/miniconda3/bin/mkdocs serve
```

MkDocs Material 9.6 is installed under miniconda, not pyenv. Source is `_docs/`,
output `_docs_site/` (gitignored).
