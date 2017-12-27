consul {
address = "consul-client.xtengine.com:8500"
}

template {
source = "/consul-template/template/prod.xtengine.com.conf.ctmpl"
destination = "/nginx/conf.d/prod.xtengine.com.conf"
command = "python /consul-template/script/UpdateNgUpstreamPool.py prod.xtengine.com"
}

template {
source = "/consul-template/template/test.xtengine.com.conf.ctmpl"
destination = "/nginx/conf.d/test.xtengine.com.conf"
command = "python /consul-template/script/UpdateNgUpstreamPool.py test.xtengine.com"
}
