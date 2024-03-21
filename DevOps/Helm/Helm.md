<!-- {% raw %} -->
# Helm
Template cheatsheet:
https://lzone.de/cheat-sheet/Helm%20Templates

## Helm vs Kustomize
Kustomize:
- Simple deployments with straightforward configuration needs.
- Applying environment-specific adjustments to existing manifests.
- Integrating with GitOps workflows for declarative configuration management.
Helm:
- Complex applications with multiple components and dependencies.
- Standardized packaging and deployment across environments.
- Leveraging pre-built charts from public repositories.

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
```yaml
rollingUpdate:
  maxSurge: 1
  {{ if gt .Values.replicaCount 3.0 }}
  maxUnavailable: 0
  {{ else }}
  maxUnavailable: 1
  {{ end }}
```

## remove whitespace `{{- xyz }}`
```
{{- 3 }} means "trim left whitespace and print 3"
```

<!-- {% endraw %} -->
