# Cluster

https://learn.microsoft.com/en-us/azure/aks/start-stop-cluster?tabs=azure-cli

## stop cluster
```
az aks show
az aks stop --name <cluster-name> --resource-group <resource-group>
```

## start cluster
```
az aks start --name <cluster-name> --resource-group <resource-group>
```

## restart VMs in scale set in AKS node pool
```
#get the AKS node resource group name
az aks show -g <resource-group> -n <cluster-name> --query nodeResourceGroup

#get the scale set info and all the instance id
az vmss list -g <node-resource-group> --query [].name
az vmss list-instances -g <node-resource-group -n <vmss-name> -o table

#restart the instance with the instance Id
az vmss restart -g <node-resource-group> -n <vmss-name> --instance-ids <id>
```