# Cluster Autoscaler

https://docs.microsoft.com/en-us/azure/aks/scale-cluster?tabs=azure-cli

https://www.danielstechblog.io/azure-kubernetes-service-cluster-autoscaler-configurations/

https://betterprogramming.pub/build-kubernetes-autoscaling-for-cluster-nodes-and-application-pods-bb7f2d716b07

Pod not deleted preventing scaling down on all nodes:
https://github.com/kubernetes/autoscaler/issues/248
Fix: After many month of period debugging found the issue to be signal handling. Installed https://github.com/Yelp/dumb-init in all the pods and the issue as cleared. I am closing this.

## cannot control which node to delete
- nodes are being removed starting from the highest IDs
- You cannot control which node will be removed when scaling down the AKS cluster - the cordoned node will not be selected.

**Workaround**: first manually scale the nodes to zero then scale back.

## Cluster autoscaler settings
https://github.com/Azure/AKS/issues/2766

https://docs.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-overview

Cannot scale down to zero? seems fixed - test it

## Autoscale pods
https://docs.microsoft.com/en-us/azure/aks/tutorial-kubernetes-scale?tabs=azure-cli#autoscale-pods

manually scale pods:
```
kubectl scale --replicas=5 deployment/<deployment-name>
```

Kubernetes supports horizontal pod autoscaling (HPA) to adjust the number of pods in a deployment depending on CPU utilization or other select metrics. 

To use the autoscaler, all containers in your pods and your pods must have CPU requests and limits defined. 

If average CPU utilization across all pods exceeds 50% of their requested usage, the autoscaler increases the pods up to a maximum of 10 instances.
```
Kubectl autoscale deployment <container-app-name> --cpu-percent=50 --min=3 --max=10
```
```
apiVersion: autoscaling/v1
kind: HorizontalPodAutoscaler
metadata:
  name: <container-app-name>-hpa
spec:  
  minReplicas: 3  # define min replica count
  maxReplicas: 10 # define max replica count
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: <container-app-name>
  targetCPUUtilizationPercentage: 50 # target CPU utilization
```
## Manually scale down nodes
https://docs.microsoft.com/en-us/azure/aks/scale-cluster?tabs=azure-cli
```
#show nodepool profiles
az aks show --resource-group <resource-group> \
    --name <cluster-name> --query agentPoolProfiles
    
#scale nodepool    
az aks scale --resource-group <resource-group> \
    --name <cluster-name> --node-count 1 --nodepool-name <nodepool-name>
    
#can scale user nodepool to zero node
az aks nodepool scale --resource-group <resource-group> \
    --cluster-name <cluster-name> --name <nodepool-name> \
    --node-count 0 

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

## Metrics
https://docs.microsoft.com/en-us/azure/azure-monitor/autoscale/autoscale-common-metrics

### scale-down-utilization-threshold
https://docs.microsoft.com/en-us/azure/aks/cluster-autoscaler#set-the-cluster-autoscaler-profile-on-an-existing-aks-cluster
```
az aks update \
  --resource-group myResourceGroup \
  --name myAKSCluster \
  --cluster-autoscaler-profile scale-down-utilization-threshold=<percentage value>
```

## Prevent autoscaler deleting node which runs a specific pod
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
