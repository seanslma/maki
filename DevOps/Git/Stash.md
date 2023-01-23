# Stash
Save uncommitted changes (both staged and unstaged) for later use, and then revert them from working copy. 

## include new files in stash
```
git add .
git stash --staged -m "stash-name"
```

## all commands
```
git stash list                 #list all stashes

git stash push -m "stash-name" #save a stash with a name
git stash pop stash@{n}        #apply and remove from the stack

git stash apply stash@{n}      #apply and keep in the stack
git stash apply stash-name     #apply by name
git stash apply n              #apply stash@{n}

git stash drop <stash-id>      #remove one stash
git stash clear                #remove all stashes
```


