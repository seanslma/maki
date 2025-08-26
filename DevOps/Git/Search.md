# Search

## search deleted code
Search for `abc xyz`
```sh
git log -G "abc +xyz" --oneline
```

## search deleted filepath
```sh
git log --oneline -- **/my_file.py
```
