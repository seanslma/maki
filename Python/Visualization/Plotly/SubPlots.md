## SubPlots
https://plotly.com/python-api-reference/generated/plotly.subplots.make_subplots.html

## vertical space between subplots
```py
from plotly.subplots import make_subplots
fig = make_subplots(
    rows=4,
    cols=1,
    row_heights=[0.2, 0.2, 0.2, 0.4], 
    shared_xaxes=True, 
    specs=[[{'secondary_y': True}]]*4,
    vertical_spacing=0.02,
)
print(fig.layout) # inspect the axes name for each subplot
```

## secondary y-axis
```py
import numpy as np
import plotly.graph_objects as go

x = np.linspace(1, 7, 12)
y1 = 100+10*np.random.rand(12)
y2 = 2+2*np.random.rand(12)
y3 = 1+3*np.random.rand(12)

t1 = go.Bar(x=x, y=y1, name='y1')  
t2 = go.Scatter(x=x, y=y2, name='y2', yaxis='y2', mode='lines+markers', line=dict(color='orange'))  
t3 = go.Scatter(x=x, y=y3, name='y3', yaxis='y2', mode='lines+markers', line=dict(color='red'))  

layout = go.Layout(    
    width=850, 
    height=450,
    title='Bar-line chart with secondary y-axis', 
    yaxis=dict(title='y1'),            
    yaxis2=dict(title='y2', overlaying='y', side='right'),
)  

fig = go.Figure(data=[t1, t2, t3], layout=layout)  
fig.show()
```

## secondary y-axis using subplots
```py
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(specs=[[{'secondary_y': True}]])

fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[50, 20, 100], name='y1'),
    secondary_y=False,
)
fig.add_trace(
    go.Scatter(x=[1, 2, 3], y=[-20, 50, -100], name='y2'),
    secondary_y=True,
)
fig.update_layout(
    width=750,
    height=450,
    title_text='Secondary y-axis',
    xaxis=dict(title_text='xaxis title'),
    yaxis=dict(title_text='yaxis left'),
    yaxis2=dict(title_text='yaxis right', overlaying='y', tickmode='sync', scaleanchor='y'),
)

fig.show()
```

## subplots with multiple y-axes
https://community.plotly.com/t/can-subplot-support-multiple-y-axes/38891/21

For each subplot, we should specify whether it's a simple x-y chart or has a second y-axis.
```py
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

fig = make_subplots(
    rows=2,
    cols=1, 
    vertical_spacing=0.05, 
    shared_xaxes=True,
    specs=[
        [{'type': 'xy'}], 
        [{'secondary_y': True}],
    ],
)

x = np.linspace(1, 7, 12)
y1 = 1+3*np.random.rand(12)
y2 = 2+2*np.random.rand(12)
y3 = 3+1*np.random.rand(12)
y4 = 4+1*np.random.rand(12)
trcolor = ['#636efa', '#EF553B', '#00cc96', '#ab63fa']
fig.add_trace(
    go.Scatter(x=x, y=y1, name='y1'), 
    row=1, col=1,
)
fig.add_trace(
    go.Scatter(x=x, y=y2, name='y2'), 
    row=2, col=1,
)
fig.add_trace(
    go.Scatter(x=x, y=y3, name='y3', showlegend=False), 
    row=2, col=1, 
    secondary_y=True,
)
fig.add_trace(
    go.Scatter(x=x, y=y4, name='y4', xaxis='x2', yaxis='y4')
)

fig.update_layout(
    title_text='Subplots with multiple yaxes', 
    title_x=0.5,
    margin_l=2,
    width=750,
    height=450,
    xaxis_domain= [0.3, 1], 
    xaxis2_title='common xaxis_title',
    xaxis2_domain=[0.3, 1],
    yaxis4=dict(
        anchor= 'free',
        overlaying= 'y2',
        side ='left',
        position=0.17,
        title_text='y4',
        titlefont_color=trcolor[3],      
        tickfont_color=trcolor[3],
    ),
)

for j, ax in enumerate(['yaxis', 'yaxis2', 'yaxis3']):
    fig.layout[ax].update(
        title_text=f'y{j+1}', #merge the initial dict fig.layout[ax] with a new ax related dict
        titlefont_color=trcolor[j],      
        tickfont_color=trcolor[j],
    )
fig.show()
```

## legend for each subplot
https://community.plotly.com/t/associating-subplots-legends-with-each-subplot-and-formatting-subplot-titles/33786/8

use `legendgroup`
```py
fig.append_trace(go.Scatter(
    x=df.query("country == 'Canada'")['year'],
    y=df.query("country == 'Canada'")['lifeExp'],
    name = 'Canada',
    legendgroup = '1'
), row=1, col=1)
```
