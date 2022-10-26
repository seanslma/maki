# Monitor

## top
Press "1" in the `top` command to show individual CPU statistics.

## vmstat
https://phoenixnap.com/kb/vmstat-command#:~:text=The%20vmstat%20command%20(short%20for,by%20specifying%20a%20sampling%20period.
```
vmstat [options][delay [count]]
vmstat 1   #output every one second
vmstat 1 5 #output every one second till 5 records
```

## strace
checks filesystem attributes
```
strace -c -- /bin/sh -c 'time  (let SUM=0; for i in $(seq 1 1000) ; do SUM+=$i ; stat / > /dev/null; done)'
```
