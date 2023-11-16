# Graph

dcc.Graph is a component for creating interactive data visualizations.

## example
Here is an example of how to use dcc.Graph and dcc.Loading:
```py
import dash
from dash import dcc

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

## fig_json['data']
When working with Dash's `dcc.Graph` component, the `fig_json['data'][0]` refers to the first trace or set of data in the graph figure.

```python
import dash
from dash imports as dcc, html
import plotly.graph_objects as go

# Sample data
x_data = [1, 2, 3, 4, 5]
y_data = [10, 11, 12, 13, 14]

# Create a Plotly Figure
fig = go.Figure()
fig.add_trace(go.Scatter(x=x_data, y=y_data, mode='lines', name='Line'))

# Create a Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```

In this example:

- `go.Figure()` is used to create a Plotly figure.
- `fig.add_trace(go.Scatter(...))` adds a trace to the figure. In this case, it's a simple scatter plot with lines connecting the points.
- `dcc.Graph(id='example-graph', figure=fig)` creates a Dash Core Component Graph, and the `figure` attribute is set to the Plotly figure (`fig`) we created earlier.

To access the data of the first trace in the graph using `fig_json['data'][0]`, you can do so by converting the figure to JSON using `fig.to_json()`:

```python
fig_json = fig.to_json()
trace_data = fig_json['data'][0]
print(trace_data)
```

This will give you access to the data of the first trace in the form of a dictionary, 
allowing you to retrieve information about the x and y coordinates, mode, name, and other attributes of the trace.
