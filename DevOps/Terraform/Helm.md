# Helm

## type casting
https://github.com/yaml/YAML2/wiki/Type-casting
```
ports:
- containerPort: !!int {{ .Values.containers.app.port }}
```

## if else
https://github.com/bitnami/charts/blob/master/bitnami/apache/templates/hpa.yaml
```
rollingUpdate:
  maxSurge: 1
  {{ if gt .Values.replicaCount 3.0}}
  maxUnavailable: 0
  {{ else }}
  maxUnavailable: 1
  {{ end }}
```  
