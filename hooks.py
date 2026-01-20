import re
import datetime


def on_page_markdown(markdown, **kwargs):
    """
    Add blank line before lists that don't have one.
    Matches: text\n- item (no blank line)
    Replaces with: text\n\n- item (adds blank line)
    """
    # Pattern: non-empty line followed by newline and list item
    # Negative lookbehind ensures previous line isn't already blank
    pattern = r'(?<!\n)\n([-*+]\s)'
    replacement = r'\n\n\1'

    return re.sub(pattern, replacement, markdown)


def on_config(config):
    # Replace {year} once globally
    now = datetime.datetime.now()
    # date = now.strftime('%-d %b %Y')
    copyright = config.get('copyright', '')
    config['raw_copyright'] = copyright.replace('{year}', str(now.year))

    return config


def on_page_context(context, page, config, nav):
    # Determine which date to use
    if page.is_homepage:
        display_date = datetime.datetime.now().strftime('%-d %b %Y')
    else:
        # Try to get the Git date from plugin metadata
        display_date = (
            page.meta.get('git_revision_date_localized')
            or page.meta.get('revision_date')
            or datetime.datetime.now().strftime('%-d %b %Y')
        )
    updated_at = f'Last updated on {display_date}'

    # Remove it from metadata to avoid auto creating `last updated` field
    page.meta.pop('git_revision_date_localized', None)

    # Build a per-page footer WITHOUT mutating the global config
    # Use context['copyright'] instead of config['copyright']
    copyright = config['raw_copyright']
    context['config']['copyright'] = f'{copyright}<br>{updated_at}'

    return context
