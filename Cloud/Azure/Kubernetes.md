# Kubernetes

  * an open-source platform used to manage containerized workloads
  * able to provide a DNS name to your container
  * can load balance and distribute network traffic, If there is a high load on containers 
  * can restart containers that fail, replace or kill containers
  * store and manage sensitive information such as passwords, OAuth tokens and ssh keys

## Azure Kubernetes
Fully managed Kubernetes service on Azure; easy to deploy and manage containerized applications; remove the burden of managing the underlying infrastructure for the Kubernetes deployment.

## aks basic
```
#get credentials to access your cluster
az aks get-credentials --resource-group rg01 --name aks01
#verify have access
kubectl get nodes
#launch app
kubectl create -f aks01.yaml
#check deployment progress
kubectl get pods
#using alias
alias k=kubectl
#following pods status
kubectl get pods --watch
##get credentials to access your cluster
az aks get-credentials --resource-group rg01 --name aks01
#verify have access
kubectl get nodes
#launch app
kubectl create -f aks01.yaml
#check deployment progress
kubectl get pods
#using alias
alias k=kubectl
#following pods status
kubectl get pods --watch
#get load balancer public IP
kubectl get service aks01-front --watch
#see all objects in Kubernetes
kubectl get all
#delete ctreated objects
kubectl delete -f aks01.yaml
```

## app deployment

