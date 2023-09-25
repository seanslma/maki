# Logs

## describe node
```
k describe node <node-name>
```

## logs
```
kubectl logs <pod-name> -n <namespace>
kubectl logs -p -c <container-name> <pod-name> #logs from previous terminated container
kubectl logs -f -c <container-name> <pod-name> #begin streaming logs from container
kubectl logs --tail=20 <pod-name> #display only the most recent 20 lines of logd
kubectl logs --since=1h <pod-name> #display all logs written in the last hour, 5 minutes (5m)
```

## how long to keep pod logs
https://unofficial-kubernetes.readthedocs.io/en/latest/concepts/cluster-administration/logging/
- output to stdout and stderr is handled and redirected to a file in json format, on node's SSD
- kubernetes performs log rotation daily (up to 5) per container, or if the log file grows beyond 10MB in size
- if a container restarts, keeps one terminated container with its logs
- if a pod is evicted, all corresponding containers are also evicted, along with their logs

