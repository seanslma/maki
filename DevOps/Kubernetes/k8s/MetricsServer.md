# MetricsServer
https://github.com/kubernetes-sigs/metrics-server

Kubernetes Metrics Server measures CPU and memory usage and shows resource usage statistics across the cluster.

## install
```
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```
Installed conponents
```
service/metrics-server
serviceaccount/metrics-server
deployment.apps/metrics-server
apiservice.apiregistration.k8s.io/v1betal.metrics.k8s.io
rolebinding.rbac.authorization.k8s.io/metrics-server-auth-reader
clusterrole.rbac.authorization.k8s.io/system: aggregated-metrics-reader
clusterrole.rbac.authorization.k8s.io/system: metrics-server
clusterrolebinding.rbac.authorization.k8s.io/metrics-server: system: auth-delegator
clusterrolebinding.rbac.authorization.k8s.io/system: metrics-server
```

## error: the server could not find the requested resource (get services http:heapster:) 
Error from `kubectl top nodes`, indicating that the metrics server `apiserver` is missing or not work correctly.
