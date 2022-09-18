# Parameter
Cheat sheet: https://devhints.io/bash

## Special parameter
```
$#  #number of arguments
$@  #array-like construct of all positional parameters, {$1, $2, ...}
$*  #IFS expansion of all positional parameters, $1 $2, ...
$0	#filename of shell script
$1  #positional parameters, 1, 2, ...
$$	#pid of shell
$!	#pid of last background task
$?	#exit status of most recent foreground pipeline (last command)
$_	#last argument of previous command
```
