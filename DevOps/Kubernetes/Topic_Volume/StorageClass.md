# StorageClass
https://kubernetes.io/docs/concepts/storage/storage-classes/

## default storageclass
When a PVC does not specify a storageClassName, the default StorageClass is used.

## set default storageclass
https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/

Mark a StorageClass as default:
```sh
kubectl patch storageclass <class-name> -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"true"}}}'
```

Mark a StorageClass as non-default:
```sh
kubectl patch storageclass <class-name> -p '{"metadata": {"annotations":{"storageclass.kubernetes.io/is-default-class":"false"}}}'
```
