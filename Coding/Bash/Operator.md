# Operator

## AND and OR
No `short circuits` but `&&`and `||` have short circuits
- `-a`: [ -r "$FN" -a \( -f "$FN" -o -p "$FN" \) ]
- `-o`: [ -z "$V1" -o -z "${V2:=YIKES}" ]

## Comparison operators
https://tldp.org/LDP/abs/html/comparison-ops.html

Always put the $var in quotes
- `-n` is not null
- `-z` is null - has zero length
Using `-n` without quoting, will return true even it's empty


- `==` string comparison
- `-eq` numerical comparison

If always use the math-style symbols for comparison:
- do numerical tests with the `double-parentheses` syntax
- do string comparisons with the `double-square-brackets` syntax

## Arithmetic operators
`=, +=, -=, *=, /=, &=, \=, ^=, <<=, >>=`
Integer arithmetic:
```sh
let 'i += j' 'j *= i'
let n+='i**2 + 1'
n=$(( n + i**2 + 1 ))
```

## File testing unary operators
Exists
```sh
-d File is a directory
-f File is a regular file
-e File exists
-s File has a size greater than zero
```

Read/write etc
```sh
-r File is readable
-w File is writable
-x File is executable
-N File has been modified since it was last read
```

Types
```sh
-b File is a block special device (for files like /dev/hda1)
-c File is character special (for files like /dev/tty)
-S File is a socket
-p File is a named pipe
-h File is a symbolic link (same as -L )
-L File is a symbolic link (same as -h )
```

bit set
```sh
-k File has its sticky bit set
-u File has its set-user-ID (setuid) bit set
-g File has its set-group-ID (setgid) bit set
-O File is owned by the effective user ID
-G File is owned by the effective group ID
```

## File testing binary operators
```sh
[ file_1 -nt file_2 ] #file_1 is newer than file_2
[ file_1 -ot file_2 ] #file_1 is older than file_2
[ file_1 -ef file_2 ] #file_1 and file_2 have the same device or inode numbers
```
