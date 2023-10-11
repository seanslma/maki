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
