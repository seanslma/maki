# Monitor

## Resource usage using `krew` plugin manager and `resource-capacity` plugin
https://www.middlewareinventory.com/blog/cpu-memory-usage-nodes-k8s/

### install `krew`
https://krew.sigs.k8s.io/docs/user-guide/setup/install/
Make sure `git` is installed and run
```
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)
```
Add $HOME/.krew/bin directory to PATH by appending the folowing line to `.bashrc`:
```
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
```

The restart the shell and check the version:
```
kubectl krew version
```
