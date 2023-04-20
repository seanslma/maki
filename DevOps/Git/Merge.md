# Merge

## how to merge
```
#edit conflict file
git add <file-path>
git commit -m "Updated"
git push
```

## in conflict state accept `theirs`
```
git checkout --theirs <file-path>
git add <file-path>
```

## resolve conflict
```
git switch master
git pull
git switch my-branch
git rebase master
```
