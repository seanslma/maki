# ACR

## aks gets images from acr
https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/cannot-pull-image-from-acr-to-aks-cluster

## pull images from acr to aks
https://learn.microsoft.com/en-us/azure/aks/cluster-container-registry-integration?tabs=azure-cli

## Validate an ACR is accessible from an AKS cluster
```sh
az aks check-acr --name MyManagedCluster --resource-group MyResourceGroup --acr myacr.azurecr.io
```
