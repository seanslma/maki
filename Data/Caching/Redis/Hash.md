# Hash
save one level json (a Python dict) but can operate on each key-value pair separately.

commands
- `hmget key k [k ...]`: get values based on sub-keys
- `hmset key k v [k v ...]`: set values with key-value pairs
- `hdel key k [k ...]`: delete key-value pairs, return number of pairs found and deleted
- `hlen key`: return number of key-value pairs
