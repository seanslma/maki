# stacked line chart

https://plotly.com/python-api-reference/

## example
```py
fig = plotly_fig(df, 'fig', 'x', 'y')
fig.write_image('c:/dev/my_figure.png', scale=1.5)
```

## chart
```py
def plotly_fig(
    df: pd.DataFrame,
    title: str,
    xtitle: str,
    ytitle: str,
    xax_cfg: dict | None,
    yax_cfg: dict | None,
    lgd_cfg: dict | None,
    fig_cfg: dict | None,
) -> go.Figure:
    '''
    create a plotly figure based on inputs
    '''

    xax_cfg = merge_dicts(xax_cfg, default_xax_cfg)
    yax_cfg = merge_dicts(yax_cfg, default_yax_cfg)
    lgd_cfg = merge_dicts(lgd_cfg, default_lgd_cfg_rv)
    fig_cfg = merge_dicts(fig_cfg, default_fig_cfg, add=lgd_cfg)

    yfmt = '%{y:,.2f}' #'$%{y:,.2f}', '%{y:,.2%}'
    yhover = f'<br><b>{ytitle}:</b> {yfmt}'
    hover_template = (
        '<b>X:</b> %{x|%Y-%m-%d}'
        '<br><b>T:</b> %{meta}'
        f'{yhover}<extra></extra>'
    )

    fig = go.Figure()
    dts = df.index.get_level_values(xtitle)
    for col in df.columns:
        fig.add_trace(
            go.Scatter(
                x=dts,
                y=df.get(col),
                name=col,
                mode='lines',
                line = dict(width=0.5),
                line_shape='hv',
                fill='tonexty',
                meta=col,
                stackgroup='one',
                hovertemplate=hover_template,
            ),
        )

    fig.update_xaxes(**xax_cfg)
    fig.update_yaxes(**yax_cfg)
    fig.update_layout(**fig_cfg)

    return fig
```

## layaout
```py
default_font = 'DejaVu Sans'
default_fig_cfg = dict(
    width=680,
    height=303,
    title=dict(
        x=0.5,
        y=0.995,
        yanchor='top',
        text=' & '.join(title).replace('_', ' ').title(),
        font_family=default_font,
        font_size=14,
        font_color='#5e6a71',
    ),
    margin=go.layout.Margin(
        l=10, #default 80
        r=3, #default 80
        b=5, #default 80
        t=25  #default 100
    ),
    hovermode='x',
    plot_bgcolor='white',
    paper_bgcolor='white',
)
```

## x-axis
```py
default_xax_cfg = dict(
    title=dict(
        #text=xtitle,
        font_family=default_font,
        font_size=12,
        standoff=0,  #distance between label and xtitle
    ),
    tickfont = dict(
        size = 10,
    ),
    autorange=True,
    fixedrange=False,
    gridcolor='#a0afb8',
    dtick='M1',
    tickformat='%b\n%Y-Q%q',
    linecolor='#5e6a71',
    showspikes=True,
)
```

## y-axis
```py
deafult_yax_cfg = dict(
    title=dict(
        text=ytitle,
        font_family=default_font,
        font_size=12,
        standoff=4,
    ),
    tickfont = dict(
        size = 10,
    ),
    gridcolor='#a0afb8',
    showspikes=True,
)
```

## legend
https://plotly.com/python/reference/#layout-legend
```py
default_lgd_cfg_th = dict(
    x=0.0,
    y=0.955,
    xanchor='left',
    yanchor='bottom',
    orientation='h', #top horizontal
    font=dict(family='Calibri', size=10)
)

default_lgd_cfg_rv = dict(
    x=1.0,
    y=1.0,
    xanchor='left',
    yanchor='top',
    orientation='v', #right vertical
    font=dict(family=default_font, size=10)
)
```
