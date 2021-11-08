# deploy app

## app deployment
```
#show more details about a deployment
kubectl describe deployment/redis-master #describe <object> <instance-name>
#delete current deployment
kubectl delete deployment/redis-master

#create configmap
kubectl create configmap example-redis-config --from-file=redis-config
#delete configmap
kubectl delete configmap/example-redis-config
#output object to yaml
kubectl get -o yaml configmap/example-redis-config
#open a redis-cli session with the running pod
kubectl exec -it redis-master-<pod-id> -- redis-cli
kubectl exec -it redis-master-<pod-id> -- bash
#create service from yaml
kubectl apply -f redis-master-service.yaml
#check service properties
kubectl get service
#delete deployment and service
kubectl delete deployment frontend redis-master redis-replica
kubectl delete service frontend redis-master redis-replica
```

## deploy complex app using Helm
"When deploying more complicated applications, across multiple environments (such as dev/test/prod), it can become cumbersome to manually edit YAML files for each environment. This is where the Helm tool comes in."

```
#add repo containing stable Helm Charts 
helm repo add bitnami https://charts.bitnami.com/bitnami
#install WordPress
helm install handsonakswp bitnami/wordpress
#delete aks
helm delete aks01
#delete pvcs 
kubectl delete pvc --all
```
