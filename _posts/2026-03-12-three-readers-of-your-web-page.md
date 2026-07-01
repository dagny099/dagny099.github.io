---
layout: post
classes: wide
title: "The Three Readers of Your Web Page"
description: "Your site doesn't have one audience — it has three machines, each fluent in a different dialect of metadata. A friendly tour of how browsers, search engines, and social platforms each parse the page head, and why Open Graph isn't the SEO lever everyone assumes it is."
date: 2026-03-12
categories: [applied-thinking, website-building]
tags: [metadata, seo, open-graph, structured-data, knowledge-representation, github-pages, jekyll]
image: /assets/images/posts/three-readers-hero.png
---

Here's the setup. You have a personal site built with Jekyll, hosted for free on GitHub Pages. The content is good. The writing is yours. And yet, when you search your own name, the result is thinner than you'd like — or when you paste a link into LinkedIn, the preview is a gray rectangle and a cropped logo. You go looking for "how to improve my metadata," and within ten minutes you're drowning in acronyms: OG, SEO, JSON-LD, canonical, schema. They all seem to live in the same place — that mysterious `<head>` tag at the top of every page — so it's natural to assume they all do the same job.

They don't. And the single most clarifying idea in this whole topic is this: **your page's `<head>` is not read by one audience. It's read by three, and each one speaks a different language.** Once you can see the three readers, every confusing acronym snaps into a slot, and you stop optimizing the wrong tag for the wrong machine.

This article is the conceptual tour. A companion piece walks through the exact changes to make in your repo. For now, let's just learn how the web actually reads you.

> **Suggested graphic — the hero.** A single page `<head>` at the top, with three labeled arrows fanning down to three "readers": a browser, a search engine, and a social/chat app. Under each reader, the short list of tags it actually consumes. This one image does most of the teaching; everything below is elaboration. (A clean SVG in the Meaning Layer palette, or a Mermaid `flowchart TD` with three branches.)

## The `<head>` is a room with three readers in it

Think of the `<head>` of an HTML page as a room where you've pinned up a set of index cards about the page. Three very different visitors walk through that room, and each one only reads the cards written in a vocabulary they understand. They ignore the rest entirely — politely, silently. The web was designed this way on purpose: a client reads the tags it knows and skips the ones it doesn't, so you can write cards for all three audiences in the same room without anyone getting confused.

The three readers are the **browser**, the **search engine**, and the **social unfurler**. They have different jobs, so they care about different cards.

