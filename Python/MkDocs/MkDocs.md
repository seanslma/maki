# MkDocs
- https://www.mkdocs.org/user-guide/
- https://mkdocs.readthedocs.io/en/0.13.3/user-guide/styling-your-docs/
- https://realpython.com/python-project-documentation-with-mkdocs/

MkDocs is a fast and simple static site generator that’s geared towards building project documentation with Markdown.
```sh
mkdocs new <proj-name> #create a new docs project
mkdocs serve           #run in preview mode
mkdocs build           #build the docs project
mkdocs build --config-file <config-file> --site-dir <output-path>
```

## packages
- `mkdocs` (mkdocs): build static pages from Markdown
- `mkdocstrings` (mkdocstrings-python): auto-generate documentation from docstrings in your code. It's the Python handler for mkdocstrings that allows mkdocstrings to parse Python code.
- `material` (mkdocs-material): style mkdocs documentation


## navigation
https://squidfunk.github.io/mkdocs-material/setup/setting-up-navigation/#instant-loading
```yaml
theme:
  name: material
  custom_dir: theme
  language: en
  features:
    - navigation.indexes
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.tracking
    - search.highlight
    - search.suggest
  palette:
    scheme: preference
    primary: amber
    accent: yellow
  font:
    text: Roboto
    code: Roboto Mono
  icon:
    logo: material/library
    repo: fontawesome/brands/git-alt
```
