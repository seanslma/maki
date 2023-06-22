# Namespace

```tf
resource "kubernetes_namespace" "main" {
  metadata {
    name        = var.namespace
    labels      = {}
    annotations = {}
  }
}
```
