# Kubectl
https://kubernetes.io/docs/reference/kubectl/

## show all info
```
kubectl get node -v=7
kubectl get node -v=10
```

## list all resources in a namespace
```
kubectl get all -n <namespace> #not list all

kubectl api-resources --verbs=list --namespaced -o name \
  | xargs -n 1 kubectl get --show-kind --ignore-not-found -n <namespace>
```
