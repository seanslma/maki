# Datetime

## basic
```
$(date "+%F %H:%M:%S"); #datatime

$(date --date='+2 days' +%F); #current date +2 days in format yyyy-mm-dd
$(date -d@"$(( $(date +%s) + 2 * 86400 ))" +"%Y-%m-%d"); #stripped more basic version
```

## day of month
```
if [[ $(date +%d) == 15 ]]; then r=365; else r=30; fi
```
