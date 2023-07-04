# Performance

https://matthewrocklin.com/blog/work/2015/03/16/Fast-Serialization

https://gist.github.com/mrocklin/4f6d06a2ccc03731dd5f

- msgpack (depreciated)
- hdfstore

## arrow
https://arrow.apache.org/docs/10.0/python/ipc.html#ipc
```py
BATCH_SIZE = 10000
NUM_BATCHES = 1000
schema = pa.schema([pa.field('nums', pa.int32())])
with pa.OSFile('bigfile.arrow', 'wb') as sink:
   with pa.ipc.new_file(sink, schema) as writer:
      for row in range(NUM_BATCHES):
            batch = pa.record_batch([pa.array(range(BATCH_SIZE), type=pa.int32())], schema)
            writer.write(batch)
#load
with pa.OSFile('bigfile.arrow', 'rb') as source:
   loaded_array = pa.ipc.open_file(source).read_all()
#more efficient load
with pa.memory_map('bigfile.arrow', 'rb') as source:
   loaded_array = pa.ipc.open_file(source).read_all()
```
