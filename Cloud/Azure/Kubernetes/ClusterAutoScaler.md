# Cluster Autoscaler

https://www.danielstechblog.io/azure-kubernetes-service-cluster-autoscaler-configurations/

Pod not deleted preventing scaling down on all nodes:
https://github.com/kubernetes/autoscaler/issues/248
Fix: After many month of period debugging found the issue to be signal handling. Installed https://github.com/Yelp/dumb-init in all the pods and the issue as cleared. I am closing this.

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
