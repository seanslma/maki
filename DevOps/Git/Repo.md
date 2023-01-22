# Repo

## create a new repo
local folder to github repo
```
#create a github repo first, do not add readme etc
git init && git checkout -b main            #initialize local directory as a git repo, old git
git init -b main                            #new git
git add . && git commit -m "initial commit" #stage and commit all files in your project
git remote add origin https://github.com/usr/repo.git  #link to github
git push -u origin main                     #push to github repo
```
```
