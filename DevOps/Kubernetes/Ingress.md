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
```
```
