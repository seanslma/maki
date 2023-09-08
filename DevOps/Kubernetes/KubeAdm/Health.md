# Health

## check k8s health status
```
kubectl get componentstatuses
```
This command will be the easiest way to discover if your `scheduler`, `controller-manager` and `etcd` node(s) are healthy. 
```
Warning: v1 ComponentStatus is deprecated in v1.19+
NAME                 STATUS      MESSAGE                                                                                        ERROR
scheduler            Unhealthy   Get "https://127.0.0.1:10259/healthz": dial tcp 127.0.0.1:10259: connect: connection refused
controller-manager   Unhealthy   Get "https://127.0.0.1:10257/healthz": dial tcp 127.0.0.1:10257: connect: connection refused
etcd-0               Healthy     {"health":"true"}
```
