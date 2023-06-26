# Traefik

https://doc.traefik.io/traefik/

Traefik is a modern HTTP reverse proxy and load balancer made to deploy microservices with ease.

An open-source Edge Router receives requests on behalf of your system and finds out which components are responsible for handling them.

Traefik is a popular Kubernetes ingress controller that acts as a reverse proxy and load balancer for routing external traffic to services running within a cluster.

## routing
https://doc.traefik.io/traefik/routing/providers/kubernetes-crd/

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

## IngressRoute
IngressRoutes expose Kubernetes applications externally to the public. Ingresses associate with Pods through references to Services.
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
```

## MiddleWare
https://doc.traefik.io/traefik/middlewares/overview/

The middleware, attached to the router, provides a means of tweaking the requests before they are sent to the service (or before the answer from the service are sent to the client).

In Traefik, there are several available middleware, some can modify the request, the headers, some are in charge of redirections, some add authentication, and so on.

Use a `StripPrefix` middleware if your backend listens on the root path (/) but should be exposed on a specific prefix.

```yaml
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
