# Tag

## tag to release
```sh
git tag -a 0.1.0 -m "Release 0.1.0"
git push origin 0.1.0
```

## delete local/remote tag
```sh
git tag -d 0.1.0
git push origin --delete 0.1.0
```

## delete remote tag
```sh
git push origin --delete 0.1.0
git push upstream --delete 0.1.0
```
