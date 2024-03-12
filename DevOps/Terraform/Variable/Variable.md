# Variable

## map vs object
- `map(string)` only accepts string value, but cannot validate the key types
- an object is a map with more explicit keying
- object does not have default keys, have to specify every key
- object will not accept any type that does not match the pattern
  ```
  object({
    id = string
    size = number
    labels = map(string)
  })
  ```
