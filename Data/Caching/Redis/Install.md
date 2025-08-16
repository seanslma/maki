# Install

## Install redis python client
```sh
pip install redis
pip install redis[hiredis] #faster performance
mamba install redis-py hiredis
```

## Start redis via a docker file
```sh
# running a redis container for local development
docker run --rm -p 6379:6379 redis:7.0-alpine
```

## Install redis server on Linux
https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-linux/

install latest stable version:
```sh
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis
```

start and connect
```sh
sudo service redis-server start
redis-cli
127.0.0.1:6379> ping
```

## Linux with build
install `build` tools
```sh
sudo apt-get update
sudo apt-get install make gcc python-dev
```

download Redis source code from: http://download.redis.io/releases/
```sh
wget -q http://download.redis.io/releases/redis-7.0.11.tar.gz
tar -xzf redis-7.0.11.tar.gz
cd 7.0.11
```

compile and install
```sh
make                       #compile redis
sudo make install          #install redis
redis-server redis.conf    #start redis server
```

## Windows
Redis is not officially supported on Windows.

Had to install it on WSL2. See Linux section.

After start the redis-server from WSL2, we can use the server from windows (Need to install redis-py in windows).
