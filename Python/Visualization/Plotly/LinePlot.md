# Line Plot

## example
Plot two columns from two dfs as lines and set the line color, legend and figure size.
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
