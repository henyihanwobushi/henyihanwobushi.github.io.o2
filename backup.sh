#!/usr/bin/env bash
HOSTNAME=`hostname -i`
for f in sudo find /var/log/ -iname '*.log.*' -mtime +1 -exec echo {} \;
do
    echo $f
done
