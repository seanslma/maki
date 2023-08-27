# Express

## line
https://plotly.com/python-api-reference/generated/plotly.express.line

Note: `width` and `height` are in `pixel` not `mm`. 1 pixel = 0.2645833333 mm and 1 mm = 3.7795275591 pixel.

how to set the legend and color???
```py
fig = px.line(d1, x='ts', y='val', width=18*60, height=7*60)
fig.add_scatter(x=d2['ts'], y=d2['val'], mode='lines')
fig.show()
```
