# Net cmd

## find a free TCP port
```bash
ss -ltn
```
-l: listening ports only\
-t: TCP ports only\
-n: See port numbers, instead of port names like "http" or "epmap"

## check what uses a port
```bash
sudo lsof -i tcp:8080
sudo kill -9 PID #kill the process based on PID
```
