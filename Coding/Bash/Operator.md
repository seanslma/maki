# Operator

## Comparison operators
https://tldp.org/LDP/abs/html/comparison-ops.html
- `-n` is not null
- `-z` is null - has zero length
Using `-n` without quoting, will return true even it's empty

## Arithmetic operators
`=, +=, -=, *=, /=, &=, \=, ^=, <<=, >>=`
Integer arithmetic:
```
let 'i += j' 'j *= i'
let n+='i**2 + 1'
n=$(( n + i**2 + 1 ))
```