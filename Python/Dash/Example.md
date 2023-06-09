# Example

```py
import numpy as np
import pandas as pd
import plotly.express as px
from jupyter_dash import JupyterDash
from dash import Dash, dcc, html, Input, Output, State, no_update
from dash.exceptions import PreventUpdate

import dash_bootstrap_components as dbc
FA = "https://use.fontawesome.com/releases/v5.15.4/css/all.css"

app = JupyterDash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP, FA],
)

country_radio = html.Div([
    dbc.RadioItems(
        id='country-radio',
        className="btn-group",
        labelClassName="btn btn-secondary",
        labelCheckedClassName="active",
        options=[{'label': i, 'value': i} for i in ['US', 'UK']],
        value='US',
    ),
], className="radio-group", style={"textAlign": 'left'})

city_dropdown = html.Div([
    dcc.Dropdown(
        id='select-city',
        options=[],
        multi=False,
    ),
], className='filter-item')

app.layout = html.Div([
    country_radio,
    city_dropdown,
    html.Div(id='population-text'),
])

data = pd.DataFrame({
    'country': ['US', 'US', 'UK', 'UK'],
    'city': ['dc', 'el', 'dc', 'ee'],
    'population': ['3m','2m','1m', '5m'],
})

@app.callback(
    Output('select-city', 'options'),
    Output('select-city', 'value'),
    Input('country-radio', 'value'),
    State('select-city', 'options'),
    State('select-city', 'value'),
)
def set_city_options(
    country,
    options,
    selection,
):
    if not country:
        raise PreventUpdate

    options = options or []
    selection = selection or []
    if isinstance(selection, str):
        selection = [selection]

    updated_list = data.query('country == @country')['city'].unique()
    updated_options = [dict(label=item, value=item) for item in updated_list]
    options_updated = options != updated_options
    if not options_updated:
        raise PreventUpdate

    updated_selection = np.intersect1d(selection, updated_list).tolist()
    updated_selection.sort()
    selection.sort()
    selection_updated = (
        updated_selection != selection
    )
    if selection_updated:
        return updated_options, updated_selection
    else:
        return updated_options, no_update

@app.callback(
    Output('population-text', 'children'),
    Input('country-radio', 'value'),
    Input('select-city', 'value'),
)
def city_population(
  country, 
  city,
):
    if not country or not city:
        raise PreventUpdate
        
    d1 = data.query('country == @country & city == @city')
    d2 = d1.groupby(['country','city']).agg(lambda col: '/'.join(sorted(set(col))))
    population = d2['population'][0]
    return f'The population of {city} in {country} is: {population}'

if __name__ == '__main__':
    app.run_server(debug=True)
```    
