# Bar Plot

```
for col in df.columns:
    col_name = ' '.join(col) if isinstance(col, tuple) else col
    fig.add_trace(
        go.Bar(
            x=df.index.get_level_values('ts'),
            y=df.get(col),
            name=col_name,
            meta=col_name,
            hovertemplate=hover_template,
        ),
    )
```
