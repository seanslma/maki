# Git Issue

## No output from `git log` in PowerShell
git command in conda env not show anything

Under PowerShell, check the linked exe to git command:
```
Get-Command git #will show the source path of git.exe
```
Solution:
- Run the command in terminal and it will show the error, e.g., msys-2.0.exe not found 
- This means the exe in the conda env is missing or corrupted
- upgrading `git` in the conda-env fixed the issue

## Procedure Entry Point Could Not Be Located in the Dynamic Link Library
- dll not exists
- dll path not included
- dll corrupted

## No PR in github after push
reset upstream to remote upstream/master
```
git branch --set-upstream-to upstream/master
git push upstream HEAD
```

## fatal: repository not found
- did not authenticate
- password has changed
- not a collaborator
- incorrect case or a word misspelled
- repo has been deleted

## fatal: refusing to merge unrelated histories
```
git reset HEAD~ #unstage last commit if not init commit, else
git update-ref -d HEAD && git rm --cached -r .
git stash       #stash changes
git pull        #fetch and merge remote branch
git pop         #unstash changes
```

## fatal: ambiguous argument 'upstream/master': unknown revision or path not in the working tree
```
git fetch upstream
git checkout master
git reset --hard upstream/master  
git push origin master --force
git branch --set-upstream-to upstream/master
```
