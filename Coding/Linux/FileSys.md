# File system

## find file in current and sub directories
```sh
find . -name index.html
```

## find folder position
```sh
find /path/to/search  -name "xyz-abc" -type d
```

## size of subfolders
```sh
du -M --max-depth=1      #current folder
du -sh /var              #only the total size
du -shc /var/*           #folder and subfolders, c for grand total
du -h --max-depth=1 /var #each folder in var folder
du -h -d 1 | sort -h     #first subfolders only
du -h /var/ | sort -rh | head -5 #top 5 largest directories
```

## Create file and add content
```sh
cat > filename
#input and then Ctrl+D to exit
```

## Create directory
```sh
mkdir
```

## Move file or folder
```sh
mv test/file-a /dev/file-b
mv test/folder-a/ folder-b/
mv /path/folder/* /anotherpath/folder/ #hidden files will be excluded
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

## Delete file and folder
```sh
rm -r my-folder/  #delete folder and files
rm -r my-folder/* # delete all in the folder
```

## Change rwx mode
```sh
chmod g+w filename
chmod g-wx filename
chmod o+w filename
chmod o-rwx foldername
```

## Change file ownership
```sh
chown <owner-name> <filename>
chown -R user:user /myfolder  #change folder and content owner/group names
chgrp <group-name> <filename>
```
