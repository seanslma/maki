# Docker

## x509: certificate signed by unknown authority
After add the tls.crt to the path `/etc/ssl/certs` or `/usr/local/share/ca-certificates` and run `update-ca-certificates`.
The command `curl -kv https://my.example.com` shows `SSL certificate verify ok` but docker build shows `x509: certificate signed by unknown authority`.


solution: https://stackoverflow.com/questions/50768317/docker-pull-certificate-signed-by-unknown-authority

After updating OS certificates, we typically need to restart the docker service to get it to detect that change. 
This is usually done with:
```sh
sudo systemctl restart docker
```
or for non-systemd environments:
```sh
sudo service docker restart
```
