---
layout: post
title: Hdfs commands(不定期更新)
date: 2018-08-10 10:08 +0800
tags: hadoop
---

* 检查各个 *datanode* 的情况, 文件会在 *namenode* 上的 *log* 文件夹生成
```
hdfs dfsadmin -metasave hdfs-meta-dump
```
* 开启 *hadoop* 的 *debug log*, 配置环境变量:
```
export HADOOP_ROOT_LOGGER=DEBUG,console
```
执行 *hadoop* 相关命令就可以看到效果
* 启动 *hdfs* 存储均衡
```
sudo -u hdfs hdfs balancer
```
* 手动执行 NameNode Checkpoint操作，主从节点执行 CheckPoint 操作采用的策略不同，主节点：
```
hdfs dfsadmin -safemode enter  
hdfs dfsadmin -saveNamespace  
hdfs dfsadmin -safemode leave 
```
从节点（Standby）：
```
hadoop secondarynamenode -checkpoint force 
```