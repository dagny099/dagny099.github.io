# Publishing and review

The pull request is the review gate. Nothing about the graph changes on the live site
until I merge.

## Branch, commit, PR

```bash
git fetch origin master
git checkout -b listen/<first-file-slug> origin/master
```

- Stage only what changed: new `_listens/` files and the edited `_data/podcast_*.yml`
  files. Unrelated working-tree changes stay out of the commit.
- Commit message: `Add listen: <Show> — <episode title>`, or for a batch
  `Add N listens: <shows>`, plus whatever attribution lines the environment requires.
- Push and open a PR against `master`. Body: one line per episode (show, title,
  listened date), then new shows, people and topics, then any draft sparks I still
  need to rewrite, then anything the session wants me to look at.
- The PR message ends with the episode's future URL: `/listening/<file name>/`.

Never push to `master` directly.

!!! note "No gh on this machine"
    The GitHub CLI is not installed locally, so a local session opens the PR through the
    browser pane on github.com's compare page after I sign in. A cloud session uses the
    GitHub tool instead.

## What the Pages workflow does

`.github/workflows/pages.yml` runs on every push to `master` and on every pull request
against it. Both run `bundle exec jekyll build`. Only the push to `master` uploads the
artifact and deploys; a PR is a build check and nothing more.

That distinction was a fix. Until 7 October 2026 the deploy steps ran on pull requests
too, so a PR went live as soon as its build passed. For a workflow whose PRs are the
review step, that defeated the point.

## What merging does

Jekyll rebuilds the site. The listens collection renders every `_listens/` file at
`/listening/<name>/` with the `listen` layout, and the Liquid template regenerates
`assets/data/listens-graph.json`. The graph page fetches that file, so the new episode
is on the graph the next time the page loads.

## Review checklist

What I look at in a listen PR, in order:

- [ ] Right episode (title and date match what I remember).
- [ ] Guests are guests, with bios that say what the description says.
- [ ] Topics are the central one to three, not everything touched.
- [ ] Spark is mine, or empty, or flagged as a draft.
- [ ] New show has the right hosts and, if a slot was free, a colour.
- [ ] Any works are titled, catalogued by title, with the right author.
- [ ] Moments carry position and chapter only.

## These docs

This documentation is built with MkDocs Material from `_docs/` into `_docs_site/`,
which is gitignored:

```bash
mkdocs build --strict
```

Jekyll ignores `_docs/` because of the leading underscore, so the markdown here never
renders on barbhs.com by accident. Hosting the built site (at `docs.barbhs.com/listening/`,
matching the other project docs, or under the Pages build) is a separate step that
touches the deploy workflow, and is not done yet.
