# Manifest

## set value of variables in helm chart values.yaml from manifest
values.yaml
```yaml
myVar:
  name: "var-name"
  id: ""
myVar2: ""
```

manifest.tf
```tf
# https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/manifest
resource "kubernetes_manifest" "my-app" {
  depends_on = [kubernetes_manifest.argo_project]
  # https://argoproj.github.io/argo-cd/operator-manual/application.yaml
  manifest = {
    "apiVersion" = "argoproj.io/v1alpha1"
    "kind" = "Application"
    "metadata" = {
      "name" = "my-app"
      "namespace" = "argocd"
    }
    "spec" = {
      "destination" = {
        "name" = "in-cluster"
        "namespace" = var.namespace
      }
      "project" = var.namespace
      "source" = {
        "helm" = {
          "parameters" = [
            {
              name = "myVar.name"
              value = module.my-app.name
            },
            {
              name = "myVar.id"
              value = module.my-app.id
            },
            {
              name = "myVar2"
              value = var.var2.name
            },
          ]
          "valueFiles" = [
            "values.yaml",
          ]
        }
        "path" = "helm/dev/my-app"
        "repoURL" = var.argocd_repo_url
        "targetRevision" = "HEAD"
      }
      "syncPolicy" = {
        "automated" = {
          "prune" = true
          "selfHeal" = true
        }
        "syncOptions" = [
          "PruneLast=true",
          "CreateNamespace=true",
        ]
      }
    }
  }
}
```
