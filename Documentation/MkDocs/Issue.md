# Issue

## Markdown files in root folder
mkdocs does not allow markdown files in root folder.

solution:
- use `symlink`
- create a new folder
- link all root files and folders to that new folder
- this new folder should also be under git source control

```sh
mkdir _docs
ln -s ../README.md _docs/index.md
ln -s ../AI _docs/AI
ln -s ../AWS _docs/AWS
ln -s ../Azure _docs/Azure
ln -s ../Coding _docs/Coding
ln -s ../Cybersecurity _docs/Cybersecurity
ln -s ../Data _docs/Data
ln -s ../DevOps _docs/DevOps
ln -s ../Documentation _docs/Documentation
ln -s ../Energy _docs/Energy
ln -s ../Learn _docs/Learn
ln -s ../ML _docs/ML
ln -s ../Optimization _docs/Optimizaton
ln -s ../PowerBI _docs/PowerBI
ln -s ../Python _docs/Python
ln -s ../SQL _docs/SQL
ln -s ../System _docs/System
```

## Remove all empty spaces in html files
Option #1: Use the `mkdocs-minify-plugin`
- not good
- the plugn is old and has many issue

```sh
pip install mkdocs-minify-plugin
```
```yaml
plugins:
  - search
  - awesome-pages
  - minify:
      minify_html: true
      minify_js: true
      minify_css: true
      htmlmin_opts:
          remove_comments: true
          reduce_empty_attributes: true
```

Option #2: Use the `minify-html`
- rust
- fast

```sh
pip install minify-html
```

Add the processing step in `deploy.sh` file
```sh
# ... after mkdocs build ...

echo "⚡ Minifying HTML files..."
python3 -c "
import os
import minify_html

for root, dirs, files in os.walk('_site'):
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r') as f:
                minified = minify_html.minify(f.read(), minify_js=True, minify_css=True)
            with open(path, 'w') as f:
                f.write(minified)
"
```

## Add `Last updated on d mmm yyyy`
- `pip install mkdocs-git-revision-date-localized-plugin`
- update `mkdocs.yml`
```yaml
plugins:
- search
- awesome-pages
- git-revision-date-localized:
    type: custom
    custom_format: "%d %b %Y"  # Results in: 19 Jan 2026
    enable_fallback: true      # Uses build date if file isn't in Git yet
```
- in `on_page_context` update footer such as `copyright`
