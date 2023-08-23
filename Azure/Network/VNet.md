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
- VNet service endpoint
- VNet peering

## Communicate with on-premises resources
- Point-to-site VPN
- Site-to-site VPN
- Azure ExpressRoute
