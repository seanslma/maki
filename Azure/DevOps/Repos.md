#  Azure Repos

## work steps
- clone repo to local machine: `git clone https://dev.azure.com/{organization}/{project}/_git/{repo-name}`
- create a new branch: `git checkout -b your-feature-branch`
- commit changes: `git add . && git commit -m "test" && git push origin your-feature-branch`
- create a pr and merge to main
- sync local branch: `git checkout main && git pull origin main`
- delete local branch: `git branch -d your-feature-branch`
- delete remote branch: `git push origin --delete your-feature-branch`

## git clone
Error
```
fatal: Cannot determine the organization name for this 'dev.azure.com' remote URL.
Ensure the `credential.useHttpPath` configuration value is set, or
set the organization name as the user in the remote URL '{org}@dev.azure.com'.
```

Solution: 
setting can be specific to Azure Repos
```sh
git config --global credential.https://dev.azure.com.useHttpPath true
```

## git clone mirror
import repot from github to azure devops
- also rename master to main.
- pull requests cann't be importted to ado

```sh
git clone --mirror https://my.github.com/<org>/<my-repo>.git
cd <my-repo>.git
git branch -m master main
git remote add ado https://<org>@dev.azure.com/<org>/<proj>/_git/<new-repo>
git push ado --all  # "refs/heads/*:refs/heads/*"
git push ado --tags # "refs/tags/*:refs/tags/*"

# git push --mirror ado # do not use it - pull will be rejected
```
