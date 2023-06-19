# Transaction

## commands
These commands will protect us from data corruption. They ensure that the data doesn't change while we're doing something important.
- MULTI/EXEC: commands after multi will run together on exec, like a pipeline
- WATCH: whe a key(s) is watched, if at any time the key is replaced, updated, or deleted before the EXEC operation, exec will fail with an error message (so we can retry
or abort the operation)
- UNWATCH: reset connection if sent after WATCH but before MULTI
- DISCARD: similar to unwatch
