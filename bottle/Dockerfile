# web server base on bottle
# version   0.1.0
FROM ubuntu:16.04
MAINTAINER itwye <itwye@qq.com> 

# create user
RUN groupadd web
RUN useradd -d /home/bottle -m bottle

# add source for ubuntu system
ADD sources.list /etc/apt/sources.list 
RUN apt-get update

# install package
RUN apt-get install python3-pip -y
RUN pip3 install bottle requests tornado

# copy code to image 
ADD server.py.example /home/bottle/server.py

# exposes port 8080
EXPOSE 8080
ENTRYPOINT ["/usr/bin/python3", "/home/bottle/server.py"]
USER bottle
