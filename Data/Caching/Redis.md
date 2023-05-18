# Redis

## read
Redis in action

## install on linux
```
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```

## data structure
- STRING: Strings, integers, or floating point values
- LIST: Linked list of strings
- SET: Unordered collection of unique strings
- HASH: Unordered hash table of keys to values
- ZSET: Ordered mapping of string members to floating-point scores, ordered by score
