# Set

commands
- `sadd key val [val ...]`: add values and return the number of values added that weren't already present
- `srem key val [val ...]`: remove values and return the number of values that were removed
- `sismember key val`: return whether the value is in the set
- `scard key`: return number of values in the set
- `smembers key`: rturns all values as a Python set
- `srandmember key [count]`: return one or more random values. positive count: distinct randomly chosen values; negative count:  randomly chosen values may not be distinct
- `spop key`: remove and return a random value
- `smove srs-key dest-key val`: if value exists, remove it from source and add it to destination, return True if the value was moved
