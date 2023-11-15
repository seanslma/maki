# Annotation

## update annotation
```py
import plotly.graph_objects as go

fig = go.Figure()
fig.add_trace(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
# Add an annotation with the same font as the subplot title
fig.add_annotation(
    text="Annotation Text",
    x=2, y=5,
    # arrowhead=2, arrowsize=1.5,
    font=dict(
        family="Arial",  # Set the font family to match the subplot title
        size=14,  # Set the font size to match the subplot title
        color="black"  # Set the font color to match the subplot title
    )
)

fig.update_layout(
    title='Subplot Title',
    xaxis_title='X Axis Title',
    yaxis_title='Y Axis Title'
)
fig.layout.annotations[0].update(text="Stackoverflow")

fig.show()
```
- `x`: X-coordinate of the annotation.
- `y`: Y-coordinate of the annotation.
- `xref` and `yref`: Specifies whether the coordinates refer to the "paper" or "axes" domain.
- `text`: The text content of the annotation.
- `showarrow`: Boolean indicating whether to draw an arrow from the annotation to the specified point.
- `arrowhead`: The arrowhead style (options: 0, 1, 2, 3, 4, 5, 6).
- `arrowcolor`: Color of the arrow.
- `arrowwidth`: Width of the arrow.
- `ax`: X-coordinate of the arrow tail.
- `ay`: Y-coordinate of the arrow tail.
- `bordercolor` and `borderwidth`: The color and width of the annotation border.
- `bgcolor`: The background color of the annotation.
- `opacity`: The opacity of the annotation.
- `font`: Dictionary specifying the font properties of the text.
- `align`: Text alignment within the annotation (options: "left", "center", "right").

## change subplot title location
