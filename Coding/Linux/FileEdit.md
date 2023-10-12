# File edit

## merge files into one
```sh
cat ./* > merged-file
```

## check new line (\n or \r\n)
displays Unix line endings (`\n` or LF) as `$` and Windows line endings (`\r\n` or CRLF) as `^M$`
```sh
cat -e <filename>
```

convert from one to another
```sh
apt-get install -y dos2unix
dos2unix <filename>

apt-get install -y unix2dos
unix2dos <filename>
```
