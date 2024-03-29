# Redis

Redis (Remote Dictionary Server) can be used for caching, logging, statistics, cookies, and so on. Each can be on a separate Redis server on a single machine on different ports.

## data structure
- STRING: Strings, integers, or floating point values
  command: set, get, del
- LIST: Linked list of strings
  command: lpush/rpush, lpop/rpop, lindex, lrange
- SET: Unordered collection of unique strings
  command: sadd, srem, sismember, smembers, sinter, sunion, sdiff
- HASH: Unordered hash table of keys to values
  command: hset, hget, hgetall, hdel
- ZSET: Ordered mapping of string members to floating-point scores, ordered by score
  command: zadd, zrem, zrange, zrangebyscore
