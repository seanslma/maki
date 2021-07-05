# OpcXmlDa

## Cisco anyconnect mobile vpn
must stop the vpnui process otherwise when you log off, the vpn will be disconnected because this ui is started by a local user. to avoid this issue, we have to ensure the vpn is connected via vpnagent the service that is shared by all users.

## check vpn status
```dos
netsh interface show interface
```

## web reference
Add -->  Web Reference --> Service Reference --> Advanced --> Address (URL)
