# File copy

## Move file or folder
```sh
mv test/file-a /dev/file-b
mv test/folder-a/ folder-b/
mv /path/folder/* /anotherpath/folder/ #hidden files will be excluded
```

## Delete file and folder
```sh
rm -r my-folder/  #delete folder and files
rm -r my-folder/* # delete all in the folder
```

## Copy folder
```sh
cp -option1 -option2 source destination
cp -r ./source/ /dest/   #copy source folder into dest folder
cp -a ./source/. ./dest/ #content in source to dest, reserve all file attributes
#example
cp -avr /home/books /usb/backup
    -a: Preserve the specified attributes such as directory and file mode, ownership, timestamps,
        if possible additional attributes: context, links, xattr, all.
    -v: Verbose output.
    -r: Copy directories recursively.
```

## copy from ssh-connected machine to current machine
scp: `secure copy` allows us to securely transfer files between machines over SSH.
```sh
scp username@remote_host:/path/to/remote_file /path/to/local/directory
```

sftp: `SSH File Transfer Protocol` allows browsing and transferring files between machines securely.
```sh
sftp username@remote_host
get remote_file ~/Downloads
put local_file.txt /uploads/local_file.txt
exit
```
