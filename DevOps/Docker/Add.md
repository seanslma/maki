# Add
Note that the destination address must not be relative. Something like `~/dev` will not copy anything to the folder.

## ADD failed: Forbidden path outside the build context
This error occurs because the path you're trying to add with the ADD instruction is located outside the Docker build context. 
Docker restricts file operations to within the build context directory for security reasons.

To resolve this issue, we need to copy the folder to under the build contect directory.

## copy content of folder x into folder y
https://stackoverflow.com/questions/26504846/copy-directory-to-another-directory-using-add-command
```sh
ADD x /home/user/y/
```

## copy folder x to folder y
```sh
ADD x /home/user/y/x
```
