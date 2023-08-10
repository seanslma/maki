# Workflow
https://github.com/argoproj/argo-workflows

## workflow
A workflow is a Kubernetes resource, consisting of one or more `templates`, with one defined as the entrypoint. 
Each template can be one of several types, such as container.

## argo server auth mode
https://argoproj.github.io/argo-workflows/argo-server-auth-mode/

## install workflow
```sh
kubectl create ns argo
kubectl apply -n argo -f https://github.com/argoproj/argo-workflows/releases/download/v3.4.9/install.yaml
```
installed
- `Workflow Controller` is responsible for running workflows
  ```sh
  kubectl -n argo get deploy workflow-controller
  ```
- `Argo Server` provides a user interface and API
  ```sh
  kubectl -n argo get deploy argo-server
  kubectl -n argo port-forward --address 0.0.0.0 svc/argo-server 2746:2746 > /dev/null &
  ```
wait for all to be ready
```sh
kubectl -n argo wait deploy --all --for condition=Available --timeout 5m
```

