# Authenticate

https://devpress.csdn.net/k8s/62ebe99189d9027116a0fbb9.html
- push charts from github in CI
- pull charts from arc in CD

## ways of authentication
- service principal
- managed identity
- image pull secret
- repository scoped token

## allow aks pull images from acr
We must set role assignment `AcrPull` for aks
