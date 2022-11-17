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

## take commits not pushed to new branch
```
git checkout -b <new-branch>
git checkout <master>
git reset --hard HEAD~<n>    #remove last n commits
```

## revert last commit pushed 
```
git revert <commit-hash> #will keep history
git push
```

## delete last commit pushed
```
git reset --hard HEAD^
git push origin -f
```

## diff between two commits
```
git log -5 --oneline                          #show commits
git diff <sha-new> <sha-old> > my.patch       #diff between new and old commits
git checkout -b <new-branch> <commit-sha-old> #make a copy from old commit
git apply my.patch                            #apply diff to copied branch
```

## cherry pick
```
git checkout master       #start from an updated master
git pull
git switch -c new-branch  #create a copy of master and switch to it
git cherry-pick <sha>     #get commit from other branch using it's sha
```
