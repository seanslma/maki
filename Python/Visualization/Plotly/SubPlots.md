## SubPlots
https://plotly.com/python-api-reference/generated/plotly.subplots.make_subplots.html

## second y-axis

## grid

## vertical space between subplots
```
from plotly.subplots import make_subplots
fig = make_subplots(
    rows=4, cols=1, row_heights=[0.2, 0.2, 0.2, 0.4], 
    shared_xaxes=True, 
    specs=[[{'secondary_y': True}]]*4,
    vertical_spacing=0.02,
)
```
## legend for each subplot
https://community.plotly.com/t/associating-subplots-legends-with-each-subplot-and-formatting-subplot-titles/33786/8

use `legendgroup`
```py
fig.append_trace(go.Scatter(
    x=df.query("country == 'Canada'")['year'],
    y=df.query("country == 'Canada'")['lifeExp'],
    name = 'Canada',
    legendgroup = '1'
), row=1, col=1)
```
