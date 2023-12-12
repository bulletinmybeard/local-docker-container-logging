#!/bin/sh

NOW=$(date +"%Y%m%d%H%M")

tar -czvf /backup/elasticsearch_data_"${NOW}".tar.gz /usr/share/elasticsearch/data
tar -czvf /backup/kibana_data_"${NOW}".tar.gz /usr/share/kibana/data
tar -czvf /backup/logstash_data_"${NOW}".tar.gz /usr/share/logstash/data

#sleep infinity
