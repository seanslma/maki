# Logs
https://theithollow.com/2020/02/12/kubernetes-logs-for-troubleshooting/#:~:text=Remember%20that%20any%20logs%20for,the%20container%20runtime%20logs%20commands.

## service logs
Any components deployed as systemd services can be found in the Linux journal on the host in which the service resides. 
This could include etcd logs, kubelet logs, or any of the components running as a service.

The kubelet runs on every node in the cluster. Logs can be accessed by using the journalctl commands on the linux host:
```
journalctl -xeu kubelet
```

## container logs
Using `kubectl` is possible
```
kubectl logs <pod-name>
```

Get the logs through container runtime if kubectl is not available
```
docker logs <container-id>
```
