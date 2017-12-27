> #### x-consul-template

当consul服务有变动时，consul-template调用xtengine upstream api直接更新nginx upstream pool，而不需nginx -s reload.

> #### usage

```
docker run -d \ 

--add-host consul-client.xtengine.com:$consul-client-ip \

--add-host manage.xtengine.com:$xtengine-ip \

itwye/x-consul-template
```