# Editor

## check available editors
```sh
update-alternatives --display editor
```

## create a file without editor
One line file:
```sh
echo "Hello World" > file.txt
```

Multiple line file:
```sh
echo "Line 1" >> file.txt
echo "Line 2" >> file.txt
```

Multiple line file:
```sh
cat << EOF > file.txt
Line 1
Line 2
EOF
```
Limitation: "$only" will became "".

## replace last line
```sh
{ head -n -1 filename.txt; echo "New last line content"; } > filename.txt
```

## escape special characters and keep leading spaces and tabs
- `'EOF'` will escape special characters
- `<<-` will keep (or strip) leading spaces and tabs???
```sh
cat <<- 'EOF' > file.txt
  Special characters: $, \, *, etc.
  Including variable: "$only"
EOF
```
