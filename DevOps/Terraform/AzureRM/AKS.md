# AKS

## network_profile example
https://github.com/fluxcd/source-controller/issues/898
```tf
  network_profile {
    network_plugin     = "azure"
    network_policy     = "azure"
    outbound_type      = "loadBalancer"
  }
```
