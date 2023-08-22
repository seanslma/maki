# VNet

https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview

- a logical representation of a network used to isolate and securely connect resources 
- contained within a resource group and is hosted within a region
- cannot span multiple regions but can span all datacenters within a region

## SubNet
- Subnets provide isolation within a virtual network
- Subnet IP range should not be too large or too small

## filter network traffic between subnets
- `Network security groups` and `application security groups` can contain multiple inbound and outbound security rules.
- These rules enable you to filter traffic to and from resources by source and destination `IP address`, `port`, and `protocol`. 
- A `network virtual appliance` is a VM that performs a network function, such as a firewall, WAN optimization, or other network function.

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
- All resources in a virtual network can communicate `outbound` to the internet, by default
- Outbound connections can also be managed by using `public IP`, `NAT gateway`, or `public load balancer`
- Communicate `inbound` to a resource by assigning a `public IP` address or a `public load balancer`

## Communicate between Azure resources
- VNet
- VNet service endpoint
- VNet peering

## Communicate with on-premises resources
- Point-to-site VPN
- Site-to-site VPN
- Azure ExpressRoute
