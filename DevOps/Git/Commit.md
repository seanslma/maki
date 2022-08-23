# Commit 

## multi-line comment
```
git commit -m "Head line" -m " * First content line" -m " * Second content line"
```
## drop commits not pushed
```
git reset --hard HEAD~3 #three commits
git reset --hard HEAD~1 #revert previous commit
```

## delete last commit
```
git reset --hard HEAD^
git push origin -f
```

## cherry pick
```
# start from an updated master
git checkout master
git pull
# create a copy of master and switch to it
git switch -c new-branch
# get commit from other branch using it's sha
git cherry-pick <sha>
```
