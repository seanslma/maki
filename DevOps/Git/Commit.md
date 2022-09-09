# Commit 

## multi-line comment
```
git commit -m "Head line" -m " * First content line" -m " * Second content line"
```
## drop commits not pushed
- `HEAD~1` the first parent of the commit
- `HEAD^`means something different, on windows cane be escaped as `HEAD^^`
```
git reset --hard HEAD~3 #delete last three commits
git reset --hard HEAD~1 #delete previous commit
git reset --soft HEAD~1 #revert previous commit to staging area
```

## revert last commit pushed 
```
git revert <commit-hash>
git push
```

## delete last commit pushed
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
