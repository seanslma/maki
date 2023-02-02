# Loop and Case

## each line in a variable
```
list=$'One\ntwo\nthree\nfour'
echo "$list"

while IFS= read -r line; do
    echo "... $line ..."
done <<< "$list"

#one line
echo "$list" | while IFS= read -r line; do echo $line; done
```

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

## for with count
```
for (( i=0 ; i < 10 ; i++ )); do
    echo $i
done

for (( i=0, j=0 ; i+j < 10 ; i++, j++ )); do
    echo $(( i*j ))
done
```

## for with seq
```
#`$()` runs the command in subshell and
#returns the result with the newlines replaced by whitespace
for v in $(seq 1 .1 1.2) ; do
    echo $v
done

#preferred: can run `seq` in parallel with `while`
seq 1 .1 1.2 |
while read v ; do
    echo $v
done
```

## case
- `;;`  break
- `;;&` continue matching next patterns
- `;&`  fall-through, run next regardless of matching, useful for version patch
```
case $fn in
    *.gif) gif2jpg $fn
        ;;
    *.tif | *.TIFF) tif2jpg $fn
        ;;
    *) printf "File not supported: %s" $fn
        ;;
esac
```

case $version in
    1.0) update to version 2
        ;&  #fall-through
    2.0) update to version 3
        ;&  #fall-through
    *) printf "Nothing to update. It's already the latest version: %s" $version
        ;;
esac
