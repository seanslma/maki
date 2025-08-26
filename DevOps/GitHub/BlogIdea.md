# blog layout idea

is it posible to create github blogs like this page so the left shows the blogs by category and we can also switch to another page showing the blogs by datetime: https://learn.microsoft.com/en-us/azure/virtual-network/tutorial-filter-network-traffic?tabs=portal?

Yes ✅ it’s possible to build a GitHub Pages blog that behaves like that Microsoft Docs page — with a **left-hand navigation tree (by category)** and a **switchable view (by date, tags, etc.)**.

GitHub Pages is just **Jekyll** (or any static site generator) behind the scenes, so you can structure your blog like a documentation site.

---

### 🔑 How to achieve it

#### 1. Left Sidebar by Category

* Use **Jekyll Collections** or **Categories**.
* In `_config.yml`, enable categories:

```yaml
collections:
  posts:
    output: true

defaults:
  - scope:
      path: ""
      type: "posts"
    values:
      layout: "post"
```

* Then create a sidebar include (`_includes/sidebar.html`) that loops through categories:

```liquid
<nav class="sidebar">
  <h3>Categories</h3>
  <ul>
    {% for category in site.categories %}
      <li>
        <a href="/categories/{{ category[0] }}">{{ category[0] }}</a>
        <ul>
          {% for post in category[1] %}
            <li><a href="{{ post.url }}">{{ post.title }}</a></li>
          {% endfor %}
        </ul>
      </li>
    {% endfor %}
  </ul>
</nav>
```

This will look like Microsoft Docs’ expandable navigation.

---

#### 2. Switch Between “By Category” and “By Date”

* Create two index pages:

  * `categories.html` → loops by category (as above).
  * `archive.html` → loops by date:

```liquid
<h3>Posts by Date</h3>
<ul>
  {% for post in site.posts %}
    <li>{{ post.date | date: "%Y-%m-%d" }} – <a href="{{ post.url }}">{{ post.title }}</a></li>
  {% endfor %}
</ul>
```

* Add navigation links (e.g., in `_layouts/default.html` or a navbar) so users can toggle between views.

---

#### 3. Layout/Theme Options

To make it look more like Microsoft Docs, you can:

* Use a **docs-like Jekyll theme**, for example:

  * [just-the-docs](https://github.com/just-the-docs/just-the-docs) (clean sidebar, like MS Docs).
  * [minimal-mistakes](https://github.com/mmistakes/minimal-mistakes) (already supports category/date archives).
  * [doxygen-awesome](https://github.com/jothepro/doxygen-awesome-css) (if you want a docset-like feel).

---

#### 4. Optional Enhancements

* **Search bar**: add [jekyll-toc](https://github.com/allejo/jekyll-toc) or [lunr.js search](https://jekyllrb.com/docs/plugins/search/).
* **Collapsible sidebar**: use Bootstrap or pure CSS/JS to expand/collapse categories.
* **Tabs (like "Portal / CLI / PowerShell")**: can be done with [tabbed content in Markdown](https://just-the-docs.github.io/just-the-docs/docs/ui-components/tabs/).

---

👉 If you want something **exactly like learn.microsoft.com**, the closest starter is [just-the-docs](https://github.com/just-the-docs/just-the-docs) — it already has:

* Sidebar navigation
* Categories
* Search
* Mobile-friendly layout

---

Would you like me to show you how to **adapt your current blog repo** to add a sidebar and archive page, or would you prefer to **start fresh with just-the-docs** and migrate posts in?
