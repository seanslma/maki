# Commit

## multi-line comment
```sh
git commit -m "Head line" -m " * First content line" -m " * Second content line"
```

## drop commits not pushed
- `HEAD~1` the first parent of the commit
- `HEAD^`means something different, on windows cane be escaped as `HEAD^^`
```sh
git reset --soft HEAD~1 #revert previous commit to staging area
git reset --hard HEAD~1 #DELETE previous commit
git reset --hard HEAD~3 #DELETE last three commits
```

## take commits not pushed to new branch
```sh
git checkout -b <new-branch>
git checkout <master>
git reset --hard HEAD~<n>    #remove last n commits
```

## revert last commit pushed
careful, the changes will be dropped!
```sh
git revert <commit-hash> #will keep history
git push origin <your-branch>
```

## delete last commit pushed
```sh
git reset --hard HEAD^
git push origin -f
```

## diff between two commits
```sh
git log -5 --oneline                          #show commits
git diff <sha-new> <sha-old> > my.patch       #diff between new and old commits
git checkout -b <new-branch>                  #make a copy from the new commit
git apply my.patch                            #apply diff to copied branch
```

## cherry pick
```sh
git checkout master       #start from an updated master
git pull
git switch -c new-branch  #create a copy of master and switch to it
git cherry-pick <sha>     #get commit from other branch using it's sha
```

## add commit to john's pr
```sh
git clone https://github.com/my/repo.git
git remote add john https://github.com/john/repo.git
git fetch john
git checkout -b john-main john/main #git checkout -b john-feature john/feature
git commit -am "my commit"
git push john HEAD:main #git push john john-feature:feature
```

## merge last n-1 commits
```sh
git rebase -i HEAD~n
#change "pick" to "squash" except the first one and save the changes
#update the new commit message and save
git push -f
```

## merge all the commits from a specific commit
squash all the commits from a specific commit (sha:xyz) up to the latest commit:
```sh
# Leave first commit as pick, for all the subsequent commits, change pick to squash
git rebase -i <sha:xyz>^ # merge commit from xyz (inclusive) to latest
git rebase -i xyz~2      # 2 commit from sha:xyz (exclusive)
```
