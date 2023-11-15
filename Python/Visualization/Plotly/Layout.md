# Layout

## fig.update_layout
```py
fig.update_layout(          
    autosize=True,
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(
        t=20,
        b=20,
        l=20,
        r=20,
    ), #the default margin might be too large
    legend=dict(
        orientation='h',
        xanchor='left',
        x=0.01,
        yanchor='top',
        y=0.98,
    ),
    xaxis=dict(
        # title=dict(text='date'),
        mirror=True,
        # ticks='outside',
        showline=True,
        linecolor='black',
        gridcolor='lightgrey',
        dtick='M1',
        tickformat='%b\n%Y',
    ), 
    xaxis2=dict(
        # title=dict(text='date'),
        mirror=True,
        # ticks='outside',
        showline=True,
        linecolor='black',
        gridcolor='lightgrey',
        dtick='M1',
        tickformat='%b\n%Y',
    ),         
    yaxis=dict(
        title=dict(text='mean'),
        mirror=True,
        ticks='outside',
        showgrid=False,
        showline=True,
        linecolor='black',
        gridcolor='lightgrey',
        # side='left',
    ),
    yaxis2=dict(
        title=dict(text='std'),
        mirror=True,
        ticks='outside',
        showgrid=False,
        showline=True,
        linecolor='black',
        gridcolor='lightgrey',
        # side='left',
    ),    
)  
```
