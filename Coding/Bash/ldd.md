# ldd

Show shared objects and the dependencies in an executable.
 
## example
```
sudo ldd /bin/bash
```
- `-v` Verbose mode, print all information
- `-u` Show unused direct dependencies
- `-d` Execute data relocation and shows missing ELF objects
- `-r` Execute data and function relocation and shows missing ELF objects and functions

## ldconfig
configure dynamic linker run-time bindings
