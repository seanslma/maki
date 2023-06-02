# Figure Update

## Update trace based on name
Update trace and change its name
```py
# create trace
fig.add_scatter(
    x=df['ts'],
    y=df['val'],
    name=f'My Trace_Name',
    marker_color='#006da0',
    line_shape='hv',
)
# find previous trace name
previous_trace_name = 'Trace_Name'
for trace in fig.data:
    trace_name = trace['name']
    if 'Trace_Name' in trace_name:
        previous_trace_name = trace_name
# update trace
fig.update_traces(
    overwrite=True,
    x=list(forecast_actual['ts']),
    y=list(forecast_actual[model]),
    name=f'current_trace_name', #update name
    selector=dict(name=previous_trace_name),
)
```
