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

A note for your own sanity before we start: several code blocks below contain Liquid (the `{% raw %}{{ ... }}{% endraw %}` and `{% raw %}{% ... %}{% endraw %}` syntax). In this article they're wrapped in Jekyll's `{% raw %}{% raw %}{% endraw %}` tags so they display literally instead of executing at build time. When you copy them into your *own* templates, drop the `raw` wrapper — you want Jekyll to actually run them there.

We'll go in order of leverage: fix what's invisible and structural first, then add understanding, then polish, then verify.

## Step 0 — Audit your own `<head>`

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

## Step 2 — Emit structured data from a `_data` file

Now the highest-value *addition*: telling the search engine what kind of thing your site is about. The key fact that resolves most confusion: **structured data is not a file the crawler fetches separately — it must be inlined into each page's HTML**, inside a `<script type="application/ld+json">` block. But you can keep the *source* in one tidy place and let Jekyll inline it. This mirrors how you'd manage any other single-source-of-truth data.

**2a.** Put your identity graph in `_data/person.json`. (Edit the values to taste; `sameAs` is the part worth investing in.)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": "WebSite",
      "@id": "https://barbhs.com/#website",
      "url": "https://barbhs.com/",
      "name": "Barbara Hidalgo-Sotelo",
      "publisher": { "@id": "https://barbhs.com/#person" }
    },
    {
      "@type": "Person",
      "@id": "https://barbhs.com/#person",
      "name": "Barbara Hidalgo-Sotelo",
      "jobTitle": "AI & Data Science Consultant",
      "description": "Cognitive scientist and data scientist exploring messy data, intelligent systems, and how people make meaning.",
      "url": "https://barbhs.com/",
      "image": "https://barbhs.com/assets/images/biopic/bhs-new-headshot-v1.png",
      "sameAs": [
        "https://github.com/dagny099",
        "https://linkedin.com/in/barbara-hidalgo-sotelo"
      ],
      "alumniOf": [
        { "@type": "CollegeOrUniversity", "name": "Massachusetts Institute of Technology" },
        { "@type": "CollegeOrUniversity", "name": "The University of Texas at Austin" }
      ]
    },
    {
      "@type": "ProfilePage",
      "@id": "https://barbhs.com/#profilepage",
      "url": "https://barbhs.com/",
      "mainEntity": { "@id": "https://barbhs.com/#person" }
    }
  ]
}
```

**2b.** Create a one-line partial, `_includes/schema/identity.html`, that inlines it:

{% raw %}
```liquid
<script type="application/ld+json">
{{ site.data.person | jsonify }}
</script>
```
{% endraw %}

The `jsonify` filter re-serializes your data structure into guaranteed-valid JSON — no hand-quoting, no escaping bugs. That `_data/person.json` file *is* your "JSON-LD file in the repo." It's edited in exactly one place and rendered wherever the partial is included.

## Step 3 — Add per-content-type schema

The unlock that keeps this simple: **a page may carry several `ld+json` blocks, and the engine merges them.** So you don't build one monster object. You emit the sitewide identity block everywhere, and each content type adds its own small block that points back at the same Person `@id`. That back-reference is the whole game — it means every project and post reinforces *one* entity instead of inventing a new anonymous author each time.

**3a.** `_includes/schema/article.html` — for posts, essays, and data stories:

{% raw %}
```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": {{ page.title | jsonify }},
  "description": {{ page.description | default: site.description | jsonify }},
  "url": {{ page.url | absolute_url | jsonify }},
  "datePublished": {{ page.date | date_to_xmlschema | jsonify }},
  "dateModified": {{ page.last_modified_at | default: page.date | date_to_xmlschema | jsonify }},
  {% if page.image %}"image": {{ page.image | absolute_url | jsonify }},{% endif %}
  "author": { "@id": "https://barbhs.com/#person" },
  "mainEntityOfPage": {{ page.url | absolute_url | jsonify }}
}
</script>
```
{% endraw %}

**3b.** `_includes/schema/project.html` — for projects (same shape, different type):

{% raw %}
```liquid
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareSourceCode",
  "name": {{ page.title | jsonify }},
  "description": {{ page.description | default: site.description | jsonify }},
  "url": {{ page.url | absolute_url | jsonify }},
  {% if page.repo %}"codeRepository": {{ page.repo | jsonify }},{% endif %}
  {% if page.language %}"programmingLanguage": {{ page.language | jsonify }},{% endif %}
  {% if page.image %}"image": {{ page.image | absolute_url | jsonify }},{% endif %}
  "author": { "@id": "https://barbhs.com/#person" }
}
</script>
```
{% endraw %}

Two footguns to internalize, because they cause every broken JSON-LD block I've ever seen. First, wrap every *value* in `{% raw %}| jsonify{% endraw %}` rather than hand-typing quotes — a title containing an apostrophe or a quotation mark will silently corrupt naked `"{% raw %}{{ page.title }}{% endraw %}"`. Second, the only property that must *not* end in a comma is the last one; notice the conditional `image` line keeps its trailing comma *inside* the `{% raw %}{% if %}{% endraw %}` so the comma vanishes cleanly when there's no image.

**3c.** Wire it up once, in the `<head>` of your default layout:

{% raw %}
```liquid
{% include schema/identity.html %}
{% if page.layout == "post" %}
  {% include schema/article.html %}
{% elsif page.layout == "project" %}
  {% include schema/project.html %}
{% endif %}
```
{% endraw %}

For projects, set `repo` and `language` in each project's front matter, and you never touch the partial again. Indexes like tag and category pages need no per-type block — the identity block alone is fine.

## Step 4 — Make the rest of the `<head>` DRY

While you're in the layout, centralize the ordinary meta so every page produces correct, consistent tags from front matter with sensible fallbacks. `_includes/head-meta.html`:

{% raw %}
```liquid
<title>{{ page.title | default: site.title }}</title>
<meta name="description" content="{{ page.description | default: site.description }}">
<link rel="canonical" href="{{ page.url | absolute_url }}">

