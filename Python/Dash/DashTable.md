# DashTable

https://dash.plotly.com/datatable

## format

## sorting
```py
sort_action = 'native'
```

## filtering
```py
filter_action = 'native'
```

## pagination

## example
```py
import dash
import dash_table

app = dash.Dash(__name__)

# Create a DataTable component
table = dash_table.DataTable(
    id='table',
    columns=[{'name': 'Name', 'id': 'name'}, {'name': 'Age', 'id': 'age'}, {'name': 'Occupation', 'id': 'occupation'}],
    data=[{'name': 'John Doe', 'age': 30, 'occupation': 'Software Engineer'}, {'name': 'Jane Doe', 'age': 25, 'occupation': 'Doctor'}, {'name': 'Peter Parker', 'age': 20, 'occupation': 'Student'}]
)

# Add the DataTable component to the app layout
app.layout = table

if __name__ == '__main__':
    app.run(debug=True)
```

## export to csv
https://stackoverflow.com/questions/61203436/export-plotly-dash-datatable-output-to-a-csv-by-clicking-download-link

## export to excel 
https://stackoverflow.com/questions/61485943/dash-data-table-download-to-excel

## filter to cols example 
https://community.plotly.com/t/show-and-tell-dashtable-filtering-by-columns-with-external-controls-sliders-dropdowns-inputs/22523/5
```py
import pandas as pd
import random
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.dash_table import DataTable
from dash.exceptions import PreventUpdate
from jupyter_dash import JupyterDash

df = pd.DataFrame({
    'int': [random.randint(1, 100) for i in range(20)],
    'float': [random.random() * x for x in random.choices(range(100), k=20)],
    'str(object)': ['one', 'one two', 'one two three', 'four'] * 5,
    'category': random.choices(['Sat', 'Sun', 'Mon', 'Tue', 'Wed','Thu', 'Fri'], k=20),
    'datetime': pd.date_range('2019-05-01', periods=20),
    'bool': random.choices([True, False], k=20),
})
df['category'] = df['category'].astype('category')

def get_str_dtype(df, col):
    """Return dtype of col in df"""
    dtypes = ['datetime', 'bool', 'int', 'float', 'object', 'category']
    for d in dtypes:
        try:
            if d in str(df.dtypes.loc[col]).lower():
                return d
        except KeyError:
            return None

app = JupyterDash(__name__)

app.layout = html.Div([
    html.Div([
        html.Div(
            id='container_col_select',
            children=dcc.Dropdown(
                id='col_select',
                options=[
                    {
                       'label': c.replace('_', ' ').title(),
                       'value': c,
                    }
                   for c in df.columns
                ]
            ),
            style={'display': 'inline-block', 'width': '30%', 'margin-left': '7%'}
        ),
        # DataFrame filter containers
        html.Div([
            html.Div(
                children=dcc.RangeSlider(id='num_filter', updatemode='drag')
            ),
            html.Div(
                children=html.Div(id='rng_slider_vals')
            ),
        ], id='container_num_filter', ),
        html.Div(
            id='container_str_filter',
            children=dcc.Input(id='str_filter')
        ),
        html.Div(
            id='container_bool_filter',
            children=dcc.Dropdown(
                id='bool_filter',
                options=[
                    {'label': str(tf), 'value': str(tf)}
                    for tf in [True, False]
                ]
            )
        ),
        html.Div(
            id='container_cat_filter',
            children=dcc.Dropdown(
                id='cat_filter', 
                multi=True,
                options=[
                    {'label': day, 'value': day}
                    for day in df['category'].unique()
                ]
            )
        ),
        html.Div([
            dcc.DatePickerRange(
                id='date_filter',
                start_date=df['datetime'].min(),
                end_date=df['datetime'].max(),
                max_date_allowed=df['datetime'].max(),
                initial_visible_month=pd.Timestamp(2019, 5, 10),
            ),
        ], id='container_date_filter'),
    ]),

    DataTable(
        id='table',
        columns=[{'name': i, 'id': i} for i in df.columns],
        style_cell={'maxWidth': '400px', 'whiteSpace': 'normal'},
        data=df.to_dict('records'),
    )
])


@app.callback(
    [
        Output(x, 'style')
        for x in [
            'container_num_filter', 'container_str_filter',
            'container_bool_filter', 'container_cat_filter', 'container_date_filter',
        ]
    ],
    [
        Input('col_select', 'value')
    ],
)
def dispaly_relevant_filter_container(col):
    if col is None:
        return [{'display': 'none'} for i in range(5)]
    dtypes = [['int', 'float'], ['object'], ['bool'],
              ['category'], ['datetime']]
    result = [{'display': 'none'} if get_str_dtype(df, col) not in d
              else {'display': 'inline-block',
                    'margin-left': '7%',
                    'width': '400px'} for d in dtypes]
    return result


@app.callback(
    Output('rng_slider_vals', 'children'),
    [Input('num_filter', 'value')],
)
def show_rng_slider_max_min(numbers):
    if numbers is None:
        raise PreventUpdate
    return 'from:' + ' to: '.join([str(numbers[0]), str(numbers[-1])])


@app.callback([Output('num_filter', 'min'),
               Output('num_filter', 'max'),
               Output('num_filter', 'value')],
              [Input('col_select', 'value')])
def set_rng_slider_max_min_val(col):
    if col is None:
        raise PreventUpdate
    if col and (get_str_dtype(df, col) in ['int', 'float']):
        vmin = df[col].min()
        vmax = df[col].max()
        return vmin, vmax, [vmin, vmax]
    else:
        return None, None, None


@app.callback(
    Output('table', 'data'),
    [
        Input('col_select', 'value'),
        Input('num_filter', 'value'),
        Input('cat_filter', 'value'),
        Input('str_filter', 'value'),
        Input('bool_filter', 'value'),
        Input('date_filter', 'start_date'),
        Input('date_filter', 'end_date'),
    ]
)
def filter_table(
    col, numbers, categories, string, bool_filter, start_date, end_date
):
    if all([
        param is None 
        for param in [
            col, numbers, categories, string, 
            bool_filter, start_date, end_date,
        ]
    ]):
        raise PreventUpdate
    if numbers and (get_str_dtype(df, col) in ['int', 'float']):
        dx = df[df[col].between(numbers[0], numbers[-1])]
        return dx.to_dict('records')
    elif categories and (get_str_dtype(df, col) == 'category'):
        dx = df[df[col].isin(categories)]
        return dx.to_dict('records')
    elif string and get_str_dtype(df, col) == 'object':
        dx = df[df[col].str.contains(string, case=False)]
        return dx.to_dict('records')
    elif (bool_filter is not None) and (get_str_dtype(df, col) == 'bool'):
        bool_filter = True if bool_filter == 'True' else False
        dx = df[df[col] == bool_filter]
        return dx.to_dict('records')
    elif start_date and end_date and (get_str_dtype(df, col) == 'datetime'):
        dx = df[df[col].between(start_date, end_date)]
        return dx.to_dict('records')
    else:
        return df.to_dict('records')

if __name__ == '__main__':
    app.run_server(debug=True)
```
