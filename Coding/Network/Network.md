# Network

## check internet
try https://xxx.xx.x.x and see if they get a webpage? if you do it's almost certainly an internet issue

## check connections
```sh
netstat -a # to show current connections
```

## when not use `ping`
The `ping` uses ICMP (Internet Control Message Protocol) packets, which may be blocked by network firewalls or restricted by network policies.

For example, an service deployed in aks might only posed the http port. In this case, we should try one of the following:
- `curl http://<service-ip>:<port>`
- `telnet <service-ip> <port>`
- `nc -vz <service-ip> <port>`
