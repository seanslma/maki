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

## $(variable)
${variable} is just a disambiguation mechanism, so `${var}text` can be different to `$vartext`.

## ${command}
$(command) is a modern synonym for `command` which stands for command substitution; it means run command and put its output here.
```
round_k() {
    echo $(( ($1 + 500) / 1000 * 1000 ))
}
x=600
y=$(round_k $x)
echo $y
```


