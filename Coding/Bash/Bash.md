# bash

book: bash cookbook

review and note ch1-5: 1-181

https://linuxize.com/post/bash-case-statement/

## Ch1 intro

### add dir to PATH variable
```sh
export PATH="$PATH:~/script"
```

### change script file permission
```
chmod u+x script1.sh #change
ls -l script1.sh #check
```

### run by special shell
```sh
rbash script_name.sh
sh script_name.sh
bash -x script_name.sh
```

The specified shell will start as a subshell of your current shell and execute the script. This is done when you want the script to start up with specific options or under specific conditions which are not specified in the script.

If you don't want to start a new shell but execute the script in the current shell, you source it:
```sh
source script_name.sh
```

## Ch2 write and debug

Entire script: traces of each command plus its arguments are printed to standard before execution:
```sh
bash -x script1.sh
```

Debugging part(s) of the script, they can be added between
```sh
set -x #activate debugging from here
w
set +x #stop debugging from here
```

Other options
```sh
set -f #disable file name generation using metacharacters
set -v #print shell input lines as they are read
set -x #print command traces before executing command
```

They can also be added to the first line:
```sh
#!/bin/bash -xv
```

## Ch3 bash env
