---
layout: single
title: "Digital Home Base Workshop Part 3- Automate Your Site with GitHub Actions"
subtitle: "Set up continuous deployment with GitHub Actions for seamless Jekyll builds"
date: 2024-08-13
sitemap:
    priority: 0.5
classes: [wide]
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

*Welcome to Part 3 of our "Make Your Own Website" learning series! Just stumbled upon this? No worries\!  If you're a fellow data enthusiast wondering whether you should bother with a personal website (spoiler: you should), Check out [Post 1](/posts/getting-started-with-github-pages/) to learn why having your own portfolio site matters and how to get started quickly, or [Post 2]( /posts/understanding-your-jekyll-site/) for a deep dive into Jekyll site builders and common pitfalls.* 

In this guide, I’ll walk you through how to set up **continuous deployment** for your Jekyll-based GitHub Pages site using GitHub Actions. Whether you’re completely new to CI/CD (Continuous Integration / Continuous Deployment) or just want a more seamless workflow, you’re in the right place.

![image-center]({{ site.url }}{{ site.baseurl }}/assets/images/series-website/build-process-w-gh-actions.png){: .align-center}

### Wait, Didn't We Already Handle Deployment? 🤔

If you've been following this series (high five\! 🖐️), you've already got a Jekyll site happily living on GitHub Pages. Every time you push changes, your site magically updates itself. Life is good\! So why another post? This was my rationale - With the default GH process, my content becomes a Live Webite (woot!) but it's a bit of a black box ▪️. 

*By the end of this post, you’ll:*    
- Control exactly how your site is built with GitHub Actions
- Run tests before deployment
- See detailed logs of the entire process
- Have the flexibility to add custom steps

## 🚀 Instructions

### Step 1: Enable GH Actions in Your Repository

First, make sure your repository is set up to use GH Actions.
1. **Go to your repository on GH**  
2. Click on **Settings > Actions**  
3. Under “Workflow permissions,” select **“Read and write permissions”** (this is required for deployment)  
4. Click **Save**

Now, you’re ready to add automation!


### Step 2: Create a GH Actions Workflow File

GH Actions uses **workflows**, defined in `.github/workflows/`, to automate tasks

#### 🔹 Add Your Workflow File:
1. Inside your repository, navigate to `.github/workflows/` (create these folders if they don’t exist)  
2. Create a new file called `pages.yml`  
3. Paste the following workflow configuration:  

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
      id-token: write # Req for authentication
      pages: write    # Req to publish to GH pages
      contents: read  # Needed to check out repo content
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Ruby
        uses: ruby/setup-ruby@v1
        with:
          ruby-version: '3.1'  # Match your Jekyll version

      - name: Install dependencies
        run: |
          gem install bundler
          bundle install

      - name: Build the site
        run: bundle exec jekyll build

      - name: Run HTML Proofer
        run: bundle exec htmlproofer ./_site --allow-hash-href

      - name: Deploy to GitHub Pages
        uses: actions/upload-pages-artifact@v3
        with:
          path: _site  # Jekyll output folder

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

This workflow will:  
✅ Check out your repo  
✅ Set up Ruby and install Jekyll dependencies  
✅ Build your site  
✅ Run HTML Proofer to validate your site (see more below)  
✅ Deploy to GitHub Pages 🎉    

### Step 3: Configure GH Pages to Use the Workflow
Once your first workflow run is complete:
1. Go to your repository on GH.
2. Click on **Settings > Pages**.
3. Under “Build and Deployment,” set the source to **GitHub Actions**.
4. Click **Save**.

Now, every time you push a change to `main`, your site will rebuild and deploy automatically!

#### (Optional) Make Sure Your Site is Error-Free with HTML Proofer
One of the most frustrating things about deploying a static site is realizing *after the fact* that there’s a broken link or missing image. That’s where **HTML Proofer** comes in—it scans your site before deployment to catch issues like broken links, missing images or assets, or invalid HTML structure. 

We already added HTML Proofer in the workflow above, but to make sure it works locally too:

1. Add this to your **Gemfile**:  
```sh
group :development do
  gem "html-proofer"
end
```

2. Run:  
```sh
bundle install
```

3. Test locally:  
```sh
bundle exec htmlproofer ./_site --allow-hash-href
```

If it finds issues, fix them *before* pushing your code! 🙌


### Step 4: Monitor Your Workflow & Debug If Needed
Once you push a commit, you can **watch your deployment happen**:  
1. Go to your repository on GH.  
2. Click on the **Actions** tab.  
3. Click on the latest workflow run to see logs and potential errors.  


🔍 If something fails:  
- Look for **error messages** in the logs.  
- Fix the issue locally and push a new commit.  
- If needed, re-run the workflow from the Actions tab.  


That’s it! You now have:  
✅ A fully automated **CI/CD pipeline** for your GH Pages Jekyll site.  
✅ A built-in **error-checking system** with HTML Proofer.  
✅ A **stress-free workflow**—just push changes, and your site updates itself!  


## 🔧 Real-World Troubleshooting Tips 
Through my own trial and error, here are some common issues you might encounter:

### 1. Branch Name Mismatch
```yaml
# What you might have:
on:
  push:
    branches:
      - main  # But your default branch might be different!
```
If your deployments aren't triggering, check your default branch name. Older repositories might still use `master` instead of `main`. You can check this in your repository's settings or by running `git branch -a`.

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
🤔 Now that I’ve automated this, I'll be thinking about how wo extend my CI/CD knowledge to **other web projects!**, including learning to use [Buddy.Works](https://buddy.works/) which I've been curious to try. More to come!  

Read the [Post 4](/posts/post-deployment-reflextions/), where I reflect and consolidate my learnings from the project (especially this last part)

[Return Home](/)
