# Failure

## Verify snapshots and append-only files
`redis-check-aof` and `redis-check-dump` commands can be used for testing the status of a snapshot and an append-only file.

## Replace a failed master
`Redis Sentinel` will monitor the Redis masters and slaves and automatically handles failover if the master goes down.

Mannually replace a failed master:
```sh
# connect to slave
ssh root@redis.slave.vpn
# run redis cli
redis-cli
# produce a fresh snapshot
SAVE and QUIT
# copy snapshot to machine X (the new master)
scp /var/local/redis/dump.rdb redis.x.vpn:/var/local/redis/dump.rdb
# connect to machine X
ssh redis.x.vpn
# start redis server
sudo /etc/init.d/redis-server start
# set slave to use machine x as master in slave cli
SLAVEOF redis.x.vpn 6379
```
