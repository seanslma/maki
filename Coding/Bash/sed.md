# sed

Perform basic text transformations on an input stream, in some ways similar to an editor.
- `-i` edit files in-place instead of printing to standard output
- `-n` suppress output

## replace
```sh
s/regexp/replacement/[flags]
```
replace `{"title":"` with nothing: `sed 's/{"title":"//g'`

## case convert
```sh
sed 's/.*/\L&/'  #to lower
sed 's/.*/\U&/'  #to upper

sed 'y/'$(printf "%s" {A..Z} "/" {a..z} )'/'
sed 'y/'$(printf "%s" {a..z} "/" {A..Z} )'/'
```

## print selected lines
only print 1st line in file1 and last line in last file
```sh
sed -n '1p;$p' one.txt two.txt three.txt
```

## delete selected lines
deletes lines 2 to 5 in the input
```sh
sed '2,5d' input.txt > output.txt
```

## delete matching lines and replace
delete lines matching regex /^foo/, and replace `hello` with `world`
```sh
seq 2 | sed -e 1ahello -e 2ifoo | sed '/^foo/d;s/hello/world/'
seq 2 | sed -e 1ahello | sed -e '2ahahahah' -e s/hello/world/
```

## select lines with step number
```sh
seq 10 | sed -n '1~2p' #1,3,...
seq 10 | sed -n '0~4p' #4,8,...
```

## select lines based on address
```sh
sed '2s/hello/world/'      #only replace on line 2
sed '2,5s/hello/world/'    #only replace lines 2-5
sed '2,5!s/hello/world/'   #only replace lines not 2-5
sed '/foo/s/hello/world/'  #only replace lines contain foo
sed '/foo/!s/hello/world/' #only replace lines not contain foo
```

## select lines with regex match
```sh
sed -n '/bash$/p' #print lines end with `bash`

#escape regex char, all match lines start with `/usr/home/`
sed -n '/^\/usr\/home\//p'
sed -n '\%^/usr/home/%p'
sed -n '\;^/usr/home/;p'
```
