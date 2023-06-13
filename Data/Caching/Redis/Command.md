# Command

https://redis.io/commands/

## string
string can be use to cache three types of values.
- Byte string values
- Integer values
- Floating-point values

incr and decr commands (assume non-existent or empty string having a value of zero):
- `incr key`: increase the value of key by 1
- `desc key`: decrease the value of key by 1
- `incrby key intval`: increase the value of key by intval
- `descby key intval`: decrease the value of key by intval
- `incrbyfloat key val`: increase the value of key by val

substring commands:
- `append key val`: concatenate value to string stored at the given key
- `getrange key start end-incl`: get substring from start to end inclusive
- `setrange key offset val`: append value to stored string ended before offset
- `getbit key idx`: get bit value at idx
- `setbit key idx val`: set bit value at idx
- `bitcount key [start, end]`: count the bits in the sub/string
- `bitop op des-key key-name [key-name2 ...]`: bitwise operations, `AND`, `OR`, `XOR`, or `NOT`, on provided strings, storing result in destination key

## list
- `l/rpush key val [val ...]`: pushe  value(s) onto the left/right end of the list
- `l/rpop key`: remove and return left/right most item from the list
- `lindex key offset`: return item at the given offset
- `lrange key start end-incl`: return items from start to end inclusive
- `ltrim key start end-incl`: trim the list to only include items between start and end inclusive
