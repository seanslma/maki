# Disk

https://techcommunity.microsoft.com/blog/fasttrackforazureblog/everything-you-want-to-know-about-ephemeral-os-disks-and-azure-kubernetes-servic/3565605

## Ephemeral OS disks 
- created on the local virtual machine (VM) storage and not saved to the remote Azure Storage, as when using managed OS disks
- work well for stateless workloads
- lower read/write latency to the OS disk and faster VM reimage

## Managed OS disks
- can set disk size
- data will be saved to the remote Azure Storage
- no data loss
- slower

## check pod disk usage
how to check disk usage:
- https://neilcameronwhite.medium.com/under-disk-pressure-34b5ba4284b6
- run into pod and execute `du -sh`
- disks and usage: `df -h /var/lib/docker`
- usage of each folder: `du -sh /var/lib/docker/* | sort -h`
- files that are open: `lsof /var/lib/docker/ | grep deleted | head`
- can use shell to get disk usage for all pods
  
## increase node disk size
- Managed disk is slower and has a cost but can specify the size.
- Ephemeral disk size should not be larger than the `temp`/`cache` size of the vm_size
- Default ephemeral disk size is set to 128GB: https://cloudchronicles.blog/blog/AKS-Best-Practices-Part2-Cost-Efficiency
```tf
os_disk_type    = "Ephemeral"  # {Ephemeral|Managed}
os_disk_size_gb = 256          # default 128 GB
```

The node pool must be recreated: https://github.com/Azure/AKS/issues/610?WT.mc_id=AZ-MVP-5005118

solution:
- create a temporal node pool - manully if tf does not support
- cordon the nodes in that node pool: `kubectl cordon aks-agentpool-xxxx-1`
- delete some pods that should be moved to the new node pool first: `kubectl delete po xyz -n namespace`
- drain all other pods in the nodes: `kubectl drain aks-agentpool-xxxx-1 --ignore-daemonsets --delete-local-data`
- change the disk size, and `kubectl uncordon aks-agentpool-xxx-1`
- drain the nodes in the temporal node pool, and delete the temporal node pool

## FreeDiskSpaceFailed
run `kubectl describe node <node-name>` the output will be
```
Events:
  Type     Reason                Age                     Message
  ----     ------                ----                    -------
  Warning  FreeDiskSpaceFailed   20m (x2195 over 8d)     Failed to garbage collect required amount of images.
                                                         Attempted to free 5852591718 bytes, but only found 1164052028 bytes eligible to free.
  Warning  FreeDiskSpaceFailed   10m                     Failed to garbage collect required amount of images.
                                                         Attempted to free 11461842534 bytes, but only found 0 bytes eligible to free.
  Warning  EvictionThresholdMet  9m28s (x20 over 7d17h)  Attempting to reclaim ephemeral-storage
  Warning  FreeDiskSpaceFailed   5m54s                   Failed to garbage collect required amount of images.
                                                         Attempted to free 7382013542 bytes, but only found 1000999069 bytes eligible to free.
  Warning  FreeDiskSpaceFailed   54s                     Failed to garbage collect required amount of images.
                                                         Attempted to free 7399114342 bytes, but only found 0 bytes eligible to free.
```

Possible solutions:
- find which pod used most disk space
- limit resource usage
  ```yaml
  resources:
  requests:
      ephemeral-storage: "1Gi"
  limits:
      ephemeral-storage: "2Gi"
  ```
- adjust Kubernetes eviction and garbage collection settings
  ```yaml
  evictionHard:
  "nodefs.available": "10%"
  "imagefs.available": "15%"
  ```
- enable image garbage collection
  ```yaml
  --image-gc-high-threshold=85
  --image-gc-low-threshold=80
  ```
