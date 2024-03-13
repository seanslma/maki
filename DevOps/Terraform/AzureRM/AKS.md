# AKS

## node pool
https://github.com/MicrosoftDocs/azure-docs/blob/main/articles/aks/custom-node-configuration.md

Provider:
https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/kubernetes_cluster_node_pool

## role assignment
https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/role_assignment

## storage container
https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/data-sources/storage_container

## network_profile example
https://github.com/fluxcd/source-controller/issues/898
```tf
  network_profile {
    network_plugin = "azure"
    network_policy = "azure"
    outbound_type  = "loadBalancer"
  }
```
