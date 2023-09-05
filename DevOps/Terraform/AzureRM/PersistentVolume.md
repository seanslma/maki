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

create a PersistentVolume
```yaml
```

create a PersistentVolumeClaim
```yaml
```
