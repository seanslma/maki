# Memory
https://stackoverflow.com/questions/68888889/does-kubernetes-pods-provide-memory-back-after-acquiring-more-than-the-requeste

Kubernetes resource requests come into effect at basically three times:
- When new pods are being initially scheduled, the resource requests (only) are used to find a node with enough space. The sum of requests must be less than the physical size of the node. Limits and actual utilization aren't considered.
- If the process allocates memory, and this would bring its total utilization above the pod's limit, the allocation will fail.
- If the node runs out of memory, Kubernetes will look through the pods on that node and evict the pods whose actual usage most exceeds their requests.
