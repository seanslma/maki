# Error

## Java gateway process exited before sending its port number

## Caused by: java.net.SocketTimeoutException: connect timed out
Even run Spark in local mode, it communicates over the network just like any other Spark deployment. 
This means that the Firewall can potentially affect the communication between different Spark components.

In local mode, Spark's `driver program` communicates with the `worker threads` over TCP/IP, and the default port used is typically 7077. 

Reason: Firewall blocked the java binary to access the network

Check if there is a firewall blocking the REST API call from the cluster to DIS nodes. 
