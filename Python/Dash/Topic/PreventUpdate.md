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
```py
@app.callback(
    [
        Output('loading-summary', 'children'),
        Output('error-modal', 'is_open'),
        Output('error-modal-message', 'children'),
    ],
    [
        Input('summary-tab', 'active_tab'),
    ],
)
def update_data(
    active_tab,
):
    # active-tab is a tab in summary-tab
    if active_tab != 'active-tab':
        raise PreventUpdate
```

## PreventUpdate vs no_update
In Dash, `PreventUpdate` and `no_update` are both used in callback functions to control the updating behavior of the components in the Dash app. However, they serve slightly different purposes.

1. **`PreventUpdate`:**
   - If a callback returns `PreventUpdate`, it tells Dash to prevent the callback from updating the output. This is useful when you want to prevent a callback from being triggered under certain conditions.
   - For example, you might have a callback that updates a graph based on a user's input, but you want to prevent the graph from updating if the input doesn't meet a certain condition. In such a case, you can return `PreventUpdate` to prevent the update from happening.

    ```python
    @app.callback(
        Output('output-graph', 'figure'),
        [Input('input-dropdown', 'value')]
    )
    def update_graph(selected_value):
        if selected_value is None or selected_value < 0:
            raise PreventUpdate
        # Your code to update the graph based on the valid input
    ```

2. **`no_update`:**
   - If a callback returns `no_update`, it tells Dash to keep the current state of the output unchanged. This is useful when you want to selectively update certain outputs while leaving others unchanged.
   - For example, you might have a callback that updates multiple components, but you only want to update one of them based on a certain condition. You can use `no_update` for the other components to keep their current state.

    ```python
    @app.callback(
        [Output('output-div', 'children'),
         Output('output-graph', 'figure')],
        [Input('input-dropdown', 'value')]
    )
    def update_components(selected_value):
        if selected_value is None or selected_value < 0:
            return 'Invalid input', no_update
        # Your code to update the output-div and output-graph
    ```

In summary, `PreventUpdate` is used to entirely prevent the callback from triggering an update, while `no_update` is used to selectively keep certain outputs unchanged while allowing others to be updated within the same callback.
