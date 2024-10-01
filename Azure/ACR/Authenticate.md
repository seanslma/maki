# Authenticate

https://devpress.csdn.net/k8s/62ebe99189d9027116a0fbb9.html
- push charts from github in CI
- pull charts from acr in CD

## allow aks pull images from acr
We must set role assignment `AcrPull` for aks

## connect issue using workload identity
Not solved: https://github.com/Azure/azure-cli/issues/28740

## ways of authentication
https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication?tabs=azure-cli
- service principal
- managed identity
- image pull secret
- repository scoped token

## user-assigned managed identity to login to acr
https://learn.microsoft.com/en-us/azure/container-registry/container-registry-authentication-managed-identity?tabs=azure-cli
```sh
az login --identity --username <identity-id>
az acr login --name my_acr
```