<meta property="og:title" content="{{ page.title | default: site.title }}">
<meta property="og:description" content="{{ page.description | default: site.description }}">
<meta property="og:url" content="{{ page.url | absolute_url }}">
<meta property="og:type" content="{{ page.layout == 'post' ? 'article' : 'website' }}">
<meta property="og:image" content="{{ page.image | default: '/assets/images/hero-banner.png' | absolute_url }}">
```
{% endraw %}

Because `absolute_url` prefixes the `url` from `_config.yml`, your canonical-host decision in Step 1 now propagates to every tag on every page for free. This is the payoff of doing Step 1 first.

## Step 5 — Upgrade `knowsAbout` to linked data

`knowsAbout` is a property on your Person that disambiguates *what kind of expert you are*. Its job isn't ranking — it's helping the engine place your entity in conceptual space. So keep it to a tight, honest set of genuine throughlines, not a keyword pile (a bloated list reads as spam and dilutes the signal).

The plain version is a list of strings. The better version — and the one worth doing if you care about linked data — gives each concept a `sameAs` edge to its canonical encyclopedic identity, turning a bare label into a node in the global graph. Add this to the Person object in `_data/person.json`:

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

These tags don't affect ranking; they make shared links render reliably and look intentional. Add to `head-meta.html`:

{% raw %}
```liquid
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png">
<meta property="og:image:alt" content="{{ page.image_alt | default: site.title }}">

<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{ page.title | default: site.title }}">
<meta name="twitter:description" content="{{ page.description | default: site.description }}">
<meta name="twitter:image" content="{{ page.image | default: '/assets/images/hero-banner.png' | absolute_url }}">
```
{% endraw %}

Confirm your share image is genuinely 1200×630 (the ideal ratio); if it isn't, the declared dimensions will lie to the unfurler and the card may render oddly. The width/height tags let a platform reserve the right space *before* fetching the image, so the card renders without a layout jump; `twitter:card` set to `summary_large_image` is what earns you the large banner on X instead of a small thumbnail.

## Step 7 — Confirm the boring infrastructure

Two files quietly determine whether you're crawlable at all. Add the `jekyll-sitemap` plugin to generate `sitemap.xml` automatically:

```yaml
# _config.yml
plugins:
  - jekyll-sitemap
```

And ensure a `robots.txt` at your site root points to it:

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

Step back and notice the structure. Your *identity* lives in one data file. Your *rendering logic* lives in a few small, named partials. Your *canonical host* is decided once and propagates everywhere through `absolute_url`. Each content type contributes its own schema while pointing back at a single Person node, so your whole site resolves to one trusted entity rather than a scatter of anonymous pages. That's not just good for search — it's the same separation of source-of-truth from presentation that makes any project pleasant to maintain. The metadata got better, and the repo got *cleaner*. That's the version worth shipping.
