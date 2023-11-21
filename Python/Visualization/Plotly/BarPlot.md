# Bar Plot

## basic
```py
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

## group gender bars together
```py
import plotly.graph_objects as go

df = pd.DataFrame({
    'country': ['USA', 'USA', 'USA', 'Canada', 'Canada', 'Canada', 'UK', 'UK', 'UK'],
    'gender': ['Male', 'Female', 'Other', 'Male', 'Female', 'Other', 'Male', 'Female', 'Other'],
    'value': [10, 15, 5, 8, 12, 4, 7, 11, 3],
})

fig = go.Figure()

for gender in df['gender'].unique():
    data = df[df['gender'] == gender]
    fig.add_trace(go.Bar(
        x=data['value'],
        y=data['country'],
        name=gender,
        legendgroup=gender,
        orientation='h',  # Set orientation to horizontal
    ))

fig.update_layout(
    barmode='group',
    bargap=0.2,       #space between groups
    bargroupgap=0.05,   #space between bars in the same group
    title='Grouped Bar Chart by Gender',
    xaxis_title='Value',
    yaxis_title='Country',
    xaxis_side='top',
)

fig.show()
```
