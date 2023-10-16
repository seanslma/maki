# Span

## difference between html.Span and html.Div
- `Span` is an inline element and `Div` is a block-level element. 
- `Span` elements will flow with the surrounding text, while Div elements will start a new line and take up the full width of their container.

**When to use Span**: 
Span elements are typically used to group together small pieces of content that need to be styled differently from the surrounding text. 
For example, you might use a Span element to highlight a word or phrase, or to add a link to a piece of text.

**When to use Div**: 
Div elements are typically used to group together larger pieces of content, such as paragraphs, headings, and images. 
Div elements can also be used to create more complex layouts, such as navigation bars, menus, and product galleries.

## example of div and span
Create an inline dropdown and single date picker
```py
html.Div([
    html.Span(
        'Model: ', style={'marginRight': '7px'}
    ),
    dcc.Dropdown(
        id='model-dropdown',
        options=[
            {'label': k, 'value': v} for (k, v) in MODELS_DICT.items()
        ],
        value=None,
        clearable=True,
        style={'width': '170px'}
    ),
    html.Span(
        'Date: ', style={'margin': '0 7px'}
    ),
    dcc.DatePickerSingle(
        id='creation-date',
        min_date_allowed=MIN_DATE,
        max_date_allowed=datetime.now().date(),
        display_format='YYYY-MM-DD',
        style={'marginRight': '7px'}
    )
], style={
    'display': 'flex',
    'alignItems': 'center',
    'flex': '0 1 auto',
    'marginTop': '7px',
    'justifyContent': 'end',
})
```
