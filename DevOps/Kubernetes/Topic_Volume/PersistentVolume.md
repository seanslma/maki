# persistent-volume

https://kubernetes.io/docs/tasks/configure-pod-container/configure-persistent-volume-storage/

- use `PersistentVolume` to create a persistent-volume
- use `PersistentVolumeClaim` to request physical storage for pods

## types
https://kubernetes.io/docs/concepts/storage/persistent-volumes/
- csi
- nfs
- local
- azureFile (replaced by azureFile CSI migration)

## mount azure files storage as pv
https://learn.microsoft.com/en-us/azure/aks/azure-csi-files-storage-provision

## mount azure blob storage as pv
https://learn.microsoft.com/en-us/azure/aks/azure-csi-blob-storage-provision?tabs=mount-nfs%2Csecret
