# Node

## manually delete a node
scaling up nodes first to make sure the cluster has enough nodes to accomodate the workloads
```
kubectl get nodes
kubectl cordon <node-name>   #mark a node unschedulable
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data  #safely evict all pods from a node before perform maintenance on the node
kubectl delete <node-name>   #delete the node after all pods are evicted from the node
```
