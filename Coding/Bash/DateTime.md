# Datetime

## basic
```
$(date "+%F %H:%M:%S"); #datatime

$(date --date='+2 days' +%F); #current date +2 days in format yyyy-mm-dd
$(date -d@"$(( $(date +%s) + 2 * 86400 ))" +"%Y-%m-%d"); #stripped more basic version
```

## day of month
```
if [[ $(date +%d) == 1 ]]; then r=360; else r=30; fi
if [[ $(date +%d) == 1 && $(( $(date +%m)%2 )) == 1 ]]; then r=180; fi #month is odd
```
