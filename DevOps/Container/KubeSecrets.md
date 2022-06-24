# Secrets

https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/

https://howchoo.com/kubernetes/read-kubernetes-secrets

## create secret
```
kubectl create secret generic db-user-pass \
  --from-file=./username.txt \
  --from-file=./password.txt
  
kubectl create secret generic db-user-pass \
  --from-file=username=./username.txt \
  --from-file=password=./password.txt
  
kubectl create secret generic db-user-pass \
  --from-literal=username=devuser \
  --from-literal=password='S!B\*d$zDsb='  
```

## edit secret
```
kubectl edit secrets <secret-name>
```

## get secret
```
kubectl get secrets
kubectl get secret <secret-name> -o yaml
kubectl get secret <secret-name> -o jsonpath="{.data.username}" | base64 --decode
kubectl describe secret <secret-name>
```
