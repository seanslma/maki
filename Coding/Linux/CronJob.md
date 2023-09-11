# CronJob

## env
`cron` or non-interactive shells may have a different environment setup compared to the interactive shell.
If a command is not found, it's better to include the command path to the `PATH`. For example, to run `kubectl` we should set
```sh
export PATH=/usr/local/bin/kubectl:$PATH
export KUBECONFIG=/path/to/.config/.kube/kubeconfig
```

## create a cronjob
`erontab -e` and add:
```sh
30 12 * * * /home/<user-name>/my.sh >> /mnt/c/tst/my.log 2>&1
```

## run every 5 minutes but start from 0:02 not 0:00
```sh
#option 1
2-59/5 * * * *
#option 2 (always works)
2,7,12,17,22,27,32,37,42,47,52,57 * * * *
```
