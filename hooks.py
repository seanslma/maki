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
    now = datetime.datetime.now()
    year = now.year
    date = now.strftime('%-d %b %Y')

    # Replace {year} placeholder with current year
    copyright = config.get('copyright', '')
    copyright = copyright.replace('{year}', str(year))

    # Define dynamic footer components
    updated_at = f'Last updated on {date}'

    # Combine them into the copyright variable
    config['copyright'] = f'{copyright}<br>{updated_at}'

    return config
