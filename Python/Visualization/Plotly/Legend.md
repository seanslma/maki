# Legend

## legend position and orientation
```py
fig.update_layout(
    legend=dict(
        xanchor='left',
        x=0.01,
        yanchor='top',
        y=0.99,
        orientation='h',    
    )
)
```

## multiple legends
https://plotly.com/python/legend/?_gl=1*lf1qk7*_ga*ODEwNTk5NTE4LjE2OTkzMTEyNDI.*_ga_6G7EE0JNSC*MTY5OTMxMTI0MS4xLjEuMTY5OTMxMTMzNS41Mi4wLjA.#adding-multiple-legends
```py
fig = go.Figure(
    data=[
        go.Scatter(x=df_germany.year, y=df_germany.gdpPercap, name="Germany"),
        go.Scatter(x=df_france.year, y=df_france.gdpPercap, name="France"),
        go.Scatter(
            x=df_averages_europe.index,
            y=df_averages_europe.gdpPercap,
            name="Europe",
            legend="legend2",
        ),
        go.Scatter(
            x=df_averages_americas.index,
            y=df_averages_americas.gdpPercap,
            name="Americas",
            legend="legend2",
        ),
    ],
    layout=dict(
        title="GDP Per Capita",
        legend={
            "title": "By country",
            "xref": "container",
            "yref": "container",
            "y": 0.65,
            "bgcolor": "Orange",
        },
        legend2={
            "title": "By continent",
            "xref": "container",
            "yref": "container",
            "y": 0.85,
            "bgcolor": "Gold",
        },
    ),
)
```

## grouped legend
https://plotly.com/python/legend/?_gl=1*1j02exd*_ga*ODEwNTk5NTE4LjE2OTkzMTEyNDI.*_ga_6G7EE0JNSC*MTY5OTMxMTI0MS4xLjEuMTY5OTMxMTY4NS42MC4wLjA.#grouped-legend-items
```py
import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[2, 1, 3],
    legendgroup="group",  # this can be any string, not just "group"
    legendgrouptitle_text="First Group Title",
    name="first legend group",
    mode="markers",
    marker=dict(color="Crimson", size=10)
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[2, 2, 2],
    legendgroup="group",
    name="first legend group - average",
    mode="lines",
    line=dict(color="Crimson")
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[4, 9, 2],
    legendgroup="group2",
    legendgrouptitle_text="Second Group Title",
    name="second legend group",
    mode="markers",
    marker=dict(color="MediumPurple", size=10)
))

fig.add_trace(go.Scatter(
    x=[1, 2, 3],
    y=[5, 5, 5],
    legendgroup="group2",
    name="second legend group - average",
    mode="lines",
    line=dict(color="MediumPurple")
))

fig.update_layout(title="Try Clicking on the Legend Items!")

fig.show()
```
