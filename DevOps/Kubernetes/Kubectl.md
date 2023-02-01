# Kubectl
https://kubernetes.io/docs/reference/kubectl/

## list all resources in a namespace
```
kubectl get all -n <namespace> #not list all

kubectl api-resources --verbs=list --namespaced -o name \
  | xargs -n 1 kubectl get --show-kind --ignore-not-found -n <namespace>
```
