# io

## path
```python
#get dir
dir = os.path.dirname(sys.argv[0])
path = os.path.join(dir, csvfile)

#get user dir
dir = os.path.expanduser('~')

#python file dir
os.path.dirname(__file__)

#python file name
os.path.basename(__file__)

#create dir
if not os.path.exists(directory): 
  os.makedirs(directory)
  
#get filename from path
os.path.basename(r'c:\x.txt')  
```

## get files
```python
import os
files = []
for (dirpath, dirnames, filenames) in os.walk(dir):
    files += [os.path.join(dirpath, file) for file in filenames if file[-3:]=='.gz']
for filename in files:
    print(filename)
```

## show list
```python
#print 1d list???
print('[' + ', '.join(map(str, mylist)) + ']') 
#print 2d list
print(*mylist, sep='')
```

## read / write
```python
with open('path_file.csv', 'r', encoding='utf-8') as f:
    lines = f.read().splitlines()
        
with open('somefile.txt', 'a') as f:
    f.write('Hello\n') 
    
#write array to csv file
np.savetxt('myfile.csv', myarray, delimiter=',')    
```

## get first line of csv
```python
with open(fpath, 'r') as f:
    r = csv.reader(f)
    line = next(r)
```

## read csv in zip
```python
from io import TextIOWrapper
from zipfile import ZipFile

with ZipFile(file,'r') as zip:
    with zip.open(zip.namelist()[0]) as zipf:
        f = TextIOWrapper(zipf)
        lines = f.read().splitlines()
```
