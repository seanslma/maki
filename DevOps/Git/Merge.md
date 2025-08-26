# Merge

## how to merge
```sh
#edit conflict file
git add <file-path>
git commit -m "Updated"
git push
```

## in conflict state accept `theirs`
```sh
git checkout --theirs <file-path>
git add <file-path>
```

## resolve conflict
```sh
git switch master
git pull
git switch my-branch
git rebase master
```

## refusing to merge unrelated histories
```sh
$ git merge azure/main
fatal: refusing to merge unrelated histories
```
- two repos do not have shared histories
- force merge: `git merge azure/main --allow-unrelated-histories`
- then solve the conflicts: `git add xxx; git commit yyy`
- `not good`: will include all commits from the source repo
- use `cherry-pick`?
