# ZSET

similar to hash or dict, but will sort ans manipulate the values (numeric).

commands
- `zadd key score member [score member ...]`: add members with scores
- `zrem key member [member ...]`: remove members, return number of members removed
- `zcard key`: return number of members
- `zincrby key incr member`: increase member score
- `zcount key min max`: return number of members with scores between min and max
- `zrank key member`: return member position
- `zscore key member`: return member score 
- `zrange key start stop [withscores]`: return members and optionally the scores with ranks between start and stop

