# Blog Layout

`Jekyll`-powered GitHub blog repository:
- **`_posts`**: The content folder for blog posts.
- **`_layouts`**: This folder contains the HTML templates (or layouts) that wrap around the content. I'll explain how it defines the structure of a page.
- **`_includes`**: This folder is for reusable code snippets that can be included in layouts or pages. I'll give examples like headers, footers, or social media links.
- **`_sass`**: This is for styling. I'll explain that it contains Sass/SCSS files that are compiled into CSS for the site's design.

## _posts
The `_posts` folder is where all of your blog content resides. Each blog post is a Markdown (`.md`) file, and the file name must follow a specific format: **`yyyy-mm-dd-blog-title.md`**.

The front matter at the top of each file (YAML data between triple-dashed lines) defines metadata like the post's title, author, and date.
```markdown
---
title: "My First Post"
tags: [intro, blog]
---
This is the content of my first post.
```

## _layouts
The `_layouts` folder contains the `page templates` that wrap around your content. A layout is a reusable HTML file that defines the structure and common elements of a page, such as the header, footer, and sidebar.

Example layouts include `default.html`, `post.html`, `page.html`, to define the overall structure and look of different types of pages on your site. When you create a new blog post, you specify which layout to use in the front matter:
```yaml
---
layout: post
---
```
Jekyll takes your content and **inserts it into that layout** via `{{ content }}`.

## _includes
The `_includes` folder is for storing small, `reusable snippets` of code or content, like headers, footers, social media links, or a comment section. These are fragments that can be inserted into a layout, post, or page to avoid code duplication.

File: `_includes/footer.html`
```html
<footer>© {{ site.time | date: "%Y" }} My Blog</footer>
```

Then in a layout:
```html
<body>
{{ content }}
{% include footer.html %}
</body>
```

## _sass
The `_sass` folder is where you keep reusable **Sass/SCSS stylesheets** (CSS with variables & nesting), which are used to style your website. Sass is a preprocessor that adds powerful features like variables, nesting, and mixins to CSS.

Sass (`.sass`) or SCSS (`.scss`) files are compiled into a standard CSS file by Jekyll before the site is built and published.

Inside `_sass`, you create `.scss` files (partials like `_variables.scss`, `_buttons.scss`). Then you import them into your main stylesheet (`assets/css/style.scss` or similar):
```scss
---
---
@import "variables";
@import "buttons";
```
Jekyll will compile Sass --> CSS when building the site. It’s for **styling structure and theming**.

## header pages
By default all `.md` files with a title under the root folder will be added to the header nav pages. By settng the `header_pages` in `_config.yml` file, we can control which file to be included and the order. These `.md` files will be added in the `header.html` file. More details: https://talk.jekyllrb.com/t/minima-header-html-functionality/6721


## width constraint only for `.wrapper` container
In Minima’s layout, the width constraint (using `$content-width`) only applies to elements that are inside the `.wrapper` container.
```html
<header class="site-header">
  <div class="wrapper">
    <!-- nav, title, etc. -->
  </div>
</header>
```
