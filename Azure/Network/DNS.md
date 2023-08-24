# DNS

 Resources in a virtual network can communicate with each other by using 
 - IP addresses, and
 - names that can be easily remembered, and do not change

## Public DNS service

## Private DNS service
### Internal DNS service
- only workds in the same vnet
- namespace: `.internal.cloudapp.net`. For example `my-vm.internal.cloudapp.net`

### Azure Private DNS Zones
They are global in scope, so can access them from any region, any subscription, any VNet, and any tenant
