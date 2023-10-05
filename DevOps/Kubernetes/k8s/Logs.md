# Logs
https://theithollow.com/2020/02/12/kubernetes-logs-for-troubleshooting

## `kubelet` service log
Any components deployed as systemd services can be found in the Linux journal on the host in which the service resides.
This could include etcd logs, kubelet logs, or any of the components running as a service.

The `kubelet` runs on every node in the cluster. Logs can be accessed by using the `journalctl` command on the linux host:
```sh
journalctl -xeu kubelet
journalctl -xeu kubelet -n 100 --no-pager
```

## container log
If using `kubectl` is possible
```sh
kubelctl logs -h
kubectl logs <pod-name>
kubectl logs <pod-name> --tail=20
kubectl logs <pod-name> --since=1h
kubectl logs <pod-name> --timestamps=true
```

Get the logs through container runtime if `kubectl` is not available
```sh
docker logs <container-id>
```

## `kube-sheduler` pod log
- kube-scheduler pod's log: same as using `kubeclt logs`
- kube-scheduler container's log: same as kube-scheduler pod's log.
- `kube-controller-manager`
- `kube-apiserver`
