# File system

## file-system became be read-only
A common reason for a file-system to be read-only is because it has errors, and needs `fsck` (file system check).
```
sudo fsck -Af -M
sudo fsck.ext4 -f /dev/sda1
```

## size of subfolders
```
du -M --max-depth=1           #current folder
sudo du -sh /var              #only the total size
sudo du -shc /var/*           #folder and subfolders, c for grand total
sudo du -h --max-depth=1 /var #each folder in var folder
sudo du -h /var/ | sort -rh | head -5 #top 5 largest directories
```

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
cp -r ./source/ /dest/   #copy folder source into dest folder
cp -a ./source/. ./dest/ #content in source to dest, reserve all file attributes
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
