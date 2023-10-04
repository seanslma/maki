# Health

## check pods not running / completed
```sh
kubectl get po -A -o wide | egrep -v 'Running|Completed'
```

## check containers of running pods are ready
```sh
kubectl get po -A -o wide | egrep 'Running'
```

## check status of nodes
```sh
kubectl get nodes
```

## check storage health
```sh
kubectl -n <namespace> get pvc
```

## check kubelet
```sh
systemctl status kubelet
```

## clusterrole
```sh
kubectl describe clusterrole system:kube-scheduler
```

## check k8s health status
```sh
kubectl get componentstatuses
```
This command will be the easiest way to discover if your `scheduler`, `controller-manager` and `etcd` node(s) are healthy.
```
Warning: v1 ComponentStatus is deprecated in v1.19+
NAME               STATUS    MESSAGE      ERROR
scheduler          Unhealthy Get "https://127.0.0.1:10259/healthz":
                                dial tcp 127.0.0.1:10259: connect: connection refused
controller-manager Unhealthy Get "https://127.0.0.1:10257/healthz":
                                dial tcp 127.0.0.1:10257: connect: connection refused
etcd-0             Healthy   {"health":"true"}
```

Solution
- check component logs
```sh
kubectl logs -n kube-system <scheduler-pod-name>
kubectl logs -n kube-system <controller-manager-pod-name>
```
- Check Service Status: ensure the services are running and have valid ip
```sh
kubectl get svc -n kube-system
```
- Check Component Health Probes: A healthy component should return an HTTP 200 OK response.
```sh
curl http://<scheduler-ip>:10251/healthz
curl http://<controller-manager-ip>:10252/healthz
```
