# Git

## create branch from another branch
```
#checkout branch to copy
git checkout dev

#create new branch
#git checkout -b dev-test [current_active_branch]
git checkout -b dev-test

#push changes in dev-test to remote
git push origin dev-test
```

## sync a fork
```
#fetch the branches and their respective commits from the upstream repository
git fetch upstream

#check out fork's local default branch
git checkout master

#merge changes from upstream default branch, upstream/master, into local default branch, without losing local changes
git merge upstream/master

#push local chnages to forked repo
git push origin master
```

## merge upstream repo into fork
```
#check out branch to merge to
git checkout branch-name

#pull the desired branch from the upstream repo
git pull https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git branch-name

#commit the merge

#push merge to GitHub repo
git push origin branch-name
```

## git tips
https://wikihub.berkeley.edu/display/drupal/Git+Tips#GitTips-Gitmessage:Yourbranchisaheadof'upstream/develop'byXXcommits

## GitHub Standard Fork & Pull Request Workflow
https://gist.github.com/Chaser324/ce0505fbed06b947d962

git example
https://forum.freecodecamp.org/t/push-a-new-local-branch-to-a-remote-git-repository-and-track-it-too/13222

## drop unstaged files
```
git checkout -- .
git checkout -- path-to-file #only one file
```

## drop commits not pushed
```
git reset --hard HEAD~3 #three commits
git reset --hard HEAD{1} #revert previous command
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
#push local chnages to forked repo (-f only needed the first time after rebased)
git push -f origin master
```

## commit changes
```
git add .
git commit
git push
```

## work example
```
git chechout master

#create a new branch
git checkout -b new-branch-name

#make changes and first commit
git add .
git commit -m "my first commit"
git push --set-upstream origin new-branch-name

#submit a pr
do it on github

#make another commit
git add .
git commit -m "my commit after pr review"
git push
```

## create/delete branch
```
#create and switch to
git branch new-branch
git checkout new-branch
#delete branch
git branch -d new-branch
```

## merge from upstream to master
```
git checkout master
git fetch upstream
git merge upstream/master
git push origin master
```

## clone repo to local folder
```
git clone https://github.com/usr/repo.git repo_name
```

## local folder to github repo
```
#initialize local directory as a git repo
git init -b main
#stage and commit all files in your project
git add . && git commit -m "initial commit"
#link to github
git remote add origin https://github.com/usr/repo.git
#push to github repo
git push -u origin main
```

## cherry pick
```
# start from an updated master
git checkout master
git pull
# create a copy of master and switch to it
git switch -c new-branch
# get commit from other branch using it's sha
git cherry-pick <sha>
```
