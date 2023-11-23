# Show and hide

## show/hide element based on html.Div display style
```py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Dropdown(
        id = 'dropdown-to-show_or_hide-element',
        options=[
            {'label': 'Show element', 'value': 'on'},
            {'label': 'Hide element', 'value': 'off'}
        ],
        value = 'on'
    ),
    # Create Div to place a conditionally visible element inside
    html.Div([
        # Create element to hide/show, in this case an 'Input Component'
        dcc.Input(
            id = 'element-to-hide',
            placeholder = 'something',
            value = 'Can you see me?',
        )
    ], 
    style= {'display': 'block'} # <-- This is the line that will be changed by the dropdown callback
    )
])

@app.callback(
   Output(component_id='element-to-hide', component_property='style'),
   [Input(component_id='dropdown-to-show_or_hide-element', component_property='value')],
)

def show_hide_element(visibility_state):
    if visibility_state == 'on':
        return {'display': 'block'}
    if visibility_state == 'off':
        return {'display': 'none'}

if __name__ == '__main__':
    app.run_server(debug=True, port=8059)
```

## show/hide radio items based on tab
```py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)

sort_options = html.Div([
    html.Div([
        html.Div(
            'Sort type: ',
            style={'fontWeight': 'bold', 'flex': '1 0 auto'},
        ),
        dbc.RadioItems(
            id='sort-by',
            options=[
                {'label': v, 'value': v}
                for v in ['name', 'country', 'region']
            ],
            value='country',
            inline=True,
        )
    ], style={'display': 'flex', 'marginTop': '5px'}),
], style={
    'flex': '0 1 auto',
    'display': 'flex',
    'flexDirection': 'column',
    'alignItems': 'center',
    'padding': '5px 7px 10px 7px',
    'marginBottom': '5px',
    'borderBottom': '1px solid #dee2e6',
})

app.layout = html.Div([
    html.Div(id='sort-option-content', children=[
        sort_options,
    ]),    
    dcc.Tabs(id='tabs-example', value='tab1', children=[
        dcc.Tab(label='Tab 1', value='tab1'),
        dcc.Tab(label='Tab 2', value='tab2'),
    ]),
])

@app.callback(
    Output('sort-option-content', 'children'),
    Input('tabs-example', 'value')
)
def update_tab_content(value):
    if value == 'tab1':
        return [sort_options]
    else:
        return []

if __name__ == '__main__':
    app.run_server(debug=True, port=8059)
```
