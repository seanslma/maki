# Command

https://redis.io/commands/

## sort
can be used to
- sort numbers character by character (via the alpha keyword argument),
- sort items based on external data, and
- fetch external data to return

## transaction commands
- WATCH,
- MULTI,
- EXEC,
- UNWATCH, and
- DISCARD

`MULTI` and `EXEC` can be used for a client to execute multiple commands without being interrupted by other clients.

example
```py
def trans():
    pipeline = r.pipeline()
    pipeline.incr('trans:', 2)
    time.sleep(.1)
    pipeline.incr('trans:', -1)
    ret = pipeline.execute()
    print(ret[0])
for i in xrange(5):
    threading.Thread(target=trans).start()
    time.sleep(.5)
```

## expiration commands
- `persist key`: remove expiration from key
- `ttl key`: return time remaining in seconds before key expires
- `expire key seconds`: set key to expire in seconds
- `expireat key timestamp`: set expiration time of unix timestamp in seconds
- `pttl key`: return time remaining in illiseconds before key expires
- `pexpire key milliseconds`: set key to expire in ms
- `pexpireat key timestamp-milliseconds`: set expiration time of unix timestamp in ms

## info command
`INFO` command can offer a wide range of information about the current status of a Redis server:
- cpu, memory used,
- server/clients, such has number of connected clients,
- stats, number of keys in each database, number of commands executed since the last snapshot, and so on
- persistence, such as `aof_pending_bio_fsync`: is 0 if all data that the server knows about has been written to disk
