# File system

## Create file and add content
```
cat > filename
#input and then Ctrl+D to exit
```

## Create directory
```
mkdir
```

## Move file or folder
```
mv test/file-a /dev/file-b
mv test/folder-a/ folder-b/
mv /path/folder/* /anotherpath/folder/ #hidden files will be excluded
```

## Copy folder
```bash
cp -option1 -option2 source destination
#example
cp -avr /home/books /usb/backup
    -a: Preserve the specified attributes such as directory an file mode, ownership, timestamps, if possible additional attributes: context, links, xattr, all.
    -v: Verbose output.
    -r: Copy directories recursively.
```

## Delete file and folder
```
rm -r my-folder/ #delete folder and files
```

## Change rwx mode
```
chmod g+w filename
chmod g-wx filename
chmod o+w filename
chmod o-rwx foldername
```

## Change file ownership
```
chown <owner-name> <filename>
chgrp <group-name> <filename>
```
