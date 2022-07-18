# Monitor

## install `krew`
`krew` is the plugin manager:
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

## resource capacity
Resource usage using `resource-capacity` plugin:
https://www.middlewareinventory.com/blog/cpu-memory-usage-nodes-k8s/

### Install the plugin
```
kubectl krew install resource-capacity
kubectl krew list #list all installed plugins
```

### Get node cpu and memory usage
```
kubectl resource-capacity
kubectl resource-capacity --sort cpu.limit
kubectl resource-capacity --sort cpu.util --util                     #include utilization
kubectl resource-capacity --sort cpu.util --util --pods              #pod level report
kubectl resource-capacity --sort cpu.util --util --pods --containers #container level report
```

### Get namespace cpu and memory usage
```
kubectl resource-capacity -n kube-system -p -c
kubectl resource-capacity -n kube-system --pods --containers
```

### Sort flags
```
cpu.util, cpu.request, cpu.limit, mem.util, mem.request, mem.limit, name
```

### `--node-labels` flag
```
kubectl resource-capacity --namespace-labels <namespace-label>
kubectl resource-capacity --node-labels <node-label>
kubectl resource-capacity --pod-labels <pod-label>
```

### Output formats:
- yaml
- json
- table ( default)
```
kubectl resource-capacity -o yaml
```
