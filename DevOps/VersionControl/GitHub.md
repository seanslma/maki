# GitHub

  * Collaborative Coding
  * Automation / CI & CD
  * Security including additional features for enterprise customers
  * Project Management
  
Features:
- branch protection rules
  
## PR review
https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/reviewing-proposed-changes-in-a-pull-request
```
#search for review request
review-requested:[USERNAME]

```

## Add PAT (Personal Access Token) 
GitHub account, go to Settings 
* => Developer Settings 
* => Personal Access Token 
* => Generate New Token (Give your password) 
* => Fill up the form 
* => Click Generate token 
* => Copy the generated Token
* 
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
  ```bash
   git:
    git add .
    git commit -m "$m"
    git push -u origin main
  ```
- make git m="message"

## delete release
- Delete the release from the Github UI
- Delete local tag if the release failed: `git tag -d 0.1.0`
- Delete the remote tag from local master: `git push --delete upstream 0.1.0`
