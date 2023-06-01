# Install

## Linux
install `build` tools
```
sudo apt-get update
sudo apt-get install make gcc python-dev
```

down load Redis source code from: https://redis.io/download/
```
wget -q https://github.com/redis/redis/archive/7.0.11.tar.gz
tar -xzf 7.0.11.tar.gz
cd 7.0.11
```

compile and install
```
make                       #compile redis
sudo make install          #install redis
redis-server redis.conf    #start redis server
```
