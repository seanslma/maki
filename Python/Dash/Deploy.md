# Deploy

## DASH_REQUESTS_PATHNAME_PREFIX
use `requests_pathname_prefix` to remove the default slask `/`:
- https://dash.plotly.com/reference
- https://lukesingham.com/how-to-deploy-plotlys-dash-using-shinyproxy/

```yaml
env:
  - name: DASH_REQUESTS_PATHNAME_PREFIX
    value: "/<namespace>/<app-name>/"
```
