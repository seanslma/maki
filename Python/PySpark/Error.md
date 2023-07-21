# Error

## Java gateway process exited before sending its port number

## Caused by: java.net.SocketTimeoutException: connect timed out
https://knowledge.informatica.com/s/article/Caused-by-java-net-SocketTimeoutException-connect-timed-out-running-a-Spark-mapping-with-Sequence-Generator?language=en_US

Reason: Firewall blocked the java binary to access the network

Check if there is a firewall blocking the REST API call from the cluster to DIS nodes. 
