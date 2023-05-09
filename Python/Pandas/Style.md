# Style
https://pandas.pydata.org/docs/user_guide/style.html

## set precision
```py
df.style.set_precision(2)
```

## format float
```py
df.style.format('{:.2%}', na_rep='NULL')
df.style.format(precision=3, thousands='.', decimal=',').format_index(str.upper, axis=1)
```

## hide index
```py
df.style.hide_index()
```

## highlight min/max/null in each col
```py
df.style.highlight_min()
df.style.highlight_max()
df.style.highlight_null(null_color='red')
df.style.set_na_rep('missing').highlight_null(null_color='orange') 
```

## bar chart
```py
df.style.bar()
```

## heat map
```py
df.style.background_gradient()
```

## set table properties
```py
df.style.set_properties(**{
    'border': '1.1px solid blue',
    'color': 'magenta',
})
```

## custom style
```py
def color_abs_red(v, x):
    """
    Return a string with css property `'color: red'` for abs(val) > x, black otherwise
    
    v is a scalar and x a non-negative value
    """
    colors = np.where(np.abs(v) > x, 'color: red', 'color: black')
    return colors
df.style.apply(color_abs_red, x=0.01)
```
