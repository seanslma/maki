<!-- {% raw %} -->
# Git

- **Rebase** will change history and best to use it in private branch.
- **Merge** will not change history and is preferred to rebase in most cases.

## terms
- `Untracked changes` are not in Git
- `Unstaged changes` are in Git but not marked for commit
- `Staged changes` are in Git and marked for commit

## update
```sh
sudo apt update
sudo apt install git
git --version
```

## untrack file
```sh
#keep file on server
git update-index --assume-unchanged <file>
#delete file from server
git rm --cached <file>
#delete folder from server
git rm -r --cached path_to_folder/
```

## git tips
https://wikihub.berkeley.edu/display/drupal/Git+Tips#GitTips-Gitmessage:Yourbranchisaheadof'upstream/develop'byXXcommits

## GitHub Standard Fork & Pull Request Workflow
https://gist.github.com/Chaser324/ce0505fbed06b947d962

git example
https://forum.freecodecamp.org/t/push-a-new-local-branch-to-a-remote-git-repository-and-track-it-too/13222

## commit changes
```
git add .
git commit
git push
```

## work example
```
git checkout master

#create a new branch
git checkout -b new-branch-name

#make changes and first commit
git add .
git commit -m "my first commit"
git push --set-upstream origin new-branch-name

#submit a pr
do it on github

#make another commit
git add .
git commit -m "my commit after pr review"
git push
```

<!-- {% endraw %} -->
