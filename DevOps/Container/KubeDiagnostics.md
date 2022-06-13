# Kube diagnostics

## check
```
kubectl version
kubectl top nodes
kubectl top pods -A
kubectl get events
kubectl get events -o wide
kubectl get events | grep <this-string>
kubectl describe job <job-name>
```

## logs
```
kubectl logs <pod-name> -n <namespace>
kubectl logs -p -c <container-name> <pod-name> #logs from previous terminated container
kubectl logs -f -c <container-name> <pod-name> #begin streaming logs from container
kubectl logs --tail=20 <pod-name> #display only the most recent 20 lines of logd
kubectl logs --since=1h <pod-name> #display all logs written in the last hour
```

## drain a node
Safely Drain a Node: 
https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/
