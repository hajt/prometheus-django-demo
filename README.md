# Web Application monitoring by Prometheus

This is a setup for familiarize with a Prometheus Monitoring System. Setup includes preconfigred Prometheus and node-exporter instances for monitoring local machine, a sample Web Application (in this particular case a Django Application) as an example of usage Prometheus Client for generating own, custom metrics and a Grafana instance with preconfigured dedicated dashboards, for a nice visualisation of generated Prometheus metrics.

## Requirements:  
- `docker` and `docker-compose` services

## Running:  
1. Clone repository to your local machine.
1. Open terminal and exec command `docker-compose up`.
1. Check your `localhost`.

## Setup specification:
***Prometheus*** instance runs on port `9090`  
***Node exporter*** instance runs on port `9100`  
***Alertmanager*** instance runs on port `9093`  
***Grafana*** instance runs on port `3000`  
*Note: Default credentials are `admin`/`admin `*  
***Web-app*** runs on port `8000`  

## Application endpoints:
`/` - home page  
`/counter` - endpoint for generate sample *counter* metrics  
`/gauge` - endpoint for generate sample *gauge* metrics  
`/summary` - endpoint for generate sample *summary* metrics  
`/histogram` - endpoint for generate sample *histogram* metrics  
`/enum` - endpoint for generate sample *enum* metrics  
`/metrics` - enpoint which returns all app metrics  

### Enjoy!
