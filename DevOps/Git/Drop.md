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

## drop all commit history
```
git checkout --orphan <branch-copy>
git add .
git commit -m "Initial commit"
git branch -D main
git branch -m main
git push -f origin main
```
