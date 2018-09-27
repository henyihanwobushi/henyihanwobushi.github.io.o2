---
layout: post
title: Nginx tcp proxy
---

Nginx 默认只提供了*http*服务的示例，并且提供了*conf.d*文件夹，进行*http*服务相关的配置，配置以及结构都不适合tcp转发。对```/etc/nginx/nginx.conf```文件中与```http {#...}```同级，添加：
```
stream {
    include /etc/nginx/stream.conf.d/*.conf;
}
```
创建文件夹：```/etc/nginx/stream.conf.d/```，并新建文件：```xxxservice.conf```
```
upstream xxxservice {
    server server-01:6379;
    server server-02:6379;
    server server-03:6379;
}

server {
    listen     6379;
    proxy_pass xxxservice;
}
```

参考：
* [https://docs.nginx.com/nginx/admin-guide/load-balancer/tcp-health-check/](https://docs.nginx.com/nginx/admin-guide/load-balancer/tcp-health-check/)