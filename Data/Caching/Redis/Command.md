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
