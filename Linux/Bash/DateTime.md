# Datetime

## basic
```
$(date --date='+2 days' +%F); #current date +2 days in format yyyy-mm-dd
$(date -d@"$(( $(date +%s) + 2 * 86400 ))" +"%Y-%m-%d"); #stripped more basic version

$(date "+%F %H:%M:%S"); #datatime
```
