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

## delete pv/pvc
```
PersistentVolumeClaim   is invalid: spec: Forbidden:
spec is immutable after creation except resources.requests for bound
```
https://stackoverflow.com/questions/60175522/kubernetes-persistentvolumeclaim-error-forbidden-is-immutable-after-creation

solution: comment out
```yaml
finalizers:
  - kubernetes.io/pv-protection
```

## pvc volume already bound to a different claim
https://vmninja.wordpress.com/2021/08/10/kubernetes-volume-x-already-bound-to-a-different-claim/

solution: edit `resourceVersion` and `uid` in `pv` section `claimRef` using the value in `pvc`.


