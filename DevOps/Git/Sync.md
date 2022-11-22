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

## local folder to github repo
```
#create a github repo first, do not add readme etc
git init && git checkout -b main            #initialize local directory as a git repo, old git
git init -b main                            #new git
git add . && git commit -m "initial commit" #stage and commit all files in your project
git remote add origin https://github.com/usr/repo.git  #link to github
git push -u origin main                     #push to github repo
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
