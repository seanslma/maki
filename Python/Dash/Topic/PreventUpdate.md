# Prevent Update

In callback how to prevent update based on context.

## Not update non-active url
Do not update when the callback is not for the current page:
```py
app.layout = html.Div(
  [
      dcc.Location(id='my-url', refresh=False),
      html.Div([]),
  ],
  className='page',
)

@app.callback(
    Output('sales-data', 'data'),
    Input('my-url', 'pathname'),
)
def my_fun(pathname):
    if not pathname.endswith('/my-url-path/'):
        raise PreventUpdate
```

## Not update non-active tab
