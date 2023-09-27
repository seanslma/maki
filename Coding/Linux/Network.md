# Network

## find a free TCP port
```sh
ss -ltn
```
-l: listening ports only\
-t: TCP ports only\
-n: See port numbers, instead of port names like "http" or "epmap"

## check what uses a port
```sh
sudo lsof -i tcp:8080
sudo kill -9 PID #kill the process based on PID
```

## nslookup
NSLOOKUP stands for "Name Server Lookup," used to query the Domain Name System (DNS) to obtain information about domain names, IP addresses, and other DNS records.

`nslookup www.example.com` will return the domain name and ip address.


## dig
used to find the domain name of provided ip address
```sh
dig -x 10.20.30.40
```
