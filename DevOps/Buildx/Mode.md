# Buildkit deployment mode

## modes
https://github.com/moby/buildkit/tree/master/examples/kubernetes
- `Pod`: good for quick-start
- `Deployment + Service`: good for random load balancing with registry-side cache
- `StateFulset`: good for client-side load balancing, without registry-side cache
- `Job`: good if you don't want to have daemon pods

## Deployment + Service
I'd recommend using a combination of `Deployment + Service` for deploying BuildKit in AKS with a self-hosted TFS agent.

**Scalability and Load Balancing:**
- Deployment allows you to scale your BuildKit pods up or down based on demand, ensuring optimal resource utilization.
- Service provides random load balancing across your BuildKit pods, distributing incoming build requests evenly.
  This is crucial for handling random spikes in build workloads.

**Caching:**
- While Deployment + Service doesn't provide registry-side caching directly,
  you can leverage Azure Container Registry (ACR) as your container image registry.
  ACR offers built-in caching capabilities, which can significantly improve build performance by reusing previously downloaded layers.

**Self-Hosted TFS Agent:**
- You can deploy your self-hosted TFS agent as a separate Deployment with a Service.
  This ensures the agent pods are always available to handle build requests triggered by TFS.

Here's a breakdown of how each mode fits your scenario:
- **Pods:** While good for quick-starts, Pods aren't ideal for production due to limitations in scaling and load balancing.
- **StatefulSet:** Client-side load balancing might not be necessary in your case if you're using a container image registry like ACR with built-in caching.
- **Job:** Jobs are suitable for one-time or infrequent tasks, not ideal for continuously running BuildKit services.

**Deployment and Service Configuration:**
1. Create a Deployment for your BuildKit pods, specifying the desired number of replicas for scaling.
2. Define a Service of type `LoadBalancer` to expose your BuildKit pods externally. This allows TFS to access the BuildKit service for initiating builds.
3. Configure ACR as your container image registry to benefit from built-in caching mechanisms.

By combining Deployment, Service, and ACR, you'll achieve a scalable, load-balanced BuildKit deployment 
with caching capabilities, making it suitable for production use with your self-hosted TFS agent.

