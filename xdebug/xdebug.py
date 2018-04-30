#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import os
import bottle
import socket
import psutil

# Student information

stdInfo = {
	
	"zhangsan":{"math":98,"chinese":99,"english":100},
	"lisi":{"math":89,"chinese":97,"english":60},
	"wangwu":{"math":88,"chinese":93,"english":67},

}

# Enviroment variables

env = os.environ.get("RUNENV","not known")

# Hostname

hostname = socket.getfqdn(socket.gethostname())

# IP address

def get_netcard():
    netcard_info = []
    info = psutil.net_if_addrs()
    for k,v in info.items():
        for item in v:
            if item[0] == 2 and not item[1]=='127.0.0.1':
                netcard_info.append((k,item[1]))
    return netcard_info


# Main

@bottle.route('/')
def hostInfo():
	return bottle.template('hostname : {{hostname}} <br> ipaddress : {{ip}} <br> runenv : {{env}}',hostname=hostname,ip=get_netcard(),env=env)


@bottle.route('/sum')
def sum():
	return bottle.template('There are a total of {{sum}} students. <br> runenv : {{env}}',sum=len(stdInfo),env=env)


@bottle.route('/name/<name>')
def find(name):
	return bottle.template('{{name}} exam results is : {{results}}. <br> runenv : {{env}}',name=name,env=env,results=stdInfo.get(name,"not find"))


bottle.run(host='0.0.0.0', port=80)

