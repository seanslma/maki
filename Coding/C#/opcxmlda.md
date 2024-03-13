# OpcXmlDa

we should first call **Subscribe** then periodically call **SubscriptionPolledRefresh**. The handle provided by Subscribe will be used as input in SubscriptionPolledRefresh. If the parameter **SubscriptionPingRate** in Subscribe is set too low, the handle will become invalid when call SubscriptionPolledRefresh so you always get invalid handle error.

The **SubscriptionPingRate** is the requested rate in milliseconds (ms) that the server should reevaluate the existence of the client. If the client has not had any communication in the specified period, then the Server is free to clean up all resources associated with that client for this Subscription.

The server should attempt to honor the client’s request, but it may reevaluate the existence of the client at a rate faster than the SubscriptionPingRate based on its own implementation, and resource constraints. If the SubscriptionPingRate is 0, then the server will use its own algorithm to reevaluate the existence of the client. It is highly recommended that clients always specify a non-zero ping rate since specifying zero will allow the server to choose a ping rate that the client will not have knowledge of and may be inappropriate.

## Cisco anyconnect mobile vpn
must stop the vpnui process otherwise when you log off, the vpn will be disconnected because this ui is started by a local user. to avoid this issue, we have to ensure the vpn is connected via vpnagent the service that is shared by all users.

## check vpn status
```bat
netsh interface show interface
```

## web reference
Add -->  Web Reference --> Service Reference --> Advanced --> Address (URL)
