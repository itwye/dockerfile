#### a web server base on bottle and python3
---
##### 1. debug server.py in local
```
pipenv --three
pipenv install
pipenv shell
python server.py
```
##### 2. docker image package
```
docker build -t bottle:0.1.0 .
```
##### 3. run
```
docker run --name mybottle  -d  -p 8080:8080 \
-v /path/to/server.py:/home/bottle/server.py \
bottle:0.1.0
```