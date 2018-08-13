---
layout: post
title: hdfs commands
date: 2018-08-10 10:08 +0800
---

* `hdfs dfsadmin -metasave hdfs-meta-dump`检查各个 *datanode* 的情况, 文件会在 *namenode* 上的 *log* 文件夹生成
* 开启 *hadoop* 的 *debug log*, 配置环境变量: `export HADOOP_ROOT_LOGGER=DEBUG,console` 执行 *hadoop* 相关命令就可以看到效果
* hdfs 存储均衡器 `sudo -u hdfs hdfs balancer`