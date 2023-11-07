# Line Plot

## line styles
```py
import numpy as np
import plotly.graph_objects as go

fig = go.Figure()

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 10, 4, 15, 9])
# the length of the dash and space in pixels
line_styles = ['0', '8,3', '8,3,2,3', '3,2', '14,2', '8,3,2,3,2,3', '4,3', '6,3,2,3,2,3,2,3', '2,5']

for i, line_stsyle in enumerate(line_styles):
    fig.add_trace(go.Scatter(
        x=x,
        y=y + 5*i,
        mode='lines',
        line=dict(color='black', dash=line_styles[i])
    ))

fig.show()
```

## example
Plot two columns from two dfs as lines and set the line color, legend and figure size.

if name is not set will be default to the df val col name and line will be using default color rotation
```py
fig = go.Figure()
fig.add_trace(go.Scatter(x=df1['ts'], y=df1['val'], mode='lines', name='line-1', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=df2['ts'], y=df2['val'], mode='lines', name='line-2', line=dict(color='red')))
fig.update_layout(
    xaxis_title='ts',
    yaxis_title='val',
    width=28 * 37.795,  # Convert cm to pixels (1 cm = 37.795 pixels)
    height=14 * 37.795,  # Convert cm to pixels (1 cm = 37.795 pixels)
)  
fig.show()
```
