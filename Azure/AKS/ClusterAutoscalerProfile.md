# Cluster Autoscaler profile

All the parameters used in the cluaster-autoscaler:

https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler#using-the-autoscaler-profile

## Reset cluster autoscaler profile to default values
```
az aks update \
  --resource-group <resource-group-name> \
  --name <cluster-name> \
  --cluster-autoscaler-profile ""
```

## Set the cluster autoscaler profile on an existing AKS cluster
```
az aks update \
  --resource-group <resource-group-name> \
  --name <cluster-name> \
  --cluster-autoscaler-profile scan-interval=30s
# scale-down-utilization-threshold=0.5
```
