# BitWarden

https://help.passageway.id/article/cli/

## cli login
```sh
bw login <email>                       #will unlock automatically
bw logout                              #logout
export BW_SESSION="$(bw unlock --raw)" #generate and save session key to env
bw lock                                #destroy the saved session key
```

## cli create item
```sh
```
