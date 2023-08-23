# VNet

https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview

https://learn.microsoft.com/en-us/training/modules/introduction-to-azure-virtual-networks/

- a logical representation of a network used to isolate and securely connect resources 
- contained within a resource group and is hosted within a region
- cannot span multiple regions but can span all datacenters within a region

## Connection
- resources within the same region and subscription 
  - VNet peering
- resources within the same (different) region in another subscription
  - VNet peering
  - Gateway: extra charges but allow encryption
- to on-premises resources
  - Point-to-site VPN
  - Site-to-site VPN  
  - ExpressRoute: not through public internet but costly

## Communicate with the internet
- `outbound` to the internet, by default, can be managed by `public IP`, `NAT gateway`, or `public load balancer`
- `inbound` to a resource by assigning a `public IP address` or `public load balancer`

## Communicate between Azure resources
- VNet
  -  connect VMs
  -  connect other Azure Resources, such as App Service Environment, Azure Kubernetes Service, and Azure Virtual Machine Scale Sets
- VNet service endpoint
  -  used to connect to other Azure resource types, such as Azure SQL databases and storage accounts
  -  services and VMs within the same VNet can communicate directly and securely with each other in the cloud
- VNet peering

## Communicate with on-premises resources
- Point-to-site VPN
- Site-to-site VPN
- Azure ExpressRoute

## Filter network traffic
filter network traffic between `subnets` using any combination of 
- network security groups and
- network virtual appliances like
- firewalls, gateways, proxies, and Network Address Translation (NAT) services

## Route network traffic
- Azure routes traffic between `subnets`, `connected virtual networks`, `on-premises networks`, and the `Internet`, by default
- You can implement `route tables` or `border gateway protocol` (BGP) routes to override the default routes Azure creates
