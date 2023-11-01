# Axis Ticks
- tickmode: linear, array
- tickformat: %, datetime
- exponentformat
- tickformatstops
- place ticks and gridlines between categories

## axis range
```py
fig.update_layout(
    xaxis_range=[1,12],
    yaxis_range=[1,10],
)
```

## example
https://plotly.com/python/tick-formatting/
```py
import plotly.graph_objects as go

fig = go.Figure(go.Scatter(
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    y = [28.8, 28.5, 37, 56.8, 69.7, 79.7, 78.5, 77.8, 74.1, 62.6, 45.3, 39.9],
))

fig.update_layout(
    xaxis = dict(
        tickmode='linear',
        tick0=0.5,
        dtick=0.5,
    )
)

fig.show()
```

## Tickformat
```py
fig.update_layout(
    title='Time Series with Custom Date-Time Format',
    xaxis_tickformat='%d %B (%a)<br>%Y',
    yaxis_tickformat='%',
)
```

## ticksuffix
Add a suffix to the tick labels
```py
fig.update_layout(
    xaxis = dict(        
        linecolor='#909497',
        gridcolor='rgba(0,0,0,0)',
        side='top',
        range=x_range,
        fixedrange=True,     
        ticks='outside',
        tickmode='array',        
        ticklen=4,
        tickwidth=1,
        tickcolor='#909497',
        ticksuffix='%',       
    )
)
```
