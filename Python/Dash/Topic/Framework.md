# Framework

## how to create a website using dash including top navbar and side toc
does not work
```py
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Create a top navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="#")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Page 1", href="#page-1"),
                dbc.DropdownMenuItem("Page 2", href="#page-2"),
            ],
            label="Pages",
        ),
    ],
    brand="Your Website",
    brand_href="#",
    dark=True,
)

# Create a side toc
side_toc = dbc.Nav(
    children=[
        dbc.NavItem(dbc.NavLink("Introduction", href="#introduction")),
        dbc.NavItem(dbc.NavLink("Data Analysis", href="#data-analysis")),
        dbc.NavItem(dbc.NavLink("Conclusion", href="#conclusion")),
    ],
    vertical=True,
)

# Create the page content
page_content = dbc.Container(
    children=[
        dbc.Row(
            children=[
                dbc.Col(side_toc, width=2),
                dbc.Col(
                    children=[
                        html.Div([
                            html.H2("Section 1", id="section-1"),
                            html.P("This is the content of Section 1."),
                        ]),
                        html.Div([
                            html.H2("Section 2", id="section-2"),
                            html.P("This is the content of Section 2."),
                        ]),
                        html.Div([
                            html.H2("Section 3", id="section-3"),
                            html.P("This is the content of Section 3."),
                        ]),                        
                    ],                    
                    width=10,
                ),
            ],
        ),
    ],
    fluid=True,
)

# Create the layout
app.layout = dbc.Container(
    children=[navbar, page_content],
)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
```
