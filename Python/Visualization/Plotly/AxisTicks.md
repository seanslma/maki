# Axis Ticks
- tickmode: linear, array
- tickformat: %, datetime
- tickangle: default is `auto`
- exponentformat
- tickformatstops
- place ticks and gridlines between categories

## tick label angle
```py
tickangle=60,
```

## axis line and tick labels
```py
showline=False,      # Hide axis line
showticklabels=True  # Show axis tick labels
```

## axis date 
```py
xaxis=dict(
    title=dict(text='date'),
    #side='top',   #show axis on top
    mirror=True,   #also show the axis line on the other side
    ticks='outside',
    showline=True,
    linecolor='black',
    gridcolor='lightgrey',
    dtick='d1', #M1
    tickformat='%d\n%b\n%Y', #%b\n%Y
)
```

## axis range
```py
fig.update_layout(
    xaxis_range=[1,12],
    yaxis_range=[1,10],
)
```

## axis ticks
```py
fig.update_xaxes(
    tickvals=x,             # Specify the tick values
    ticktext=xtick_labels,  # Specify the tick labels
)

fig.update_layout(
    xaxis=dict(
        tickmode='array',       # Enable the custom tick values and labels
        tickvals=x,             # Specify the tick values
        ticktext=xtick_labels,  # Specify the tick labels
    )
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
