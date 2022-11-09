# Node Pool

https://learn.microsoft.com/en-us/azure/aks/use-multiple-node-pools

## abort operation on node pool 
```
az aks nodepool operation-abort --name <node-pool> \
  --cluster-name <cluster-name> --resource-group <resource-group> 
```

## abort operation on managed cluster
```
az aks operation-abort --name <cluster-name> --resource-group <resource-group>
```
