<!-- {% raw %} -->
# Helm
Template cheatsheet:
https://lzone.de/cheat-sheet/Helm%20Templates

## install
https://helm.sh/docs/intro/install/
- download it: `wget https://get.helm.sh/helm-v3.0.0-linux-amd64.tar.gz` from https://github.com/helm/helm/releases
- unpack it: `tar -zxvf helm-v3.0.0-linux-amd64.tar.gz`
- move to desired destination: `mv linux-amd64/helm /usr/local/bin/helm`

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

<!-- {% endraw %} -->
