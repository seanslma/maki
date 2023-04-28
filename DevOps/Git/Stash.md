# Stash
Save uncommitted changes (both staged and unstaged) for later use, and then revert them from working copy. 

When run `git stash`, will stash any changes that haven't been committed, reverting the branch back to the latest commit. If switch branches and run `git stash pop`, Git will then apply the changes to the new branch.

## include new files in stash
```
git add .
git stash --staged -m "stash-name"
```

## save and pop
```
git stash list                 #list all stashes
git stash push -m "stash-name" #save a stash with a name
git stash pop stash@{n}        #apply and remove from the stack
```

## apply only
```
git stash apply stash@{n}      #apply and keep in the stack
git stash apply stash-name     #apply by name
git stash apply n              #apply stash@{n}
```

## remove stash
```
git stash drop <stash-id>      #remove one stash
git stash clear                #remove all stashes
```


## untracked files
```
git stash -u #--include-untracked stash untracked files
git stash -a #--all stash untracked files and ignored files
```

## error: unknown switch `e`
Curly braces have special meaning in PowerShell. 
```
git stash pop 'stash@{0}'
```
