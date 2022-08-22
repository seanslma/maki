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
```
git config --global core.editor "vim"
git config --global --unset core.excludesfile #remove the setting
```

Avoid ssl error
```
[http]
	sslbackend = schannel 
```

Use windows Credentials Manager,
`git config --global credential.helper manager-core`
```
[credential]
	helper = manager-core
```

## system
System level config file lives in the system root path: 
- unix: `$(prefix)/etc/gitconfig` 
- windows: `C:\ProgramData\Git\config`
```
```

## config git editor
```
#error: cannot spawn more: No such file or directory
git config --global core.pager ""
```
