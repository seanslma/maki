# ZSET

similar to hash or dict, but will sort ans manipulate the values (numeric).

commands
- `zadd key score member [score member ...]`: add members with scores
- `zrem key member [member ...]`: remove members, return number of members removed
- `zcard key`: return number of members
- `zincrby key incr member`: increase member score
- `zcount key min max`: return number of members with scores between min and max
- `z[rev]rank key member`: return member position
- `zscore key member`: return member score 
- `z[rev]range key start stop [withscores]`: return members and optionally the scores with ranks between start and stop

other commands
- `z[rev]rangebyscore key min max [withscores] [limit offset count]`: get members with scores between min and max
- `zremrangebyrank key start stop`: remove members with ranks between start and stop
- `zremrangebyscore key min max`: remove members with scores between min and max
- `zinterstore dest-key nkey key [key ...] [weights weight [weight ...]] [aggregate sum|min|max]`: save intersection of zsets to new zset, default sum scores
- `zunionstore dest-key nkey key [key ...] [weights weight [weight ...]] [aggregate sum|min|max]`: save union of zsets to new zset, default sum scores
