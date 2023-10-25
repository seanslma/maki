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

## check network connection in docker pod without `curl`, `ping` etc
can only work under bash
```sh
host=1.2.3.4
port=10
echo >/dev/tcp/${host}/${port}
(echo >/dev/tcp/${host}/${port}) &>/dev/null && echo "open" || echo "closed"
```

## connection refused
https://stackoverflow.com/questions/2333400/what-can-be-the-reasons-of-connection-refused-errors

reasons:
- The port is not open on the destination machine.
- The port is open on the destination machine, but its backlog of pending connections is full.
- A firewall between the client and server is blocking access (also check local firewalls).

After checking for firewalls and that the port is open, use telnet to connect to the ip/port to test connectivity. This removes any potential issues from your application.