> **The other side of the glass.** This piece is about who *reads* the cards. If you're curious who *writes* them, here's [a map of how this very site's `<head>` is assembled]({{ '/assets/diagrams/head-architecture-v2.svg' | relative_url }}) — every Jekyll include and data file, and the exact tags each one injects. The [companion implementation post]({% post_url 2026-03-18-implementing-structured-metadata-jekyll %}#audit-your-head) embeds it in context.

## Reader one: the browser (it has to *render* you)

The browser is the only reader a human directly experiences, and ironically it cares least about the cards you agonize over. It wants the practical stuff: the character encoding (`charset`, so your apostrophes don't turn into mojibake), the `viewport` (so the layout adapts to a phone), the `<title>` (which becomes the tab label), and a few cosmetic touches like `theme-color` and the favicon. That's mostly it. The browser is here to *paint the page*, and these tags tell it how.

If your site renders correctly on a phone and shows the right name in the tab, the browser is satisfied. None of this affects how you're found — it affects how you're *displayed once someone has already arrived*.

## Reader two: the search engine (it has to *find*, *judge*, and *show* you)

This is the reader you actually care about when you say "metadata positioning," and it's worth understanding that it doesn't do one thing — it does three, in sequence. I find it clearest to think of a three-stage pipeline.

**Stage one is crawl and index — traffic control.** A search crawler fetches your URL and asks two yes/no questions: *am I allowed to store this page, and which version of it is the real one?* The tags that answer are the `robots` directive (index or noindex, follow or nofollow) and the `canonical` link, which points at the official URL when several near-duplicates exist. These don't make you rank. They're the gate. Get them wrong and a page silently never enters the index at all — the worst failure, because it's invisible. You won't see an error; you'll just never appear.

**Stage two is understand and rank — meaning.** Now the engine asks *what is this page about, and how much should I trust it?* The honest answer is that this is driven overwhelmingly by your **actual content** — your headings, your prose, your links, your image alt text — read by some fairly sophisticated language models. Among the metadata, the `<title>` tag is the one strong signal here. And then there's a special category called **structured data**, which doesn't rank you but does something subtler and, for some of us, more interesting: it states, in a machine-readable vocabulary, *what kind of thing* the page is about. A person. An article. A piece of software. We'll come back to this, because it's the layer most personal sites are missing.

**Stage three is display — the result on screen.** Finally the engine decides how you look in the results list. Your `<title>` becomes the blue clickable line. Your `meta description` becomes the gray snippet underneath — though a useful thing to know is that the engine rewrites that snippet roughly more often than not, whenever it thinks a sentence pulled from your page answers the query better. So treat your description as a strong suggestion, not a guarantee. Structured data, if present, can unlock richer result formats here too.

> **Suggested graphic — the pipeline.** Three boxes left to right: *Crawl & index → Understand & rank → Display*, each annotated with the tags that act at that stage (robots/canonical, then title/structured-data, then title/description). The point of the visual is that **different tags act at different stages** — a reader should leave understanding that `canonical` and `meta description` aren't competing, they're working in different rooms.

## Reader three: the social unfurler (it has to *preview* you)

The third reader shows up whenever someone pastes your link into a feed or a chat — LinkedIn, Slack, iMessage, WhatsApp, Discord, X. Its job is to "unfurl" the bare URL into a rich preview card: a title, a blurb, and a big image. The vocabulary it reads is **Open Graph** — the family of tags that start with `og:`. `og:title`, `og:description`, `og:image`, and a few companions are what make your shared link look like a designed object instead of a naked string.

This reader is the reason your LinkedIn previews look the way they do. If the card is ugly, this is the reader to talk to.

## The misconception that reorganizes everything

Here's the part worth slowing down for, because almost everyone gets it backwards. **Open Graph is a social-sharing protocol, not a search-engine protocol.** It was invented by Facebook in 2010 so platforms could render previews. The major search engines, for ranking purposes, essentially ignore it. Which means: perfecting your `og:` tags will make your shared links *beautiful* — and will do almost nothing for how you *rank*.

There is exactly one crossover, and it's worth knowing precisely because it's the exception that proves the rule: a search engine may borrow your `og:image` as one candidate when it needs to pick a thumbnail for a result. So of all the Open Graph tags, the image is the only one that brushes up against search at all, and even then only for *display*, never for ranking.

The practical upshot for your Jekyll site: the work that makes your links *look* great (Open Graph) and the work that makes you *findable and legible* (titles, canonical/robots, and structured data) are two different projects. Both are worth doing. But conflating them is why people pour effort into `og:` tags and wonder why their search presence doesn't budge.

> **Suggested graphic — the myth-buster.** A simple two-column "common belief vs. reality" card. Left: *"Open Graph tags improve my Google ranking."* Right: *"Open Graph governs link previews. Search ranking runs on title + content + structured data. The one overlap: og:image can become a thumbnail."* Keep it spare — this is the single correction the whole article hinges on.

## The deeper idea: metadata is a knowledge graph in disguise

If you have any background in knowledge representation — or you just like when things turn out to be the same thing underneath — this is the satisfying part.

An Open Graph tag isn't a magic keyword. The `property="og:title"` syntax is RDFa, and `og` is a namespace prefix pointing at a published vocabulary. Which means an `og:` tag is literally a **triple** — a tiny statement of the form *(subject) — (predicate) — (object)*: *this page → has the title → "…"*. It's the same subject-predicate-object grammar you'd write in a graph database, just expressed in HTML instead of Cypher or Turtle.

Structured data (the JSON-LD kind) is the same idea, one level richer. Instead of describing the *page*, it describes the **entities** the page is about, using a shared public ontology called Schema.org. A personal homepage isn't really "a page" — it's a page *about a person*. Structured data lets you say exactly that: *there is a Person named Barbara; her job title is this; here is her image; and — crucially — she is the **same as** this GitHub profile and that LinkedIn profile.*

That last move is the one I'd underline. The `sameAs` property in Schema.org is, functionally, `owl:sameAs` — the identity statement that lets a reasoner merge two references into one entity. When you list your profiles in `sameAs`, you are handing the search engine the edges it needs to reconcile your scattered web presence — your site, your code, your writing, your professional profile — into a single, trusted node. You are, in the most literal sense, doing entity reconciliation on yourself.

There's a cognitive-science echo here too, which is why I keep coming back to this topic. A memory isn't retrieved by brute force; it's retrieved through *context* — the cues and associations that point to it. Metadata is the web's version of that context. The page is the memory; the structured data is the set of associations that let the right query surface it. "Metadata matters" isn't a slogan about tidiness. It's a claim about how retrieval works, in heads and in machines alike.

> **Suggested graphic — the triple.** Three connected nodes: *This page → og:title → "…"* drawn as a graph edge, sitting next to the equivalent JSON-LD *Person → sameAs → GitHub*. The visual argument: "these tags you've been treating as form fields are actually graph statements." For your audience specifically, this is the image that earns the article.

## Where this goes next

So that's the map. Your `<head>` serves three readers; the browser renders you, the search engine finds and judges and shows you, and the social unfurler previews you. Open Graph dresses the link; titles, canonical/robots, and structured data make you legible to search. 

The companion piece, *Implementing Structured Metadata on a Jekyll + GitHub Pages Site*, turns this understanding into a checklist: how to audit your own `<head>`, how to pick and enforce a single canonical home for your site, how to emit clean structured data from a `_data` file the way you'd manage any other source of truth, and how to verify the result against the tools each reader actually uses. The concepts are the hard part, and now you have vocabulary and an understanding of the non-human consumers of your webpage. The rest is plumbing — satisfying, legible plumbing.
