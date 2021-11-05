# Kubernetes

  * an open-source platform used to manage containerized workloads
  * able to provide a DNS name to your container
  * can load balance and distribute network traffic, If there is a high load on containers 
  * can restart containers that fail, replace or kill containers
  * store and manage sensitive information such as passwords, OAuth tokens and ssh keys

## Azure Kubernetes
Fully managed Kubernetes service on Azure; easy to deploy and manage containerized applications; remove the burden of managing the underlying infrastructure for the Kubernetes deployment.

## Access cluster
```
#get credentials to access your cluster
az aks get-credentials --resource-group rg01 --name aks01
#verify have access
kubectl get nodes
```

