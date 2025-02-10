# Git Config

Git will search the config settings from  `local`, `global` to `system`.

## local
Local config file can be found in the repo's .git directory: `.git/config`.
```
```

## global
Global config file locates in user's home directory:
- unix: `~/.gitconfig`
- windows: `C:/Users/<usr>/.gitconfig`
```sh
git config --global core.editor "vim"
git config --global --unset core.excludesfile #remove the setting
```

Avoid ssl error
```sh
[http]
	sslbackend = schannel
```

Use windows Credentials Manager,
`git config --global credential.helper manager`

Note that credential-manager-core was renamed to credential-manager.
```sh
[credential "https://user.github.com"]
	provider = github
[credential]
	helper = manager
```

## system
System level config file lives in the system root path:
- unix: `$(prefix)/etc/gitconfig`
- windows: `C:\ProgramData\Git\config`
```
```

## config git editor
```sh
#error: cannot spawn more: No such file or directory
git config --global core.pager ""
```

## create git alias
```sh
git config --global alias.a '! git pull && git add . && git commit -m "d" && git push'
git config --global --unset alias.a
```
open `.gitconfig` and add
```sh
[alias]
	a = ! git fetch && git merge origin/master && git add . && git commit -m sdoc && git push 
```

```sh
a = "!sh -c \"git pull && git add . && if [ -z \\\"$1\\\" ]; then git commit -m \\\"update\\\"; else git commit -m \\\"$1\\\"; fi && git push\""
```
Here is an example to use it: `git a "My first commit"`.

## user config example
```
# This is Git's per-user configuration file.
[core]
	editor = \"C:\\Users\\<user>\\AppData\\Local\\Programs\\Microsoft VS Code\\bin\\code\" --wait
[http]
	sslbackend = schannel 
[user]
	name = <user>
	email = my.email@example.com   
[alias]
	a = ! git fetch && git merge origin/master && git add . && git commit -m sdoc && git push 
        m = ! git checkout master && git pull     
[credential "https://repo.example.com"]
	provider = github
[credential]
	helper = manager
[credential "https://dev.azure.com"]
	useHttpPath = true
```
