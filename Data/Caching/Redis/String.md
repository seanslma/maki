# string

string can be use to cache three types of values.
- Byte string values
- Integer values
- Floating-point values

## incr/decr commands 
assume non-existent or empty string having a value of zero:
- `incr key`: increase the value of key by 1
- `desc key`: decrease the value of key by 1
- `incrby key intval`: increase the value of key by intval
- `descby key intval`: decrease the value of key by intval
- `incrbyfloat key val`: increase the value of key by val

## substring commands
- `append key val`: concatenate value to string stored at the given key
- `getrange key start end-incl`: get substring from start to end inclusive
- `setrange key offset val`: append value to stored string ended before offset
- `getbit key idx`: get bit value at idx
- `setbit key idx val`: set bit value at idx
- `bitcount key [start, end]`: count the bits in the sub/string
- `bitop op des-key key-name [key-name2 ...]`: bitwise operations, `AND`, `OR`, `XOR`, or `NOT`, on provided strings, storing result in destination key
