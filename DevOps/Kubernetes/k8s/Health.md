# Health

## check pods not running / completed
```
kubectl get po -A -o wide | egrep -v 'Running|Completed'
```

## check containers of running pods are ready
```
kubectl get po -A -o wide | egrep 'Running'
```

## check status of nodes
```
kubectl get nodes
```

## check storage health
```
kubectl -n <namespace> get pvc
```

## check kubelet 
```
systemctl status kubelet
```
