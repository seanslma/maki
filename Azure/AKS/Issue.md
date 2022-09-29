# Issue

## Unable to connect to the server: dial tcp: lookup : no such host
The `Private Cluster` option is enabled while creating the AKS cluster.
```
az aks show -n <aks-name> -g <resource-group-name> | grep private
```
