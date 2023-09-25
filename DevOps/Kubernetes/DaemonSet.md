# DaemonSet

In Kubernetes, a DaemonSet is a type of workload controller that ensures that a copy of a specified pod runs on every node within a cluster. 
DaemonSets are primarily used for running system daemons or background tasks that need to be scheduled on every node, 
such as log collectors, monitoring agents, or networking components.

Here are some key characteristics and use cases for DaemonSets in Kubernetes:
- **One Pod Per Node**: DaemonSets are designed to create exactly one instance (pod) of the specified workload on each node within a cluster.
  This ensures that the workload is distributed across all nodes.
- **Node-Affinity**: You can configure node affinity and anti-affinity rules to control which nodes the DaemonSet pods
  should be scheduled on or avoid scheduling on. This allows you to target specific nodes or node groups for running your pods.
- **Replacement and Scaling**: DaemonSets automatically manage the pod lifecycle.
  When nodes are added or removed from the cluster, DaemonSets will create or delete pods to maintain the desired number of pods per node.
- **Rolling Updates**: You can update the DaemonSet by changing its pod template, which will trigger rolling updates to each node.
  This allows you to roll out changes to all nodes in a controlled manner.
- **Use Cases**: Common use cases for DaemonSets include running cluster-wide services like container runtime monitoring agents
  (e.g., Prometheus Node Exporter), logging agents (e.g., Fluentd), or networking components (e.g., CNI plugins).

Here's an example of a simple DaemonSet YAML configuration:
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: my-daemonset
spec:
  selector:
    matchLabels:
      app: my-app
  template:
    metadata:
      labels:
        app: my-app
    spec:
      containers:
      - name: my-container
        image: my-image:latest
```

In this example:
- The `metadata.name` field specifies the name of the DaemonSet.
- The `spec.selector.matchLabels` field defines the labels that are used to select nodes where the pods should be scheduled.
- The `spec.template.metadata.labels` field specifies labels for pods created by the DaemonSet.
- The `spec.template.spec.containers` field defines the container specification for the pods.

When you apply this configuration, Kubernetes will automatically schedule one pod of `my-container` on each node in the cluster that matches the selector.

DaemonSets are a powerful tool for ensuring that certain pods run on every node in a Kubernetes cluster, 
which can be crucial for managing infrastructure and system-level services.
