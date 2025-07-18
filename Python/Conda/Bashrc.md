# Bashrc

## auto activate env
run `mamba shell init` to add code in `.bashrc`.
after that add `mamba activate my-env`

## conda env name not show in terminal
You have custom `PS1` definitions that are being applied after your `mamba activate my-env` command.

This custom PS1 is being applied after `mamba activate my-env`, effectively overwriting the prompt modification that Mamba attempts to do.

Move custom PS1 definitions before `conda/mamba initialize`.

## show git branch name in color
```sh
# Show git branch name
force_color_prompt=yes
color_prompt=yes
parse_git_branch() {
   git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}
if [ "$color_prompt" = yes ]; then
   PS1='${debian_chroot:+($debian_chroot)}\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[01;31m\]$(parse_git_branch)\[\033[00m\]\$ '
else
   PS1='${debian_chroot:+($debian_chroot)}\u@\h:\w$(parse_git_branch)\$ '
fi
unset color_prompt force_color_prompt
```
