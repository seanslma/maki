# VNet

https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview

- a logical representation of a network used to isolate and securely connect resources 
- contained within a resource group and is hosted within a region
- cannot span multiple regions but can span all datacenters within a region

## SubNet
- Subnets provide isolation within a virtual network
- Subnet IP range should not be too large or too small

## Connection
- resources within the same region and subscription 
  - VNet peering
- resources within the same (different) region in another subscription
  - VNet peering
  - Gateway: extra charges but allow encryption
- to on-premises resources
  - Site-to-site VPN
  - Point-to-site VPN
  - ExpressRoute: not through public internet but costly
