# Ingress

Ingress is an API object that manages external access to services within a Kubernetes cluster.
It acts as a smart router or entry point for incoming traffic and provides advanced routing and load balancing capabilities.

Ingress typically works at the application layer (Layer 7) of the OSI model and can perform tasks such as URL-based routing, SSL termination, and request rewriting.

It allows you to define rules and configuration for handling different types of incoming traffic and directing them to appropriate services or paths within the cluster.

Compared to NodePort, Ingress is a more advanced and flexible way to expose services, providing application-layer routing and load balancing capabilities.

## Ingress Controller
Ingress relies on an `Ingress Controller`, which is a separate component responsible for implementing the Ingress rules defined in the Kubernetes API.

Popular Ingress Controllers include
- Nginx Ingress Controller,
- Traefik, and
- HAProxy Ingress.

To use Ingress, you need to
- have an Ingress Controller deployed in your cluster, and
- the controller must be properly configured and integrated with an external load balancer or an ingress controller that supports bare metal environments.

## troubleshooting ingress and services traffic flows
https://medium.com/@ManagedKube/kubernetes-troubleshooting-ingress-and-services-traffic-flows-547ea867b120
```
Internet <-> Load Balancer <-> Ingress <-> Service <-> Pods
```
- check pod
- check service
- check ingress
- check load balancer

## Ingress controller logs
Find the type of Ingress Controller used. Then get the log of that Ingress Controller pod.
```sh
kubectl logs --tail=20 <pod-name>  #display only most recent 20 lines of logs
kubectl logs --since=1h <pod-name> #display all logs written in the last hour
```

## Ingress Middleware
n Kubernetes, an IngressRoute is a custom resource definition (CRD) introduced by the Traefik Proxy for defining ingress routes in a declarative manner. If you have multiple apps defined on the same route path in an IngressRoute, the behavior depends on how the Ingress controller (such as Traefik) and the backend applications are configured.

If you're using the Traefik IngressRoute and you have middleware configured with StripPrefix, it will remove a specified prefix from the request URL before forwarding the request to the backend service. This is useful when your backend service expects requests without a certain prefix.

```yaml
apiVersion: traefik.containo.us/v1alpha1
kind: IngressRoute
metadata:
  name: my-ingressroute
spec:
  entryPoints:
    - web
  routes:
  - match: Host(`example.com`) && PathPrefix(`/app1`)
    kind: Rule
    services:
    - name: app1-service
      port: 80
    middlewares:
    - name: strip-app1-prefix

  - match: Host(`example.com`) && PathPrefix(`/app2`)
    kind: Rule
    services:
    - name: app2-service
      port: 80
    middlewares:
    - name: strip-app2-prefix

---
apiVersion: traefik.containo.us/v1alpha1
kind: Middleware
metadata:
  name: strip-app1-prefix
spec:
  stripPrefix:
    prefixes:
      - /app1

---
apiVersion: traefik.containo.us/v1alpha1
kind: Middleware
metadata:
  name: strip-app2-prefix
spec:
  stripPrefix:
    prefixes:
      - /app2
```
