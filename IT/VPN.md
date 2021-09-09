# VPN

VPN connectio ncan be blocked by company firewall.

## OpenConnect
The group name should be put in the authgroup. 

Decrease the value of base-mtu if get error: Failed to write to SSL socket: The transmitted packet is too large.

Limitation: It seems OpenConnect CLI does not provide the method to get the VPN connection status in Windows.
```
openconnect.exe my.svr.com --authgroup my-grp --protocol=anyconnect -u usr --base-mtu=1000 -q --passwd-on-stdin
```

## Cisco Mobile VPN Client
```
vpncli connect my.svr.com grp usr pwd y
vpncli disconnect
vpncli status
```
