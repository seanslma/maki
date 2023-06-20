# CSS

## link className attribute of Dash components to css
```py
app.layout = html.Div([
    html.Div(className="x-div"),
    html.Div(className="y-div"),
])
```

CSS style
```css
.x-div {
    color: red;
}
.y-div {
    color: steelblue;
}
```
