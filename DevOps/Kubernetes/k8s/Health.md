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
