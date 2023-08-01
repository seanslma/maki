# Alias

Bash alias does not directly accept parameters. We have to create a function.

## create a permanent alias
```sh
vi ~/.bash_aliases               #edit
alias my_alias='sudo -- sh -c "/root/bin/chk_disk && dnf update"' #add alias
source ~/.bash_aliases           #active alias
```
