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
## custom css
https://stackoverflow.com/questions/50844844/python-dash-custom-css
- make a `assets` folder in the same directory as your app.py. Put all your .cssand .js files there.
- initialize the app object by giving the `__name__` as the first argument; use `app = dash.Dash(__name__)` instead of `app = dash.Dash()`.
- Now Dash will automatically load your CSS and JS files. To force a correct loading order (especially important with CSS), it is recommended to name your files as 01_first.css, 02_some_customization.css, .. 25_load_this_last.css. (the loading order is always alphanumerical)
