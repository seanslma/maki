# Drop

## drop local changes
```
git checkout -- .
```

## drop unstaged files
```
git checkout -- .
git checkout -- path-to-file #only one file
```

## drop deleted file history
```
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch ./dev/my_file.json" --prune-empty --tag-name-filter cat -- --all
git push origin --force --all
```
