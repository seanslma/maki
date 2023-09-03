# Node pool

## node labels and node taints
- `node_labels` - (Optional) A map of Kubernetes labels which should be applied to nodes in this Node Pool.
- `node_taints` - (Optional) A list of Kubernetes taints which should be applied to nodes in the agent pool (e.g key=value:NoSchedule).
  Changing this forces a new resource to be created.

These properties can be used to only allow some pods to be deployed in this node pool.
```tf
# https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/kubernetes_cluster_node_pool
resource "azurerm_kubernetes_cluster_node_pool" "np01" {
...
  node_labels = {
    "hub.jupyter.org/node-purpose" = "dev-user"
  }
  node_taints = [
    "hub.jupyter.org/dedicated=dev-user:NoSchedule"
  ]
}
```

And in jupyterhub `values.yaml`
```yaml
singleuser:
  nodeSelector:
    hub.jupyter.org/node-purpose: dev-user
scheduling:
  userPods:
    nodeAffinity:
      matchNodePurpose: require
```
