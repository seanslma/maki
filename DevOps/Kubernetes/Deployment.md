# Deployment

## get pod associated with a deployment
```
kubectl get pods --show-labels
kubectl get pods --selector=app=http-svc
```

## Change Replicas
```
kubectl scale --replicas=3 deployment/demo-deployment
```
