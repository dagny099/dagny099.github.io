---
layout: post
title: "Digital Home Base Workshop Part 3- Automate Your Site with GitHub Actions"
subtitle: "Set up continuous deployment with GitHub Actions, so every Jekyll build is visible and checked"
date: 2024-08-13
last_modified_at: 2026-11-09
sitemap:
    priority: 0.5
classes: wide
permalink: /blog/deploy-jekyll-gh-actions/
redirect_from:
  - /posts/deploy-jekyll-gh-actions/
  - /tutorial/deploy-jekyll-gh-actions/
header:
  overlay_image: "/assets/images/midjourney/reimagined-offices/office-of-my-imagination-robotic-arm-building_arsq.png"
excerpt: "Every good engine needs a monitoring system. Learn how to install a proper CI/CD pipeline that watches your engine's performance, catches issues before they become problems, and keeps everything running smoothly"
excerpt_display: false
tags: [cicd, automation, deployment, devops]
stack: [GitHub Actions, Jekyll, YAML, Git]
categories: [tutorial]
pagination: 
  enabled: true
---

*Part 3 of the Digital Home Base Workshop. New here? [Part 1](/blog/getting-started-with-github-pages/) covers why a personal site is worth having and how to start one, and [Part 2](/blog/understanding-your-jekyll-site/) explains how Jekyll turns your files into a website.*

*Updated November 2026: the workflow below is now the one that deploys this site. It deploys only on pushes to `main`, checks pull requests with a build, and caches gems between runs.*

In this guide, I'll walk you through how to set up **continuous deployment** for your Jekyll-based GitHub Pages site using GitHub Actions. Whether you're completely new to CI/CD (Continuous Integration / Continuous Deployment) or just want a workflow you can see into, you're in the right place.

![Diagram of a Jekyll build and deploy process run by GitHub Actions]({{ site.url }}{{ site.baseurl }}/assets/images/series-website/build-process-w-gh-actions.png){: .align-center}

### Wait, Didn't We Already Handle Deployment?

If you've been following this series, you've already got a Jekyll site living on GitHub Pages. Every time you push changes, your site updates itself. So why another post? With the default GitHub Pages process, my content became a live website (woot!), but how it got there was a black box.

*By the end of this post, you'll:*
- Control exactly how your site is built with GitHub Actions
- Check every pull request with a build before it goes live
- See detailed logs of the entire process
- Have the flexibility to add custom steps

## Instructions

### Step 1: Point GitHub Pages at GitHub Actions

Do this first, so the workflow has somewhere to deploy:
1. Go to your repository on GitHub.
2. Click **Settings > Pages**.
3. Under "Build and deployment," set **Source** to **GitHub Actions**.

You don't need to change any other repository settings. The workflow below asks for exactly the permissions it needs, in its own `permissions:` block.

### Step 2: Create a GitHub Actions workflow file

GitHub Actions uses **workflows**, defined in `.github/workflows/`, to automate tasks.

1. Inside your repository, create the folders `.github/workflows/` if they don't exist.
2. Create a new file called `pages.yml`.
3. Paste in this workflow. It's the one that deploys this site, with the branch name changed to `main`:

```yaml
name: Deploy GitHub Pages

on:
  push:
    branches:
      - main  # Change this if your primary branch is different
  pull_request:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write # Required for authentication
      pages: write    # Required to publish to GitHub Pages
      contents: read  # Needed to check out repo content

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Ruby and install gems
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.1'  # Match your Jekyll version
          bundler-cache: true  # Runs bundle install and caches the gems between runs

      - name: Build the site
        run: bundle exec jekyll build

      # Pull requests stop here: the build is the check. Publishing happens on pushes to main.
      - name: Upload Pages artifact
        if: github.event_name == 'push'
        uses: actions/upload-pages-artifact@v3
        with:
          path: _site  # Jekyll output folder

      - name: Deploy to GitHub Pages
        if: github.event_name == 'push'
        id: deployment
        uses: actions/deploy-pages@v4
```

This workflow will:
- Check out your repo
- Set up Ruby, install your gems, and cache them so later runs are faster
- Build your site
- On a push to `main`, upload the built site and deploy it to GitHub Pages
- On a pull request, stop after the build, so the pull request gets a check without touching your live site

The two `if: github.event_name == 'push'` lines are what keep pull requests to a check. Leave them out, and the deploy steps run on pull requests too.

### Step 3: Push, then watch it run

Commit `pages.yml` and push it to `main`. Then you can **watch your deployment happen**:
1. Go to your repository on GitHub.
2. Click on the **Actions** tab.
3. Click on the latest workflow run to see logs and potential errors.

If something fails:
- Look for **error messages** in the logs.
- Fix the issue locally and push a new commit.
- If needed, re-run the workflow from the Actions tab.

That's it! You now have:
- A fully automated **CI/CD pipeline** for your GitHub Pages Jekyll site
- A build check on every pull request
- A workflow where you just push changes, and your site updates itself

### Optional: catch broken links with HTML Proofer

One of the most frustrating things about deploying a static site is realizing *after the fact* that there's a broken link or missing image. **HTML Proofer** scans your built site to catch issues like broken links, missing images or assets, and invalid HTML structure.

1. Add it to your **Gemfile**:
```ruby
group :development do
  gem "html-proofer"
end
```

2. Install it, build your site, and test locally:
```sh
bundle install
bundle exec jekyll build
bundle exec htmlproofer ./_site --allow-hash-href
```

3. To run it on every build, add this step to the workflow, right after "Build the site":
```yaml
      - name: Run HTML Proofer
        run: bundle exec htmlproofer ./_site --allow-hash-href
```

If it finds issues, fix them *before* pushing your code.

## Real-World Troubleshooting Tips
Through my own trial and error, here are some common issues you might encounter:

### 1. Branch Name Mismatch
```yaml
# What you might have:
on:
  push:
    branches:
      - main  # But your default branch might be different!
```
If your deployments aren't triggering, check your default branch name. Older repositories might still use `master` instead of `main` (this site's does). You can check this in your repository's settings or by running `git branch -a`.

### 2. Taming HTML-Proofer
HTML-Proofer is great for catching broken links and missing assets, but it can be overzealous. If it's blocking your deployments, you have options:

```yaml
- name: Run HTML Proofer
  run: bundle exec htmlproofer ./_site --allow-hash-href --ignore-urls "/^http://127.0.0.1/,/^http://0.0.0.0/"
  continue-on-error: true  # Add this line to prevent blocking deployment
```

### 3. Action Version Conflicts
Always check the latest versions of actions you're using. For example, I had to update:
```yaml
# Old version
- uses: actions/upload-pages-artifact@v1
# New version
- uses: actions/upload-pages-artifact@v3
```

---

In [Part 4](/blog/post-deployment-reflextions/), I reflect on what I actually learned from this project, especially that last part.
