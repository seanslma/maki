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

## cordon a node
```
# set node to be unschedulable
kubectl cordon <node-name>
kubectl drain <node-name> --ignore-daemonsets

# clean docker disk or do other things
docker system prune --all

# reset node as schedulable
kubectl uncordon <node-name>
```

## find the mount of of a path
```
findmnt --target /var/lib/docker
```

## error: /var/lib/docker/overlay2/xxx: no such file or directory
This might be caused `docker system prune`. Solution:
```
systemctl stop docker
umount /var/lib/docker/overlay2
rm -rf /var/lib/docker
systemctl start docker
```

## Node stays on `Ready,SchedulingDisabled`
Solution
```
kubectl uncordon <node-name>
```
https://github.com/kubereboot/kured/issues/63
- incompatibility between the version of kubectl in the kured images you're using and AKS???
- when there is only 1 node in AKS, because the pod cannot be re-created after node rebooted
- this happens when the reboot can not occur because a `Pod Disruption Budget` does not allow pods to be killed on the node `kured` is trying to drain
  `error when evicting pods/"user-scheduler-xxxxx-xxx" -n "jhub" (will retry after 5s): Cannot evict pod as it would violate the pod's disruption budget.`
  check the `pdb` settings - some settings are invalid: `kubectl get pdb -A`, `kubectl get pdb -n <namespace> <pdb-name> -o yaml`
- scheduling disabled represents that node got into maintenance mode - due to maintainance???
