# Kube diagnostics
https://thenewstack.io/living-with-kubernetes-12-commands-to-debug-your-workloads/

## check
```
kubectl version
kubectl get cm #ConfigMaps
kubectl get nodes --no-headers | wc -l #cluster node count
kubectl top nodes
kubectl top pods -A
kubectl get events
kubectl get events -o wide
kubectl get events | grep <this-string>
kubectl get jobs/<job-name>
kubectl describe job <job-name>
kubectl describe jobs/<job-name> -n <namespace>
```

## drain a node
Safely Drain a Node: 
https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/

## pending pods
https://www.datadoghq.com/blog/debug-kubernetes-pending-pods/

