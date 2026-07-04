# Hooks

- Add `hooks.py` file in the same folder of `mkdocs.yml` file.
- In `mkdocs.yml` file add:
  ```yml
  hooks:
  - hooks.py
  ```

## Hooks for pre-processing markdown files
In `hooks.py` add function `def on_page_markdown(markdown, **kwargs)`.

## Hooks for processing config file
In `hooks.py` add function `def on_config(config)`.

## Hooks for processing page files
In `hooks.py` add function `def on_page_context(context, page, config, nav)`.
