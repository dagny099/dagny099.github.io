---
layout: single
title: "Implementing Structured Metadata on a Jekyll + GitHub Pages Site"
description: "A step-by-step guide to turning a metadata audit into shipped reality: choosing a canonical home for your site, emitting clean structured data from a _data file, wiring per-content-type schema, and verifying it all against the tools each reader uses."
date: 2026-03-18
categories: [website-building, tutorials]
tags: [jekyll, github-pages, metadata, structured-data, json-ld, seo, dns]
image: /assets/images/posts/metadata-implementation-hero.png
---

This is the hands-on companion to [*The Three Readers of Your Web Page*]({% post_url 2026-03-12-three-readers-of-your-web-page %}). That piece explained *why* the page `<head>` serves three different audiences. This one is the *how* — the specific, ordered changes that take a Jekyll site on GitHub Pages from "decent metadata" to "legible to machines and consistent everywhere."

For the bigger-picture case behind all of this, see [*Why Metadata Matters*]({% post_url 2025-11-7-metadata-matters %}). And if you're still assembling the underlying stack, my *Digital Home Base Workshop* series covers the groundwork: [getting started with GitHub Pages]({% post_url 2024-07-28-kickstart-web-portfolio-gh-pages-website-series %}), [understanding the Jekyll build]({% post_url 2024-07-31-what-does-jekyll-do-website-series %}), and [automating deploys with GitHub Actions]({% post_url 2024-08-13-auto-deploy-jekyll-w-gh-actions-website-series %}).

A note for your own sanity before we start: several code blocks below contain Liquid (the `{% raw %}{{ ... }}{% endraw %}` and `{% raw %}{% ... %}{% endraw %}` syntax). In this article they're wrapped in Jekyll's `{% raw %}{% raw %}{% endraw %}` tags so they display literally instead of executing at build time. When you copy them into your *own* templates, drop the `raw` wrapper — you want Jekyll to actually run them there.

We'll go in order of leverage: fix what's invisible and structural first, then add understanding, then polish, then verify.

