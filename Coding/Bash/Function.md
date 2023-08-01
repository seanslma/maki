# Function

## create a function
put the defined function in `.bashrc` and run `source ~/.bashrc`.
```sh
myfun() {
    mv "$1" "$1.bak"
    cp "$2" "$1"
}
```
