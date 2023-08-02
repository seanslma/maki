# Callback

https://dash.plotly.com/basic-callbacks

callback functions must be imported to layout, otherwise there is no response when click the tab.

## Input
Changes in any of inputs will trigger callback run. 

## Output
Output can be used as the input of another callback.

## State
State will not trigger callback run. But will provide the current value of the state variables as input.

## dash.exceptions.PreventUpdate
https://dash.plotly.com/advanced-callbacks

By raising a `PreventUpdate` exception, the callback outputs will not be updated.

Can be used to prevent update when the callback is not for the current page:
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

## dash.no_update
Using dash.no_update to update only some of the callback outputs.

Detect which input trigged the callback: 
https://stackoverflow.com/questions/62642418/is-there-a-way-to-prevent-a-callback-from-firing-in-dash
```py
from dash import callback_context, no_update

@app.callback(
    Output("url", "search"),
    Output("picker-id", "value"),
    Input("url", "search"),
    Input("picker-id", "value"),
)
def my_update(url_search):
    changed_inputs = [
        x["prop_id"]
        for x in callback_context.triggered
    ]
    if "picker-id.value" in changed_inputs:
        return no_update, 100
    else:
        return '?userid=100', no_update
```

## clientside callback
```py
app.layout = html.Div(
    html.Div(id='my-div'),
    dcc.Tabs(
        id='tabs-a',
        value=None,
        children=[
            dcc.Tab(label='Tab 1', value='tab1'),
            dcc.Tab(label='Tab 2', value='tab2'),
        ],
    )
)

app.clientside_callback(
    '''
    function(tab_value) {
        if (tab_value === 'tab1') {
            document.title = 'Tab DEV'
        }
        else if (tab_value === 'tab2') {
            document.title = 'Tab PRD'
        }
    }
    ''',
    Output('my-div', 'children'),
    [Input('tabs-a', 'value')],
)
```
