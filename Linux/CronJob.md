# CronJob

## create a cronjob
`erontab -e` and add:
```
30 12 * * * /home/<user-name>/my.sh >> /mnt/c/tst/my.log 2>&1
```
