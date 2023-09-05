# Application

https://argo-cd.readthedocs.io/en/stable/operator-manual/application.yaml

Config file for setting the helm chart parameters and other paremeters.

## delete app
https://argo-cd.readthedocs.io/en/stable/user-guide/app_deletion/

cascade deletion
```sh
kubectl patch app APPNAME  -p '{"metadata": {"finalizers": ["resources-finalizer.argocd.argoproj.io"]}}' --type merge
kubectl delete app APPNAME
```

non-cascade deletion
```sh
kubectl patch app APPNAME  -p '{"metadata": {"finalizers": null}}' --type merge
kubectl delete app APPNAME
```
