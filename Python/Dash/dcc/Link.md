# Link

## link to other url
Without setting `refresh=True` only the url will change but the web content (linked to external app) will remain the same. Seems does not work! Must use full url!
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
this one?
https://stackoverflow.com/questions/66127435/dash-plotly-how-to-redirect-to-external-link-which-will-redirect-to-dash

Redirect to a new tab:
https://community.plotly.com/t/link-to-an-external-site-in-a-new-browser-tab/7249
