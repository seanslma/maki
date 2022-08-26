# Secrets

https://kubernetes.io/docs/tasks/configmap-secret/managing-secret-using-kubectl/

https://howchoo.com/kubernetes/read-kubernetes-secrets

## get secret
```
kubectl get secrets
kubectl get secret <secret-name> -n <namespace> -o yaml
kubectl get secret <secret-name> -o jsonpath="{.data.username}" | base64 --decode
kubectl get secret <secret-name> -o jsonpath="{.data.user\.name}" | base64 --decode
kubectl get secret <secret-name> -o jsonpath="{.data['user\.name']}" | base64 --decode
kubectl describe secret <secret-name>
```

## delete secret
```
kubectl delete secret <secret-name>
```

## create secret
```
kubectl create secret generic <secret-name> \
  --from-file=./username.txt \
  --from-file=./password.txt
  
kubectl create secret generic <secret-name> \
  --from-file=username=./username.txt \
  --from-file=password=./password.txt
  
kubectl create secret generic <secret-name> \
  --namespace=default
  --from-literal=username=devusr \
  --from-literal=password='S!X\*d$zAsb=' 
  
kubectl create secret <secret-name> \
  --key /etc/certs/{name}.com.key \
  --cert /etc/certs/{name}.com.crt \
  -n <namespace>  
```

## edit secret
```
kubectl edit secrets <secret-name>

dk=$(base64 < "./a.key" | tr -d '\n')
dv=$(base64 < "./a.crt" | tr -d '\n')

kubectl get secrets <secret-name> -n <namespace> -o json \
    | jq ".data[\"a.key\"] |= \"$dk\"" \
    | jq ".data[\"a.crt\"] |= \"$dv\"" \
    | kubectl apply -f -
        
kubectl patch secret <secret-name> -n <namespace> \
    -p "{\"data\":{\"a.key\":\"${dk}\",\"a.crt\":\"${dv}\"}}"        
```
