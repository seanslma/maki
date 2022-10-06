# Sync

## clone repo to local folder
```
git clone https://github.com/usr/repo.git repo_name
```

## clone local to azure repo
```
git remote add azure https://azure.com/repo-name
git push -u azure --all
```

## local folder to github repo
```
#create a github repo first, do not add readme etc
git init -b main                            #initialize local directory as a git repo
git add . && git commit -m "initial commit" #stage and commit all files in your project
git remote add origin https://github.com/usr/repo.git  #link to github
git push -u origin main                     #push to github repo
```

## sync a fork
```
#fetch the branches and their respective commits from the upstream repository
git fetch upstream

#check out fork's local default branch
git checkout master

#merge changes from upstream default branch, upstream/master, into local default branch, without losing local changes
git merge upstream/master

#push local changes to forked repo
git push origin master
```

## upstream to master
```
git checkout master
git fetch upstream
git merge upstream/master
git push origin master #master to origin/master
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
# git pull origin master, OK but better use
git fetch origin
git merge origin/master
```

## remote `azure` branch to local master
```
# git pull <repo> <remote-branch>:<local-branch>
# git pull azure <remote-branch>, Ok but better use
git fetch azure <remote-branch>

git merge <remote-branch>    #merge to local master

git checkout <local-branch>  #merge to local branch
git merge <repo>/<remote-branch>
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
