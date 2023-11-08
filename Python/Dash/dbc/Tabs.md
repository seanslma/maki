# Tabs

https://dash-bootstrap-components.opensource.faculty.ai/docs/components/tabs/

https://dash.plotly.com/dash-core-components/tabs

## example
```py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import datetime

# Create a Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the dropdown and date range picker
dropdown_layout = dbc.FormGroup([
    dbc.Label("Select an item from the dropdown:"),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {"label": "Option 1", "value": "option1"},
            {"label": "Option 2", "value": "option2"},
            {"label": "Option 3", "value": "option3"},
        ],
        value="option1",
    ),
])

date_range_layout = dbc.FormGroup([
    dbc.Label("Select a date range:"),
    dcc.DatePickerRange(
        id="date-range",
        start_date=datetime.date(2023, 1, 1),
        end_date=datetime.date(2023, 1, 7),
    ),
])

# Create the Tabs component
tabs = dbc.Tabs([
    dbc.Tab(label="Dropdown", children=dropdown_layout),
    dbc.Tab(label="Date Range", children=date_range_layout),
])

# Define the app layout
app.layout = dbc.Container([
    html.H1("Dropdown and Date Range Tabs Example"),
    tabs,
])

# Run the app
app.run_server(mode="inline")
```
