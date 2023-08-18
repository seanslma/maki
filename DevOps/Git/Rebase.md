# Rebase

https://github.com/openedx/edx-platform/wiki/How-to-Rebase-a-Pull-Request

## fetch latest version of upstream master
```sh
git fetch upstream
```

## find hash of commit which is base of my-branch
```sh
git merge-base my-branch upstream/master # will return a commit hash
```

## merge commits by rebasing the pr branch
```sh
git rebase -i <hash>
```
Replace "pick" with "squash" except first one. Then save and close the file.

## perform a rebase
```sh
git rebase upstream/master
# resolve conflicts and
git rebase --continue
# push the changes
git push -f
```
