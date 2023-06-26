# Transaction

## commands
These commands will protect us from data corruption. They ensure that the data doesn't change while we're doing something important.
- MULTI/EXEC: commands after multi will run together on exec, like a pipeline
- WATCH: whe a key(s) is watched, if at any time the key is replaced, updated, or deleted before the EXEC operation, exec will fail with an error message (so we can retry
or abort the operation)
- UNWATCH: reset connection if sent after WATCH but before MULTI
- DISCARD: similar to unwatch

## example of watch
WATCH/MULTI/EXEC transactions sometimes don't scale at load.
```py
pipe = conn.pipeline()
while time.time() < end:
    try:
        pipe.watch('key-a', 'key-b')
        if not pipe.sismember('key-a', 'itemid'):
            pipe.unwatch()
            return None # condotion not satisfied
        # do the transaction
        pipe.multi()
        pipe.zadd('key-x', 'item', 100)
        pipe.srem('key-a', 'itemid')
        pipe.execute()
        return True
    except redis.exceptions.WatchError:
        pass # values in key-a or key-b were changed
```
