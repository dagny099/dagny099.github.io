---
layout: single
title: "Digital Home Base Workshop Part 2- Under the Hood: Understanding Your Site's Engine"
sitemap:
    priority: 0.5
permalink: /blog/understanding-your-jekyll-site/
redirect_from:
  - /posts/understanding-your-jekyll-site/
  - /tutorial/understanding-your-jekyll-site/
header:
  overlay_image: "/assets/images/midjourney/reimagined-offices/office-of-my-imagination-below-sea-ar4by3.png"
excerpt: "Explore Jekyll's inner workings, understand how it transforms your content into a smooth-running website, and learn how to fine-tune its performance"
excerpt_display: false
classes: [wide]
tags: [jekyll, static site builders]
categories: [tutorial]
pagination: 
  enabled: true
---
## How Jekyll Brings Your Site to Life
![image-right]({{ site.url }}{{ site.baseurl }}/assets/images/series-website/mermaid-diagram-website-post-1-jekyll-build.png){: .align-right style="max-width:400px"}
If you've followed our [first guide](/posts/getting-started-with-github-pages/), you've already got a working website. Now let's peek under the hood and understand how Jekyll transforms your content into a beautiful, responsive website. Why? Because understanding your tools makes you a better craftsperson! 

Pretty neat, right? Jekyll takes your Markdown files, applies your chosen theme, and creates a complete website. 

Let's break down each component 🛠️

## 🏗️ Your Site's Building Blocks 

**Understanding Your Site's Structure:**  
Here's the basic directory structure of your new site:
```
yourusername.github.io/
├── README.md              # Project documentation
├── _config.yml           # Main site configuration
├── Gemfile               # Ruby dependencies
├── index.md              # Homepage
├── _data/                # Site data files
│   └── navigation.yml    # Navigation structure
├── _includes/            # Reusable page components
├── _layouts/             # Page templates
├── _pages/               # Static pages
├── _posts/               # Blog posts
├── _sass/                # Style customizations
└── assets/              # Images, CSS, JS files
```

Key files and their purposes:
- `_config.yml`: Your site's main configuration
- `Gemfile`: Manages Ruby gem dependencies
- `_data/navigation.yml`: Controls site navigation
- `_posts/`: Where your blog posts live
- `_pages/`: For static pages like About, Portfolio
- `assets/`: For images and other media

#### Configuration (_config.yml)
Think of this as your site's control panel. It controls everything from basic settings to complex theme customization:
```yaml
# Basic Settings
title: "Your Amazing Site"
description: "Data Science | Machine Learning | Insights"

# Advanced Settings
permalink: /:categories/:title/
paginate: 5
```
Pro tip: Changes to `_config.yml` require a full site rebuild. Don't panic if changes take a minute to show up!

#### Content Organization
Jekyll uses a smart system to organize your content:
- **Posts** (`_posts/`): Your blog entries
  ```markdown
  ---
  title: "Analyzing COVID Data"
  date: 2024-02-15
  categories: [data-science, visualization]
  ---
  ```

- **Pages** (`_pages/`): Static content like About, Portfolio
  ```markdown
  ---
  title: "About Me"
  permalink: /about/
  ---
  ```

## 💻 Don't Neglect: Set Up Your Local Environment 
Want to preview changes before pushing them live? Let's set up local development:
![image]({{ site.url }}{{ site.baseurl }}/assets/images/series-website/mermaid-diagram-website-post-1-git.png){: .align-center style="max-width:85%"}

1. Install Ruby and Jekyll:
   ```bash
   # macOS (with Homebrew)
   brew install ruby
   gem install bundler jekyll
   
   # Ubuntu/Debian
   sudo apt-get install ruby-full build-essential
   gem install bundler jekyll
   ```

2. Clone your repository:
   ```bash
   git clone https://github.com/yourusername/yourusername.github.io.git
   cd yourusername.github.io
   ```

3. Install dependencies and serve:
   ```bash
   bundle install
   bundle exec jekyll serve
   ```

Now visit<span style="color:red"> `http://localhost:4000` </span> to see your site! Changes will update in real-time (except for `_config.yml`).

## 🎨 Making Your Site Truly Yours 

### Customizing Your Theme
The Minimal Mistakes theme offers tons of customization options:

```yaml
# _config.yml
minimal_mistakes_skin: "dark" # Try: default, air, aqua, contrast
```

### Adding Custom Styles
Want to tweak specific elements? Create `assets/css/main.scss`:

```scss
---
---

@import "minimal-mistakes";

// Your custom CSS here
.page__title {
  color: #2ecc71;
}
```

## 🔧 Troubleshooting Like a Pro 

Common issues and their solutions:

1. **Build Errors**
   - Check YAML formatting (spaces, not tabs!)
   - Verify front matter has three dashes (`---`)
   - Look for special characters in filenames

2. **Style Issues**
   - Clear your browser cache
   - Check CSS specificity
   - Verify theme skin settings

3. **Performance**
   - Optimize images
   - Use Jekyll's incremental build (`--incremental`)
   - Implement lazy loading for images

## 🧠 Advanced Features 

### Collections
Perfect for organizing related content:

```yaml
# _config.yml
collections:
  projects:
    output: true
    permalink: /:collection/:path/
```

### Custom Layouts
Create unique templates for different content types:

```liquid
{% raw %}
---
layout: default
---
<div class="project-page">
  <h1>{{ page.title }}</h1>
  {{ content }}
</div>
{% endraw %}
```

## What's Next? 

In [Post 3](/posts/deploy-jekyll-gh-actions/), we'll automate your workflow with GitHub Actions. You'll learn how to:
- Set up continuous integration
- Automatically check for broken links
- Deploy with confidence
- Get notifications when something goes wrong

## Resources 📚
- [Jekyll Configuration](https://jekyllrb.com/docs/configuration/)
- [Minimal Mistakes Theme Guide](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/)
- [Liquid Template Language](https://shopify.github.io/liquid/)


[Home](/)
