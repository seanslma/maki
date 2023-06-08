# Issue

## challenges
https://medium.com/analytics-vidhya/5-challenges-when-using-plotly-dash-for-interactive-web-apps-849f442582f7

- same input will trigger callbacks for all pages - can we only run callbacks for that page?
- cannot update the same output using two callbacks - need to merge them into one and use `dash.callback_context` to determine which input has changes

## Dependent callbacks are not waited and executed in order 
https://github.com/plotly/dash/issues/1519

when city is `dc` and select country `UK`, the callback will fail as there is no population for country `UK` and city `dc`.

```py
COUNTRIES = ['US', 'UK']
PUPOLATION = [
    ['US', 'dc'],
    ['UK', 'el'],
]
country_radio = html.Div([
    dbc.RadioItems(
        id='country-radio',
        className="btn-group",
        labelClassName="btn btn-secondary",
        labelCheckedClassName="active",
        options=[{'label': i, 'value': i} for i in COUNTRIES],
        value='US',
    ),
], className="radio-group", style={"textAlign": "center"})

city_dropdown = dcc.Dropdown(
    id='select-city',
    options=[],
    multi=False,
)

@app.callback(
    Output('population', 'data'),
    Input('country-city-population', 'data'),
    Input('country-radio', 'value'),
    Input('select-city', 'value'),
)
def city_population(
  country_city_population, 
  country, 
  city,
):
    df = (
        pd.DataFrame(country_city_population)
        .query('country == @country & city == @city')
    )
    population = df['population]'[0]
    return population
```
