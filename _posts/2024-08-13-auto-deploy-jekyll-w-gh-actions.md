---
layout: single
title: "Automate Your GitHub Pages Jekyll Site with GitHub Actions: A Beginner-Friendly Guide"
sitemap:
    priority: 0.5
permalink: /posts/deploy-jekyll-gh-actions/
header:
  overlay_image: "/assets/images/midjourney/office-of-my-imagination-robotic-arm-building_arsq.png"
excerpt: Ever Wanted to Automate Your Jekyll Site Deployment? Here’s How!  #displayed on index.html and blog.html
tags: [cicd, github actions]
categories: [tutorial]
pagination: 
  enabled: true
---

# Automate Your GitHub Pages Jekyll Site with GitHub Actions: A Beginner-Friendly Guide

If you’ve ever manually built and deployed a Jekyll site to GitHub Pages, you’ve probably wondered: *Isn’t there a way to make this process automatic?* The answer is a resounding **YES**, and the key is **GitHub Actions**!

In this guide, I’ll walk you through how to set up **continuous deployment** for your Jekyll-based GitHub Pages site using GitHub Actions. Whether you’re completely new to CI/CD (Continuous Integration / Continuous Deployment) or just want a more seamless workflow, you’re in the right place.

By the end of this post, you’ll:
✅ Have a GitHub Actions workflow that **automatically builds and deploys** your Jekyll site.  
✅ Ensure your site is **error-free** using **html-proofer** to catch broken links and missing assets.   
✅ Feel **empowered** to tweak and extend this automation for future projects.   

Let’s dive in! 🚀

---

## Step 1: Enable GitHub Actions in Your Repository

First, make sure your repository is set up to use GitHub Actions.
1. **Go to your repository on GitHub**.  
2. Click on **Settings > Actions**.  
3. Under “Workflow permissions,” select **“Read and write permissions”** (this is required for deployment).  
4. Click **Save**.

Now, you’re ready to add automation!


## Step 2: Create a GitHub Actions Workflow File

GitHub Actions uses **workflows**, defined in `.github/workflows/`, to automate tasks.

### 🔹 Add Your Workflow File:
1. Inside your repository, navigate to `.github/workflows/` (create these folders if they don’t exist).  
2. Create a new file called `pages.yml`.  
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
        uses: actions/upload-pages-artifact@v2
        with:
          path: _site  # Jekyll output folder

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

This workflow will:
✅ Check out your repo  
✅ Set up Ruby and install Jekyll dependencies  
✅ Build your site  
✅ Run HTML Proofer to validate your site  
✅ Deploy to GitHub Pages 🎉    


## Step 3: Configure GitHub Pages to Use the Workflow

Once your first workflow run is complete:

1. Go to your repository on GitHub.
2. Click on **Settings > Pages**.
3. Under “Build and Deployment,” set the source to **GitHub Actions**.
4. Click **Save**.

Now, every time you push a change to `main`, your site will rebuild and deploy automatically!


## Step 4: Make Sure Your Site is Error-Free with HTML Proofer

One of the most frustrating things about deploying a static site is realizing *after the fact* that there’s a broken link or missing image. That’s where **HTML Proofer** comes in—it scans your site before deployment to catch issues like:
✅ Broken links
✅ Missing images or assets
✅ Invalid HTML structure

We already added HTML Proofer in the workflow above, but to make sure it works locally too:

1. Add this to your **Gemfile**:

```ruby
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


## Step 5: Monitor Your Workflow & Debug If Needed

Once you push a commit, you can **watch your deployment happen**:  
1. Go to your repository on GitHub.  
2. Click on the **Actions** tab.  
3. Click on the latest workflow run to see logs and potential errors.  

🔍 If something fails:  
- Look for **error messages** in the logs.  
- Fix the issue locally and push a new commit.  
- If needed, re-run the workflow from the Actions tab.  


## Step 6: Enjoy Your Fully Automated Deployment! 🎉  

That’s it! You now have:  
✅ A fully automated **CI/CD pipeline** for your GitHub Pages Jekyll site.  
✅ A built-in **error-checking system** with HTML Proofer.  
✅ A **stress-free workflow**—just push changes, and your site updates itself!  

Now that you’ve automated this, you can explore even more:  
💡 Add **automated tests** for custom scripts.  
💡 Experiment with **content validation** (like checking metadata completeness).  
💡 Extend your CI/CD knowledge to **other web projects!**  


