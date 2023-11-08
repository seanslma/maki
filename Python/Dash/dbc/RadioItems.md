# RadioItems

## example
An inline radio items list with a lable `Metric: `.
```py
html.Div([
    html.Div(
        'Metric: ',
        style={
            'fontWeight': 'bold',
            'flex': '0 0 auto',
            'marginRight': '3px',
        }
    ),
    dbc.RadioItems(
        id='accuracy-metric-radio',
        options=[
            {'label': k, 'value': v}
            for (k, v) in METRICS_DICT.items()
        ],
        value=list(METRICS_DICT.values())[0],
        inline=True,
    )
], style={
    'display': 'flex',
    'flex': '1',
    'justifyContent': 'end',
})
```
