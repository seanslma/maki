# Issue

## challenges
https://medium.com/analytics-vidhya/5-challenges-when-using-plotly-dash-for-interactive-web-apps-849f442582f7

- same input will trigger callbacks for all pages - can we only run callbacks for that page?
- cannot update the same output using two callbacks - need to merge them into one and use `dash.callback_context` to determine which input has changes

