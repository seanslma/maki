# Persistent Volume

## Link Azure File Storage `File Shares` to a PersistentVolume (PV) in Kubernetes without using a StorageClass
create a secret a terraform including the `storage account name` and `storage account key`
```tf
# https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/secret
resource "kubernetes_secret" "dev_storage" {
  depends_on = [kubernetes_namespace.main]
  metadata {
    name        = "dev-storage"
    labels      = {}
    annotations = {}
    namespace   = var.namespace
  }
  data = {
    "azurestorageaccountname" = var.dev_storage_account.name
    "azurestorageaccountkey"  = var.dev_storage_account.key
  }
}
```

create a PersistentVolume. The share name is the `File Shares` name of the storage account
```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: azure-pv
spec:
  capacity:
    storage: 5Gi
  volumeMode: Filesystem
  accessModes:
    - ReadWriteMany
  azureFile:
    secretName: azure-secret
    secretNamespace: dev
    shareName: myshare
    readOnly: false
  mountOptions:
    - dir_mode=0777
    - file_mode=0777
    - uid=1000
    - gid=1000
    - mfsymlinks
    - nobrl
```

create a PersistentVolumeClaim
```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: azure-pvc
  namespace: dev
spec:
  accessModes:
    - ReadWriteMany
  resources:
    requests:
      storage: 2Gi
  volumeName: azure-pv
```
