# Sync

## push
push local branch to remote branch with the same name
```
git push <remote> <local-branch>
```

## fetch
fetch remote branch
```
git fetch <repo> <remote-branch>
```

## merge
merge remote branch to current branch
```
git merge <repo>/<remote-branch>
```

## pull
fetch remote branch and merge to local branch
```
git pull <repo> <remote-branch>:<local-branch>
```

## remove a local repo
```
rm -fr .git  #will keep all
```

## clone repo to local folder
```
git clone https://github.com/usr/repo.git repo_name
```

## clone local to azure repo
```
git remote add azure https://azure.com/repo-name
git push -u azure --all
```

## upstream to master (sync a fork)
```
git checkout master       #check out fork's local default branch
git fetch upstream        #fetch upstream branches and commits
git merge upstream/master #merge upstream/master into local current branch
git push origin master    #push local changes to origin/master
```

## upstream to local branch (rebase)
```
git checkout my-branch
git stash
git fetch upstream
git rebase upstream/master #rebase my-branch from the upstream’s master branch
git stash pop
```

## master to local branch
```
git checkout my-branch
git fetch origin        #git pull origin master, OK but better use
git merge origin/master
```

## remote `azure` branch to local master
```
git checkout <local-branch>  
git fetch azure
git merge <repo>/<remote-branch> #merge to local checked-out branch

# example
git checkout main
git fetch origin
git merge origin/main
```

## remote `azure` branch to local new branch
```
git fetch <repo> <remote-branch>
git checkout -b <local-branch> <repo>/<remote-branch>
```

## local branch to remote `azure` branch
```
# first time add upstream
git push -u azure local-branch
# git push <repo> <local-branch>:<remote-branch>
git push azure local-branch:remote-branch
```

## merge upstream repo into fork
```
#check out branch to merge to
git checkout my-branch

#pull the desired branch from the upstream repo
git pull https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git branch-name

#commit the merge

#push merge to GitHub repo
git push origin branch-name
```

## cherry-pick
cherry-pick from github repo to azure devops repo
```
git checkout -b sync-1
git fetch azure
git reset --hard azure/main

git fetch github

# one by one
git cherry-pick <commit-hash-1>
..
git cherry-pick <commit-hash-n>

# or in a range
git cherry-pick <oldest-commit-hash>^..<newest-commit-hash>

git push azure sync-1
```
