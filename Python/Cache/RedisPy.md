# Redis-py

## methods
`time` can be represented by int or a Python timedelta/datetime object
- `r.setx(key, time, value)`	
  set value of key that expires in time seconds
- `r.expire(key, time)`	
  set expire flag for time seconds
- `r.psetex(key, time_ms, value)`
  set value of key that expires in time_ms milliseconds
- `r.expireat(key, when)`
  set an expire flag
- `r.persist(key)`
  remove expiration
- `r.ttl(key)`
  return the number of seconds until the key expires
- `r.pttl(key)`
  return the number of milliseconds until the key expires
