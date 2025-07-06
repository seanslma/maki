# Terminal

## troubleshoot terminal launch failures
https://code.visualstudio.com/docs/supporting/troubleshoot-terminal-launch

## shell integration
https://code.visualstudio.com/docs/terminal/shell-integration

Manual installation (add to .bashrc):
```
[[ "$TERM_PROGRAM" == "vscode" ]] && . "$(code --locate-shell-integration-path bash)"
```

Better to copy the `bash` output to a shell script file to enhance loading performance.
```
# Output the executable's path first:
code --locate-shell-integration-path bash

# Add the result of the above to the source statement:
[[ "$TERM_PROGRAM" == "vscode" ]] && . "/path/to/shell/integration/script.sh"
```

## show branch in color in ubuntu bash
https://askubuntu.com/questions/730754/how-do-i-show-the-git-branch-with-colours-in-bash-prompt
- Add these lines in your `~/.bashrc` file
- Reload the `.bashrc` file with this command: `source ~/.bashrc`
```
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

## git bash terminal auto activate conda env
https://github.com/microsoft/vscode-python/discussions/20800
- where the command is from? not answered
- the path for the `activate` command is in windows path format, not correct
- but can disable conda env auto activation (not good, env is base): `"python.terminal.activateEnvironment": false`
