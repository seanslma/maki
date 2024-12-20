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

## increase node disk size
```tf
os_disk_type    = "Ephemeral"  # {Ephemeral|Managed}
os_disk_size_gb = 256          # default 128 GB
```
