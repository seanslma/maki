# Managed identity

## Service principal
not recommended:
https://learn.microsoft.com/en-us/azure/aks/kubernetes-service-principal?tabs=azure-cli

## managed identity
https://learn.microsoft.com/en-us/azure/aks/use-managed-identity

check type of managed identity the cluster is used:
```sh
az aks show --name myAKSCluster --resource-group myResourceGroup --query identity.type --output tsv 
```
- If the cluster is using a managed identity, the value of the type property will be either `SystemAssigned` or `UserAssigned`.
- If the cluster is using a service principal, the value of the type property will be `null`. 
