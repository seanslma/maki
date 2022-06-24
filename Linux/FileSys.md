# File system

## change file ownership
```
chown <owner-name> <filename>
chgrp <group-name> <filename>
```

## change rwx mode
```
chmod g+w filename
chmod g-wx filename
chmod o+w filename
chmod o-rwx foldername
```

## create a new file and add content
```
cat > filename
#input and then Ctrl+D to exit
```

## copy folder
```bash
cp -option1 -option2 source destination
#example
cp -avr /home/books /usb/backup
    -a: Preserve the specified attributes such as directory an file mode, ownership, timestamps, if possible additional attributes: context, links, xattr, all.
    -v: Verbose output.
    -r: Copy directories recursively.
```
