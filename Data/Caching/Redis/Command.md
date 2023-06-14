# Command

https://redis.io/commands/

## list
- `l/rpush key val [val ...]`: pushe  value(s) onto the left/right end of the list
- `l/rpop key`: remove and return left/right most item from the list
- `lindex key offset`: return item at the given offset
- `lrange key start end-incl`: return items from start to end inclusive
- `ltrim key start end-incl`: trim the list to only include items between start and end inclusive

block pop and item move
- `bl/rpop key- [key ...] timeout`: pop left/right most item from first non-empty LIST, or wait timeout in seconds for an item
- `rpoplpush src-key dest-key`: pop right most item from source and lpush to dest, also return the item to the user
- `rpoplpush src-key dest-key timeout`: pop right most item from source and lpush to dest, also return to the user, and wait up to timeout if source is empty
