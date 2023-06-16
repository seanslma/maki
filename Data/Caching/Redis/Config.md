# Config

## Persistence
- snapshot: write a snapshot to disk
- append-only file: copy new write to disk

```
#for both
dir ./

#snapshot
save 60 1000
stop-writes-on-bgsave-error no
rdbcompression yes
dbfilename dump.rdb

#append-only file
appendonly no
appendfsync everysec
no-appendfsync-on-rewrite no
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb
```
