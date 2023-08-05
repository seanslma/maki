# Function
Unlike functions in “real” programming languages, Bash functions don’t allow you to return a value when called.
When a bash function completes, its return value is the status of the last statement executed in the function, 0 for success and non-zero decimal number in the 1 - 255 range for failure.

## create a function
put the defined function in `.bashrc` and run `source ~/.bashrc`.
```sh
myfun() {
    mv "$1" "$1.bak"
    cp "$2" "$1"
}
```

## how to return a value
using `echo` to return a value from a function
```sh
myfun() {
    echo $(( $1+1 ))
}
```
