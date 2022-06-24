# Secrets

https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/

https://howchoo.com/kubernetes/read-kubernetes-secrets

## get secret
```
kubectl get secrets
kubectl get secret <secret-name> -o yaml
kubectl get secret <secret-name> -o jsonpath="{.data.username}" | base64 --decode
kubectl describe secret <secret-name>
```
