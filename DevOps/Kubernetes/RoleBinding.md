# Role Binding

## Role and ClusterRole
ClusterRole and Role are resources used for defining sets of permissions within a cluster:
- **ClusterRole**: Applies cluster-wide and can be used to define permissions across all namespaces within the cluster.
- **Role**: Applies to a specific namespace and defines permissions for resources within that namespace.

## RoleBinding
Defines access within the Kubernetes cluster, such as the ability to list, get, or watch specific resources (pods, services, etc.).
