# Common

## GitHub Standard Fork & Pull Request Workflow
https://gist.github.com/Chaser324/ce0505fbed06b947d962

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
