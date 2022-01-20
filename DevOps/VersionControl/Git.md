# Git

## GitHub Standard Fork & Pull Request Workflow
https://gist.github.com/Chaser324/ce0505fbed06b947d962

## create/delete branch
```
#create and switch to
git branch new-branch
git checkout new-branch
#delete branch
git branch -d new-branch
```

## commit changes
```
git add .
git commit
git push
```

## merge from upstream to master
```
git checkout master
git fetch upstream
git merge upstream/master
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
git remote add origin https://github.com/seanslma/aks.git
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
