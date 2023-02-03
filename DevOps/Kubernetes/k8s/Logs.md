# Logs
https://theithollow.com/2020/02/12/kubernetes-logs-for-troubleshooting

## service logs
Any components deployed as systemd services can be found in the Linux journal on the host in which the service resides.
This could include etcd logs, kubelet logs, or any of the components running as a service.

The kubelet runs on every node in the cluster. Logs can be accessed by using the journalctl commands on the linux host:
```
journalctl -xeu kubelet
journalctl -xeu kubelet | tail
journalctl -xeu kubelet | less #will not truncate lines
```

## container logs
If using `kubectl` is possible
```
kubectl logs <pod-name>
```

Get the logs through container runtime if kubectl is not available
```
docker logs <container-id>
```
