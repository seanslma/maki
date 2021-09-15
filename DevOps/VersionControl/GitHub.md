# GitHub

  * Collaborative Coding
  * Automation / CI & CD
  * Security including additional features for enterprise customers
  * Project Management
  
## Add PAT (Personal Access Token) 
GitHub account, go to Settings 
* => Developer Settings 
* => Personal Access Token 
* => Generate New Token (Give your password) 
* => Fill up the form 
* => Click Generate token 
* => Copy the generated Token
### linux
Configure the local GIT client with a username and email address
```bash
$ git config --global user.name "your_github_username"
$ git config --global user.email "your_github_email"
$ git config -l
#after first use cache token
#git config --global credential.helper cache #not good
git config credential.helper store 
#delete cache record if needed
git config --global --unset credential.helper
git config --system --unset credential.helper
#pull verify
git pull -v
```
### windows
Credential Manager from Control Panel 
* => Windows Credentials 
* => find git:https://github.com => Edit 
* => On Password replace with GitHub Personal Access Token

If you cannot find git:https://github.com 
* => Click on Add a generic credential 
* => Internet address will be git:https://github.com 
* => type in username and password (GitHub Personal Access Token)

### macos
launch app eychain access
* => In Keychain Access, search for github.com 
* => Find the internet password entry for github.com 
* => Edit or delete the entry accordingly

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

## one line add commit and push
  * creat a makefile in repo folder
  * add the lines to the file (tab not spaces)
```bash
 git:
  git add .
  git commit -m "$m"
  git push -u origin main
```
  * make git m="message"
