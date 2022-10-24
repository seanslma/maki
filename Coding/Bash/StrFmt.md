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

## printf format
`printf "%-10.10s [%8d]:", i, v[i]`
- `%-10.10s` left align and pad to 10 characters but also truncate at 10 characters
- `%8d` assure the integer is printed in an 8-character field (right aligned)
