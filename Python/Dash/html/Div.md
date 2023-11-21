# html.Div

In Dash, `html.Div` is a component used to group and organize other components within your layout. It represents a generic HTML division or container.

Here are some key points about `html.Div` in Dash:
- **Container Element:** `html.Div` is an HTML `<div>` element. In web development, the `<div>` element is a generic container that is often used to group and structure content.
- **Structuring Layout:** It helps organize the layout of your Dash application by grouping components together. You can use it to create sections, columns, or other structural divisions in your app.
- **Styling and CSS:** `html.Div` can be assigned CSS classes and styles to control its appearance. You can set properties such as background color, width, height, margins, and more.
- **Children Components:** You can include other Dash components, including other `html.Div` elements, as children of an `html.Div`. This allows you to create nested structures for your layout.

## styling example
Adjust the vertical space between two dcc.Loading objects
```py
left_tab = html.Div([
    html.Div([
        dcc.Loading(
            id='loading-metrics-breakdown-graph',
            type='default',
            color=PRIMARY_COLOR,
        ),
    ], style={'margin-top': '10px'}), #adjust the top space
    html.Div([
        dcc.Loading(
            id='loading-benchmark-metrics-graph',
            type='default',
            color=PRIMARY_COLOR,
        ),
    ], style={'margin-top': '10px'}),
],
className='h-100 justify-content metrics-breakdown',
style={'position': 'absolute', 'inset': '0'},
)
```
