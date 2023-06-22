# Secret

```tf
# https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/secret
resource "kubernetes_secret" "main" {
  depends_on = [kubernetes_namespace.main]
  metadata {
    name        = var.name
    namespace   = var.namespace
    labels      = {}
    annotations = {}    
  }
  data = {
    "mysql.username" = file("//example.com/share/mysql.username.txt")
    "mysql.password" = file("//example.com/share/mysql.password.txt")
  }
}
```
