# Logs

## Find out which log file the syslogd process is using
```sh
sudo lsof -p $(pgrep syslog) | grep log$
```

## Show most recent output as it goes into the syslog
```sh
tail -f /var/log/syslog
```
