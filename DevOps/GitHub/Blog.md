# Blog

## how to setup github pages for blogging
- https://chadbaldwin.net/2021/03/14/how-to-build-a-sql-blog.html
- https://github.com/chadbaldwin/chadbaldwin.github.io

## test github pages locally
https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/testing-your-github-pages-site-locally-with-jekyll
- install `Ruby`, `Gem`, and `Bundler`
- create Gemfile in root folder
  - https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll
```
source "https://rubygems.org"
gem "github-pages", "~> 232", group: :jekyll_plugins
```
- run
  - `sudo apt update & sudo apt install ruby3.2-dev build-essential`
  - `bundle config set --local path 'vendor/bundle'`
  - `bundle install` and
  - `bundle exec jekyll serve`


## install rougify
```sh
sudo apt install ruby-rouge
```

## Generate Rouge Stylesheet (github style)
```sh
rougify style github > assets/css/syntax.css
```

## Integrate the Stylesheet
Link the generated CSS file in website's HTML <head> section (_layouts/post.html):
```html
<link href="/assets/css/syntax.css" rel="stylesheet">
```

## Rouge sample highlighter
http://rouge.jneen.net/v3.26.0/r/

_config.yml
```yaml
markdown: kramdown
highlighter: rouge

kramdown:
  input: GFM
  syntax_highlighter: rouge
```

## template
- https://github.com/gangdong/gangdong.github.io (https://dqdongg.com/)
- https://github.com/purplediane/purplediane.github.io (https://purplediane.github.io/)

## training/book template
- https://github.com/olohmann/azure-hands-on-labs/blob/master/labs/03_terraform/terraform.md (https://olohmann.github.io/azure-hands-on-labs/labs/01_serverless/serverless.html)

## jekyll
- http://simpleprimate.com/jekyll-for-designers/blog/css/


## hits and page views
https://wxguy.in/posts/how-to-enable-no-of-hits-page-view-counter-on-jekyll-github-blog-posts/
