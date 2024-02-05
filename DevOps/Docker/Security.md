# Security

## check image packages/CVEs
install `syft` and `grype`
```sh
curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /usr/local/bin
curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh | sh -s -- -b /usr/local/bin
```

check packages
```sh
syft ubuntu:18.04
syft <repo>:1.0.0
```

check CVEs
```sh
grype ubuntu:18.04
grype <repo>:1.0.0
```