## Step 0 — Audit your own `<head>`
{: #audit-your-head}

Before you can improve the `<head>`, it helps to see the whole thing at once: which template and data files inject which tags. Here's that map for *this very site* as it stands today — the "before" the rest of this guide builds on.

{% include figure image_path="/assets/diagrams/head-architecture-v2.svg" alt="Diagram of how this site's <head> is assembled. The theme default.html layout includes head.html and head/custom.html; those include seo.html, schema.html, and schema-jsonld.html. Each include is annotated with the literal meta, link, and script tags it injects. They are fed by _config.yml, page front matter, and _data/portfolio.json, with external CDNs loaded directly." caption="How this site's `<head>` is assembled end to end — every include and data file, and the exact tags each one injects. ([full SVG]({{ '/assets/diagrams/head-architecture-v2.svg' | relative_url }})) This reflects the *current* wiring; the steps below evolve some of these pieces." class="align-center" %}

Before changing anything, look at what you already emit. View source on your homepage (or use your browser's dev tools) and find these. For each, ask the question in the second column:

- `<title>` and `<meta name="description">` — present, unique per page, and human-written?
- `<link rel="canonical">` — present, and does its host match the host actually serving the page?
- `robots` — are you accidentally `noindex`-ing anything you want found?
- The `og:` set — title, description, image, url, type, site_name?
- Structured data — any `<script type="application/ld+json">` at all?

The most common findings on an otherwise-healthy personal site are: no structured data, an inconsistency between the canonical host and the served host, and `og:` tags that exist but lack image dimensions. We'll fix exactly those.

## Step 1 — Choose and enforce one canonical home

This is the invisible structural fix, so it goes first. If both `https://yourdomain.com` and `https://www.yourdomain.com` serve your site and each claims to be canonical, you're quietly asking the search engine to guess which one is real — splitting your signals across two identities. Pick one. (I chose the bare apex, `barbhs.com`.)

On a Jekyll + GitHub Pages setup, this lives in three places that must agree:

**1a. `_config.yml`** — set the one true home:

```yaml
url: "https://barbhs.com"   # no www, no trailing slash
```

Everything downstream derives from this, so getting it right here makes the rest automatic.

**1b. GitHub Pages** — in your repo, go to Settings → Pages → Custom domain and set it to your apex (`barbhs.com`, no `www`). Saving this commits a `CNAME` file to your source branch containing that domain. GitHub then **automatically redirects** the `www` host to the apex — you don't write the redirect yourself. (If the field currently shows `www.barbhs.com`, simply changing it to the apex flips the direction of the redirect.)

**1c. Your DNS provider** — this is where the domain's records live (for me, that's Squarespace, which now manages former Google Domains). In the DNS / Custom Records area, ensure:

- Four **A records**, Host `@`, pointing the apex at GitHub Pages: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
- Four **AAAA records**, Host `@` (for IPv6): `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
- One **CNAME record**, Host `www`, pointing to `<your-username>.github.io`

Remove any stale `@` or `www` records that point elsewhere, and disable any registrar-level "domain forwarding," which would fight GitHub's redirect. Leave unrelated subdomains (`docs`, `twin`, etc.) untouched — they're separate records.

Then wait for propagation (minutes to hours) and tick **Enforce HTTPS** in Settings → Pages. Verify from a terminal:

```bash
dig barbhs.com +noall +answer -t A        # should list the four GitHub IPs
curl -sI https://www.barbhs.com | grep -i location   # should 301 to https://barbhs.com/
```

Because every URL your templates emit is built from `_config.yml`'s `url` via the `absolute_url` filter, your `canonical` and `og:url` tags are now guaranteed to point at the same host the server actually serves. One decision, enforced everywhere.

## Step 2 — Emit your site identity graph

Now the highest-value *addition*: telling the search engine what kind of thing your site is about. The key fact that resolves most confusion: **structured data is not a file the crawler fetches separately — it must be inlined into each page's HTML**, inside a `<script type="application/ld+json">` block.

On this site that lives in `_includes/schema-jsonld.html`, wired into the `<head>` from `_includes/head/custom.html` (trace it in the diagram above). One file, three conditional blocks depending on the page.

**2a. The homepage identity graph.** On the home page only, it emits a single `@graph` describing the site as a `WebSite` published by a `Person` — the canonical node every other page will point back to. The identity is hand-authored inline (the one thing worth curating by hand), while `site.url` and `site.description` come from `_config.yml`:

{% raw %}
```liquid
{% assign site_url   = site.url | default: "https://barbhs.com" %}
{% assign person_id  = site_url | append: "/#person" %}

{% if page.url == "/" %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    { "@type": "WebSite", "@id": "{{ site_url }}/#website",
      "publisher": { "@id": "{{ person_id }}" }, "inLanguage": "en" },
    {
      "@type": "Person",
      "@id": "{{ person_id }}",
      "name": "Barbara Hidalgo-Sotelo",
      "honorificSuffix": "PhD",
      "jobTitle": ["Cognitive Scientist", "Data Scientist", "Applied AI Consultant"],
      "alumniOf": [
        { "@type": "CollegeOrUniversity", "name": "Massachusetts Institute of Technology" },
        { "@type": "CollegeOrUniversity", "name": "The University of Texas at Austin" }
      ],
      "sameAs": [
        "https://www.linkedin.com/in/barbara-hidalgo-sotelo/",
        "https://github.com/dagny099",
        "https://scholar.google.com/citations?user=nQG25vkAAAAJ",
        "https://sensemaking-ai.com"
      ],
      "worksFor": { "@type": "Organization", "name": "Sensemaking AI" }
    },
    { "@type": "SiteNavigationElement", "name": "Main Navigation", "hasPart": [ ... ] }
  ]
}
</script>
{% endif %}
```
{% endraw %}

That stable `#person` `@id` is the spine of the whole strategy: it's the single entity every article and project references, so your scattered web presence reconciles to one node. (`sameAs` is the part worth investing in — it's how the engine merges your site, GitHub, LinkedIn, and Scholar into the same person.)

**2b. Breadcrumbs on every inner page.** When `page.url != "/"`, the same file splits the URL into segments and emits a `BreadcrumbList`, so a result can show a `Home › Section › Page` trail instead of a bare string.

