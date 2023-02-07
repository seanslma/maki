# Logs
https://theithollow.com/2020/02/12/kubernetes-logs-for-troubleshooting

## service log
Any components deployed as systemd services can be found in the Linux journal on the host in which the service resides.
This could include etcd logs, kubelet logs, or any of the components running as a service.

The `kubelet` runs on every node in the cluster. Logs can be accessed by using the journalctl commands on the linux host:
```
journalctl -xeu kubelet
journalctl -xeu kubelet -n 100 --no-pager
```

## container log
If using `kubectl` is possible
```
kubectl logs <pod-name>
```

Get the logs through container runtime if kubectl is not available
```
docker logs <container-id>
```

## pod log
kube-sheduler log might be in `/var/log/kube-scheduler.log`
- kube-scheduler pod's log: same as using `kubeclt logs`
- kube-scheduler container's log: same as kube-scheduler pod's log.
