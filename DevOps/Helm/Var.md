# Variable

## variable name
Hyphen in helm chart var/subchart names
- Hyphen `-` is not allowed in variable and subchart names and `index` is a workaround
- https://github.com/helm/helm/issues/2192
- https://stackoverflow.com/questions/63853679/helm-templating-doesnt-let-me-use-dash-in-names
- example
```yaml
mysub-chart:
  servicename: mysubchart-service
# solution
value: {{ index .Values "mysub-chart" "servicename" }}

# another example
x.y-def: '{{ index .Values.x "y-def" }}'
```
