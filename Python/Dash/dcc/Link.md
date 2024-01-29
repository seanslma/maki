# Link

## link to other url
Without setting `refresh=True` only the url will change but the web content will remain the same.
```py
dbc.Col([
    dcc.Link(
        'test',
        href='sales/test',
        refresh=True, #refresh the page after redirect
        id='sales-test',
        className='navbar-link',
    ),
    dcc.Link(
        'prod',
        href='sales/prod',
        refresh=True, #refresh the page after redirect
        id='sales-prod',
        className='navbar-link',
    ),
], className='navbar-links'
)
```
