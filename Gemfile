source "https://rubygems.org"

# Hello! This is where you manage which Jekyll version is used to run.
# When you want to use a different version, change it below, save the
# file and run `bundle install`. Run Jekyll with `bundle exec`, like so:
#
#     bundle exec jekyll serve
#
# This will help ensure the proper Jekyll version is running.
# Happy Jekylling!
#gem "jekyll", "~> 4.1.1"

# This is the default theme for new Jekyll sites. You may change this to anything you like.
#gem "minima", "~> 2.5"
#gem "minimal-mistakes-jekyll"
#gem "minimal-mistakes-jekyll", "~> 4.27.1"

# If you want to use GitHub Pages, remove the "gem "jekyll"" above and
# uncomment the line below. To upgrade, run `bundle update github-pages`.
gem "github-pages", "~> 228", group: :jekyll_plugins
gem "jekyll-remote-theme"         # ← **add this** so local builds see the plugin


# If you have any plugins, put them here!
group :jekyll_plugins do
  gem "jekyll-paginate-v2"
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-sitemap"
  gem "jekyll-paginate"
  gem "jekyll-gist"
  gem "jekyll-archives"
end

#Add HTML Proofer for automated testing and linting.
# Best to include only in development so not loaded in production build
#group :development do
#  gem "html-proofer"
#end

# Windows and JRuby does not include zoneinfo files, so bundle the tzinfo-data gem
# and associated library.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Performance-booster for watching directories on Windows
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

gem "jekyll-include-cache"

gem "webrick", "~> 1.8"
