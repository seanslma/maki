# VNet
- a logical representation of a network used to isolate and securely connect resources 
- contained within a resource group and is hosted within a region
- cannot span multiple regions but can span all datacenters within a region

## SubNet
- Subnets provide isolation within a virtual network
- Ssubnet IP range should not be too large or too small

## connection
- resources within the same region and subscription 
  - VNet peering
- resources within the same region in another subscription
  - VNet peering
  - Gateway: extra charges but allow encryption
