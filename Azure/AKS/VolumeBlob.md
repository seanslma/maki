# Volume blob stoarge

## nfs 3.0
https://learn.microsoft.com/en-us/azure/storage/blobs/network-file-system-protocol-support-how-to

`No such file or directory`: 
- wrong container name or
- the account isn't enabled for NFS 3.0

To mount a container by using NFS 3.0:
- you must create a storage account
- you can't enable existing accounts

Storage account features:
- Hierarchical namespace: enabled
- NFS V3: enabled

## mount azure blob storage as pv
- https://medium.com/@er.singh.nitin/mount-azure-blob-storage-to-aks-pod-358ee55040ac
- https://learn.microsoft.com/en-us/azure/aks/azure-csi-blob-storage-provision?tabs=mount-nfs%2Csecret
- https://learn.microsoft.com/en-us/troubleshoot/azure/azure-kubernetes/storage/mounting-azure-blob-storage-container-fail

## blob storage csi driver
enable/disable csi driver on aks
```sh
az aks create --enable-blob-driver -n <cluster-name> -g <resource-group-name> #new aks
az aks update --enable-blob-driver -n <cluster-name> -g <resource-group-name> #existing aks
az aks update --disable-blob-driver -n <cluster-name> -g <resource-group-name> #disable
```
Once we have enabled the driver, we should see two storage classes created in our cluster:
```
azureblob-nfs-premium
azureblob-fuse-premium
```

List all the CSI drivers available on the worker nodes
```sh
kubectl describe csinodes
```

List storage classes available in aks
```sh
kubectl get storageclass
```

## use managed identity to access blob storage from aks pod
https://www.youtube.com/watch?v=azBHvHKsMhM

https://github.com/HoussemDellai/docker-kubernetes-course/tree/main/47_blob_fuse_msi
- Create `managed identity`
- Assign `rbac role`
- Attach `anaged identity` to AKS VMSS
- Configure `pv` with managed identity
  ```yaml
  csi:
    volumeAttributes:
      AzureStorageAuthType: msi  # key, sas, msi, spn
      AzureStorageIdentityResourceID: $IDENTITY_ID  
  ```

## create persistent volume
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  annotations:
    pv.kubernetes.io/provisioned-by: blob.csi.azure.com
  name: pv-blob
spec:
  storageClassName: azureblob-nfs-premium
  persistentVolumeReclaimPolicy: Retain
  capacity:
    storage: 1Pi
  accessModes:
    - ReadWriteMany  
  mountOptions:
    - nconnect=4
  csi:
    driver: blob.csi.azure.com
    volumeHandle: <storage-account>-<container-name>
    volumeAttributes:
      resourceGroup: <storage-recource-group> # unique id
      storageAccount: <storage-account>
      containerName: <container-name>      
      AzureStorageAuthType: msi  # key, sas, msi, spn
      AzureStorageIdentityResourceID: $IDENTITY_ID  
      protocol: nfs      
---
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-blob
spec:
  volumeName: pv-blob
  storageClassName: azureblob-nfs-premium 
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 10Gi 
```

## create app pod
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-blob
  namespace: retail
  labels:
    aadpodidbinding: managed-identity-name  
spec:
  nodeSelector:
    "kubernetes.io/os": linux
  containers:
    - name: nginx-blob
      image: mcr.microsoft.com/oss/nginx/nginx:1.17.3-alpine
      command:
        - "/bin/bash"
        - "-c"
        - |
          while true; do sleep 3600; done      
      volumeMounts:
        - name: blob-storage
          mountPath: /home/user/data
          readOnly: false
  volumes:
    - name: blob-storage
      persistentVolumeClaim:
        claimName: pvc-blob
```
