# Architecture

## Configure domain name servers settings in Azure
https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/6-exercise-configure-domain-name-servers-configuration-azure

configure DNS name resolution for Contoso Ltd:
- create a private DNS zone named contoso.com
- link VNets for registration and resolution
- create two virtual machines

[private dns zone] -> [vnet link] -> [vnet] -> [subnet: vm1, vm2]
