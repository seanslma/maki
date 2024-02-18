# VNet
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
  - can connect virtual networks to each other by using virtual peering

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

## IP address space
can be used:
```
10.0.0.0 - 10.255.255.255 (10/8 prefix)
172.16.0.0 - 172.31.255.255 (172.16/12 prefix)
192.168.0.0 - 192.168.255.255 (192.168/16 prefix)
```
Cannot be used:
```
224.0.0.0/4 (Multicast)
255.255.255.255/32 (Broadcast)
127.0.0.0/8 (Loopback)
169.254.0.0/16 (Link-local)
168.63.129.16/32 (Internal DNS)
```
