# Multi-page

## switch page based on page url
```py
app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content'),
    ]
)

@app.callback(
   Output('page-content', 'children'),
   Input('url', 'pathname'),
)
def load_page(pathname):
    if pathname == '/':
        return html.Div("Main")
    elif pathname == "/dev":
        return html.Div("DEV")
    else:
        return no_update
```
