# Certificate

## check expiration
https://github.com/Azure/AKS/issues/2347

## rotate certificate
- https://stackoverflow.com/questions/65219904/kubernetes-azures-aks-suddenly-gives-error-kubectl-x509-certificate-has-expi
- https://learn.microsoft.com/en-us/azure/aks/certificate-rotation

manual certificate rotation
```sh
az aks rotate-certs -g $RESOURCE_GROUP_NAME -n $CLUSTER_NAME
az aks get-credentials -g $RESOURCE_GROUP_NAME -n $CLUSTER_NAME --overwrite-existing
```