**2c. The projects list — straight from a `_data` file.** This is where the single-source-of-truth pattern earns its keep. On `/projects/`, the file loops over `_data/portfolio.json` and emits an `ItemList` of `SoftwareApplication`s, each pointing its `author` back at `#person`:

{% raw %}
```liquid
{% if page.url == "/projects/" and site.data.portfolio.projects %}
<script type="application/ld+json">
{ "@context": "https://schema.org", "@type": "ItemList",
  "numberOfItems": {{ site.data.portfolio.projects | size }},
  "itemListElement": [
    {% for p in site.data.portfolio.projects %}
    { "@type": "ListItem", "position": {{ forloop.index }},
      "item": {
        "@type": "SoftwareApplication",
        "name": {{ p.name | jsonify }},
        "description": {{ p.tagline | default: p.summary | jsonify }},
        "author": { "@id": "{{ person_id }}" }
      }
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ]
}
</script>
{% endif %}
```
{% endraw %}

The `jsonify` filter re-serializes each value into guaranteed-valid JSON — no hand-quoting, no escaping bugs — so the project data you already maintain in `_data/portfolio.json` becomes structured data for free. Edit the data in one place; the schema regenerates on build.

> **An honest trade-off.** The *identity* block above is authored inline rather than pulled from a `_data/person.json`. That's deliberate — it's one block, edited rarely. But if you'd rather keep identity in a data file too (the more DRY option), the projects pattern shows exactly how: move the object into `_data/person.json` and inline it with `{% raw %}{{ site.data.person | jsonify }}{% endraw %}`.

## Step 3 — Add per-content-type schema

The unlock that keeps this simple: **a page may carry several `ld+json` blocks, and the engine merges them.** The identity block from Step 2 describes *you*; a second, page-level block describes *this page*. On this site that page-level block lives in `_includes/schema.html`, included from `_includes/head.html`. Rather than a separate partial per content type, it decides the page's type once and branches internally:

{% raw %}
```liquid
{% assign is_project = false %}
{% if page.layout == 'project' or page.collection == 'projects' %}{% assign is_project = true %}{% endif %}
{% assign is_tutorial = false %}
{% if page.tags contains 'tutorial' %}{% assign is_tutorial = true %}{% endif %}
```
{% endraw %}

**3a. Dated writing → `Article` (or `HowTo`).** Any page with a `date` that isn't a project emits an `Article` — or a `HowTo` when it's tagged `tutorial` — with both `author` and `publisher` pointing back at the same `#person`:

{% raw %}
```liquid
{% if page.date and is_project != true %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": {% if is_tutorial %}"HowTo"{% else %}"Article"{% endif %},
  "headline": {{ page.title | jsonify }},
  "description": {{ page_description | jsonify }},
  "datePublished": {{ page.date | date_to_xmlschema | jsonify }},
  "dateModified": {{ page.last_modified_at | default: page.date | date_to_xmlschema | jsonify }},
  "author":    { "@id": "{{ person_id }}" },
  "publisher": { "@id": "{{ person_id }}" }
}
</script>
{% endif %}
```
{% endraw %}

**3b. Projects → `SoftwareSourceCode`.** Project pages get a `SoftwareSourceCode` block instead, deriving `programmingLanguage` and `about` from each project's `stack` front matter and `creativeWorkStatus` from its `status`:

{% raw %}
```liquid
{% if is_project == true %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareSourceCode",
  "name": {{ page.title | jsonify }},
  "author":  { "@id": "{{ person_id }}" },
  "creator": { "@id": "{{ person_id }}" },
  {% if page.stack %}"programmingLanguage": [{% for tech in page.stack %}{{ tech | jsonify }}{% unless forloop.last %},{% endunless %}{% endfor %}],{% endif %}
  {% if page.status %}"creativeWorkStatus": {{ page.status | jsonify }}{% endif %}
}
</script>
{% endif %}
```
{% endraw %}

