# Volume blob stoarge

## mount azure blob storage as pv
https://learn.microsoft.com/en-us/azure/aks/azure-csi-blob-storage-provision?tabs=mount-nfs%2Csecret

## blob storage csi driver
enable/disable csi driver on aks
```sh
az aks create --enable-blob-driver -n <cluster-name> -g <resource-group-name> #new aks
az aks update --enable-blob-driver -n <cluster-name> -g <resource-group-name> #existing aks
az aks update --disable-blob-driver -n <cluster-name> -g <resource-group-name> #disable
```
