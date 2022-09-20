# Loop

## while
```
#arithmetic condition
while (( n < m )); do
    ...
    let n++
done

#file system condition
while [ -z "$fn" ]; do
    ...
done

#from input
while read line; do
    process $line
done

#from file
while read line; do
    process $line
done < file.input

#cat to standard output
cat file.input |
while read line; do
    process $line
done
```
