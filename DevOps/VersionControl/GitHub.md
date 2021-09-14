# GitHub

  * Collaborative Coding
  * Automation / CI & CD
  * Security including additional features for enterprise customers
  * Project Management

## Sync proj
```bash
#clone project
git clone https://github.com/usr/proj.git
cd repo
#list forked repo
git remote -v
#sync from upstream
git fetch upstream
#checkout to master
git checkout master
git merge upstream/master
```
## Add proj to GitHub
```bash
#move to proj folder
cd proj-folder
#init local dir as git repo
git init -b main
#create proj repo on github
gh repo create proj-name
#pull changes from new github repo
git pull --set-upstream origin main
#stage, commit, and push all files local proj
git add . && git commit -m "initial commit" && git push
```
