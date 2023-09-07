# acr

## yaml
```yaml
resource "azurerm_container_registry" "acr" {
  name                          = var.name
  resource_group_name           = var.resource_group_name
  location                      = var.location
  sku                           = "Standard"
  admin_enabled                 = true
  public_network_access_enabled = true
  zone_redundancy_enabled       = var.zone_redundancy_enabled

  retention_policy {
    enabled = true
    days    = var.untagged_retention_days
  }
  lifecycle {
    create_before_destroy = true
  }
  tags = {
    environment = local.env
  }
}
```
