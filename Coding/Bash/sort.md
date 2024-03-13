# sort

options
- `-r` reverse the order
- `-f` ignore case
- `-n` sort data as number
- `-u` unique, remove duplicates
- `-t` field separator
- `-k` sort via a key

## sort ip address
192.168.0.2: sort from first field to last field as number
```sh
sort -t . -k 1,1n -k 2,2n -k 3,3n -k 4,4n ip.list
```
