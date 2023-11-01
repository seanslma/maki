# Hover
Show extra info when the cursor is over the figure data.

## example
```py
fig = go.Figure(
    go.Bar(
        x=df['population'],
        y=df['country'],
        orientation='h',
        name='population',
        marker=dict(color=df['color']),
        customdata=np.stack((
            df['country'],
            df['area'],
            df['population'],
        ), axis=-1)
    )
)

hover_items = [
    '<span style="font-size: 1rem;"><b>%{customdata[0]}</b></span>',
    '<span style="font-size: 1rem;">Area: <i>%{customdata[1]}</i></span>',
    '<span style="font-size: 0.9rem;">Population: %{customdata[2]}</span>'
]

fig.update_traces(
    hovertemplate='<br>'.join(hover_items) + '<extra></extra>'
)
```
