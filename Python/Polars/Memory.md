# Memory

## polars mem
- Polars switched to `jemalloc`
- Fragmentation in `mimalloc` allocator will lead to memory increase (leak? workaround: `MIMALLOC_ABANDONED_PAGE_RESET = 1`): https://github.com/pola-rs/polars/issues/18074
- A memory allocator cannot return the memory to the OS because it is fragmented
- Run operations with memory allocation in another process (`multiprocessing`) will help - memory will released once the process finished

free memory:
```py
del df
del d2
gc.collect()

df.estimated_size('mb')
```

## jemalloc
In jemalloc, memory goes through multiple stages:
- `Active`: currently in use.
- `Dirty`: freed but not yet zeroed; can be reused by the program.
- `Muzzy`: freed and zeroed, but not yet returned to the OS.
- `Returned`: truly unmapped (returned to the OS).

`muzzy_decay_ms:-1`: Jemalloc never releases zeroed (muzzy) memory to the OS.
why using `muzzy_decay_ms:-1`?
- page faults will significantly slowdown operations
- `muzzy_decay_ms:-1` will disable `MADV_DONTNEED`

Setting the parameters via env var before loading polars:
```sh
_RJEM_MALLOC_CONF="background_thread:true,dirty_decay_ms:500,muzzy_decay_ms:-1"
```
