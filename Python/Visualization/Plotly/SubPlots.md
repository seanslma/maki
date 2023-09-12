## SubPlots
https://plotly.com/python-api-reference/generated/plotly.subplots.make_subplots.html

## second y-axis

## grid

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
