# SSH

## SSH key pair
The key pair consists of a public and a private key. The public key is kept on the server, while the private key is kept on your computer. When you connect via SSH, a trust relationship between your computer and the server is established using the key pair. If any of the keys is missing or there is a discrepancy between the keys, a connection cannot be established.

## ssh-keygen
- The algorithm is selected using the `-t` option [rsa, dsa, ecdsa, ed25519]
- The key size using the `-b` option [2048, 4096]
- The filename is defined using the `-f` option
```sh
# create SSH key pair via Linux
ssh-keygen -b 2048 -f id123_ssh_key
# validate SSH key pair via Linux
ssh-keygen -lf id123_ssh_key
```
