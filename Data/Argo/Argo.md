# Argo

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
