# Pip

## install another version of python in linux
```
sudo apt update
sudo apt install python3.9
sudo apt install python3.9-venv
```

## create and activate venv
```
python3.9 -m venv venv39   #create
source venv39/bin/activate #activate
exit                       #exit venv
```

## build whl package
```
pip wheel . --no-deps -w . --no-cache-dir --verbose
```
