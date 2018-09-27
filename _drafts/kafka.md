---
layout: post
title: kafka
---

```bash
# topic list
/usr/hdp/current/kafka-broker/bin/kafka-topics.sh --zookeeper tdp01:2181/kafka_10_1 --list

# console consumer
/usr/hdp/current/kafka-broker/bin/kafka-console-consumer.sh  --bootstrap-server tdp01:9092,tdp02:9092,tdp03:9092 --topic jarvis-test.jarvis.login_info --from-beginning

# 
```