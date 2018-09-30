#!/usr/bin/env bash
HOSTNAME=`hostname -i | awk '{print $1}'`
export JAVA_HOME=/usr/local/jdk1.8.0_74/
for f in $(sudo find /var/log/ -iname '*.log.*' -mtime +1 -exec echo {} \;)
do
    hadoop fs -mkdir -p /tmp/server_logs/$HOSTNAME`dirname $f`
    hadoop fs -put $f /tmp/server_logs/$HOSTNAME$f
    rm $f
done

