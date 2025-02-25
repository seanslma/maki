# AKS

- Fully managed Kubernetes service on Azure;
- easy to deploy and manage containerized applications;
- remove the burden of managing the underlying infrastructure for the Kubernetes deployment.

## Kubernetes
  * an open-source platform used to manage containerized workloads
  * able to provide a DNS name to your container
  * can load balance and distribute network traffic, If there is a high load on containers
  * can restart containers that fail, replace or kill containers
  * store and manage sensitive information such as passwords, OAuth tokens and ssh keys

## AKS credentials
```sh
az aks list -o table
az aks get-credentials --resource-group rg01 --name aks01
```

## AKS available versions
```
az aks get-versions -l australiaeast -o table
```

## kubectl basic
```sh
alias k=kubectl                      #using alias
kubectl get nodes                    #verify have access
kubectl create -f aks01.yaml         #launch app
kubectl get pods                     #check deployment progress
kubectl get pods --watch             #following pods status
kubectl get service aks01-front --watch #get load balancer public IP
kubectl get all                      #see all objects in Kubernetes
kubectl delete -f aks01.yaml         #delete created objects
```

## upgrade
```sh
az aks get-upgrades -n <cluster-name> -g <resource-group> -o table                 #list available versions
az aks upgrade -n <cluster-name> -g <resource-group> --kubernetes-version  1.25.5  #upgrade
```
