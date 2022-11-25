# Callback

https://dash.plotly.com/basic-callbacks


## Input
Changes in any of inputs will trigger callback run. 

## Output
Output can be used as the input of another callback.

## State
State will not trigger callback run. But will provide the current value of the state variables as input.

## dash.exceptions.PreventUpdate
https://dash.plotly.com/advanced-callbacks

By raising a `PreventUpdate` exception, the callback outputs will not be updated.

## dash.no_update
Using dash.no_update to update only some of the callback outputs.
