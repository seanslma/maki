# Deployment

## get pod associated with a deployment
```sh
kubectl get pods --show-labels
# single label
kubectl get pods -l=app=http-svc
kubectl get pods --selector=app=http-svc
# multiple labels
kubectl get pods --selector key1=value1,key2=value2
```

## Change Replicas
```sh
kubectl scale --replicas=3 deployment/demo-deployment
```
