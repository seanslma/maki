# Git Branch

## check the setup tracking branches
```
git branch -vv
#if it shows that the tracking branch is not upstream/master
# we need to fix it as below
```

## point local master to upstream/master
```
git checkout master
git reset --hard upstream/master
git branch --set-upstream-to upstream/master
```

## Show branches
```
git branch             #list all local branches
git branch -r          #list all remote branches
git branch -a          #list both local and remote branches
git branch --merged    #list all branches that have been merged
git branch --no-merged #list all branches not merged
```

## rename `master` to `main`
```
git branch -m master main       #local
git push -u origin main         #remote
git push origin --delete master #delete remote master
```

## create branch
```
git branch <new-branch>
git checkout -b <new-branch>  #create and switch to
```

## create branch from commit
```
git checkout -b <new-branch> <commit-hash or HEAD~i>
```

## restore deleted branch
```
git reflog show --all             #get sha1 of the deleted branch
git branch <NewBranchName> <sha1> #restore the branch
```

## Create branch from another branch
```
#checkout branch to copy
git checkout dev

#create new branch
#git checkout -b dev-test [current_active_branch]
git checkout -b dev-test

#push changes in dev-test to remote
git push origin dev-test
```

## Delete local branches
```
git branch -d <branch-name> #delete merged branch
git branch -D <branch-name> #force delete branch (even if not merged)
```

## Delete multiple local branches
```
# UNIX
git branch --merged | egrep -v "(^\*|master|main|develop)" | xargs git branch -d    #merged
git branch --no-merged | egrep -v "(^\*|master|main|develop)" | xargs git branch -D #unmerged

# PowerShell: `%` shortcut to foreach, `$_` is the piped variable
git branch --merged | Where-Object { !($_ | Select-String "master|main|develop" -quiet) } | %{git branch -d $_.Trim()}
git branch --no-merged | Where-Object { !($_ | Select-String "master|main|develop" -quiet) } | %{git branch -D $_.Trim()}
```

## Delete remote branches
```
git push origin --delete <branch-name>
git push --delete <remote name> <branch name> #delete remote branch
```

## Delete multiple remote branches
```
git branch -r --merged | egrep -v "(^\*|master|main|develop)" | sed 's/origin\///' | xargs -n 1 git push origin --delete #UNIX
git branch -r | Where-Object { !($_ | Select-String "HEAD|upstream|master|main|develop" -quiet) } |
  %{$_ -replace ([regex]::Escape('origin/'))} | %{git push origin --delete $_} #PowerShell
```

## branch is out-of-date with the base branch
```
git remote add upstream remote-upstream-repo-url
git checkout my-branch
git pull upstream master
git push origin my-branch
```

## Your branch is ahead of 'origin/master' by x commit
```
#origin/master is the remote forked branch
# you need to push your changes to the forked branch (origin/master)
#add the upstream repo if not (forked from)
git remote add upstream https://github.com/whoever/whatever.git
#get all change from the upstream
git fetch upstream
#go to local master branch
git checkout master
#rewrite master branch based on upstream
git rebase upstream/master
#push local changes to forked repo (-f only needed the first time after rebased)
git push -f origin master
```
