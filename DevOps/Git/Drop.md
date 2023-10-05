# Drop

## drop local changes
```sh
git checkout -- .
```

## drop unstaged files
```sh
git checkout -- .
git checkout -- path-to-file #only one file
```

## drop untracked files
```sh
git clean -n  # --dry-run
git clean -f  # delete untracked files and directories
git clean -fx # delete any ignored files (according to your .gitignore rules) as well
```

## drop deleted file history
```sh
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch ./dev/my_file.json" --prune-empty --tag-name-filter cat -- --all
git push origin --force --all
```

## drop all commit history
```sh
git checkout --orphan <branch-copy>
git add .
git commit -m "Initial commit"
git branch -D main
git branch -m main
git push -f origin main
```
