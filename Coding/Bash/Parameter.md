# Parameter
Cheat sheet: https://devhints.io/bash

## Special parameter
```sh
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

## Default value
```sh
${var:-x} #default value is x
```

## shift one parameter
```sh
while (( $# > 0 )); do
    case $1 in
        [0-9]*) LEN=$1
        ;;
        -c) shift; CHAR=${1:--}
        ;;
        *) printf 'usage: %s [-c X] [#]\n' ${0##*/} >&2 #strip off leading path part
        exit 2
        ;;
    esac
    shift #drop 2st param so $# to be one smaller
done
```
