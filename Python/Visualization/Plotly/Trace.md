# Trace

## visibility
https://stackoverflow.com/questions/71260018/plotly-hiding-the-trace-initially

Add a trace for legend only
```py
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[1, 2, 3, 4, 5],
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3, 4, 5],
    y=[5, 4, 3, 2, 1],
    visible='legendonly', #True, False and 'legendonly'
))

fig.show()
```
