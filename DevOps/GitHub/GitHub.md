# GitHub

  * Collaborative Coding
  * Automation / CI & CD
  * Security including additional features for enterprise customers
  * Project Management

Features:
- branch protection rules

## Github vs Gitlab
https://automateinfra.com/2023/05/05/gitlab-vs-github

## PR review
https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request
```
#search for review request
review-requested:[USERNAME]
```

## Sync proj
```sh
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
```sh
cd proj-folder #move to proj folder
git init -b main #init local dir as git repo
gh repo create proj-name #create proj repo on github
git pull --set-upstream origin main #pull changes from new github repo
git add . && git commit -m "initial commit" && git push #stage, commit, and push all files local proj

#old git version
git init
git add . && git commit -m "initial commit"
git remote add origin https://github.com/yourusername/your-repo-name.git
git pull origin master
git push origin master
```

## one line add commit and push
- creat a makefile in repo folder
- add the lines to the file (tab not spaces)
  ```sh
   git:
    git add .
    git commit -m "$m"
    git push -u origin main
  ```
- make git m="message"

## pr not shown
open the link to create a pr:
https://xyz.github.com/usr/<repo-name>/pull/new/<branch-name>

## delete release
- Delete the release from the Github UI
- Delete local tag if the release failed: `git tag -d 0.1.0`
- Delete the remote tag from local master: `git push --delete upstream 0.1.0`
