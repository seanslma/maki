# Auth

## update pat
```sh
gh auth login #then input the pat
# check status: https://www.githubstatus.com/
```

## check pat
```sh
curl -H "Authorization: token <my-pat>" https://api.github.com/user
```

## Error: {'message': 'Bad credentials'}
The PAT expired and should be updated.

## Add PAT (Personal Access Token)
GitHub account, go to Settings
* => Developer Settings
* => Personal Access Token
* => Generate New Token (Give your password)
* => Fill up the form
* => Click Generate token
* => Copy the generated Token

### clone with PAT
```
git clone https://username:ghp_MY-PERSONAL-ACCESS-TOKEN@github.com/username/my-repo.git
```

### linux
Configure the local GIT client with a username and email address
```sh
$ git config --global user.name "your_github_username"
$ git config --global user.email "your_github_email"
$ git config -l
#after first use cache token
#git config --global credential.helper cache #not good
git config credential.helper store
#delete cache record if needed
git config --global --unset credential.helper
git config --system --unset credential.helper
#pull verify
git pull -v
```
### windows
Credential Manager from Control Panel
* => Windows Credentials
* => find git:https://github.com => Edit
* => On Password replace with GitHub Personal Access Token

If you cannot find git:https://github.com
* => Click on Add a generic credential
* => Internet address will be git:https://github.com
* => type in username and password (GitHub Personal Access Token)

### macos
launch app eychain access
* => In Keychain Access, search for github.com
* => Find the internet password entry for github.com
* => Edit or delete the entry accordingly

## .gitconfig
Configure Git to use the GitHub CLI (gh) as the credential helper.
```
[credential "https://github.com"]
	helper =
	helper = !/usr/bin/gh auth git-credential
[credential "https://gist.github.com"]
	helper =
	helper = !/usr/bin/gh auth git-credential
```

check the credentials
```
gh auth status
gh auth status --show-token
```
