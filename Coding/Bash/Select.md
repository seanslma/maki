# Select
`select` statement can create simple character-based screen menu.
You select the number and the value for the number will be recorded.

```sh
files=$(ls)
select fn in $files; do
    echo File: $fn
    #do something
done
```
