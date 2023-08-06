# Event

## Install Argo Events
Argo Events is normally installed into a namespace called `argo-events`
```sh
# create namespace
kubectl create ns argo-events
# create argo events
kubectl apply -n argo-events -f https://github.com/argoproj/argo-events/releases/download/v1.8.0/install.yaml
# create event bus where events will be sent to
kubectl apply -n argo-events -f https://raw.githubusercontent.com/argoproj/argo-events/stable/examples/eventbus/native.yaml
```

## Trigger a workflow based on an event
create a sensor to trigger the event
```yaml
apiVersion: argoproj.io/v1alpha1
kind: Sensor
metadata:
  name: my-sensor
spec:
  dependencies:
    - name: example-dep
      eventSourceName: my-sensor
      eventName: example
  triggers:
    - template:
```

## Troubleshoot Kubernetes RBAC issues related to Argo Events and Workflows
rbac: https://kubernetes.io/docs/reference/access-authn-authz/rbac/

The default `Service Account` in the `argo-events` namespace does not have permission to create workflows in the `argo` namespace.

We will grant the default Service Account permission to create workflows using a `ClusterRole`, 
and a `ClusterRoleBinding` to bind the role to the Service Account.
```yaml
kind: ClusterRole
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: argo-events-create-wf-role
  namespace: argo-events
rules:
- apiGroups: ["argoproj.io"]
  resources: ["workflows"]
  verbs: ["create"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: argo-events-create-wf-role-binding
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: argo-events-create-wf
subjects:
- kind: ServiceAccount
  name: default
  namespace: argo-events
```
