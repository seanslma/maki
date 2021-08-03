# bash

## Ch1 intro

### add dir to PATH variable
``` bash
export PATH="$PATH:~/script"
```
  
### change script file permission
``` bash
chmod u+x script1.sh #change
ls -l script1.sh #check
```
  
### run by special shell
``` bash
rbash script_name.sh
sh script_name.sh
bash -x script_name.sh
```
  
The specified shell will start as a subshell of your current shell and execute the script. This is done when you want the script to start up with specific options or under specific conditions which are not specified in the script.

If you don't want to start a new shell but execute the script in the current shell, you source it:
``` bash
source script_name.sh
```

## Ch2 write and debug
 
Entire script: traces of each command plus its arguments are printed to standard before execution:
``` bash
bash -x script1.sh
```

Debugging part(s) of the script, they can be added between 
``` bash
set -x #activate debugging from here
w
set +x #stop debugging from here
```
  
Other options
``` bash
set -f #disable file name generation using metacharacters
set -v #print shell input lines as they are read
set -x #print command traces before executing command
```

They can also be added to the first line:
``` bash
#!/bin/bash -xv
```
  
## Ch3 bash env

