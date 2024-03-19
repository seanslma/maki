# DNS

 Resources in a virtual network can communicate with each other by using
 - IP addresses, and
 - names that can be easily remembered, and do not change

## Public DNS service

## Private DNS service
### Internal DNS service
- only works in the same vnet
- namespace: `.internal.cloudapp.net`. For example `my-vm.internal.cloudapp.net`

### Azure Private DNS Zone
They are global in scope, so can access them from
- any region,
- any subscription,
- any VNet, and
- any tenant.

A Private DNS Zone in Azure is a feature that allows you
to create a `custom DNS namespace` for your virtual networks in Azure.

It provides `name resolution` within your virtual network,
enabling you to use custom domain names for your resources
while keeping the DNS queries and responses `within the Azure network`.

## Azure Private DNS Zone Virtual Network Link
An Azure Private DNS Zone Virtual Network Link is a resource
that connects a `virtual network` within Azure to a specific `Azure Private DNS zone`.

It essentially bridges the gap between private DNS and your virtual network,
allowing resources within the virtual network to resolve host names defined in the private zone.

## Hybrid DNS resolution
https://learn.microsoft.com/en-us/azure/dns/private-resolver-hybrid-dns

## Private DNS best practices
https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/private-link-and-dns-integration-at-scale
- private DNS zones live in the hub
- an Azure policy automatically creates dnsZoneGroups for private endpoints
- for DNS resolution, spokes point to either a custom DNS or Azure Private Resolver in the hub

## Migrate private DNS zone
multiple-azure-private-dns-zones: https://serverfault.com/questions/1104244/multiple-azure-private-dns-zones

Not to have two different private DNS zones for the same Azure service tied with VNET links to the same VNE:
```
Creating multiple zones with the same name for different virtual networks would need manual operations to merge the DNS records.
```

If we need to migrate the private DNS zone to another private DNS zone. 
We first create the new DNS zone then delete the old one - this will not work.
- Need to restore the deleted old one
- When the info in the old DNS merged to the new one, we can then delete the old one
