# Argo

You have a running Kubernetes Cluster: use Argo.

Argo has all configuration written in YAML and all tasks containerized running on Kubernetes. 
Writing DAGs is completly independent of any programming language. 

## Argo Server
And the Argo Server provides a user interface and API
```sh
kubectl -n argo get deploy argo-server
```

## Workflow Controller
The Workflow Controller is responsible for running workflows
```sh
kubectl -n argo get deploy argo-workflow-controller
```
