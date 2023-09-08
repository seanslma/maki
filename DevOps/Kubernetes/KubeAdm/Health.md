# Health

## check k8s health status
```
kubectl get componentstatuses
```
This command will be the easiest way to discover if your `scheduler`, `controller-manager` and `etcd` node(s) are healthy. 
