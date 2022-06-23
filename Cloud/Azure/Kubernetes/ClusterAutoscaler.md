# Cluster Autoscaler

https://docs.microsoft.com/en-us/azure/aks/scale-cluster?tabs=azure-cli

https://www.danielstechblog.io/azure-kubernetes-service-cluster-autoscaler-configurations/

https://betterprogramming.pub/build-kubernetes-autoscaling-for-cluster-nodes-and-application-pods-bb7f2d716b07

Pod not deleted preventing scaling down on all nodes:
https://github.com/kubernetes/autoscaler/issues/248
Fix: After many month of period debugging found the issue to be signal handling. Installed https://github.com/Yelp/dumb-init in all the pods and the issue as cleared. I am closing this.

## cluster autoscaler settings:
https://github.com/Azure/AKS/issues/2766

## manually scale down nodes
https://docs.microsoft.com/en-us/azure/aks/scale-cluster?tabs=azure-cli
```
az aks show --resource-group <resource-group> \
    --name <cluster-name> --query agentPoolProfiles
az aks scale --resource-group <resource-group> \
    --name <cluster-name> --node-count 1 --nodepool-name <nodepool-name>

#disable ca
az aks nodepool update --resource-group <resource-group> \
    --cluster-name <cluster-name> --name <nodepool-name> \
    --disable-cluster-autoscaler

#enable ca
az aks nodepool update --resource-group <resource-group> \
    --cluster-name <cluster-name> --name <nodepool-name> \
    --enable-cluster-autoscaler --min-count 0 --max-count 4
  
#change node pool count
az aks update --resource-group <resource-group> \
    --cluster-name <cluster-name> --name <nodepool-name> \
    --update-cluster-autoscaler --min-count 0 --max-count 4
```

## prevent autoscaler deleting node which runs a specific pod
https://faun.pub/how-to-make-sure-kubernetes-autoscaler-not-deleting-the-nodes-which-run-a-specific-pod-8df3f2c28c46

### Solution 1:
Can add the annotation to the critical pods or deployments:
```
"cluster-autoscaler.kubernetes.io/safe-to-evict": "false"
```

Update a running deployment with the below command:
```
kubectl annotate deployment.apps/efs-provisioner cluster-autoscaler.kubernetes.io/safe-to-evict": "false"
```

### Solution 2:
Autoscaler provides an option to exclude nodes from the scale-down process.
This annotation is applied to a specific node so make sure the critical pods running on this Kubernetes node.
```
"cluster-autoscaler.kubernetes.io/scale-down-disabled": "true"
```

### Solutions 3:
If a pod is using local storage AutoScaler will skip that node from deletion. 
So mounting local storage to a pod also can use as a trick to protect the nodes which run our critical pods.
