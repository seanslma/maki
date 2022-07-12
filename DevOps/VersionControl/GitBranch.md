# Git Branch

## Show branches
```
git branch             #list all local branches
git branch -r          #list all remote branches
git branch -a          #list both local and remote branches
git branch --merged    #list all branches that have been merged
git branch --no-merged #list all branches not merged
```

## Delete branches
```
git branch -d <branch-name> #delete merged branch
git branch -D <branch-name> #force delete branch (even if not merged)
```

## Delete multiple local branches
```
git branch --merged | egrep -v "(^\*|master|main|develop)" | xargs git branch -d    #UNIX, merged
git branch --no-merged | egrep -v "(^\*|master|main|develop)" | xargs git branch -D #UNIX, unmerged

# `%` shortcut to foreach, `$_` is the piped variable
git branch --merged | Where-Object { !($_ | Select-String "master|main|develop" -quiet) } | %{git branch -d $_}    #PowerShell, merged
git branch --no-merged | Where-Object { !($_ | Select-String "master|main|develop" -quiet) } | %{git branch -D $_} #PowerShell, unmerged
```

## Delete remote branches
```
git push origin --delete <branch-name>
```

## Delete multiple remote branches
```
git branch -r --merged | egrep -v "(^\*|master|main|develop)" | sed 's/origin\///' | xargs -n 1 git push origin --delete
```
