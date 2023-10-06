# WebApi

Traffic flow:
```
Internet <-> Load Balancer <-> Ingress <-> Service <-> Pods
```

To ensure an api is accessible from the public internet, we should provide `ingress` and `service`, 
the `load balancer` is provided on the Kubernetes level.
