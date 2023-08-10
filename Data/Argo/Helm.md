# Helm
https://github.com/argoproj/argo-helm/blob/main/charts/argo-workflows/values.yaml

## install Argo using Helm
```
helm repo add argo https://argoproj.github.io/argo-helm
helm repo update
helm install argo argo/argo-workflows --namespace argo --create-namespace
```
