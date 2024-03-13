# DNS Record
https://learn.microsoft.com/en-us/azure/dns/dns-zones-records

## Record types
- `apex record` (`@`) is a DNS record at the root (or apex) of a DNS zone. 
- `A record` (short for Address record) is a type of DNS (Domain Name System) record
  that maps a hostname (or domain name) to its corresponding `IPv4` address
- `AAAA records` (for IPv6 addresses)
- `CNAME records` (for creating aliases)
- `MX records` (for email servers)

## Record sets
Used to create more than one DNS record with a given name and type. 

For example, suppose a web site is hosted on two different IP addresses. The website requires two different A records, one for each IP address.

The `SOA` and `CNAME` record types can only contain a single record.
