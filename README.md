# Synchronize Databases with Kafka Connect

Real-time synchronization from PostgreSQL to Amazon Redshift with Kafka Connect API in distributed mode, and the same approach can be applied to other database systems.

[Link](https://docs.google.com/presentation/d/1hL5E2GRLjzhrK5PiQAm20N_Cro8w7o1EwX2ITdvy_ZU/edit?usp=sharing) to my presentation.\
[Link](https://youtu.be/FVhEfxEdU4c) to my live demo on youtube.

## Introduction
Kafka Connect API is a core component of Apache Kafka platform, and it provides a scalable and fault-tolerant database synchronization option between various database systems.

In this project, a streaming data pipeline was created with Kafka Connect API to continuously capture any changes in a PostgreSQL database and replicate them into an Amazon Redshift data warehouse.

## Architecture

Once the streaming pipeline is constructed, a snapshot of the source PostgreSQL database will be captured, and all data in the source database will be streaming through a Kafka cource connector, a Kafka broker cluster, and a Kafka sink connector into Amazon Redshift data warehouse. 
<img src="https://github.com/wanlipu/insight-de/blob/master/images/architecture.png" alt="architecture" />

When there are any changes in the source database, the streaming system will capture them and replicate them into the Amazon Redshift data warehouse.
<img src="https://github.com/wanlipu/insight-de/blob/master/images/new_data.png" alt="new_data" />

## System Setup

Deploy Kafka Brokeer cluster and Kafka Connect cluster on AWS EC2 instances with [Ansible Playbook](https://docs.confluent.io/current/installation/cp-ansible/index.html)
- [Prepare Ansible Playbooks for Confluent Platform](https://docs.confluent.io/current/installation/cp-ansible/ansible-inventory.html)
  - An example of `hosts.yml` is shown in `kafka/cp-ansible/hosts.yml`
- [Install Ansible Playbooks for Confluent Platform](https://docs.confluent.io/current/installation/cp-ansible/ansible-install.html)
  - `ansible-playbook -i hosts.yml all.yml`
- [Installing the Redshift JDBC Driver](https://docs.confluent.io/current/connect/kafka-connect-aws-redshift/index.html)
  - Download the latest JDBC 4.0 driver JAR file that comes with the AWS SDK from [here](https://docs.aws.amazon.com/redshift/latest/mgmt/configure-jdbc-connection.html#jdbc-previous-versions).
  - Save the JDBC driver JAR file to `/<plugin.path>/kafka-connect-jdbc/`

Postgres Node
- [Simply Install: PostgreSQL](https://blog.insightdatascience.com/simply-install-postgresql-58c1e4ebf252)
  - `sudo apt update`
  - `sudo apt upgrade -y`
  - `sudo apt install postgresql postgresql-contrib`
  - `sudo service postgresql start`

Amazon Redshift
- [Getting started with Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/gsg/getting-started.html)

## Run Demo
- Create tables in PostgreSQL database
  - `python3 /postgres/create_tables.py <db-name> <user> <password> <server-address> <port> <table-name> <sample-file>`
- Create tables on Amazon Redshift cluster
  - `python3 /redshift/create_tables.py <db-name> <user> <password> <server-address> <port> <table-name>`
- Run Kafka source connector
  - `bash postgresql_source.sh`
- Run Kafka sink connector
  - `bash redshift_sink.sh`
- Load more data into PostgreSQL database
  - `python3 /postgres/create_tables.py <db-name> <user> <password> <server-address> <port> <table-name> <data-file>`
 
 
