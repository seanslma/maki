# Datetime

## x-axis datetime format
https://plotly.com/python/time-series/
```py
import plotly.express as px
df = px.data.stocks()
fig = px.line(
    df, x="date", y=df.columns,
    hover_data={"date": "|%B %d, %Y"},
    title='custom tick labels',
)
fig.update_xaxes(
    dtick="M1",
    tickformat="%b\n%Y",
)
fig.show()
```
