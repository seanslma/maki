# Volume blob stoarge

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