Two footguns to internalize, because they cause every broken JSON-LD block I've ever seen. First, wrap every *value* in `{% raw %}| jsonify{% endraw %}` rather than hand-typing quotes — a title containing an apostrophe or a quotation mark will silently corrupt naked `"{% raw %}{{ page.title }}{% endraw %}"`. Second, the only property that must *not* end in a comma is the last one; notice how `schema.html` keeps a conditional field's trailing comma *inside* its `{% raw %}{% if %}{% endraw %}` so the comma vanishes cleanly when the field is absent.

**3c. Where it all attaches.** Unlike a data-driven include, `schema.html` is a single file that branches internally, so the layout includes it just once. The two structured-data files hook into the head at different points:

{% raw %}
```liquid
<!-- _includes/head.html -->
{% include seo.html %}
{% include schema.html %}

<!-- _includes/head/custom.html -->
{% include schema-jsonld.html %}
```
{% endraw %}

Index pages (tags, categories) have no `date` and aren't projects, so they match neither branch and emit no page-level block — the identity graph alone is enough.

## Step 4 — Centralize the ordinary meta in `seo.html`

The everyday `<head>` furniture — title, description, canonical, and the Open Graph / Twitter tags — is centralized in `_includes/seo.html` (a customized version of the Minimal Mistakes default), included from `head.html`. One file produces correct, consistent tags for every page from front matter, with site-level fallbacks. Near the top it derives a few variables once, then spends them:

{% raw %}
```liquid
{% if page.date %}{% assign og_type = "article" %}{% else %}{% assign og_type = "website" %}{% endif %}
{% assign canonical_url = page.url | replace: "index.html", "" | absolute_url %}

<title>{{ seo_title | default: site.title }}</title>
<meta name="description" content="{{ seo_description }}">
<link rel="canonical" href="{{ canonical_url }}">

<meta property="og:type" content="{{ og_type }}">
<meta property="og:title" content="{{ page.title | default: site.title }}">
<meta property="og:url" content="{{ canonical_url }}">
<meta property="og:image" content="{{ page_large_image }}">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{ page.title | default: site.title }}">
<meta name="twitter:image" content="{{ page_large_image }}">
```
{% endraw %}

(`seo_description` and `page_large_image` are likewise resolved up top — description falls back from `page.description` to `page.excerpt` to `site.description`; the image from `page.header.og_image` to `overlay_image` to a site default.) Because `canonical_url` is built with `absolute_url` from `_config.yml`'s `url`, your canonical-host decision in Step 1 propagates to every tag on every page for free. This is the payoff of doing Step 1 first.

## Step 5 — Upgrade `knowsAbout` to linked data

`knowsAbout` is a property on your Person that disambiguates *what kind of expert you are*. Its job isn't ranking — it's helping the engine place your entity in conceptual space. So keep it to a tight, honest set of genuine throughlines, not a keyword pile (a bloated list reads as spam and dilutes the signal).

The plain version is a list of strings — which is exactly what this site emits today (see the `knowsAbout` array in `_includes/schema-jsonld.html`). The better version — and the one worth doing if you care about linked data — gives each concept a `sameAs` edge to its canonical encyclopedic identity, turning a bare label into a node in the global graph. Here's the upgrade for that same Person object:

```json
"knowsAbout": [
  { "@type": "Thing", "name": "Knowledge graphs",
    "sameAs": "https://en.wikipedia.org/wiki/Knowledge_graph" },
  { "@type": "Thing", "name": "Retrieval-augmented generation",
    "sameAs": "https://en.wikipedia.org/wiki/Retrieval-augmented_generation" },
  { "@type": "Thing", "name": "Knowledge representation",
    "sameAs": "https://en.wikipedia.org/wiki/Knowledge_representation_and_reasoning" },
  { "@type": "Thing", "name": "Semantic Web",
    "sameAs": "https://en.wikipedia.org/wiki/Semantic_Web" },
  { "@type": "Thing", "name": "Ontology design",
    "sameAs": "https://en.wikipedia.org/wiki/Ontology_(information_science)" },
  { "@type": "Thing", "name": "Cognitive science",
    "sameAs": "https://en.wikipedia.org/wiki/Cognitive_science" },
  { "@type": "Thing", "name": "Data visualization",
    "sameAs": "https://en.wikipedia.org/wiki/Data_and_information_visualization" }
]
```

