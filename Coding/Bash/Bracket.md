# Bracket

https://stackoverflow.com/questions/2188199/how-to-use-double-or-single-brackets-parentheses-curly-braces

## Test construct
`[` is just a different name for the `test` command, and `]` is required
as the last parameter, for readability and aesthetic reasons.
```
x=2
v=x
if [ $v == x ] ; then echo yes ; else echo no ; fi
# if test $v == x ; then echo yes ; else echo no ; fi
yes
```

## Extended test construct
```
v=x
if [[ $v == 1 ]] ; then echo yes ; else echo no ; fi
no
```

- Using the [[ ... ]] test construct, rather than [ ... ] can prevent many logic errors in scripts
  - the &&, ||, <, and > operators work within a [[ ]] test, despite giving an error within a [ ] construct
- Arithmetic evaluation of octal / hexadecimal constants takes place automatically within a [[ ... ]] construct


## Double Parentheses: arithmetic operations
```
(( i = 78 ))
i = $(( 20 + 5 ))
(( i++ ))
```

## ${var}
${var} is just a disambiguation mechanism, so `${var}text` can be different to `$vartext`.

```
echo Variable: ${var}1
var: x1

{ date; top -b -n1 | head ; } >logfile
```

## $(command)
$(command) is a modern synonym for `command` which stands for command substitution; it means run command and put its output here.
```
round_k() {
    echo $(( ($1 + 500) / 1000 * 1000 ))
}
x=600
y=$(round_k $x)
echo $y
```


