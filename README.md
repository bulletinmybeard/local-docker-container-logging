# Local Logging
Local Docker Container Logging with Elasticsearch, Kibana, Logstash, and Fluentd.

## Table of Contents
- [Introduction](#introduction)
- [The Stack](#the-stack)
- [Running Backups](#running-backups)
- [Demo Applications](#demo-applications)
- [License](#license)

## Introduction
Local logging comes with the log management and data pipeline tools: `fluentd` and `logstash`.
Depending on the given `--profile` argument, the stack will run Elasticsearch and Kibana,
together with either `fluentd` (e.g., `docker-compose --profile fluentd up`)
or `logstash` (e.g., `docker-compose --profile logstash up`).

## The Stack
Configuration files for all services can be found in the `./docker` directory.
arm64!!!!!!

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

docker-compose up fluentd-demo-app
docker-compose up fluentd-demo-app --build

docker-compose up logstash-demo-app
docker-compose up logstash-demo-app --build

docker-compose --profile all up
docker-compose --profile all up --build
```

```bash
# Run Demo App sending logs to `fluentd`
docker-compose --profile fluentd up

# Run Demo App sending logs to `logstash`
docker-compose --profile logstash up
```

## Update your existing `docker-compose.yml` application files
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

## Running Backups
For backing up data volumes, such as `elasticsearch_data`, we spin up a `busybox` Docker container
and run the shell script `./backup/volume_backups.sh`. The data is being backed up in the `backup` folder.


```bash
# Run Docker Container and shell script
docker-compose run backup
```

You can run the Docker container periodically by adding the docker-compose command to your crontab.
```bash
# Adds execute permission to the shell script
chmod +x volume_backups.sh

# Open your crontab file in edit mode
crontab -e

# Add a line like this to run the backup daily at a specific time, such as 2 AM:
0 2 * * * docker-compose -f /path/to/your/docker-compose.yml run backup
```

## License
This project is licensed under the [MIT License](LICENSE).
