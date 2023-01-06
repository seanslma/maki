# Docker

## Python mamba workaround
```
# Workaround for mamba SSL issue https://github.com/mamba-org/mamba/issues/628
ENV REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```

## Python conda ssl config
```
# SSL configuration for httpx https://www.python-httpx.org/compatibility/#ssl-configuration
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt
ENV MINIFORGE_ROOT=/home/user/miniforge/
```
