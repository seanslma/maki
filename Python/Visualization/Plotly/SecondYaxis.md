# Second y-axis

## Syncing Axes Ticks does not work in 5.16.1
```py
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(
    go.Scatter(
        x=df['date'], 
        y=df['price'], 
        mode='lines', 
        name='price', 
        line=dict(color='blue'),
    ), 
)
fig.add_trace(
    go.Scatter(
        x=df['date'], 
        y=df['quantity'], 
        yaxis='y2',
        mode='lines', 
        name='quantity', 
        line=dict(color='red'),
    ),     
)
fig.update_layout(          
    plot_bgcolor='white',
    width=28 * 37.795,  # Convert cm to pixels (1 cm = 37.795 pixels)
    height=14 * 37.795,  # Convert cm to pixels (1 cm = 37.795 pixels)
    legend=dict(
        xanchor='left',
        x=0.01,
        yanchor='top',
        y=0.99,        
    ),
    xaxis=dict(
        # title=dict(text='date'),
        mirror=True,
        # ticks='outside',
        showline=True,
        linecolor='black',
        gridcolor='lightgrey',
    ),   
    yaxis=dict(
        title=dict(text='price'),
        mirror=True,
        # ticks='outside',
        showgrid=False,
        showline=True,
        linecolor='black',
        gridcolor='lightgrey',
        side='left',
    ),
    yaxis2=dict(
        title=dict(text='quantity'),
        mirror=True,
        # ticks='outside',
        showgrid=False,
        showline=True,
        linecolor='black',
        gridcolor='lightgrey',
        side='right',
        overlaying='y',
        tickmode='sync', # does not work
    ),    
)  
fig.show()
```
