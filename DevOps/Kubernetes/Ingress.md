# Ingress

Ingress is an API object that manages external access to services within a Kubernetes cluster.
It acts as a smart router or entry point for incoming traffic and provides advanced routing and load balancing capabilities.

Ingress typically works at the application layer (Layer 7) of the OSI model and can perform tasks such as URL-based routing, SSL termination, and request rewriting.

It allows you to define rules and configuration for handling different types of incoming traffic and directing them to appropriate services or paths within the cluster.

Ingress relies on an Ingress Controller, which is a separate component responsible for implementing the Ingress rules defined in the Kubernetes API. Popular Ingress Controllers include
- Nginx Ingress Controller,
- Traefik, and
- HAProxy Ingress.

To use Ingress, you need to have an Ingress Controller deployed in your cluster, and the controller must be properly configured and integrated with an external load balancer or an ingress controller that supports bare metal environments.
