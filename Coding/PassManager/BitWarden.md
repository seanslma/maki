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
create item with password from file and name/username from inputs
```sh
read -r urps < "$HOME/bw.txt" && bw get template item | jq --arg name "$1" --arg username "$2" --arg password "$urps" '.name = $name | .login.username = $username | .login.password = $password' | bw encode | bw create item > /dev/null
```

## cli list items with selected columns
```sh
bw list items #json output
bw list items | jq -r '.[] | [.id, .name, .login.username, .login.password] | @tsv' | column -t -s $'\t' #convert json to table, last ensures col vals being aligned
```

## cli list username
```sh
bw get item "$1" | jq -r '.login.username' > bw.txt
```
