# DNS

 Resources in a virtual network can communicate with each other by using 
 - IP addresses, and
 - names that can be easily remembered, and do not change

## Public DNS service

## Private DNS service
### Internal DNS service
- only workds in the same vnet
- namespace: `.internal.cloudapp.net`. For example `my-vm.internal.cloudapp.net`

### Azure Private DNS Zone
They are global in scope, so can access them from any region, any subscription, any VNet, and any tenant.

A Private DNS Zone in Azure is a feature that allows you to create a `custom DNS namespace` for your virtual networks in Azure. 
It provides `name resolution` within your virtual network, enabling you to use custom domain names for your resources 
while keeping the DNS queries and responses `within the Azure network`. 