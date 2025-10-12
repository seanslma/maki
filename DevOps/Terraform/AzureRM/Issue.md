# Issue

## how to find the api version for managedClusters used in hashicorp/azurerm
- goto `https://github.com/hashicorp/terraform-provider-azurerm/blob/v3.99.0/internal/services/containers/client/client.go`
- locate `".../containerservice/2025-07-01/managedclusters"`
- api-version for managedclusters is `2025-07-01`
