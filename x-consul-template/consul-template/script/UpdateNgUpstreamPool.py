#!/usr/bin/python

import sys
import json
import urllib
import httplib


consul_addr = "consul-client.xtengine.com"
consul_port = 8500
nginx_manage_addr = "manage.xtengine.com"
nginx_manage_port = 8081


def CallApiGetData(Host,Port,ReqUrlSuffix):
    """
    Call api interface for get docker and container information
    """
    httpClient = None
    try:
        httpClient = httplib.HTTPConnection(Host,Port,timeout=2)
        httpClient.request('GET',ReqUrlSuffix)
        response = httpClient.getresponse()
        if response.status == 200:
            resp_string = response.read()
            resp_format_data = json.loads(resp_string)
            return resp_format_data
        else:
            print("return code %s"%response.status)
            sys.exit(1)
    except Exception,e:
        print("call api error!,%s"%e)
        sys.exit(1)
    finally:
        if httpClient:
            httpClient.close()


def SendDataToApi(Host,Port,ReqUrlSuffix,method,Data):
    httpClient = None
    try:
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        httpClient = httplib.HTTPConnection(Host,Port,timeout=2)
        httpClient.request(method,ReqUrlSuffix,Data,headers)
        response = httpClient.getresponse()
        print "Info -- Call nginx upstream interface, ReturnCode is %s , NginxResp is %s"%(response.status , response.read())
    except Exception,e:
        print "Error -- Call nginx upstream interface, ErrInfo is %s"%e
    finally:
        if httpClient:
            httpClient.close()

def ServiceDataFormat(Data):
    upstream_hosts = []
    for service in Data:
        node = service["Node"]["Address"]
        port = service["Service"]["Port"]
        upstream_host = "server %s:%s"%(node,port)
        upstream_hosts.append(upstream_host)
    return ";".join(upstream_hosts)+";"

if __name__ == "__main__":

    service_domain_name = sys.argv[1]
    service_name = service_domain_name.replace(".","-")

    #get health service
    #http://192.168.1.101:8500/v1/health/service/test-cloudiya-com?passing

    ret_data = CallApiGetData(consul_addr,consul_port,"/v1/health/service/%s?passing"%service_name)
    if ret_data:
        upstream_hosts_str = ServiceDataFormat(ret_data)
        method = "POST"
    else:
        upstream_hosts_str = ""
        method = "DELETE"
   
    #send upstream data to nginx
    #curl -d "server 192.168.1.100:8090;server 192.168.1.101:8090;" 127.0.0.1:8081/upstream/test.cloudiya.com
    SendDataToApi(nginx_manage_addr,nginx_manage_port,"/upstream/%s"%service_domain_name,method,upstream_hosts_str)
    
