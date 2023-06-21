# Docker

## command
```
# create and run a iotdb Docker container
docker run -d -p 6667:6667 -p 31999:31999 -p 8181:8181 --name iotdb apache/iotdb
# run commands inside the running iotdb Docker container
docker exec -it iotdb /bin/bash
# change to iotdb folder
cd /iotdb/
```

## ports
The ports that IoTDB uses by defaut:
- 6667: RPC port
- 31999: JMX port
- 8181: Monitor port
- 5555: Data sync port
- 9003: internal metadata rpc port (for cluster)
- 40010: internal data rpc port (for cluster)
