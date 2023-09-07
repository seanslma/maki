# role assignment

https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/role_assignment

## acrPull/Push
AcrPull
```yaml
resource "azurerm_role_assignment" "kubweb_to_acr" {
  scope                = azurerm_container_registry.acr.id
  role_definition_name = "AcrPull"
  principal_id         = azurerm_kubernetes_cluster.aks.kubelet_identity[0].object_id
}
```
