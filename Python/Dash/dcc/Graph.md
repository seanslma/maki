# Graph

dcc.Graph is a component for creating interactive data visualizations.

## example
Here is an example of how to use dcc.Graph and dcc.Loading:
```py
import dash
import dash_core_components as dcc

app = dash.Dash()

# Create a dcc.Graph component.
graph = dcc.Graph(
    id="my-graph",
    figure={
        "data": [
            {
                "x": [1, 2, 3],
                "y": [4, 5, 6],
                "type": "scatter",
                "name": "Series 1",
            },
        ],
        "layout": {"title": "My Graph"},
    },
    style={'height': '100%', 'width': '100%'},
    #style={'height': '500px', 'width': '100%'} # can be relative or absolute size
)

# Wrap the graph component in a dcc.Loading component.
loading_graph = dcc.Loading(
    id="loading-graph",
    children=graph,
    type="circle",
)

# Add the loading_graph component to the layout.
app.layout = html.Div([
    loading_graph,
])

if __name__ == "__main__":
    app.run_server(debug=True)
```
