# Monitor

## azure monitor
- Best to enable azure monitor.
- It provides valuable insights into the health and performance of your aks resources.
- The specific cost will depend on the amount of data you collect and the retention period you choose.

## Commands for monitoring
```sh
kubectl get <resource type> <resource name>
kubectl describe <resource type> <resource name>
kubectl logs <pod name>
```

### kubectl get
Lists resources such as pods, ReplicaSets, ingresses, nodes, deployments, secrets, and so on.
```sh
#show all deployments, ReplicaSets, pods, and services
kubectl get all
#get pods status
kubectl get pods
#output with extra columns
kubectl get pods -o wide
```

### kubectl describe
It contains the details of the object itself, as well as any recent events
related to that object.
```sh
#just pods
kubectl describe pods
#a particular pod
kubectl describe pod/<pod-name> #or use space: kubectl describe pod <pod-name>
#get all events in a cluster
kubectl get events
```

## debug app

### image pull error
```sh
#create error
kubectl edit deployment/frontend
kubectl get pods
#get full error details
kubectl describe pods/<failed pod name>
```

### app error
```sh
kubectl get service
#scale down frontend
kubectl scale --replicas=1 deployment/frontend
#launch bash shell on pod
kubectl exec -it <frontend-pod-name> -- bash
#install vim
apt update
apt install -y vim
#update guestbook.php
vim guestbook.php
#get logs
kubectl logs <frontend-pod-name>
#get live log stream
kubectl logs <pod-name> -f
#solve error
kubectl delete pod <podname>
```

## probe
A **liveness probe** monitors the availability of an application while it is
running. If a liveness probe fails, Kubernetes will restart your pod.

A **readiness probe** monitors when your application becomes available. If a
readiness probe fails, Kubernetes will not send any traffic to the unready
pods.

218
