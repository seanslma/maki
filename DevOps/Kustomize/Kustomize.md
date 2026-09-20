# Kustomize

- Helm excels in managing complex applications with multiple configurations, while
- Kustomize is a solid choice for fine-tuning and `patching` existing manifests

## render a kustomize folder
install `kubernetes-helm` via conda. avoid helm version 4.x if kustomize version is low.
```sh
kubectl kustomize --enable-helm argocd/kustomize/sales/overlays/dev
```

