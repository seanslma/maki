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
