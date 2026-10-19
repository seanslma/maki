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

## mutiple tags pointed to the same commit
if more than one tag has pointed to the same commit, setuptools-scm might still use the old tag.

Solution option #1: delete the old tag
```sh
git tag -d 2.0.0
git push origin --delete 2.0.0
```

Solution option #2: create an empty commit
```sh
git commit --allow-empty -m "Release 2.0.1"
git tag 2.0.1
git push origin HEAD --tags
```
