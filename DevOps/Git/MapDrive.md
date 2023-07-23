# Network Drive

## Tips
Stop tracking the file but not delete it from your system use:
```sh
git rm --cached filename
```
Tracking the file again:
```sh
git add filename
```

To untrack every file that is now in your .gitignore:
- commit any outstanding code changes
- removes any changed files from the index: `git rm -r --cached .`
- then just run: `git add .`
- commit it: `git commit -m ".gitignore is now working"`


## Using Git on a Windows Network Drive
- move to the soon to be git repository `cd /D "Y:\dev\MyProject"`
- create an empty git repository `git init --bare`
- clone a local reporitory (this will copy to local) `cd /D "C:\dev\MyProject & git clone file:"//Y:\dev"`

already have a local git repository
```sh
cd "C:\dev\MyProject
git remote add origin file:"//Y:\dev\MyProject"
git push origin master
```

Fetch master branch from Windows Network Drive
- move to the soon to be git repository `cd "C:\dev\MyProject"`
- reate an empty git repository `git init`
- fetch master branch from origin `$ git pull "Y:\dev\MyProject" "master"`
