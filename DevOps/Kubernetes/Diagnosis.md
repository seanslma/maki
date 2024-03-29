# Kube diagnosis
https://thenewstack.io/living-with-kubernetes-12-commands-to-debug-your-workloads/

https://kubernetes.io/docs/tasks/debug/debug-cluster/

https://kubernetes.io/docs/tasks/debug/debug-application/determine-reason-pod-failure/

## run every 2 seconds
```sh
watch -n 2 kubectl top node
```

## check
```sh
kubectl version
kubectl get cm #ConfigMaps
kubectl get nodes --no-headers | wc -l #cluster node count
kubectl top nodes
kubectl top pods -A
kubectl get events
kubectl get events -o wide
kubectl get events | grep <this-string>
kubectl get events -A --sort-by='.lastTimestamp' | sed -r 's/ {2,}/,/g' > /mnt/c/tmp/aks_events.csv #fixed col to csv
kubectl get jobs/<job-name>
kubectl describe job <job-name>
kubectl describe jobs/<job-name> -n <namespace>
```

Excel `7s`, `8m` or `5m8s` to seconds
```vb
=IFERROR(LEFT(B2,FIND("m",B2)-1)*60 + IF(LEN(RIGHT(B2,LEN(B2)-FIND("m",B2)))=0, 0, LEFT(RIGHT(B2,LEN(B2)-FIND("m",B2)), LEN(RIGHT(B2,LEN(B2)-FIND("m",B2)))-1)), LEFT(B2,FIND("s",B2)-1))
```

## get node events
```sh
kubectl get events --field-selector involvedObject.kind=Node,involvedObject.name=<node-name> --sort-by=.metadata.creationTimestamp
```

## drain a node
Safely Drain a Node:
https://kubernetes.io/docs/tasks/administer-cluster/safely-drain-node/

## ssh to a node
https://docs.microsoft.com/en-us/azure/aks/node-access

## pending pods
https://www.datadoghq.com/blog/debug-kubernetes-pending-pods/
```sh
kubectl get pods --all-namespaces=true --field-selector=status.phase=Pending
kubectl delete pods -A  --field-selector='status.phase=Failed' #delete failed pods
```
