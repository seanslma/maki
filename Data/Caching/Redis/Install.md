# Install

## Linux
latest stable version
```
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```

start and connect
```
sudo service redis-server start
redis-cli 
127.0.0.1:6379> ping
```

## Linux with build
install `build` tools
```
sudo apt-get update
sudo apt-get install make gcc python-dev
```

download Redis source code from: http://download.redis.io/releases/
```
wget -q http://download.redis.io/releases/redis-7.0.11.tar.gz
tar -xzf redis-7.0.11.tar.gz
cd 7.0.11
```

compile and install
```
make                       #compile redis
sudo make install          #install redis
redis-server redis.conf    #start redis server
```

install redis python client
```
pip install redis
pip install redis[hiredis] #faster performance
```

## Windows
Redis is not officially supported on Windows. Had to install it on WSL2.