A few notes on getting this right. Confirm each `sameAs` URL actually resolves before shipping — a 404 identifier is worse than none. For the most stable, language-independent identity, you can upgrade each `sameAs` from a Wikipedia URL to its **Wikidata** entity URI (the `Q`-number): open the Wikipedia article, click "Wikidata item" in the sidebar, and use that `https://www.wikidata.org/wiki/Q…` URL instead. Wikidata is itself a knowledge graph, so this is the most semantically correct form — you're linking your `knowsAbout` edges to canonical nodes rather than to encyclopedia articles *about* those nodes. Whichever you choose, I'd keep the list short: the handful of concepts you actually want to be *known for*, not an inventory of every tool you've touched.

## Step 6 — Polish the social preview

These tags don't affect ranking; they make shared links render reliably and look intentional. `seo.html` already emits the `twitter:` set and `og:image`; the piece it's missing is the image *dimensions* that let a platform reserve space before the image even downloads. Add to `seo.html`:

{% raw %}
```liquid
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png">
<meta property="og:image:alt" content="{{ page.image_alt | default: site.title }}">
```
{% endraw %}

Confirm your share image is genuinely 1200×630 (the ideal ratio); if it isn't, the declared dimensions will lie to the unfurler and the card may render oddly. The width/height tags let a platform reserve the right space *before* fetching the image, so the card renders without a layout jump; `twitter:card` set to `summary_large_image` is what earns you the large banner on X instead of a small thumbnail.

## Step 7 — Confirm the boring infrastructure

Two files quietly determine whether you're crawlable at all. The first is the sitemap: the `jekyll-sitemap` plugin — already in this site's `_config.yml` — generates `sitemap.xml` on every build, no maintenance required:

```yaml
# _config.yml
plugins:
  - jekyll-sitemap
```

The second is `robots.txt`, and here's a nuance worth knowing: `jekyll-sitemap` already generates a minimal one for you at build time, containing just the `Sitemap:` line — so you're covered by default. You only need to author your own if you want explicit crawl rules. The catch: the moment a source `robots.txt` exists, it *replaces* the generated one, so you must include the sitemap line yourself:

```
User-agent: *
Allow: /
Sitemap: https://barbhs.com/sitemap.xml
```

Then submit the sitemap once in Google Search Console (Sitemaps → enter `sitemap.xml`). Search Console is also your ongoing source of truth for which pages are actually indexed — worth checking back after these changes propagate.

## Step 8 — Verify against each reader's own tool

Don't trust; test. Each of the three readers has an inspector, so check your work against the machine that actually parses the tag rather than against your assumptions.

- **Structured data & indexing:** the [Rich Results Test](https://search.google.com/test/rich-results) validates your JSON-LD and shows what was parsed; Search Console's URL Inspection shows the rendered `<head>` the crawler actually saw, plus index status.
- **LinkedIn preview:** the [Post Inspector](https://www.linkedin.com/post-inspector/) renders your card *and* clears LinkedIn's cache — important, because platforms cache previews aggressively, and without a re-scrape your old gray rectangle persists for days.
- **General Open Graph:** the [Facebook Sharing Debugger](https://developers.facebook.com/tools/debug/) does the same for the broader OG ecosystem.
- **The literal tags Google sees:** Search Console → URL Inspection → View crawled page.

A good final habit: after you ship `og:` changes, run the LinkedIn and Facebook inspectors once each to force a fresh scrape, then paste your own link into a real Slack or LinkedIn draft to see the card the way a visitor will.

## The shape of what you built

Step back and notice the structure. Your *identity* lives in one curated block and your *project data* in one `_data` file. Your *rendering logic* lives in a few small, named partials — `seo.html`, `schema.html`, `schema-jsonld.html`. Your *canonical host* is decided once and propagates everywhere through `absolute_url`. Each content type contributes its own schema while pointing back at a single Person node, so your whole site resolves to one trusted entity rather than a scatter of anonymous pages. That's not just good for search — it's the same separation of source-of-truth from presentation that makes any project pleasant to maintain. The metadata got better, and the repo got *cleaner*. That's the version worth shipping.
