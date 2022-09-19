# Pattern Match

## wildcard
```
if [[ "$fn" == *.jpg ]]
```
- `*` to match any number of characters
- `?` to match a single character
- `[]` for including a list of possible characters

## shell options
```
shopt -s extglob
if [[ "$fn" == *.@(jpg|jpeg) ]]
```
`extglob` option deals with extended pattern matching (or globbing)
and `shopt -s nocasematch` for case-insensitive match.
- `@(...)` only one occurrence
- `+(...)` one or more occurrences
- `?(...)` zero or one occurrence
- `*(...)` zero or more occurrences
- `!(...)` not this, but anything else

## regular expression
Filename example: `Ludwig Van Beethoven - 05 - "Coriolan" Overture, Op. 12.ogg`
```
for fn in *
do
    if [[ "$fn" =~ "([[:alpha:][:blank:]]*)- ([[:digit:]]*) - (.*)$"
    then
        echo Track ${BASH_REMATCH[2]} is ${BASH_REMATCH[3]}
        mv "$fn" "Track${BASH_REMATCH[2]}"
    fi
done
```
- `${BASH_REMATCH[0]}` entire string matched by the regular expression
- `${BASH_REMATCH[1]}` any subexpressions, 1 ... n
