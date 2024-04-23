# Volume files storage

## mount azure file storage as pv
- https://learn.microsoft.com/en-us/azure/aks/azure-csi-files-storage-provision
- https://github.com/HoussemDellai/aks-file-share

### pv and pvc
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-azurefile
spec:
  capacity:
    storage: 5Gi
  accessModes:
    - ReadWriteMany
  azureFile:
    secretName: azure-secret
    SecretNamespace: <namespace>
    shareName: <share-name (must already exist in the storage account)>
    readOnly: false
  mountOptions:
    - dir_mode=0777
    - file_mode=0777
    - uid=1000
    - gid=1000
    - mfsymlinks
    - nobrl
  persistentVolumeReclaimPolicy: Retain  
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-azurefile
  namespace: <namespace>
spec:
  accessModes:
    - ReadWriteMany  
  resources:
    requests:
      storage: 5Gi  
  storageClassName: azurefile
```

### create a secret in aks
```sh
kubectl create secret generic <secret-name> --from-literal=azurestorageaccountname=filestoragename --from-literal=azurestorageaccountkey=filestoragekey
```

### test pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mypod
spec:
  containers:
  - image: mcr.microsoft.com/oss/nginx/nginx:1.15.5-alpine
    name: my-pod-name
    resources:
      requests:
        cpu: 100m
        memory: 128Mi
      limits:
        cpu: 250m
        memory: 256Mi
    volumeMounts:
      - name: azure
        mountPath: /home/user/azure
  volumes:
  - name: azure
    persistentVolumeClaim:
      claimName: pvc-azurefile
```

## custom storage class
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: my-azurefile
provisioner: file.csi.azure.com
reclaimPolicy: Delete
volumeBindingMode: Immediate
allowVolumeExpansion: true
mountOptions:
  - dir_mode=0640  # default 0777
  - file_mode=0640 # default 0777
  - uid=0
  - gid=0
  - mfsymlinks
  - cache=strict # https://linux.die.net/man/8/mount.cifs
  - nosharesock
parameters:
  skuName: Standard_LRS
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-azurefile
spec:
  accessModes:
    - ReadWriteMany
  storageClassName: my-azurefile
  resources:
    requests:
      storage: 100Gi
```

## private Azure Files storage (private endpoint)
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: private-azurefile-csi
provisioner: file.csi.azure.com
allowVolumeExpansion: true
parameters:
  resourceGroup: <resourceGroup>
  storageAccount: <storageAccountName>
  server: <storageAccountName>.file.core.windows.net 
reclaimPolicy: Delete
volumeBindingMode: Immediate
mountOptions:
  - dir_mode=0777
  - file_mode=0777
  - uid=0
  - gid=0
  - mfsymlinks
  - cache=strict  # https://linux.die.net/man/8/mount.cifs
  - nosharesock  # reduce probability of reconnect race
  - actimeo=30  # reduce latency for metadata-heavy workload
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: private-azurefile-pvc
spec:
  accessModes:
    - ReadWriteMany
  storageClassName: private-azurefile-csi
  resources:
    requests:
      storage: 100Gi
```

## NFS file shares
```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: azurefile-csi-nfs
provisioner: file.csi.azure.com
allowVolumeExpansion: true
parameters:
  protocol: nfs
mountOptions:
  - nconnect=4
  - rsize=262144
  - wsize=262144
```

## issue
mount a file storage:
- https://stackoverflow.com/questions/74825923/aks-kubernetes-pod-volume-mounting-failing-even-after-pv-is-bound-and-attached
- https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/storage/fail-to-mount-azure-file-share
