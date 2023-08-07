# Datetime

## basic
```sh
$(date "+%F %H:%M:%S"); #datatime

$(date --date='+2 days' +%F); #current date +2 days in format yyyy-mm-dd
$(date -d@"$(( $(date +%s) + 2 * 86400 ))" +"%Y-%m-%d"); #stripped more basic version
```

## day of month
```sh
if [[ $(date +%d) == 1 ]]; then r=360; else r=30; fi
if [[ $(date +%d) == 1 && $(( $(date +%m)%2 )) == 1 ]]; then r=180; fi #month is odd
```

## example of scripts for `/bin/sh`
How to change scripts to work in sh

1. `numdays=$(($NDAYS-1));`
This line tries to subtract 1 from the value of `NDAYS`, but it seems that the shell is interpreting `$NDAYS` as a string rather than a number.
To fix this, you can use double parentheses for arithmetic expansion:
- Replace: `numdays=$(($NDAYS-1));`
- With: `numdays=$((NDAYS-1));`

2. `if [[ $(date +%d) == 10 ]]; then numdays=$((30*6-1)); fi;`
This is to check if the current day is the 10th day of the month.
However, the date format `+%d` returns the day of the month with leading zeros (e.g., `07` instead of `7`).
To fix this, you can use the `-eq` operator for integer comparison and remove the leading zeros:
- Replace: `if [[ $(date +%d) == 10 ]]; then numdays=$((30*6-1)); fi;`
- With: `if [ $(date +%e) -eq 10 ]; then numdays=$((30*6-1)); fi;`

3. `if [[ $(date +%d) == 10 && $(( $(date +%m)%2 )) == 1 ]]; then numdays=$((30*13-1)); fi;`
Here, we check if it's the 10th day of the month and if the current month is an odd number.
However, you should use `-eq` for integer comparison:
- Replace: `if [[ $(date +%d) == 10 && $(( $(date +%m)%2 )) == 1 ]]; then numdays=$((30*13-1)); fi;`
- With: `if [ $(date +%e) -eq 10 && $(( $(date +%m) % 2 )) -eq 1 ]; then numdays=$((30*13-1)); fi;`
