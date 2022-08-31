# Memory
https://stackoverflow.com/questions/68888889/does-kubernetes-pods-provide-memory-back-after-acquiring-more-than-the-requeste

Kubernetes resource requests come into effect at basically three times:
- When new pods are being initially scheduled, the resource requests (only) are used to find a node with enough space. The sum of requests must be less than the physical size of the node. Limits and actual utilization aren't considered.
- If the process allocates memory, and this would bring its total utilization above the pod's limit, the allocation will fail.
- If the node runs out of memory, Kubernetes will look through the pods on that node and evict the pods whose actual usage most exceeds their requests.

## Node reserved memory
Memory - reserved memory includes the sum of two values.

The kubelet daemon is installed on all Kubernetes agent nodes to manage container creation and termination. 
By default on AKS, this daemon has the following eviction rule: 
- memory.available < 750Mi, which means a node must always have at least 750 Mi allocatable at all times. 
- When a host is below that threshold of available memory, the kubelet will terminate one of the running pods to free memory on the host machine and protect it.

The second value is a progressive rate of memory reserved for the kubelet daemon to properly function (kube-reserved).
```
- 25% of  0-  4 GB (  4 GB)
- 20% of  4-  8 GB (  4 GB)
- 10% of  8- 16 GB (  8 GB)
- 06% of 16-128 GB (112 GB)
- 02% of   >128 GB
```
