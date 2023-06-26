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
{"ingress":"dev-dashboard","level":"error",
"msg":"Failed to create middleware keys: middleware traefik/auth is not in the IngressRoute namespace dev",
"namespace":"dev","providerName":"kubernetescrd","time":"2023-06-22T22:37:12Z"}
```

## self-signed certificate
https://community.traefik.io/t/internal-server-error-when-proxing-to-https-with-self-signed-cert/11087/5

When proxying to a server that uses a self-signed certificate, we need to configure a `serversTransport` to tell Traefik how to handle the certificate. 

## example of IngressRoute and MiddleWare
```yaml
# https://doc.traefik.io/traefik/routing/providers/kubernetes-crd/#kind-ingressroute
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: "my-api"
  namespace: "dev"
spec:
  entryPoints:
    - websecure
  routes:
    - kind: Rule
      match: "Host(`dashboards.example.com`) && PathPrefix(`/dev/api`)"
      middlewares:
        - name: "my-api-stripprefix"
      services:
        - kind: Service
          name: "my-api"
          namespace: "dev"
          passHostHeader: true
          port: 5000
  tls: {}
---
apiVersion: traefik.containo.us/v1alpha1
kind: Middleware
metadata:
  name: "my-api-stripprefix"
  namespace: "dev"
spec:
  stripPrefix:
    prefixes:
      - "/dev/api"
```
