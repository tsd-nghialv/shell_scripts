#!/bin/bash
#exec > /var/log/telgraf.log
#echo -e "Time: $(date +%F)"
/usr/bin/find /opt/sandbox/influxdb/data/data/telegraf/autogen/ -mtime +10 -delete -and -print >> /var/log/telgraf.log
docker restart sandbox_influxdb_1
