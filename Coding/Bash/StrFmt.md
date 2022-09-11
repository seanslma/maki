# String Format

## convert to lowercase
```
${var,,}
# Example: rename files
for fn in *.JPG; do
    mv "$fn" "${fn,,}"
done
```

## convert to uppercase
```
${var^^}
```

## swap case
```
${var~~}
```

## convert to camel case
```
while read txt; do
    a=($txt)      #treat as array init by parentheses, each word an element
    echo ${a[@]^} #[@] references all elements at once, and ^ converts first character to uppercase
done
```