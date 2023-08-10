# BitWarden

https://help.passageway.id/article/cli/

## cli login
```sh
bw login <email>                       #will unlock automatically
bw logout                              #logout
export BW_SESSION="$(bw unlock --raw)" #generate and save session key to env
bw lock                                #destroy the saved session key
```

## create item
create item with password from file and name/username from inputs
```sh
read -r val < "$HOME/bw.txt" && bw get template item | jq --arg name "$1" --arg username "$2" --arg password "$val" '.name = $name | .login.username = $username | .login.password = $password' | bw encode | bw create item > /dev/null
```

## list items with selected columns
```sh
bw list items #json output
bw list items | jq -r '.[] | [.id, .name, .login.username, .login.password] | @tsv' | column -t -s $'\t' #convert json to table, last ensures col vals being aligned
```

## list username
```sh
bw get item "$1" | jq -r '.login.username' > bw.txt
```

## get folder id
```sh
fid=$(bw list folders | jq --arg name "$1" -r '.[] | select(.name==$name) | .id') && echo $fid;
```

## get item id
```sh
iid=$(fid=$(bwfid "$1") && bw list items --folderid "$fid" | jq --arg name "$2" -r '.[] | select(.name==$name) | .id') && echo $iid;
```

## create folder
```sh
bw get template folder | jq --arg name "$1" '.name=$name' | bw encode | bw create folder;
```

## create item
```sh
read -r val < "bw.txt" && fid=$(get_folder_id "$1") && bw get template item | jq --arg folderid "$fid" --arg name "$2" --arg username "$3" --arg password "$val" '.folderId = $folderid | .name = $name | .login.username = $username | .login.password = $password' | bw encode | bw create item > /dev/null;
```

## list older
```sh
bw list folders | jq -r '.[] | [.id, .name] | @tsv' | column -t -s $'\t';
```

## list item
```sh
fid=$(get_folder_id "$1") && bw list items --folderid "$fid" | jq -r '.[] | [.id, .name, .creationDate] | @tsv' | column -t -s $'\t';
```

## get item username
```sh
bw get item "$1" | jq -r '.login.username' > ~/bw.txt;
```

## edit item
```sh
read -r val < "bw.txt" && bw get item "$1" | jq --arg password "$val" '.login.password=$password' | bw encode | bw edit item "$1";
```
