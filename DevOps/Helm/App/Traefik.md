# Traefik

https://doc.traefik.io/traefik/

Traefik is a modern HTTP reverse proxy and load balancer made to deploy microservices with ease.

An open-source Edge Router receives requests on behalf of your system and finds out which components are responsible for handling them.

Traefik is a popular Kubernetes ingress controller that acts as a reverse proxy and load balancer for routing external traffic to services running within a cluster.

## TLSStore
https://doc.traefik.io/traefik/routing/providers/kubernetes-crd/#kind-tlsstore
- TLSStore is the CRD implementation of a Traefik "TLS Store".
- Register the TLSStore kind in the Kubernetes cluster before creating TLSStore objects.

## tsl
https://doc.traefik.io/traefik/https/tls/

## allowCrossNamespace
Allow IngressRoute to reference resources in namespaces other than theirs.

https://doc.traefik.io/traefik/providers/kubernetes-crd/
```yaml
providers:
  kubernetesCRD:
    allowCrossNamespace: true
```

The default value is false and will get this error when the `auth` MiddleWare is in the traefik namespace
```
{"ingress":"dev-dashboard","level":"error","msg":"Failed to create middleware keys: middleware traefik/auth is not in the IngressRoute namespace dev","namespace":"dev","providerName":"kubernetescrd","time":"2023-06-22T22:37:12Z"}
```
