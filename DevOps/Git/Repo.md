# Repo

## create a repo
local folder to github repo
```sh
#create a github repo first, do not add readme etc
git init && git checkout -b main            #initialize local directory as a git repo, old git
git init -b main                            #new git
git add . && git commit -m "initial commit" #stage and commit all files in your project
git remote add origin https://github.com/usr/repo.git  #link to github
git push -u origin main                     #push to github repo
```

## clone a repo
```sh
fork repo to sma
git clone https://github.com/<user>/repo.git
cd repo
git remote add upstream https://github.com/<upstream>/repo.git
git remote -v
pip install --no-deps --editable .
# wrong? delete it: pip uninstall repo
code .
```
