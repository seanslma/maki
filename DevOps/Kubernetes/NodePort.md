# NodePort

NodePort is another mechanism to expose a Kubernetes service externally.
It opens a static port on each node in the cluster, and any traffic coming to that port is forwarded to the corresponding service.

NodePort works at the transport layer (Layer 4) of the OSI model and can be considered a simple form of load balancing.

When you expose a service using NodePort, Kubernetes automatically assigns a port from the range 30000-32767, which is accessible on all nodes in the cluster. For example, if a service is assigned NodePort 30080, any traffic coming to any node's IP address on port 30080 will be forwarded to the service.

NodePort is often used for development and testing purposes or when you have a specific requirement to expose a service on a known port across all nodes. However, it has some limitations, such as exposing the service on a high port range, which might not be desirable in certain production scenarios.

NodePort is a simple way to expose services by opening a port on each node in the cluster, but it lacks the advanced features of Ingress.
