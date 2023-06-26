# Memory

## methods to reduce memory
- short data structures
- sharding to make larger structures small
- packing fixed-length data into STRINGs

## ziplist
ziplist is more compact then general list, hash and zset.
```
list-max-ziplist-entries 512
list-max-ziplist-value 64

hash-max-ziplist-entries 512
hash-max-ziplist-value 64

zset-max-ziplist-entries 128
zset-max-ziplist-value 64
```
