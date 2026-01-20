# Hooks

Add `hooks.py` file in the same folder of `mkdocs.yml` file.

## Hooks for pre-processing markdown files
In `hooks.py` add function `def on_page_markdown(markdown, **kwargs)`.

## Hooks for processing config file
In `hooks.py` add function `def on_config(config)`.

## Hooks for processing page files
In `hooks.py` add function `def on_page_context(context, page, config, nav)`.
