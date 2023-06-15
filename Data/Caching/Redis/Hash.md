# Hash
save one level json (a Python dict) but can operate on each key-value pair separately.

commands
- `hmget key k [k ...]`: get values based on sub-keys `deprecated`?
- `hmset key k v [k v ...]`: set values with key-value pairs
- `hdel key k [k ...]`: delete key-value pairs, return number of pairs found and deleted
- `hlen key`: return number of key-value pairs

other commands
- `hexists key k`: check key existence
- `hkeys key`: get keys
- `hvals key`: get values
- `hgetall key`: get all key-value pairs
- `hincrby key k val_incr`: increase value at k
- `hincrbyfloat key k val_incr`: increase value at k by float
