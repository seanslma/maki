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
```
30 12 * * * /home/<user-name>/my.sh >> /mnt/c/tst/my.log 2>&1
```
