# Node

## show node agentpool
Every node pool has a label `agentpool`. Get the node agentpool label
```
kubectl get nodes -L agentpool
```
`agentpool` is a label on the nodepool. Can view them using `kubectl get nodes --show-labels`.
```
spec:
  containers:
  - name: <container-name>
    image: <image-name>
  nodeSelector:
    agentpool: <pool-name>
```

## manually delete a node
scaling up nodes first to make sure the cluster has enough nodes to accomodate the workloads
```
kubectl get nodes
kubectl cordon <node-name>   #mark a node unschedulable
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data  #safely evict all pods from a node before perform maintenance on the node
kubectl delete <node-name>   #delete the node after all pods are evicted from the node
```
