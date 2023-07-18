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
