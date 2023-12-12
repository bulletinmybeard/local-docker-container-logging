# Local Logging
Local Docker Container Logging with Elasticsearch, Kibana, Logstash, and Fluentd.

## The 'Local Logging' stack
Local logging comes with the log management and data pipeline tools: `fluentd` and `logstash`.
Depending on the given `--profile` argument, the stack will run Elasticsearch and Kibana,
together with either `fluentd` (e.g., `docker-compose --profile fluentd up`)
or `logstash` (e.g., `docker-compose --profile logstash up`).

## Service Configurations
Configuration files for all services can be found in the `./docker` directory.

### Elasticsearch
### Fluentd
Uses a Dockerfile to install Fluentd plugins and downgrade the Elasticsearch library version.
The config `elasticsearch-fluent.conf` is being mounted and can be updated at any time. To apply config changes,
run `docker exec fluentd kill -HUP 1` to gracefully do some magic.

### Kibana
Uses a Dockerfile to copy over a shell script for generating and exposing a random encryption key to Kibana. 

### Logstash
Elasticsearch pipeline with a log message parser, including `logstash.yml` and `pipelines.yml` configurations.
Config files are being mounted and local changes can be be applied by running `docker exec logstash kill -HUP 1`.


```bash
# Fluentd (Elasticsearch, Kibana, and Logstash)
docker-compose --profile logstash up
docker-compose --profile logstash up --build

# Fluentd (Elasticsearch, Kibana, and Fluentd)
docker-compose --profile fluentd up
docker-compose --profile fluentd up --build
```

## Demo Applications

```bash
docker-compose up -d fluentd-demo-app
docker-compose up -d logstash-demo-app

docker-compose up fluentd-demo-app
docker-compose up logstash-demo-app

docker-compose stop fluentd-demo-app
docker-compose stop logstash-demo-app

docker-compose up --build fluentd-demo-app
docker-compose up --build logstash-demo-app

docker-compose rm -f fluentd-demo-app
docker-compose rm -f logstash-demo-app
```

```bash
# Run Demo App sending logs to `fluentd`
docker-compose --profile fluentd up

# Run Demo App sending logs to `logstash`
docker-compose --profile logstash up

# Run both Demo Apps sending logs to `logstash` and `fluentd`
docker-compose --profile all up
```

## Send Docker container logs to LogDockA
### For `Logstash` 
```bash
    ...
    logging:
      driver: gelf
      options:
        tag: "<name_of_your_application_here>"
        gelf-address: "udp://172.30.0.4:12201"
```


### For `Fluentd` 
```bash
    ...
    logging:
      driver: fluentd
      options:
        tag: "<name_of_your_application_here>"
        fluentd-address: "172.30.0.5:24224"
```

## Backups Docker Volumes
```bash
docker-compose run backup
```

## Cron Job Setup
Edit your crontab as follows
```bash
crontab -e
```

```bash
chmod +x volume_backups.sh
```

Add a line like this to run the backup daily at a specific time, such as 2 AM:
```bash
0 2 * * * /usr/local/bin/docker-compose -f /path/to/your/docker-compose.yml run backup
```

