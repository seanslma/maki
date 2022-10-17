# File edit

## check new line (\n or \r\n)
displays Unix line endings (`\n` or LF) as `$` and Windows line endings (`\r\n` or CRLF) as `^M$`
```
cat -e <filename>
```

convert from one to another
```
apt-get install -y dos2unix
dos2unix <filename>

apt-get install -y unix2dos
unix2dos <filename>
```
