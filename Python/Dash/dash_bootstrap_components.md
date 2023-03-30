# dash_bootstrap_components

`dbc.Modal` is a component in the `dash_bootstrap_components` library that allows you to create a modal dialog box in a Dash application using Bootstrap styling.

A modal dialog box is a type of popup window that appears on top of the current page and blocks interaction with the rest of the page until the user closes it. 
It is often used to display important information or to prompt the user for input.

```py
import dash
import dash_bootstrap_components as dbc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

modal = dbc.Modal(
    [
        dbc.ModalHeader("Modal Header"),
        dbc.ModalBody("Modal Body"),
        dbc.ModalFooter(
            html.Button("Close", id="close-modal", className="ml-auto")
        ),
    ],
    id="modal",
    size="lg",
    centered=True,
)

app.layout = html.Div(
    [
        html.H1("Dash Modal Example"),
        html.Button("Open Modal", id="open-modal"),
        modal,
    ]
)

@app.callback(
    dash.dependencies.Output("modal", "is_open"),
    [dash.dependencies.Input("open-modal", "n_clicks"), dash.dependencies.Input("close-modal", "n_clicks")],
    [dash.dependencies.State("modal", "is_open")],
)
def toggle_modal(open_clicks, close_clicks, is_open):
    if open_clicks or close_clicks:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)

```
