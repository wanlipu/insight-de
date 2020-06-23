# Synchronize Databases with Kafka Connect

Real-time synchronization from PostgreSQL to Amazon Redshift with Kafka Connect API in distributed mode, and the same approach can be applied to other database systems.

[Link](https://docs.google.com/presentation/d/1hL5E2GRLjzhrK5PiQAm20N_Cro8w7o1EwX2ITdvy_ZU/edit?usp=sharing) to your presentation.

<hr/>

## How to install and get it up and running


<hr/>

## Introduction
Kafka Connect API is a core component of Apache Kafka platform, and it provides a scalable and fault-tolerant database synchronization option between various database systems.

In this project, a streaming data pipeline was created with Kafka Connect API to continuously capture any changes in a PostgreSQL database and replicate them into an Amazon Redshift data warehouse.

## Architecture

Once the streaming pipeline is constructed, a snapshot of the source PostgreSQL database will be captured, and all data in the source database will be streaming through a Kafka cource connector, a Kafka broker cluster, and a Kafka sink connector into Amazon Redshift data warehouse. 
<img src="https://github.com/wanlipu/insight-de/blob/master/images/architecture.png" alt="architecture" />

When there are any changes in the source database, the streaming system will capture them and replicate them into the Amazon Redshift data warehouse.
<img src="https://github.com/wanlipu/insight-de/blob/master/images/new_data.png" alt="new_data" />



## Dataset

## Engineering challenges

## Trade-offs
