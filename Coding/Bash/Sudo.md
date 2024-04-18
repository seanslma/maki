# Sudo

## sudo with echo
`sudo echo 7 > /proc/fs/cifs/cifsFYI)`
- only the echo command runs with elevated privileges due to the sudo prefix
- the file redirection (>) is still executed by your shell before sudo is applied, and it's done with your regular user's permissions

Solution 1: Use sudo with a shell command
```sh
sudo sh -c 'echo 7 > /proc/fs/cifs/cifsFYI'
```

Solution 2: Use sudo with tee
```sh
echo 7 | sudo tee /proc/fs/cifs/cifsFYI
```
