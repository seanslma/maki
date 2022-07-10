# Bracket

https://stackoverflow.com/questions/2188199/how-to-use-double-or-single-brackets-parentheses-curly-braces

## Test construct  
```
$ VARIABLE=x
$ if [ $VARIABLE == x ] ; then echo yes ; else echo no ; fi
yes
```

## Extended test construct 
```
$ VARIABLE=x
$ if [[ $VARIABLE == 1 ]] ; then echo yes ; else echo no ; fi
no
```

```
$ echo Variable: ${VARIABLE}1
Variable: x1

$ { date; top -b -n1 | head ; } >logfile 
```

## Double Parentheses: arithmetic operations
```
(( i = 78 ))  
i = $(( 20 + 5 ))   
(( i++ ))
```
