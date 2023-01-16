# Search

## search deleted code
Search for `abc xyz`
```
git log -G "abc +xyz" --oneline
```

## search deleted filepath
```
git log --oneline -- **/my_file.py
```
