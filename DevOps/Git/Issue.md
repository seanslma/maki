# Git Issue

## fatal: repository not found
- did not authenticate
- password has changed
- not a collaborator
- incorrect case or a word misspelled
- repo has been deleted

## fatal: ambiguous argument 'upstream/master': unknown revision or path not in the working tree
```
git fetch upstream
git checkout master
git reset --hard upstream/master  
git push origin master --force
git branch --set-upstream-to upstream/master
```
