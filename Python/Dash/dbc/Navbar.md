# Navbar

## example
```py
navbar = html.Div([dbc.Navbar([
    dbc.Container(
        dbc.Row([
            dbc.Col(
                html.Img(src=app.get_asset_url('logo.png'), height="20px")
            ),
            dbc.Col(
                dbc.NavbarBrand('My First Dashboard', id='page-title', className='page-title'),
                className='text-center'
            ),
            dbc.Col(),
        ], className='custom-navbar-row', align="center"
        ), fluid=True
    )
], color="#5e6b73", dark=True, className='custom-navbar')])
```
