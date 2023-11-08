# Row

## example
Put two figs at left-top and 2 at right-top, and 1 at the bottom

Content in `[]` will be aligned horizontally.
```py
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Sample data and figures
fig1 = px.scatter(x=[1, 2, 3], y=[4, 5, 6])
fig2 = px.bar(x=[1, 2, 3], y=[7, 8, 9])
fig3 = px.line(x=[1, 2, 3], y=[4, 5, 6])
fig4 = px.scatter(x=[1, 2, 3], y=[7, 8, 9])
fig5 = px.bar(x=[1, 2, 3], y=[10, 11, 12])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig1), width=6),
        dbc.Col(dcc.Graph(figure=fig2), width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig3), width=6),
        dbc.Col(dcc.Graph(figure=fig4), width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig5), width=12),
    ]),
], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
```
